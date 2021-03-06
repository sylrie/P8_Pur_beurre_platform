# Generated by Django 3.0.3 on 2020-03-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='link',
            field=models.URLField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='stores',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
