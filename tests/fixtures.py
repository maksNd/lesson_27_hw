import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = '1'
    password = 'pass'
    birth_date = '2000-1-1'
    role = 'admin'

    django_user_model.objects.create_user(
        username=username, password=password, birth_date=birth_date, role=role
    )

    response = client.post(
        '/user/token/',
        {'username': username, 'password': password},
        format='json'
    )

    return response.data['access']


@pytest.fixture
@pytest.mark.django_db
def user_with_access_token(client, django_user_model):
    username = '1'
    password = 'pass'
    birth_date = '2000-1-1'
    role = 'admin'

    test_user = django_user_model.objects.create_user(
        username=username, password=password, birth_date=birth_date, role=role
    )

    response = client.post(
        '/user/token/',
        {'username': username, 'password': password},
        format='json'
    )

    return test_user, response.data['access']
