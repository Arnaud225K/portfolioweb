from django.db import models

# Model ----Post-----
class Post(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="Title", unique=True)
    description = models.CharField(max_length=1024, verbose_name="Description", blank=True)
    main_image = models.ImageField(upload_to='uploads/image', verbose_name="Main image", blank=True, null=True, editable=False)
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)	

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title

# Model ----Additionnal Image Post-----
class ImagePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/image', blank=True, null=True)

    def __str__(self):
        return self.post.title + "_image"
