from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from .views import categories_list, CommentsListAPIView, CommentDetailAPIView, categories_vouchers, vouchers_list, \
    vouchers_detail, \
    UsersListAPIView, UsersDetailAPIView, RegisterView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('categories/', categories_list),
    path('categories/<int:category_id>/', categories_vouchers),
    path('vouchers/', vouchers_list),
    path('vouchers/<int:voucher_id>/', vouchers_detail),
    path('vouchers/<int:voucher_id>/comments/', CommentsListAPIView.as_view()),
    path('vouchers/<int:voucher_id>/comments/<int:pk>/', CommentDetailAPIView.as_view()),
    path('users/', UsersListAPIView.as_view()),
    path('users/<int:pk>/', UsersDetailAPIView.as_view()),
    path('comments/', CommentsListAPIView.as_view()),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view()),
    path('api/register', RegisterView.as_view()),
    path('api/login', LoginView.as_view()),
]
