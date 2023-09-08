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

# AutoHotkey Integration

## Running the Script

You can easily run this script using AutoHotkey to automate scene management in Home Assistant. Press `Win+Home` to trigger the script, which will execute your Python code for scene control.

**Note:** Ensure that AutoHotkey is installed on your system before running the script.

Example AutoHotkey v1.1 script:

```ahk

#Home:: ; Press Win+Home to run the Python script using AutoHotkey
dir := "path\to\your\python\script\" ; Set the directory path to your Python script
script := dir . "sceneSwapper.py ; Define the Python script to run
Run, % ComSpec " /k python " script ,, Hide ; Press F3 to execute the Python script
return

```

Example AutoHotkey v2.0 script:
```ahk
#Home:: ; Press Win+Home to run the Python script using AutoHotkey
dir := "path\to\your\python\script\" ; Set the directory path to your Python script
script := dir . "sceneSwapper.py" ; Define the Python script to run
Run, % ComSpec " /k python " script ,, Hide ; Execute the Python script without F3
return
```

## Dependencies

requests library for making HTTP GET and POST requests.

## License

This project is licensed under the GNU General Public License version 3.0 (GPL-3.0).

