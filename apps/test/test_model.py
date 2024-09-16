import pytest

from apps.models import Books
from apps.test.fixture import books_name


@pytest.mark.django_db
def test_my_user(books_name):
    books = Books.objects.get(name='Texnika')
    assert books.name == 'Texnika'
    assert books.id == 1
