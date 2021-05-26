from _pytest import pytest
from src.config import CONFIG
from scout_client import scout
from src.tools.helpers.parsers.scout_queries_par..

@pytest.fixture(scope="class")
def scout():
    return scout(CONFIG_SCOUT_BASE_URL)