from django.urls import path
from .views import VoucherList, VoucherDetail, CategoryList, CategoryDetail, CommentsListAPIView, CommentDetailAPIView, \
    ManagerListAPIView, ManagerDetailAPIView, CommentsList

urlpatterns = [
    path('vouchers/', VoucherList.as_view(), name='voucher-list'),
    path('vouchers/<int:pk>/', VoucherDetail.as_view(), name='voucher-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('vouchers/<int:pk>/comments/', CommentsListAPIView.as_view()),
    path('vouchers/<int:pk>/comments/<int:id>/', CommentDetailAPIView.as_view()),
    path('managers/', ManagerListAPIView.as_view()),
    path('managers/<int:pk>/', ManagerDetailAPIView.as_view()),
    path('comments/', CommentsList.as_view()),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view())
]
