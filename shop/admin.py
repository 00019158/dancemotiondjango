from django.contrib import admin
from .models import Category, Product, Order, OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'discount', 'is_new', 'created_at')
    list_filter = ('category', 'is_new')
    search_fields = ('title',)
    readonly_fields = ('created_at',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'status', 'total', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'phone')
    readonly_fields = ('created_at', 'total', 'cashback')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'price', 'qty')
