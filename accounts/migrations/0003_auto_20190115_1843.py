# Generated by Django 2.1.4 on 2019-01-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190115_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=63, verbose_name="If you don't provide one. your username will be used"),
        ),
    ]
