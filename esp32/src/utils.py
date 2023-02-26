from typing import Dict, Any, List, Optional
import pytz
import logging
import os
from dotenv import load_dotenv


load_dotenv(".env")


# Setup basic logging
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


LOCAL_TIMEZONE = pytz.timezone("America/Sao_Paulo")


def load_bool_env(env_name) -> bool:
    return os.getenv(env_name, 'False').lower() in ('true', '1', 't')
