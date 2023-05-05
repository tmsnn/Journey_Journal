from django.http import Http404, JsonResponse
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
import jwt,datetime
from django.db.models import Q

from .models import Voucher, Category, Comment, User, Favorite
from .serializers import VoucherSerializer, CategorySerializer, CommentSerializer, UserSerializer, FavoritesSerializer


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

@api_view(['GET', 'POST'])
def favorite_list(request):
    if request.method == 'GET':
        favorites = Favorite.objects.all()
        serializer = FavoritesSerializer(favorites, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FavoritesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
def get_favorite_by_voucher(request,id):
    if request.method == 'GET':
        voucher_obj = Voucher.objects.get(id=id)
        favorites_obj = Favorite.objects.filter(voucher=voucher_obj)
        favorites = FavoritesSerializer(favorites_obj,many=True)

        return Response(favorites.data)
    if request.method == 'DELETE':
        try:
            voucher_obj = Voucher.objects.get(id=id)
            favorite = Favorite.objects.filter(voucher=voucher_obj)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def get_favorites_by_user(request,id):
    if request.method == 'GET':
        user_obj = User.objects.get(id=id)
        favorites_obj = Favorite.objects.filter(user=user_obj)
        favorites = FavoritesSerializer(favorites_obj,many=True)

        return Response(favorites.data)




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


class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(Q(username=username) & Q(password=password)).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'id':user.id,
            'username':user.username
        }
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response