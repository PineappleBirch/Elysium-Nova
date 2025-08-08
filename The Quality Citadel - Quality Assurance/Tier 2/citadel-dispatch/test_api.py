import requests
import pytest

# Defining the base URL for the API under test
BASE_URL = "https://jsonplaceholder.typicode.com"


# Note: All test cases and assertions in this file are designed based on the
# public API documentation and observed responses from https://jsonplaceholder.typicode.com/

def test_get_users_returns_200():
    """
    Verifies that making a GET request to the /users endpoint
    returns a successful 200 OK status code.
    """
    # Sending a GET request to the /users endpoint
    response = requests.get(f"{BASE_URL}/users")

    # Asserting that the status code is 200 (OK)
    assert response.status_code == 200


def test_get_users_response_contains_correct_data():
    """
    Verifies that the response body for the /users endpoint
    contains the expected data structure and values.
    """
    # Sending a GET request to the /users endpoint
    response = requests.get(f"{BASE_URL}/users")

    # Converting the JSON response into a Python list of dictionaries
    response_data = response.json()

    # Asserting that the response is a list of 10 users
    assert isinstance(response_data, list)
    assert len(response_data) == 10
    # Asserting that the first user in the list has an 'email' key
    assert "email" in response_data[0]


def test_create_post_returns_201():
    """
    Verifies that making a POST request to the /posts endpoint
    successfully creates a post and returns a 201 Created status code.
    """
    # Defining the payload for the new post
    payload = {
        "title": "Elysium Nova",
        "body": "API Test",
        "userId": 1
    }

    # Sending a POST request to create the post
    response = requests.post(f"{BASE_URL}/posts", json=payload)

    # Asserting that the status code is 201 (Created)
    assert response.status_code == 201

    # Asserting that the response contains the data we sent
    response_data = response.json()
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]