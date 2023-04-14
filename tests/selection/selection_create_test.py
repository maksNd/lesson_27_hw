import pytest

from ads.serializers import SelectionSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_selection_create(client, user_with_access_token):
    user, token = user_with_access_token

    ad_list = AdFactory.create_batch(4)

    data = {
        "name": "test_selection",
        "items": [ad.pk for ad in ad_list]
    }

    expected_response = {
        "id": 1,
        "owner": user.username,
        "name": "test_selection",
        "items": [ad.pk for ad in ad_list]
    }

    response = client.post(
        '/selection/',
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION=f'Bearer {token}'
    )

    assert response.status_code == 201
    assert response.data == expected_response
