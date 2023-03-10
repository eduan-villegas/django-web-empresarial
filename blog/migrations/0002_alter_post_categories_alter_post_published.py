# Generated by Django 4.1.3 on 2023-03-07 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_posts', to='blog.category', verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 5, 52, 6, 988296, tzinfo=datetime.timezone.utc), verbose_name='Fecha de publicacion'),
        ),
    ]
