# Generated by Django 4.2.4 on 2023-10-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='detail_image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
