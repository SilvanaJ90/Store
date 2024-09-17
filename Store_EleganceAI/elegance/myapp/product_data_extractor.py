import os
import sys
import django
from models import Product


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elegance.settings')

django.setup()


def get_product_data():
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category.id,
            'brand': product.brand,
            'color': product.color,
            'size': product.size,
            'image': product.image.url,
        })
    return data

