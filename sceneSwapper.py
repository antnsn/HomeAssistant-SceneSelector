import requests

# Remember to change 
# - your-homeassistant-url
# - your-homeassistant-token

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

# Define the URL and headers
url = "http://your-homeassistant-url:8123/api/states/"
lights_on = "http://your-homeassistant-url:8123/api/services/scene/turn_on"
token = "your-homeassistant-token"  # Replace with your actual authentication token
headers = {
    "Authorization": f"Bearer {token}"
}

# Define an array of scene entities
scenes = [
    {"entity_id": "scene.scene-1"},
    {"entity_id": "scene.scene-2"},
    # Add more scene entities as needed
]

# Initialize variables to store the oldest scene and timestamp
oldest_scene = None
oldest_timestamp = None

# Iterate through the scene entities to find the oldest one
for scene in scenes:
    # Get the state for the current scene
    scene_state = get_scene_state(url, headers, scene["entity_id"])
    scene_timestamp = scene_state.get("last_updated")

    # Compare the timestamps to determine the oldest scene
    if oldest_timestamp is None or scene_timestamp < oldest_timestamp:
        oldest_scene = scene["entity_id"]
        oldest_timestamp = scene_timestamp

# Use a POST request to turn on the oldest scene
response = turn_on_scene(lights_on, headers, oldest_scene)

# Print the result
print(response)
