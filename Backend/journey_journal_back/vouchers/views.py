from rest_framework import generics, permissions
from .models import Voucher, Category
from .serializers import VoucherSerializer, CategorySerializer


class VoucherList(generics.ListCreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = (permissions.AllowAny,)


class VoucherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = (permissions.AllowAny,)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
