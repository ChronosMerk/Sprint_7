import pytest

@pytest.fixture
def auth_payload():
    return {"login": "test235", "password": "test1234"}