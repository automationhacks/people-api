from unittest.mock import patch

import pytest
import requests
from assertpy.assertpy import assert_that

from users.mocks import get_free_port, start_mock_server
from users.services import get_users


@pytest.fixture
def mock():
    mock_server_port = get_free_port()
    start_mock_server(mock_server_port)
    yield mock_server_port


def test_request_response(mock):
    mock_users_url = f'http://localhost:{mock}/users'

    # The patch.dict() function temporarily replaces the value of the USERS_URL variable. In fact, it does
    # so only within the scope of the with statement. After that code runs, the USERS_URL variable is
    # restored to its original value. This code patches the URL to use the mock server address.
    with patch.dict('users.services.__dict__', {'USERS_URL': mock_users_url}):
        response = get_users()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    assert_that(response.headers).contains_entry({'Content-Type': 'application/json; charset=utf-8'})

    response_json = response.json()
    assert_that(response_json).is_instance_of(list)
    assert_that(response_json).is_empty()
