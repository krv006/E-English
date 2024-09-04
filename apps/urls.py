from django.urls import path

from apps.views import CategoryListCreateAPIView, ProductListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, \
    ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view())
]
