import requests
from dotenv import load_dotenv
import os
from dateutil.parser import parse as parse_date

# Determine the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Function to create .env file if it doesn't exist
def create_env_file():
    env_path = os.path.join(script_dir, '.env')
    if not os.path.exists(env_path):
        base_url = input("Enter the BASE_URL: ")
        token = input("Enter the HOMEASSISTANT_TOKEN: ")
        scenes = input("Enter the scenes as a comma-separated list (e.g., scene.kontor_normal,scene.scene_kjeller_kontor_mote): ")

        with open(env_path, 'w') as env_file:
            env_file.write(f"BASE_URL={base_url}\n")
            env_file.write(f"HOMEASSISTANT_TOKEN={token}\n")
            env_file.write(f"SCENES={scenes}\n")

# Create .env file if it doesn't exist
create_env_file()

# Load environment variables from .env file located in the script directory
env_path = os.path.join(script_dir, '.env')
load_dotenv(dotenv_path=env_path)

# Get environment variables
base_url = os.getenv('BASE_URL')
token = os.getenv('HOMEASSISTANT_TOKEN')
scenes_str = os.getenv('SCENES')

# Convert scenes string to a list of dictionaries
scenes = [{"entity_id": scene.strip()} for scene in scenes_str.split(",")]

# Define the URL and headers
url = f"{base_url}/api/states/"
lights_on = f"{base_url}/api/services/scene/turn_on"
headers = {
    "Authorization": f"Bearer {token}"
}

def get_scene_state(url, headers, entity_id):
    try:
        # Make an HTTP GET request to retrieve the scene state for the specified entity
        response = requests.get(f"{url}{entity_id}", headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the response JSON
            data = response.json()
            return data
        else:
            return {"Error": f"HTTP request failed with status code {response.status_code}"}
    except Exception as e:
        return {"Error": str(e)}

def turn_on_scene(url, headers, entity_id):
    try:
        # Make an HTTP POST request to turn on the specified scene entity
        data = {"entity_id": entity_id}
        response = requests.post(url, headers=headers, json=data)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return f"Turned on {entity_id}"
        else:
            return {"Error": f"HTTP request failed with status code {response.status_code}"}
    except Exception as e:
        return {"Error": str(e)}

# Initialize variables to store the oldest scene and timestamp
oldest_scene = None
oldest_timestamp = None

# Iterate through the scene entities to find the oldest one
for scene in scenes:
    # Get the state for the current scene
    scene_state = get_scene_state(url, headers, scene["entity_id"])
    
    # Check for errors in the scene state
    if "Error" in scene_state:
        print(f"Error retrieving state for {scene['entity_id']}: {scene_state['Error']}")
        continue

    scene_timestamp_str = scene_state.get("last_updated")

    # Parse the timestamp and compare it
    if scene_timestamp_str:
        try:
            scene_timestamp = parse_date(scene_timestamp_str)
            if oldest_timestamp is None or scene_timestamp < oldest_timestamp:
                oldest_scene = scene["entity_id"]
                oldest_timestamp = scene_timestamp
        except Exception as e:
            print(f"Error parsing date for {scene['entity_id']}: {e}")

# Use a POST request to turn on the oldest scene
if oldest_scene:
    response = turn_on_scene(lights_on, headers, oldest_scene)
    print(response)  # Not used when running with AHK
else:
    print("No valid scene found to turn on.")
