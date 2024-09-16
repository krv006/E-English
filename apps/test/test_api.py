from os.path import join

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.reverse import reverse
from django.test.client import Client

from apps.test.fixture import books_name
from root.settings import BASE_DIR

@pytest.mark.django_db
def test_book_create(client: Client):
    path = reverse("apps:books-list")
    with open(join(BASE_DIR , "apps" , "img.png"), "rb") as f:
        file = SimpleUploadedFile(
            "rasm.png" , f.read() , content_type="image/png"
        )
    data = {
        "name" : "Essential 1",
        "image" : file
    }

    response = client.post(path , data=data, format = "multipart")
    assert response.status_code == 201
    assert response.data['id'] == 1