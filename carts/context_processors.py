# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from django.core.exceptions import ObjectDoesNotExist
from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    cart_items = []

    if 'admin' in request.path:
        return {}

    try:
        # For authenticated users
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            # For non-authenticated users
            cart_id = _cart_id(request)
            cart = Cart.objects.filter(cart_id=cart_id).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart)

        # Count total quantity of items in the cart
        cart_count = sum(item.quantity for item in cart_items)
    except ObjectDoesNotExist:
        cart_count = 0

    return {
        'cart_count': cart_count,
        'cart_items': cart_items  # Include cart_items to access in navbar
    }
