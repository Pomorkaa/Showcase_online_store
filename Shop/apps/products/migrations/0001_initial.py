# Generated by Django 4.1.7 on 2023-03-18 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='Название')),
                ('product_type', models.CharField(max_length=200, verbose_name='Категория')),
                ('product_prices', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('product_img1', models.ImageField(default='Null', upload_to='img', verbose_name='Фотография товара 1')),
                ('product_img2', models.ImageField(blank=True, default='Null', upload_to='img', verbose_name='Фотография товара 2')),
                ('product_info', models.TextField(verbose_name='Описание товара')),
                ('delivery_date', models.DateField(verbose_name='Ближайший срок доставки')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]