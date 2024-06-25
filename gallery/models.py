from django.db import models
from tinymce.models import HTMLField


# Model ----TypePorfolio-----
class TypePorfolio(models.Model):
    name = models.CharField(max_length=255, verbose_name="Type Porfolio", unique=True)
    description = models.CharField(max_length=1024, verbose_name="Description", blank=True, null=True, default="")

    class Meta:
        verbose_name = 'Type Porfolio'
        verbose_name_plural = 'Types Porfolio'

    def __str__(self):
        return self.name
    

# Model ----Portfolio-----
class Portfolio(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    type_porfolio = models.ForeignKey(TypePorfolio, verbose_name="Type porfolio", related_name='type_porfolio_set', on_delete=models.CASCADE)
    # name = models.CharField(max_length=255, verbose_name="Portfolio", unique=True)
    title = models.CharField(max_length=255, verbose_name="Title", blank=True)
    description = HTMLField(verbose_name="Description", default="")
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)	
    main_image = models.ImageField(upload_to='uploads/image', verbose_name="Main image", blank=True, null=True)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'portfolio'

    def __str__(self):
        return self.title
    
# Model ----Additionnal Image gallery-----
class ImageGallery(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/image', blank=True, null=True)

    def __str__(self):
        return self.portfolio.title + "_image"
