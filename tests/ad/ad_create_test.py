import pytest


@pytest.mark.django_db
def test_create(client, access_token):
    expected_response = {
        "id": 1,
        "category": None,
        "author": '1',
        "is_published": False,
        "name": "12345678910",
        "price": 10,
        "description": "1",
        "image": None
    }

    data = {
        "name": "12345678910",
        "price": 10,
        "description": "1"
    }

    response = client.post(
        '/ad/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {access_token}'
    )

    assert response.status_code == 201
    assert response.data == expected_response
