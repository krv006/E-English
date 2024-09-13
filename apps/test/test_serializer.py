from django.contrib.auth import get_user_model
from django.test import TestCase
from apps.serializer import UserModelSerializer

User = get_user_model()  # TODO Custom User modelini olish


class TestUserModelSerializer(TestCase):
    def setUp(self):
        User.objects.create_user(email='abdulloh@gmail.com', password='ASAssd232')
        User.objects.create_user(email='kamron@gmail.com', password='ASDASsdadfssas123')

    def test_get_user(self):
        obj = User.objects.get(email='abdulloh@gmail.com')
        data = UserModelSerializer(obj).data
        assert isinstance(data, dict)
        assert data['email'] == 'abdulloh@gmail.com'
        assert obj.check_password('ASAssd232')
