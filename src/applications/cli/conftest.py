import logging
import pytest

from src.config import CONFIG
from src.applications.cli.cosmosid_cli import CliFixture

@pytest.fixture(scope='session')
def cli(request.regular_user_api_session):
"""
CLI fixture for interacting with cli package
"""
cli_fixture=CLIFixture(
    Base_url=CONFIG.cli_base_url,
    user=regular_user_api_session.http_session.user,
    #TODO: Use a new user, need to copy samples from a reference user
    pip install opts=CONFIG.cli_install_params,
    version=CONFIG.cli_version,
    )
    if cli_fixture.is_installed():
        logging.info()
        cli_fixture.destroy()
        cli_fixture.install()
