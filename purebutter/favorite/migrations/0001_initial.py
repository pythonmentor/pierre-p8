# Generated by Django 2.2.1 on 2019-05-22 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substitution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfavorite_substitute', to='products.Product')),
                ('to_substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfavorite_tosubstitute', to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]