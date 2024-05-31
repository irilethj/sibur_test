import time
from dataclasses import dataclass, field
from typing import Literal, Union
from aiohttp import ClientSession


@dataclass
class Event:
    name: str
    value: Union[int, float]
    timestamp: float
    agg_func: Literal["sum", "avg", "min", "max"] = "sum"


@dataclass
class Metric:
    name: str
    value: Union[int, float]
    timestamp: float = field(default_factory=lambda: time.time())


class VaBus:
    def __init__(self, url: str):
        self.url = url
        self._session = ClientSession(base_url=url)

    async def __aenter__(self) -> "VaBus":
        """
        Initialize connection to bus
        """
        await self._session.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Close connection to bus
        """
        await self._session.__aexit__(exc_type, exc_val, exc_tb)

    # async def get_event(self) -> Event:
    #     pass

    async def get_event(self) -> Event:
        # Заглушка, возвращающая простой объект Event для демонстрации.
        return Event(name="DemoEvent", value=1, timestamp=time.time(), agg_func="sum")

    async def send_metric(self, metric: Metric):
        pass
