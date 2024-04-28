
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from newsletter.forms import SubscriptionForm


def index(request):
    """ A view to return the index page """
    form = SubscriptionForm()
    return render(request, 'home/index.html', {'form': form})


def about_us(request):
    """ A view to return the about us page """

    return render(request, 'home/about_us.html')


def privacy_policy(request):
    """ A view to return the privacy policy page """

    return render(request, 'home/privacy_policy.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Thank You. Your Message Was Successfully Sent!')
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'home/contact_us.html', context)

    contact_form = ContactForm(data=request.POST)
    if contact_form.is_valid():
            contact_form.instance.email = request.user.email
            contact_form.instance.name = request.user.username
            contact = contact_form.save(commit=False)
            contact.article = article
            contact.save()
    else:
            contact_form = ContactForm()

    return render(
            {
                "contact_form": contact_form
            },
        )
