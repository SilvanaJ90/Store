"""
URL configuration for elegance project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from myapp.views import index, cart, dashboard, order_complete, place_order,register, search_result, signin, store, product_detail, categories, products, get_products, CategoryListView,  CommentCreateView


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
    path('index', index, name='home'), 
    path('', index, name='index'), # Path to the server root
    path('cart/', cart, name='cart'),
    path('admin-categories/', categories, name='admin_categories'),
    
    path('categories/<int:category_id>/products/', get_products, name='get_products'),

    path('admin-products/', products, name='admin_products'),
    path('dashboard/', dashboard, name='dashboard'),
    path('order-complete/', order_complete, name='order_complete'),
    path('place-order/', place_order, name='place_order'),
    path('product-detail/', product_detail, name='product_detail'),
    path('product/<int:product_id>/', product_detail, name='product-detail'),
    path('register/', register, name='register'),
    path('search-result/', search_result, name='search_result'),
    path('signin/', signin, name='signin'),
    path('store/', store, name='store'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('myapp.urls')),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('products/<int:product_id>/comments/', CommentCreateView.as_view(), name='add-comment'),

    # Routes for documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

