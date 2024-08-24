from django.urls import path
from .views import CategoryListView, CategoryDetailView, post_category
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/create/', post_category, name='category-create'),
    path('categories/<int:category_id>/products/', views.get_products, name='get_products'),
    path('products/', views.get_all_products, name='get_all_products'),
    path('products/<int:product_id>/', views.get_product, name='get_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('categories/<int:category_id>/products/create/', views.post_product, name='post_product'),
    path('products/<int:product_id>/update/', views.put_product, name='put_product'),
    path('users/', views.get_users, name='get_users'),
    path('users/<int:user_id>/', views.get_user, name='get_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('users/register/', views.register_user, name='register_user'),
    path('users/login/', views.login, name='login'),
    path('protected/', views.protected, name='protected'),
    path('logout/', views.logout, name='logout'),
]
