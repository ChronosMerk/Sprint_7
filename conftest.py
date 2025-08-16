import pytest
from data import URLS

@pytest.fixture(scope="session")
def base_url_courier():
    return URLS.BASE_URL + URLS.COURIER_URL

@pytest.fixture(scope="session")
def base_url_order():
    return URLS.BASE_URL + URLS.ORDERS_URL

@pytest.fixture
def auth_payload():
    return {"login": "test235", "password": "test1234"}