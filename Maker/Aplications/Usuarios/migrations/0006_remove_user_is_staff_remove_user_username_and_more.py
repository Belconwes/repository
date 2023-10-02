# Generated by Django 4.2.4 on 2023-10-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_user_is_staff_alter_user_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='User_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='User name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, verbose_name='password'),
        ),
    ]