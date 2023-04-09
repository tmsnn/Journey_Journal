from django.urls import path
# from rest_framework_simplejwt import views as jwt_views
from .views import VoucherList, VoucherDetail, CategoryList, CategoryDetail, CommentsListAPIView, CommentDetailAPIView, \
    ManagerListAPIView, ManagerDetailAPIView, CommentsList

urlpatterns = [
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
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
