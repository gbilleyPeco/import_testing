'''
How to import utility_function from utils, which is one module up...
'''
#%% Look at parent directories.
print('\n\n------------------------------\n\n')
print('PATH Section\n')
import sys
import os
# print('Before:\n')
# print(sys.path)
# print('\n\n')
ROOT = os.path.abspath(os.path.join('..'))
if ROOT not in sys.path:
    sys.path.append(ROOT)

# print('After:\n')
# print(sys.path)

#%% Try the import.
print('\n\n------------------------------\n\n')
print('Utility Function Section\n')
from utils import utility_function
utility_function()

#%% Get params from the config.toml file under ROOT
print('\n\n------------------------------\n\n')
print('Config Section\n')
from utils import parse_config
# ROOT Config
cfg_path = os.path.join(ROOT, 'config.toml')
root_cfg = parse_config(cfg_path)
# print(f'ROOT Config: {root_cfg}\n\n')
# PFM Config
pfm_cfg = parse_config('config.toml')
# print(f'PFM Config: {pfm_cfg}\n\n')

#%% Figure out how to get the utils file to read from app.key
from utils import read_app_key
read_app_key()
