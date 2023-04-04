from django.urls import path
from .views import VoucherList, VoucherDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('vouchers/', VoucherList.as_view(), name='voucher-list'),
    path('vouchers/<int:pk>/', VoucherDetail.as_view(), name='voucher-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
