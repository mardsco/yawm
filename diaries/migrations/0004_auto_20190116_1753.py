# Generated by Django 2.1.4 on 2019-01-16 17:53

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0003_auto_20190115_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
