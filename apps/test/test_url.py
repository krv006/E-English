import pytest

from rest_framework.reverse import reverse_lazy


class TestUrl:
    @pytest.mark.parametrize("url,name", [
        ('/api/v1/books/', 'apps:books-list'),
        ('/api/v1/units/', 'apps:units-list'),
        ('/api/v1/tests/', 'apps:tests-list'),

        ('/api/v1/user/', 'apps:user-create'),
        ('/api/v1/user/register/', 'apps:user_register'),
        ('/api/v1/user/verification/', 'apps:user_check'),

        ('/api/v1/admin/', 'apps:admin'),
        ('/api/v1/auth/send-email/', 'apps:send-email'),
        ('/api/v1/auth/verify-code/', 'apps:verify-email'),
    ])
    def test_url_name(self, url, name):
        assert url == reverse_lazy(name)
