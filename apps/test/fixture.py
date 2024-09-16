import pytest

from apps.models import Books


@pytest.fixture()
def books_name():
    Books.objects.create(name='Texnika')
    Books.objects.create(name='Choqinirgan ota')
    Books.objects.create(name='Shaxmat Doskasi')
    Books.objects.create(name='Janna Dark')
    Books.objects.create(name='Million dollorlik xatolar')
