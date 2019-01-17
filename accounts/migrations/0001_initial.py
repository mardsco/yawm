# Generated by Django 2.1.4 on 2018-12-30 19:12

import core.utils
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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=63, null=True, verbose_name="If you don't provide one. your username will be used")),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.utils.get_image_upload_path)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('n', 'I prefer not to say')], max_length=1)),
                ('followers', models.ManyToManyField(blank=True, related_name='followed_profiles', to='accounts.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]