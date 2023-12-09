from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.views.generic import TemplateView
from django_daraja.mpesa.core import MpesaClient
from django.conf import settings
from .models import Appointment


# Create your views here.
def home(request):
    if request.method == "POST":
        appointment_name = request.POST['appointment_name']
        appointment_email = request.POST['appointment_email']
        date = request.POST['date']
        appointment_time = request.POST['appointment_time']
        appointment_message = request.POST['appointment_message']

        appointment = Appointment.objects.create(
            appointment_name=appointment_name,
            appointment_email=appointment_email,
            date=date,
            appointment_time=appointment_time,
            appointment_message=appointment_message
        )

        return HttpResponse("Appointment received")
    else:
        return render(request, template_name="home.html")


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        unmessage = 'unmessage' in request.POST and request.POST['unmessage']

        email = EmailMessage(
            subject=f"{message_subject} ",
            body=unmessage,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[message_email]
        )
        email.send()
        return HttpResponse("Email Sent Successfull")
    else:
        return render(request, template_name="contact.html")


def about(request):
    return render(request, template_name='about.html')


def services(request):
    return render(request, template_name='services.html')


class PaymentTemplateView(TemplateView):
    template_name = 'payment.html'

    def post(self, request):
        phone_numbers = request.POST.get("phone_number")

        cl = MpesaClient()
        # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
        phone_number = phone_numbers
        amount = 1
        account_reference = 'reference'
        transaction_desc = 'Description'
        callback_url = 'https://api.darajambili.com/express-payment';
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

        return HttpResponse(response)


def stk_push_callback(request):
    data = request.body

    return HttpResponse("STK Push in Django👋")


class PricingTemplateView(TemplateView):
    template_name = 'pricing.html'
