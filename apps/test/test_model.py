# import pytest
#
# from apps.models import Books
#
#
# @pytest.mark.django_db
# def test_books():
#     Books.objects.create(name='Texnika')
#     book = Books.objects.get('Texnika')
#     assert book.name == 'Texnika'
#     assert book.id == 1
