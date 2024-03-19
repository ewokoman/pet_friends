import pytest
import logging
import logging.config
import os
from helpers.const import PROJECT_DIR


@pytest.fixture(scope='session', autouse=True)
def setup_logging():
    """ Настраиваем логирование"""
    log_config_path = os.path.join(PROJECT_DIR, 'log_config.conf')
    logging.config.fileConfig(fname=log_config_path,
                              disable_existing_loggers=False)
