# Generated by Django 3.0 on 2021-12-12 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post'),
        ),
    ]
