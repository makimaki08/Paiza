class Customer():
	def __init__(self):
		self.sum_payment = 0

	def set_food(self, price):
		self.sum_payment += price

	def set_softdrink(self, price):
		self.sum_payment += price
		
	def set_alchol(self):
		pass

	def get_sumPayment(self):
		return self.sum_payment

class AdultCustomer(Customer):
	def __init__(self):
		super().__init__()
		self.alcohol_check = False

	def set_food(self, price):
		# 飲酒済みの場合、料金から200円引き
		if(self.alcohol_check):
			self.sum_payment += price - 200
		else:
			self.sum_payment += price

	def set_alchol(self, price=500):
		self.sum_payment += price
		self.alcohol_check = True

customer_num, order_num = [int(x) for x in input().split()]

customer_arr = [None]*customer_num

for i in range(customer_num):
	age = int(input())
	if(age>=20):
		customer_arr[i] = AdultCustomer()
	else:
		customer_arr[i] = Customer()

for _ in range(order_num):
	input_line = input().split()
	index = int(input_line[0])-1
	order = input_line[1]
	# 注文が0=ビールの場合
	if(order=="0"):
		customer_arr[index].set_alchol()

	# 注文がビール以外の場合
	else:
		price = int(input_line[2])
		# 注文がfoodの場合	
		if(order=="food"):
			customer_arr[index].set_food(price)

		# 注文がalcoholの場合
		elif(order=="alcohol"):
			customer_arr[index].set_alchol(price)		

		# 注文がsoftdrinkの場合
		elif(order=="softdrink"):
			customer_arr[index].set_softdrink(price)

for customer in customer_arr:
	print(customer.get_sumPayment())
