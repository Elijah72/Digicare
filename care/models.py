from django.db import models

# Create your models here.
class Appointment(models.Model):
    appointment_name = models.CharField(max_length=20)
    appointment_email =models.CharField(max_length=20)
    date =models.CharField(max_length=20)
    appointment_message=models.TextField(blank=True)
    appointment_time =models.CharField(max_length=20)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date =models.DateField(auto_now_add=False,null=True,blank=True)

    def __str__(self):
        return self.appointment_name
    class Meta:
        ordering = ['-accepted']

class Plan(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)

    def __str__(self):
        return  str(self.name)


