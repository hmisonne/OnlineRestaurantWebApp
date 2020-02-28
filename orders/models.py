from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=64)
	custom_topping = models.BooleanField(default=False)
	custom_extra = models.BooleanField(default=False)
	custom_size = models.BooleanField(default=False)


	def __str__(self):
		return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Topping(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return f"{self.name}"

class Extra(models.Model):
	name = models.CharField(max_length=64)
	def __str__(self):
		return f"{self.name}"

		
class Price_List(models.Model):
	name = models.CharField(max_length=64)
	base_price = models.FloatField()
	large_supp = models.FloatField()

	def __str__(self):

		return f"{self.name}, Base: {self.base_price}, large_supp: {self.large_supp}"


class Item_List(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	name = models.CharField(max_length=64)
	base_price_id = models.ForeignKey(Price_List, on_delete=models.CASCADE)


	def __str__(self):
		return f" {self.name}, Base Price: ${self.base_price_id.base_price}"
# {self.category.name}

class Cart_List(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Item_List, on_delete=models.CASCADE)
	size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True,)
	extra = models.ManyToManyField(Extra, blank=True)
	toppings = models.ManyToManyField(Topping, blank=True)
	calculated_price = models.FloatField()
	is_current = models.BooleanField(default=True)

	def __str__(self):
		topping_list = []
		for topping in self.toppings.all():
			topping_list.append(topping)
		extra_list = []
		for extra in self.extra.all():
			extra_list.append(extra)
		if self.size ==None:
			return f"{self.item_id.category.name} {self.item_id.name} - Price: ${self.calculated_price}"
		else:
			return f"{self.item_id.category.name} {self.item_id.name}, {self.size.name} { topping_list } { extra_list }- Price: ${self.calculated_price}"
	

class Order(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	cart_id = models.ManyToManyField(Cart_List)
	complete = models.BooleanField(default=False)
	
	def __str__(self):
		if self.complete == False:
			return f"{self.user_id}, Status: On Order"
		else:
			return f"{self.user_id}, Status: Complete"