from django.db import models
import uuid


class TicketsSupport(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey('Users', on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class AccumulativePoints(models.Model):
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    amount = models.IntegerField()

    def __str__(self):
        return self.amount


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    tg_id = models.BigIntegerField()
    tg_username = models.CharField(max_length=50)
    custom_shipping_address = models.CharField(max_length=100)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Orders(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    products = models.ForeignKey('Products', on_delete=models.PROTECT)
    status = models.CharField(max_length=50)
    total_price = models.FloatField(default=0.0)
    payment_status = models.CharField(max_length=20)
    user = models.ForeignKey('Users', on_delete=models.PROTECT)
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.PROTECT)
    promo = models.ForeignKey('Promo', on_delete=models.PROTECT)


class ShippingAddress(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class Promo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=20)
    products = models.ForeignKey('Products', on_delete=models.PROTECT)
    condition = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # images = models.ImageField(upload_to='photos/%Y/%m/%d/')   - Узнать / доработать
    price = models.FloatField(default=0.0)
    amount = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.PROTECT)
    tags = models.CharField(max_length=20)
    vendor_code = models.IntegerField()

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=100)
    # icon = models.ImageField(upload_to='photos/%Y/%m/%d/')   - Узнать / доработать

    def __str__(self):
        return self.name


class Keyboards(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=100)


class HelpInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class AboutInfo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
