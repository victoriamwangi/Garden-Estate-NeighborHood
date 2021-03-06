# Generated by Django 4.0.5 on 2022-06-19 12:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('occupants_count', models.IntegerField(blank=True, default=0, null=True)),
                ('health_contact', models.CharField(blank=True, max_length=20)),
                ('police_contact', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('prof_image', models.ImageField(default='default.png', upload_to='profiles/')),
                ('bio', models.CharField(blank=True, max_length=30, null=True)),
                ('first_name', models.CharField(max_length=40, null=True)),
                ('second_name', models.CharField(max_length=40, null=True)),
                ('neighborhood', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborapp.neighborhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='posts/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neighborapp.neighborhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200, null=True)),
                ('business_url', models.CharField(max_length=200, null=True)),
                ('business_email', models.CharField(max_length=100, null=True)),
                ('neighborhood', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighborapp.neighborhood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
