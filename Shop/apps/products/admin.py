from django.contrib import admin
from .models import Product                 #,    Category
# Register your models here.

admin.site.register(Product)
# admin.site.register(Category)
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['category_name','slug']
#     prepopulated_fields = {'slug': ('category_name',)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['product_name','slug','product_type']