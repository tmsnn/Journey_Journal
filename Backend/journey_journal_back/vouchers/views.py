from django.http import Http404, JsonResponse
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from .models import Voucher, Category, Comment, User
from .serializers import VoucherSerializer, CategorySerializer, CommentSerializer, UserSerializer


class Permission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.user and request.user.is_staff:
            return True
        else:
            return False


@api_view(['GET'])
def vouchers_list(request):
    vocuhers = Voucher.objects.all()
    serializers = VoucherSerializer(vocuhers, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def vouchers_detail(request, voucher_id):
    try:
        voucher = Voucher.objects.get(id=voucher_id)
    except Voucher.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    serializer = VoucherSerializer(voucher)
    return Response(serializer.data)


@api_view(['GET'])
def categories_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categories_vouchers(request, category_id):
    try:
        vouchers = Voucher.objects.filter(category=category_id)
    except Voucher.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
    serializer = VoucherSerializer(vouchers, many=True)
    return Response(serializer.data)


class UsersListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UsersDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CommentsListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_objects(self, voucher_id):
        try:
            return Comment.objects.filter(voucher=voucher_id)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, voucher_id=None):
        comments = self.get_objects(voucher_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, voucher_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(id=pk)
        except Comment.DoesNotExist as e:
            raise Http404

    def get(self, request, voucher_id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, voucher_id=None, pk=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, voucher_id=None, pk=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def LoginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vouchers') # replace 'home' with your desired URL
        else:
            error_msg = 'Invalid username or password'
            return redirect('vouchers')
    else:
        error_msg = ''
        return render(request, 'login.html', {'error_msg': error_msg})