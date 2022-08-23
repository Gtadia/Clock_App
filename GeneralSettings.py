import json
from kivy.properties import ObjectProperty

with open("general_settings.json", 'r') as open_file:
    settings = json.load(open_file)
    dark_mode = ObjectProperty(settings['is_dark_mode'])
    hour_format = ObjectProperty(settings['is_24_format'])
    animation = ObjectProperty(settings['animation_enabled'])


def dark_light_mode_change(self, is_active):
    dark_light_mode_dict = {}
    with open("general_settings.json", "r") as open_file:
        dark_light_mode_dict = json.load(open_file)

    dark_light_mode_dict["is_dark_mode"] = is_active

    with open("general_settings.json", "w") as open_file:
        open_file.write(json.dumps(dark_light_mode_dict, indent=4))
    


def hour_format_change(self, is_active):
    hour_format_dict = {}
    with open("general_settings.json", "r") as open_file:
        hour_format_dict = json.load(open_file)

    hour_format_dict["is_24_format"] = is_active

    with open("general_settings.json", "w") as open_file:
        open_file.write(json.dumps(hour_format_dict, indent=4))


def enable_animation(self, is_active):
    animation_dict = {}
    with open("general_settings.json", "r") as open_file:
        animation_dict = json.load(open_file)

    animation_dict["animation_enabled"] = is_active

    with open("general_settings.json", "w") as open_file:
        open_file.write(json.dumps(animation_dict, indent=4))


def reset_data(self):
    # Have a popup show up with confirmation
    with open("general_settings.json", "w") as open_file:
        open_file.write(json.dumps(
            {
            "is_dark_mode": False,
            "is_24_format": False,
            "animation_enabled": True
        }, indent = 4
        ))

    with open("general_settings.json", 'r') as open_file:
        settings = json.load(open_file)
        dark_mode = ObjectProperty(settings['is_dark_mode'])
        hour_format = ObjectProperty(settings['is_24_format'])
        animation = ObjectProperty(settings['animation_enabled'])



