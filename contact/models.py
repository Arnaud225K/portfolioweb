from django.db import models

# Model ----Contact Me-----
class Contact(models.Model):
    name = models.CharField(max_length=255, verbose_name="Fullname", unique=True)
    email = models.EmailField(verbose_name="E-mail", max_length=50, default="")
    # type_client = models.CharField(verbose_name="Client", max_length=128, default='')
    subject = models.CharField(verbose_name="Subject", max_length=128, default='')
    message = models.TextField(verbose_name="Message", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'contact'

    def __str__(self):
        return self.name
