from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.html import strip_tags

def send_confirmation_email(order):
    """
    Send a confirmation email to the customer
    """
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order}
    ).strip()

    # HTML version of the email body
    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.html',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    order_email_address = 'ugworders@gmail.com'

    
    # Send the email to the customer
    email_to_customer = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
    )
    email_to_customer.content_subtype = "html"  # Ensure HTML content is rendered correctly
    email_to_customer.send()

    # Send a copy of the email to the desired email address using BCC
    email_copy = EmailMessage(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [order_email_address],
    )
    email_copy.content_subtype = "html"  # Ensure HTML content is rendered correctly
    email_copy.send()
