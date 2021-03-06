from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

    def upload_to_db(self, category):
        new_category = ProductCategory(name=category)
        try:
            new_category.save()
        except Exception as e:
            pass


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название товара', max_length=128)
    vendor_id = models.CharField(verbose_name='Артикул', max_length=10, unique=True, blank=True)
    image = models.ImageField(upload_to='products_image', blank=True)
    short_descript = models.CharField(verbose_name='Краткое описание', max_length=64, blank=True)
    description = models.TextField(verbose_name='Описание товара', blank=True)
    price = models.DecimalField(verbose_name='Цена товара', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во на складе', default=0)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return '{} ({})'.format(self.name, self.category.name)

    def upload_to_db(self, product):
        row = product
        category = ProductCategory.objects.get(name=row[0])
        name = row[1]
        vendor_id = row[2]
        image = row[3]
        short_descript = row[4]
        description = row[5]
        price = row[6]
        quantity = row[7]
        prod = Product(category=category, name=name, vendor_id=vendor_id, image=image, short_descript=short_descript,
                       description=description, price=price, quantity=quantity)
        try:
            prod.save()
        except Exception as e:
            pass
