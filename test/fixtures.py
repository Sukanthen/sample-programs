import docker
import pytest

from test import source

sources = source.get_sources('../archive')


@pytest.fixture
def docker_client():
    return docker.from_env()