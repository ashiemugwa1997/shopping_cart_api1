# Generated by Django 4.0.4 on 2022-05-24 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_price',
            field=models.BigIntegerField(max_length=180),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_quantity',
            field=models.IntegerField(max_length=180),
        ),
    ]
