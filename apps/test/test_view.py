import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestView:
    def test_list_book(self, client):
        url = reverse('apps:books-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_book(self, client):
        url = reverse('apps:books-list')
        response = client.post(url, data={'name': 'Test Book'})
        assert response.status_code == status.HTTP_201_CREATED
