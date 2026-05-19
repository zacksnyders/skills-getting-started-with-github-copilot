import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_dict


@pytest.fixture
def client():
    """Provides a TestClient for the FastAPI app."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory `activities` dict before/after each test to ensure isolation."""
    original = copy.deepcopy(activities_dict)
    yield
    activities_dict.clear()
    activities_dict.update(original)
