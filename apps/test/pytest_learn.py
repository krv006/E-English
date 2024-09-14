import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from apps.models import Books


@pytest.fixture()
def books():
    Books.objects.create(name='10 ta Negir bolasi')
    Books.objects.create(name='Choqinirgan ota')
    Books.objects.create(name='Shaxmat Doskasi')
    Books.objects.create(name='Janna Dark')
    Books.objects.create(name='Million dollorlik xatolar')


@pytest.mark.django_db
class TestView:
    def test_list_book(self, client):
        url = reverse('apps:books-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_book(self, client):
        url = reverse('apps:books-list')
        response = client.post(url, data={'name': 'Test Book', 'photo': 'sc'})
        assert response.status_code == status.HTTP_201_CREATED
