
from django.urls import path
from . import views
from .views import PaymentTemplateView,PricingTemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact.html', views.contact, name='contact'),
    path('about.html',views.about,name ='about'),
    path('services.html', views.about, name='services'),
    path('pricing.html',PricingTemplateView.as_view(),name = 'pricing'),
    path('payment/', PaymentTemplateView.as_view(), name='payment'),
    path('messagesent/',views.message_sent,name ='message'),
    path('appointmentreceived/', views.appointment, name='appointment')

]
