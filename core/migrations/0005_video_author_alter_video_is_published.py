# Generated by Django 5.1.2 on 2024-11-11 01:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_video_description_alter_video_is_published_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='video',
            name='is_published',
            field=models.BooleanField(default=False, null=True, verbose_name='Está publicado'),
        ),
    ]
