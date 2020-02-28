from django.contrib import admin
from .models import Size, Category, Topping, Price_List, Item_List, Cart_List, Extra, Order


# Register your models here.


class CartInLine(admin.StackedInline):
	model = Cart_List.toppings.through
	# model = Cart_List.extra.through
	extra = 1

class ToppingAdmin(admin.ModelAdmin):
	inlines = [CartInLine]


class CartAdmin(admin.ModelAdmin):
	filter_horizontal = ("toppings",)
	# filter_horizontal = ("extra",)

admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Price_List)
admin.site.register(Item_List)
admin.site.register(Cart_List, CartAdmin)
admin.site.register(Extra)
admin.site.register(Order)






# class MenuPriceResource(resources.ModelResource):

#     class Meta:
#         model = MenuPrice