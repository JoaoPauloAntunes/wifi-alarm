from typing import Dict, Any, List, Optional
import pytz
import logging


# Setup basic logging
logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


LOCAL_TIMEZONE = pytz.timezone("America/Sao_Paulo")


class ResponseDataAny:
    def __init__(self, message: str, data: Optional[Any] = None) -> None:
        self.message = message
        self.data = data


class ResponseDataDict:
    def __init__(self, message: str, data: Optional[Dict] = None) -> None:
        self.message = message
        self.data = data


class ResponseDataList:
    def __init__(self, message: str, data: Optional[List] = None) -> None:
        self.message = message
        self.data = data


class ResponseDataStr:
    def __init__(self, message: str, data: Optional[str] = None) -> None:
        self.message = message
        self.data = data
