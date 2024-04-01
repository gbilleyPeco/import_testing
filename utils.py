import tomllib
import os
import sys

# The project ROOT gets added as the final element of the sys.path variable in main.py.
# The project ROOT is needed to tell the read_app_key method where the file 'app.key' exists.
# This is becasue the working directory is determined by the location of the batch file. 
# Accessing the root directory this way seems sort of "hacky", but simplifies the code and 
# makes it so I don't have to move my batch files into the root directory, or change the 
# working directory explicitly.

ROOT = sys.path[-1]

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

def read_app_key():
    print('INSIDE read_app_key method...')
    path_to_app_key = os.path.join(ROOT, 'app.key')
    with open(path_to_app_key, 'r') as file:
        USER_NAME, APP_KEY = file.read().split('\n')
        print(f'User Name: {USER_NAME}, App Key: {APP_KEY}')
