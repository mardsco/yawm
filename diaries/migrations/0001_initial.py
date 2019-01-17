# Generated by Django 2.1.4 on 2019-01-09 18:51

import core.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written_comments', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_likes', to='diaries.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_likes', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=275)),
                ('content', models.TextField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=core.utils.get_image_upload_path)),
                ('is_visible', models.CharField(choices=[('all', 'All'), ('no_one', 'No One')], default='all', max_length=7, verbose_name='Who can see this diary?')),
                ('is_commentable', models.CharField(choices=[('all', 'All'), ('no_one', 'No One')], default='all', max_length=7, verbose_name='Who can comment on this diary?')),
                ('feeling', models.CharField(blank=True, choices=[(0, 'Angry'), (1, 'Happy'), (2, 'Excited'), (3, 'Sad')], max_length=15, null=True, verbose_name='How do you feel?')),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='Date to publish')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written_diaries', to='accounts.Profile')),
            ],
            options={
                'verbose_name_plural': 'diaries',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='DiaryLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_likes', to='diaries.Diary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary_likes', to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='likes',
            field=models.ManyToManyField(through='diaries.DiaryLike', to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='diary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='diaries.Diary'),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='liked_comments', through='diaries.CommentLike', to='accounts.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='diarylike',
            unique_together={('user', 'diary')},
        ),
    ]
