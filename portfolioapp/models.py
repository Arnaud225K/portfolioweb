from django.db import models
from tinymce.models import HTMLField


STATUS_OWNER=[
    ('Available','Available'),
    ('Not Available','Not Available'),
]
  
# Model ----Owner-----
class Owner(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Fullname", unique=True)
    degree = models.CharField(max_length=255, verbose_name="Degree")
    about_me = HTMLField(verbose_name="About me", default='')
    is_hidden = models.BooleanField(verbose_name="Hide" ,blank=True, default=False)	
    year_experience = models.CharField(max_length=255, verbose_name="Number of years experience")
    address = models.CharField(max_length=255, verbose_name="Address", blank=True, null=True)
    phone = models.CharField(max_length=50, verbose_name="Phone", blank=True, null=True)
    email = models.CharField(max_length=50, verbose_name="Email", blank=True, null=True)
    freelance=models.CharField(max_length=15,choices=STATUS_OWNER, default='Available')
    main_picture = models.ImageField(upload_to='uploads/picture', verbose_name="Picture", blank=True, null=True)
    
    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural = 'owner'

    def __str__(self):
        return self.fullname


# Model ----Function-----
class Function(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Function", unique=True)
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)
    comment = models.CharField(max_length=1024, verbose_name="Comment", blank=True, null=True, default="")

    class Meta:
        verbose_name = 'Function'
        verbose_name_plural = 'functions'

    def __str__(self):
        return self.name
    

    
# Model ----Social link-----
class Sociallink(models.Model):
    name = models.CharField(max_length=255, verbose_name="Social", unique=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)	
    icon_name = models.CharField(max_length=128, verbose_name="Icon name (css)", default="")
    link = models.CharField(max_length=1024, verbose_name="Link", default="")


    class Meta:
        verbose_name = 'Social link'
        verbose_name_plural = 'social links'

    def __str__(self):
        return self.name

# Model ----Language-----
class Language(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="Language name", unique=True)
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'languages'

    def __str__(self):
        return self.owner.fullname +  self.name + "_language"

# Model ----Additionnal Picture-----
class Picture(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='uploads/picture', blank=True, null=True)

    def __str__(self):
        return self.owner.fullname + "_picture"



# Model ----Review-----
class Review(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Reviewer", unique=True)
    profession = models.CharField(max_length=255, verbose_name="Profession", blank=True)
    company = models.CharField(max_length=255, verbose_name="Company", blank=True)
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)
    picture = models.ImageField(upload_to='uploads/image', verbose_name="Picture", blank=True, null=True)
    message = models.CharField(max_length=1024, verbose_name="Message", blank=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'review'

    def __str__(self):
        return self.name
    