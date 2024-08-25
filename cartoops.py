#shopping cart using oops concept

class shopping:
	def __init__(self):
		self.items={}

	def additems(self,quantity,itemname,price):
		self.itemname=itemname
		self.quantity=quantity
		self.price=price
		if itemname in self.items:
			self.items[itemname]+=quantity
			print(self.items)
		else:
			self.items[itemname]={'price': price, 'quantity': quantity}
			print(self.items)


	
	def removeitems(self,itemname,quantity=1):
		self.itemname=itemname
		self.quantity=quantity
		if itemname in self.items:
			if self.items[itemname]["quantity"]<=quantity: 
				self.items.pop(itemname)
				print(self.items)
			else:
				self.items[itemname]["quantity"]-=quantity
				print(self.items)
		else:
			print("Item not Found..!")

		
	def get_total_price(self):
		total_price=0
		for items,details in self.items.items():
				total_price+=details['price']*details['quantity']
		print("Price",total_price)


	def displaycart(self):
		toatl=0
		if not self.items:
			print("This cart is Empty..!")
		else:
			for items,details in self.items.items():
				toatl+=details['price']*details['quantity']
				print(f"{items}:{details['price']}*{details['quantity']}")
			print(f"Total Price:${toatl:.2f}")




	def __str__(self):
		return f"{self.items}"

if __name__ == "__main__":
	cart=shopping()
	cart.additems(12,"pappaya",120)
	cart.additems(10,"Banana",110)
	cart.additems(1,"Apple",120)
	cart.additems(13,"Orange",120)
	cart.additems(5,"Dragon Fruit",100)
	cart.removeitems("pappaya",2)
	cart.get_total_price()
	cart.displaycart()
	print(cart)