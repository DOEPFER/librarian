import winreg as registry  # pip install winregistry

key_name = "Librarian"

# FILE
key_path = rf"*\\shell\\{key_name}"
command_key_path = rf"*\\shell\\{key_name}\\command"

registry.DeleteKey(registry.HKEY_CLASSES_ROOT, command_key_path)
registry.DeleteKey(registry.HKEY_CLASSES_ROOT, key_path)

# FOLDER
key_path = rf"Directory\\shell\\{key_name}"
command_key_path = rf"Directory\\shell\\{key_name}\\command"

registry.DeleteKey(registry.HKEY_CLASSES_ROOT, command_key_path)
registry.DeleteKey(registry.HKEY_CLASSES_ROOT, key_path)
