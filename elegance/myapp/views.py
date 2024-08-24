from django.shortcuts import render

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .models import Product, Category, User
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse



def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


class CategoryListView(APIView):
    """
    Retrieves the list of all category objects
    """
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryDetailView(APIView):
    """
    Retrieves, updates, or deletes a specific category
    """
    def get_object(self, category_id):
        try:
            return Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found")

    def get(self, request, category_id, *args, **kwargs):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, category_id, *args, **kwargs):
        category = self.get_object(category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, category_id, *args, **kwargs):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def post_category(request):
    """
    Creates a category
    """
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_products(request, category_id):
    """
    Retrieves the list of all products objects of a specific category.
    """
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_products(request):
    """ Consult all the products """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, product_id):
    """
    Retrieves a specific product based on id
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_product(request, product_id):
    """
    Deletes a product based on id provided
    """
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def post_product(request, category_id):
    """
    Creates a product
    """
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(category=category)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_product(request, product_id):
    """
    Updates a product
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    """ Retrieves the list of all user objects """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, user_id):
    """ Retrieves a specific user """
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_user(request, user_id):
    """ Deletes a user """
    try:
        user = User.objects.get(pk=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def register_user(request):
    """ Registers a new user """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'User created',
            'access_token': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    """ User login """
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'User authenticated',
            'access_token': str(refresh.access_token),
            'is_user': user.is_user
        }, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def protected(request):
    """ Protected route """
    user_id = request.user.id
    try:
        user = User.objects.get(pk=user_id)
        if user.is_user:
            return Response({'message': 'Welcome to the user area!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Welcome to the admin area!'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def logout(request):
    """ User logout """
    response = Response({'logout': True}, status=status.HTTP_200_OK)
    response.delete_cookie('access_token')
    return response
