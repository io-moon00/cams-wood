from django.db import models
from django.utils.html import mark_safe

# Create your models here.

POSITIONS = [
    ('center', 'Center'),
    ('top', 'Top'),
    ('bottom', 'Bottom'),
    ('left', 'Left'),
    ('right', 'Right'),
]

class Image(models.Model):
    img = models.ImageField(upload_to='media/uploads')
    img_alt = models.CharField(max_length=50, blank=True)
    subtitle = models.TextField(blank=True)
    img_position = models.CharField(max_length=20, choices=POSITIONS, default='center')

    def __str__(self):
        return self.subtitle

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')

class Page(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField(blank=False)
    img = models.ImageField(upload_to='uploads', null=True, blank=True)
    img_alt = models.CharField(max_length=50, blank=True)
    img_position = models.CharField(max_length=20, choices=POSITIONS, default='center')

    def img_preview(self): 
        return mark_safe(f'<img src = "{self.img.url}" width = "200"/>')    

    def __str__(self):
        return self.title
    


    

