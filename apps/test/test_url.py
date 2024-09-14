from rest_framework.reverse import reverse_lazy


class TestUrl:
    def test_auth_url(self, client):
        url = reverse_lazy('send-email')
        assert url == '/api/v1/auth/send-email/'
        url = reverse_lazy('verify-email')
        assert url == '/api/v1/auth/verify-code/'

    def test_user_url(self, client):
        url = reverse_lazy('user-create')
        assert url == '/api/v1/user/'

    def test_auth_url1(self, client):
        url = reverse_lazy('user_register')
        assert url == '/api/v1/user/register/'
        url = reverse_lazy('user_check')
        assert url == '/api/v1/user/verification//'
