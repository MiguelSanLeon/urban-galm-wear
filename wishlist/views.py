from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
from profiles.models import UserProfile


@login_required
def wishlist(request):
    user_profile = UserProfile.objects.get(user=request.user)
    products = Product.objects.filter(user_wishlist=user_profile)
    template = "wishlist/user_wishlist.html"
    context = {
        'wishlist': products,
    }
    return render(request, template, context)


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    user_profile = UserProfile.objects.get(user=request.user)
    if product.user_wishlist.filter(id=user_profile.id).exists():
        product.user_wishlist.remove(user_profile)
        messages.success(request, f'Removed {product.name}'
                         ' from your wishlist.')
    else:
        product.user_wishlist.add(user_profile)
        messages.success(request, f'Added {product.name}'
                         ' to your wishlist.')

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
