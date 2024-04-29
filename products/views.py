from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, Category
from django.contrib import messages
from django.db.models.functions import Lower
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from products.models import Product
from profiles.models import UserProfile


def search_products(query):
    """ A helper function to search for products based on a query """
    return Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    wishlist = []

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    try:
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            wishlist = Product.objects.filter(user_wishlist=user_profile)
    except UserProfile.DoesNotExist:
        messages.error(request, "UserProfile does not exist for the authenticated user.")
        
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'wishlist': wishlist,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    user_profile = None
    wishlist = []
    
    try:
        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            wishlist = Product.objects.filter(user_wishlist=user_profile)
    except UserProfile.DoesNotExist:
        messages.error(request, "UserProfile does not exist for the authenticated user.")
    
    context = {
        'product': product,
        'wishlist': wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a Product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this action is allowed only for authorized users.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure all data entries are correct and valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a Product """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this action is allowed only for authorized users.')
        return redirect(reverse('home'))

    product =get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'The product { product.name } has been updated successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to update product { product.name }. Please check all data entries are correct')
    else:

        form = ProductForm(instance=product)
        messages.info(request, f'You are editing { product.name }')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@csrf_protect
@login_required
def delete_product(request, product_id):
    """ Delete a product """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, this action is allowed only for authorized users.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name

    if request.method == 'POST':
        try:
            product.delete()
            messages.success(request, f'The product "{product_name}" has been deleted successfully.')
            print(f'Redirecting to products page... {str(e)}')
            return redirect(reverse('products'))
        except Exception as e:
            messages.error(request, f'Error deleting product "{product_name}": {str(e)}')
   
    print('Redirecting to Home page...')
    return redirect(reverse('home'))
