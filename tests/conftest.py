import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

_INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory data before each test for isolation."""
    app_module.activities = copy.deepcopy(_INITIAL_ACTIVITIES)
    yield


@pytest.fixture
def client():
    """Provide a FastAPI test client."""
    return TestClient(app_module.app)
