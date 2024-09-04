from django.urls import path
from . import views
from .views import post_category, get_category, put_category, delete_category, get_all_categories

urlpatterns = [
    path('', views.index, name='home'),
    
    # Routes to manage categories using decorators
    path('categories/create/', post_category, name='post_category'),
    path('categories/<int:category_id>/', get_category, name='get_category'),
    path('categories/<int:category_id>/update/', put_category, name='put_category'),
    path('categories/<int:category_id>/delete/', delete_category, name='delete_category'),
    path('categories/', get_all_categories, name='get_all_categories'),
    
    
    # Routes for handling products
    path('categories/<int:category_id>/products/', views.get_products, name='get_products'),
    path('categories/<int:category_id>/products/create/', views.post_product, name='post_product'),
    path('products/', views.get_all_products, name='get_all_products'),
    path('products/<int:product_id>/', views.get_product, name='get_product'),
    path('products/<int:product_id>/update/', views.put_product, name='put_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    # Routes for handling comments
    path('comments/', views.get_all_comments, name='get_all_comments'),
    path('comments/<int:product_id>/', views.get_comments_by_product, name='get_comments_by_product'),

    # Routes to manage users
    path('users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/register/', views.register_user, name='register_user'),
    path('users/login/', views.login, name='login'),
    
    # Additional routes
    path('protected/', views.protected, name='protected'),
    path('logout/', views.logout, name='logout'),

]
