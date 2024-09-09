from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken import views

from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('apps.urls')),

                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

                  path('api-token-auth/', views.obtain_auth_token),

              ] + static(MEDIA_URL, document_root=MEDIA_ROOT)
