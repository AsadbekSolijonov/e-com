from django.contrib import admin

from shop.models import Category, Picture, Product, OrderItem, Order

admin.site.register([Category, OrderItem, Order])
admin.site.register([Product, Picture])


class PictureAdmin(admin.StackedInline):
    model = Picture
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureAdmin]
