import pytest


@pytest.fixture
def os_mock(mocker):
    yield mocker.patch('garbage_destroyer.clean.os')


@pytest.fixture
def glob_mock(mocker):
    yield mocker.patch('garbage_destroyer.clean.glob.glob')


@pytest.fixture
def config_mock(mocker):
    yield mocker.patch('app.config')
