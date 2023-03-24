from django.db import models

class Product(models.Model):
    product_name = models.CharField("Название", max_length=200)
    product_type = models.CharField("Категория", max_length=200)
    product_prices = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    product_img1 = models.ImageField('Фотография товара 1', upload_to='img', default="Null")
    product_img2 = models.ImageField('Фотография товара 2', upload_to='img', blank=True, default="Null")
    product_info = models.TextField('Описание товара')
    delivery_date = models.DateField('Ближайший срок доставки')

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
