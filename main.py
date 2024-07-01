import requests
from dotenv import load_dotenv
import os
from dateutil.parser import parse as parse_date

# Load environment variables from .env file
load_dotenv()

# Get environment variables
base_url = os.getenv('BASE_URL')
token = os.getenv('HOMEASSISTANT_TOKEN')

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

# Define an array of scene entities
scenes = [
    {"entity_id": "scene.kontor_normal"},
    {"entity_id": "scene.scene_kjeller_kontor_mote"},
    # Add more scene entities as needed
]

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