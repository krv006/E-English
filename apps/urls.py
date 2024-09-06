from django.urls import path

from apps.views import AddressListCreateAPIView, CategoryOfEggsListCreateAPIView, CustomersListCreateAPIView, \
    CustomerStatisticsListCreateAPIView, EmployeesListCreateAPIView, OrderListCreateAPIView, \
    OrderRetrieveUpdateDestroyAPIView, AddressRetrieveUpdateDestroyAPIView, EmployeesRetrieveUpdateDestroyAPIView, \
    SendEmailAPIView, VerifyEmailAPIView

urlpatterns = [

    path('address/', AddressListCreateAPIView.as_view(), name='address'),
    path('address/<int:pk>', AddressRetrieveUpdateDestroyAPIView.as_view(), name='addre'),

    path('category-egg/', CategoryOfEggsListCreateAPIView.as_view()),

    path('customer/', CustomersListCreateAPIView.as_view()),
    path('customer-statistic/', CustomerStatisticsListCreateAPIView.as_view()),

    path('employees/', EmployeesListCreateAPIView.as_view()),
    path('employees/<int:pk>', EmployeesRetrieveUpdateDestroyAPIView.as_view()),

    path('order/', OrderListCreateAPIView.as_view()),
    path('order-detail/<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view()),

    path('auth/send-email', SendEmailAPIView.as_view(), name='send_email'),
    path('auth/verify-code', VerifyEmailAPIView.as_view(), name='verify-email'),
]
