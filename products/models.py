from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from paypal.standard.forms import PayPalPaymentsForm
import uuid


# Create your models here.
class Product(models.Model):
    image = models.ImageField(upload_to="../media/images")
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    price = models.IntegerField()

    def __unicode__(self):
        return self.title

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.title,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

