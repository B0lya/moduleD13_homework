# Generated by Django 3.2.3 on 2023-04-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]