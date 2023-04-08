from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Voucher, Category, Comment, Manager
from .serializers import VoucherSerializer, CategorySerializer, CommentSerializer, ManagerSerializer


class Permission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.user and request.user.is_staff:
            return True
        else:
            return False


class VoucherList(APIView):
    def get(self, request):
        vouchers = Voucher.objects.all()
        serializer = VoucherSerializer(vouchers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VoucherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = (Permission,)


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (Permission,)


class ManagerListAPIView(APIView):
    def get(self, request):
        users = Manager.objects.all()
        serializer = ManagerSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    permission_classes = (permissions.IsAdminUser,)


class ManagerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Manager.objects.get(id=pk)
        except Manager.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        user = self.get_object(pk)
        serializer = ManagerSerializer(user)
        return Response(serializer.data)

    permission_classes = (permissions.IsAdminUser,)


class CommentsListAPIView(APIView):
    def get(self, request, pk):
        comments = Comment.objects.filter(voucher_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (Permission,)


class CommentsList(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (Permission,)


class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(id=pk)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=None, pk=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)