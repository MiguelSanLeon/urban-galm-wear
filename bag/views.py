from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if item_id in bag:
        if size:
            items_by_size = bag[item_id].setdefault('items_by_size', {})
            items_by_size[size] = items_by_size.get(size, 0) + quantity
        else:
            bag[item_id] += quantity
    else:
        if size:
            bag[item_id] = {'items_by_size': {size: quantity}}
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)