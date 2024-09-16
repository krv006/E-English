import pytest

from apps.models import Books


@pytest.fixture()
def categories():
    Books.objects.create(name='Texnika')
    Books.objects.create(name='Choqinirgan ota')
    Books.objects.create(name='Shaxmat Doskasi')
    Books.objects.create(name='Janna Dark')
    Books.objects.create(name='Million dollorlik xatolar')


@pytest.mark.django_db
def test_my_user(categories):
    books = Books.objects.get(name='Texnika')
    assert books.name == 'Texnika'
    assert books.id == 1
