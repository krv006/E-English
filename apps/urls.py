from django.urls import path

from apps.views import AddressListCreateAPIView, CategoryOfEggsListCreateAPIView, CustomersListCreateAPIView, \
    CustomerStatisticsListCreateAPIView, EmployeesListCreateAPIView, OrderListCreateAPIView, \
    OrderRetrieveUpdateDestroyAPIView

urlpatterns = [

    path('address/', AddressListCreateAPIView.as_view()),

    path('category-egg/', CategoryOfEggsListCreateAPIView.as_view()),

    path('customer/', CustomersListCreateAPIView.as_view()),
    path('customer-statistic/', CustomerStatisticsListCreateAPIView.as_view()),

    path('employees/', EmployeesListCreateAPIView.as_view()),

    path('order/', OrderListCreateAPIView.as_view()),
    path('order-detail/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view()),
]
