from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from myapp.views import (
    index, cart, dashboard, order_complete, place_order, register, search_result, signin, store, 
    product_detail, get_products, get_comments_by_product, get_all_comments,
    post_category, get_category, put_category, delete_category, post_product, put_product, delete_product, 
    get_all_products, get_user, delete_user, register_user, login, protected, logout, get_users, get_product,
    get_all_categories, qa_admin
)
from myapp.chatbot_views import ask_question


# Define the API schema
schema_view = get_schema_view(
    openapi.Info(
        title="Elegance API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Home and static pages
    path('', index, name='index'),  # Path to the server root
    path('cart/', cart, name='cart'),
    path('dashboard/', dashboard, name='dashboard'),
    path('order-complete/', order_complete, name='order-complete'),
    path('place-order/', place_order, name='place_order'),
    path('product/<int:product_id>/', product_detail, name='product-detail'),
    path('register/', register, name='register'),
    path('search-result/', search_result, name='search_result'),
    path('signin/', signin, name='signin'),
    path('store/', store, name='store'),
    path('qa_admin/', qa_admin, name='qa_admin'),
  

    # API routes
    path('api/v1/categories/create/', post_category, name='post_category'),  # Create a category (POST)
    path('api/v1/categories/<int:category_id>/', get_category, name='get_category'),  # Get a specific category (GET)
    path('api/v1/categories/<int:category_id>/update/', put_category, name='put_category'),  # Update a specific category (PUT)
    path('api/v1/categories/<int:category_id>/delete/', delete_category, name='delete_category'),  # Delete a specific category (DELETE)
    path('api/v1/categories/<int:category_id>/products/', get_products, name='get_products'),  # Get products by category (GET)
    path('api/v1/categories/<int:category_id>/products/create/', post_product, name='post_product'),  # Create a product in a category (POST)
    path('api/v1/categories/', get_all_categories, name='get_all_categories'),
    path('api/v1/products/', get_all_products, name='get_all_products'),  # Get all products (GET)
    path('api/v1/products/<int:product_id>/', get_product, name='get_product'),  # Get a specific product (GET)
    path('api/v1/products/<int:product_id>/update/', put_product, name='put_product'),  # Update a specific product (PUT)
    path('api/v1/products/<int:product_id>/delete/', delete_product, name='delete_product'),  # Delete a specific product (DELETE)
    path('api/v1/products/<int:product_id>/comments/', get_comments_by_product, name='get_comments_by_product'),  # Get comments for a product (GET)
    path('api/v1/comments/', get_all_comments, name='get_all_comments'),  # Get all comments (GET)
   
    # User management
    path('api/v1/users/', get_users, name='get_users'),  # Get all users (GET)
    path('api/v1/users/<int:user_id>/', get_user, name='get_user'),  # Get a specific user (GET)
    path('api/v1/users/<int:user_id>/delete/', delete_user, name='delete_user'),  # Delete a specific user (DELETE)
    path('api/v1/users/register/', register_user, name='register_user'),  # Register a new user (POST)
    path('api/v1/users/login/', login, name='login'),  # User login (POST)

    # Authentication
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token obtain (POST)
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh (POST)

    # Routes for documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Admin
    path('api/v1/', include('myapp.urls')),

    path('ask_question/', ask_question, name='ask_question'),

    # Media files
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
