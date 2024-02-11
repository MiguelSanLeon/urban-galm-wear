from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from products.models import Product
from django.contrib import messages

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if item_id in bag:
        items_by_size = bag[item_id].setdefault('items_by_size', {})
        items_by_size[size] = items_by_size.get(size, 0) + quantity
        messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {items_by_size[size]}')
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(request, f'Added {size.upper()} {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust the quantity of a product in the bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {quantity}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {quantity}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove products from the bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST.get('product_size')
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
