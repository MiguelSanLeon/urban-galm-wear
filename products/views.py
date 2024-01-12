from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q


def search_products(query):
    """ A helper function to search for products based on a query """
    return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))


def all_products(request):
    """ A view to show all products, sorting and search queries """

    query = request.GET.get('q')
    category_query = request.GET.get('category')
    sort_by = request.GET.get('sort', 'name')
    direction = request.GET.get('direction', 'asc')

    categories = None
    products = Product.objects.all()

    if category_query:
        categories = category_query.split(',')
        products = products.filter(category__name__in=categories)

    if query:
        products = search_products(query)
        if not products.exists():
            messages.warning(
                request, "No products match your search criteria.")

    if sort_by in ['name', 'price', 'rating', 'carbon_footprint']:
        if direction == 'asc':
            products = products.order_by(sort_by)
        else:
            products = products.order_by(f'-{sort_by}')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sort_by': sort_by,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
