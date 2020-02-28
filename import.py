import csv

from orders.models import MenuPrice, Category, Topping_qty, Size, Topping, Cart


def main():
    f = open("products.csv")
    reader = csv.reader(f)
    for category, name, topping_qty, size, price in reader:
    	if topping_qty	== "" and size =="":
       		product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=None, size=None, price=price)
       	elif size =="":
       		product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=None, size=None, price=price)
    	else:
    		product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=Topping_qty.objects.get(pk = topping_qty), size=Size.objects.get(pk = size), price=price)
    	product.save()

if __name__ == "__main__":
    main()


f = open("toppings.csv")
reader = csv.reader(f)
for name in reader:
  topping = Topping(name=name)
  topping.save()

c=Cart(user_id=User.objects.get(pk =1),menu_id=MenuPrice.objects.get(pk =1))

import csv
from orders.models import MenuPrice, Category, Topping_qty, Size
f = open("products.csv")
reader = csv.reader(f)
for category, name, topping_qty, size, price in reader:
  if topping_qty == "" and size =="":
    product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=None, size=None, price=price)
  elif topping_qty == "":
      product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=None, size=Size.objects.get(pk = size), price=price)
  else:
      product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=topping_qty, size=Size.objects.get(pk = size), price=price)
  product.save()


MenuPrice.objects.all().delete()

topping_qty=Size.objects.get(pk = topping_qty)

# price list import
import csv
from orders.models import Price_List
f = open("pricelist.csv")
reader = csv.reader(f)
for name, base_price, large_supp in reader:
    product = Price_List(name=name,base_price=base_price,large_supp=large_supp)
    product.save()
    
# item list import
import csv
from orders.models import Item_List, Price_List, Category
f = open("itemlist.csv")
reader = csv.reader(f)
for category, name, base_price_id in reader:
  product = Item_List(category=Category.objects.get(pk = category), name=name, base_price_id=Price_List.objects.get(pk = base_price_id))
  product.save()

# 	else:
# 		product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=Topping_qty.objects.get(pk = topping_qty), size=Size.objects.get(pk = size), price=price)
#     product.save()

# product = MenuPrice(category=Category.objects.get(pk = 15),name='Regular',topping_qty=Topping_qty.objects.get(pk = None), size=Size.objects.get(pk = 6), price=price)
# product = MenuPrice(category=Category.objects.get(pk = 15),name='Regular',topping_qty= None, size=Size.objects.get(pk = 6), price=price)

# import csv
# from orders.models import MenuPrice, Category, Topping_qty, Size
# f = open("products.csv")
# reader = csv.reader(f)
# for category, name, topping_qty, size, price in reader:
# 	if size =="":
# 		product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=topping_qty, size=None, price=price)
# 	else:
# 		product = MenuPrice(category=Category.objects.get(pk = category),name=name,topping_qty=topping_qty, size=Size.objects.get(pk = size), price=price)
#     product.save()