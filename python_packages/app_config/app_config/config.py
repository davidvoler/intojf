import pathlib
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import os 
import logging
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import os 

def get_configs(conf):
    config = {}
    if not os.path.isfile(f"/conf/{conf}.yaml"):
        logging.warning(f'No configuration file found at /conf')
        return False
    with open(f"/conf/{conf}.yaml", 'r') as cfg:
        config = load(cfg, Loader=Loader)
    return config
