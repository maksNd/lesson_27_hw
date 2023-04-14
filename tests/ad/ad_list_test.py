import pytest

from ads.serializers import AdSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_retrieve_ad(client):
    ad_list = AdFactory.create_batch(4)

    response = client.get(
        f'/ad/'
    )

    assert response.status_code == 200
    assert response.data == {
        'count': 4,
        'next': None,
        'previous': None,
        'results': AdSerializer(ad_list, many=True).data}
