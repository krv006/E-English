import datetime

import pytest

from apps.models import Books
from apps.serializer import BooksModelSerializer
from apps.test.fixture import books_name


@pytest.mark.django_db
def test_serializer(books_name):
    books = {
        "id": 1,
        "name": 'Texnika',
        "created_at": datetime.datetime.now()
    }
    books1 = {
        "id": 2,
        "name": 'py',
        "created_at": datetime.datetime.now()
    }
    obj = BooksModelSerializer(data=books)
    obj1 = BooksModelSerializer(data=books1)
    assert obj.is_valid()
    assert obj1.is_valid()
    assert obj.validated_data['name'] == 'Texnika'


@pytest.mark.django_db
def test_deserializer():
    book = Books.objects.create(id=1, name='Texnika')
    data = BooksModelSerializer(book).data
    assert isinstance(data, dict)
    assert data['id'] == 1
    assert data['name'] == 'Texnika'
