# Generated by Django 2.2 on 2019-05-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_link',
            field=models.CharField(default='....', max_length=255),
            preserve_default=False,
        ),
    ]
