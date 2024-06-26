from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import SubscriptionForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Subscriber


def subscribe(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if Subscriber.objects.filter(email=email).exists():
                messages.warning(request, 'This email is already subscribed.')
            else:
                subscriber = form.save()
                subject_templ = 'newsletter/email_subject.txt'
                body_templ = 'newsletter/email_body.html'

                subject = render_to_string(subject_templ).strip()
                body = render_to_string(body_templ, {'subscriber': subscriber})

                send_mail(
                    subject,
                    strip_tags(body),
                    'urbanglamwear@urb.com',
                    [subscriber.email],
                    fail_silently=False,
                    html_message=body
                )

                messages.success(request, 'Thank you for subscribing to our'
                                 'newsletter. You will receive a'
                                 ' Welcome email soon.')
                return redirect('home')

    context = {'form': form}
    return render(request, 'newsletter/subscribe.html', context)
