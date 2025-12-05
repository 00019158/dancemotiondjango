from django.db import models
from django.conf import settings   # ← импорт здесь


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    is_new = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def final_price(self):
        return round(self.price * (1 - self.discount / 100))

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'В обработке'),
        ('forming', 'Формируется'),
        ('shipping', 'Доставляется'),
        ('delivered', 'Доставлено'),
    ]

    # ← вот это мы добавили правильно
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders"
    )

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='processing')
    total = models.PositiveIntegerField(default=0)
    cashback = models.PositiveIntegerField(default=0)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def recalc_total(self):
        total = sum([item.subtotal() for item in self.items.all()])
        self.total = total
        self.cashback = round(total * 0.05)
        self.save()

    def __str__(self):
        return f'Заказ #{self.id} ({self.name})'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    qty = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"

    def subtotal(self):
        return self.price * self.qty

    def __str__(self):
        return f'{self.title} x{self.qty}'
