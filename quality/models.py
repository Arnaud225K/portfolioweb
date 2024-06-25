from django.db import models
from tinymce.models import HTMLField


  
# Model ----TypeQuality-----
class TypeQuality(models.Model):
    name = models.CharField(max_length=255, verbose_name="Type Quality", unique=True)
    comment = models.CharField(max_length=1024, verbose_name="Comment", blank=True, null=True, default="")

    class Meta:
        verbose_name = 'Type Quality'
        verbose_name_plural = 'Types Quality'

    def __str__(self):
        return self.name
    

# Model ----Quality-----
class Quality(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    quality_name = models.CharField(max_length=255, verbose_name="Quality", unique=True)
    type_quality = models.ForeignKey(TypeQuality, verbose_name="Type Quality", related_name='type_quality_owner_set', default="", on_delete=models.CASCADE)
    location = models.CharField(max_length=255, verbose_name="Place", blank=True, null=True)
    started_at = models.DateField(verbose_name='Start date', blank=True, null=True)
    ended_at = models.DateField(verbose_name='End date', blank=True, null=True)
    description = HTMLField(verbose_name="Description", default='')
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)	
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Quality'
        verbose_name_plural = 'quality'

    def __str__(self):
        return self.quality_name
