# Generated by Django 4.2.7 on 2023-11-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_image_img_alt_page_img_page_img_alt'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_position',
            field=models.CharField(choices=[('center', 'Center'), ('top', 'Top'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], default='center', max_length=20),
        ),
        migrations.AddField(
            model_name='page',
            name='img_position',
            field=models.CharField(choices=[('center', 'Center'), ('top', 'Top'), ('bottom', 'Bottom'), ('left', 'Left'), ('right', 'Right')], default='center', max_length=20),
        ),
    ]
