from django.urls import path

from apps.views import CategoryListCreateAPIView, ProductListCreateAPIView

urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view()),
    path('products/', ProductListCreateAPIView.as_view())
]

