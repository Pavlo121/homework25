from typing import List
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .models import Product, Order, CartItem
from .schemas import ProductIn, ProductOut, OrderIn, OrderOut

ninja_api = NinjaAPI()

@ninja_api.post("/products/", response=ProductOut)
def create_product(request, product: ProductIn):
    product_obj = Product.objects.create(**product.dict())
    return ProductOut.from_orm(product_obj)

@ninja_api.get("/products/", response=List[ProductOut])
def list_products(request):
    products = Product.objects.all()
    return products

@ninja_api.get("/products/{product_id}", response=ProductOut)
def get_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    return product

@ninja_api.put("/products/{product_id}", response=ProductOut)
def update_product(request, product_id: int, product: ProductIn):
    product_obj = get_object_or_404(Product, id=product_id)
    for key, value in product.dict().items():
        setattr(product_obj, key, value)
    product_obj.save()
    return product_obj

@ninja_api.delete("/products/{product_id}", response={204: None})
def delete_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return 204

# Операції з замовленнями
@ninja_api.post("/orders/", response=OrderOut)
def create_order(request, order: OrderIn):
    new_order = Order.objects.create(customer_name=order.customer_name)
    for item in order.items:
        product = get_object_or_404(Product, id=item['product_id'])
        CartItem.objects.create(order=new_order, product=product, quantity=item['quantity'])
    return new_order

@ninja_api.get("/orders/{order_id}", response=OrderOut)
def get_order(request, order_id: int):
    order = get_object_or_404(Order, id=order_id)
    return order

@ninja_api.put("/orders/{order_id}", response=OrderOut)
def update_order_status(request, order_id: int, status: str):
    order = get_object_or_404(Order, id=order_id)
    order.status = status
    order.save()
    return order
