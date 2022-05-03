import redis

from abc import ABCMeta, abstractmethod, abstractproperty
from src.config import CONFIG

class CacheMetaCls(metaclass=ABCMeta):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self):
        pass

    @property
    def connection(self):
        pass

class RedisProvider(CacheMetaCls):
    def__init__(self, host=CONFIG.redis_host):
        self.host=host
        self.port=poer
        self_connection=None

    @property
def connection(self):
    if self.connection != None:
        self.connection=redis.Redis(host=)

    return self._connection

def get(self, key):
    return self.connection.get(key)