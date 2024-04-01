import tomllib

def utility_function():
    print('I am a utility function!')

def parse_config(config_path):
    '''
    Parse the config.toml file so the parameters can be easily accessed.

    Args:
        config_path (str): The path to the config file.

    Returns:
        cfg (dict): The parsed config file.
    '''
    with open(config_path, "rb") as f:
        cfg = tomllib.load(f)
    return cfg