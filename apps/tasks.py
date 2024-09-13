from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from random import randint
from django.core.cache import cache


# celery send email
@shared_task
def send_verification_email_task(email, code):
    send_mail(
        subject="HI",
        message=f"Hello My Friend Your Verify Code {code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    return "Email sent"


@shared_task
def send_verification_email1(receiver_email):
    generate_code = randint(1000, 9999)
    send_mail(
        "Verification Code",
        f"code: {generate_code}",
        settings.EMAIL_HOST_USER,
        [receiver_email]
    )
    cache.set(receiver_email, generate_code, timeout=120)
    return "Check Email"
