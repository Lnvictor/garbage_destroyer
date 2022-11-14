import pytest


@pytest.fixture
def os_mock(mocker):
    yield mocker.patch('garbage_destroyer.app.os')


@pytest.fixture
def glob_mock(mocker):
    yield mocker.patch('garbage_destroyer.app.glob.glob')


@pytest.fixture
def config_mock(mocker):
    yield mocker.patch('garbage_destroyer.app.config')
