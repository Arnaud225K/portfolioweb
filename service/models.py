from django.db import models
from tinymce.models import HTMLField


# Model ----Service-----
class Service(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    service_name = models.CharField(max_length=255, verbose_name="Service", unique=True)
    title = models.CharField(max_length=255, verbose_name="Title", blank=True)
    description = HTMLField(verbose_name="Description", default="")
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)
    icon_name = models.CharField(max_length=128, verbose_name="Icon name (css)", default="")
    image = models.ImageField(upload_to='uploads/image', verbose_name="Image", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)	


    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.service_name
