def config_command():
    pass

def set_config(command:str):
    commands = {
        'config': config_command
    }

    return commands[command]()