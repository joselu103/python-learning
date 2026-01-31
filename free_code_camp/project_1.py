def add_setting(settings: dict, key_value: tuple[str, str]) -> str:
    key, value = map(str.lower, key_value)
    if key in settings:
        return (
            f"Setting '{key}' already exists! Cannot add a new setting"
            " with this name."
        )
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, key_value: tuple[str, str]) -> str:
    key, value = map(str.lower, key_value)
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict, key: str) -> str:
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"


def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."
    return "Current User Settings:\n" + "\n".join(
        key.capitalize() + ": " + value for key, value in settings.items()
    )+'\n'


test_settings = {"Theme": "dark", "Notifications": "enabled", "Volume": "high"}

print(view_settings(test_settings))
print(add_setting({"theme": "light"}, ("THEME", "dark")))
