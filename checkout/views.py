from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(reuqest, "there's nothing in your baf at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template =  'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)