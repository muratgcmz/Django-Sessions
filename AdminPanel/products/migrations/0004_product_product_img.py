# Generated by Django 4.0.5 on 2022-06-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, default='defaults/clarusway(1).png', null=True, upload_to='product/'),
        ),
    ]
