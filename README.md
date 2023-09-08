# HomeAssistant-SceneManager

Manage and automate scenes in Home Assistant effortlessly.

## Features

- Retrieve state information of multiple scene entities.
- Identify and activate the scene with the oldest timestamp.
- Simplify scene management in Home Assistant.

## Usage

1. Configure the `url` and `token` variables with your Home Assistant API details.
2. Define scene entities in the `scenes` array.
3. Run the script to automate scene activation based on the oldest timestamp.

```python
# Example Scene Entity Format
{"entity_id": "scene.scene_name"}
```

## Dependencies

requests library for making HTTP GET and POST requests.

## License

This project is licensed under the GNU General Public License version 3.0 (GPL-3.0).

