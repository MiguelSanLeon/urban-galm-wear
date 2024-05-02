from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_confirmation_email(order):
    """
    Send a confirmation email to the customer
    """
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order}
    ).strip()

    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    send_mail(
        subject,
        strip_tags(body),  # Plain text version of the email body
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        html_message=body,  # HTML version of the email body
    )
