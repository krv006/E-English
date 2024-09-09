from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserListCreateAPIView, BooksViewSet, UnitsViewSet, AdminSiteSettingsListCreateAPIView, TestViewSet, \
    SendEmailAPIView, VerifyEmailAPIView

router = DefaultRouter()

router.register(r'books', BooksViewSet)
router.register(r'units', UnitsViewSet)

router.register(r'tests', TestViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/', UserListCreateAPIView.as_view(), name='user'),
    path('admin/', AdminSiteSettingsListCreateAPIView.as_view(), name='admin'),
    path('auth/send-email', SendEmailAPIView.as_view(), name='send_email'),
    path('auth/verify-code', VerifyEmailAPIView.as_view(), name='verify-email'),

]
