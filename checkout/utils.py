from django.template.loader import render_to_string
from django.core.mail import send_mail
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
    html_body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.html',
        {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    )

    # Plain text version of the email body
    plain_text_body = strip_tags(html_body)

    send_mail(
        subject,
        plain_text_body,
        settings.DEFAULT_FROM_EMAIL,
        [order.email],
        html_message=html_body,
    )