from pathlib import Path
from typing import Dict

import yaml

BASE_DIR = Path(__file__).resolve().parent

DATABASE_URL = ''


def _load_config(file_name: str) -> Dict:
    with open(BASE_DIR.joinpath(file_name)) as f_obj:
        config = yaml.load(f_obj, Loader=yaml.FullLoader)

    return config


# APP_CONFIG = _load_config('app_config.yaml')
LOGGER_CONFIG = _load_config('logger_config.yaml')