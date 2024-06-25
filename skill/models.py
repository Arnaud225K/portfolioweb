from django.db import models

ALIGNEMENT=[
    ('Left','Align Left'),
    ('Rigth','Align Rigth'),
]

# Model ----Skill-----
class Skill(models.Model):
    order_number = models.FloatField(verbose_name="Order number", blank=True, null=True)
    skill_name = models.CharField(max_length=255, verbose_name="Skill", unique=True)
    percent = models.CharField(max_length=50, verbose_name="Percent", blank=True)
    position = models.CharField(max_length=15,choices=ALIGNEMENT, default='Left')
    color = models.CharField(max_length=100, verbose_name="Color", blank=True)	
    is_hidden = models.BooleanField(verbose_name="Hide", blank=True, default=False)	


    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.skill_name
