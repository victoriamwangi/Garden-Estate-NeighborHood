# Generated by Django 4.0.5 on 2022-06-17 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0003_alter_post_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='neighborhood',
        ),
        migrations.DeleteModel(
            name='Neighborhood',
        ),
    ]
