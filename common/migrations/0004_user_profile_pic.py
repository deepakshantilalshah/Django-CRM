# Generated by Django 2.1.1 on 2018-10-09 06:44

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.FileField(blank=True, max_length=1000, null=True, upload_to=common.models.img_url),
        ),
    ]
