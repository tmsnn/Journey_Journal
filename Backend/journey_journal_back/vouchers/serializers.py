from rest_framework import serializers
from .models import Voucher, Category, User, Comment, Favorite
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100, allow_blank=True)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

class VoucherSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    rate = serializers.CharField(max_length=300, allow_blank=True)
    img = serializers.CharField(max_length=300, allow_blank=True)
    like = serializers.IntegerField(default=0)
    price = serializers.FloatField()
    category = CategorySerializer()

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category = Category.objects.create(**category_data)
        voucher = Voucher.objects.create(category=category, **validated_data)
        return voucher

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category')
        category_serializer = CategorySerializer(instance.category, data=category_data)
        if category_serializer.is_valid():
            category = category_serializer.save()
        else:
            raise serializers.ValidationError(category_serializer.errors)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.img = validated_data.get('img', instance.img)
        instance.like = validated_data.get('like', instance.like)
        instance.price = validated_data.get('price', instance.price)
        instance.category = category
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'







# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=300)
#     password = serializers.CharField(max_length=300)
#
#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')
#
#         user = authenticate(username=username, password=password)
#         if not user:
#             raise serializers.ValidationError('Invalid credentials')
#
#         token, created = Token.objects.get_or_create(user=user)
#         data['token'] = token.key
#         return data
