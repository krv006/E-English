from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import UserListCreateAPIView, BooksViewSet, UnitsViewSet, AdminSiteSettingsListCreateAPIView, \
    TestViewSet, \
    SendEmailAPIView, VerifyEmailAPIView, SendEmail, VerificationCode

router = DefaultRouter()

app_name = 'apps'

router.register(r'books', BooksViewSet, basename='books')
router.register(r'units', UnitsViewSet, basename='units')
router.register(r'tests', TestViewSet, basename='tests')

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserListCreateAPIView.as_view(), name='user-create'),
    path('user/register/', SendEmail.as_view(), name='user_register'),
    path('user/verification/', VerificationCode.as_view(), name='user_check'),

    path('admin/', AdminSiteSettingsListCreateAPIView.as_view(), name='admin'),
    path('auth/send-email/', SendEmailAPIView.as_view(), name='send-email'),
    path('auth/verify-code/', VerifyEmailAPIView.as_view(), name='verify-email'),

]
