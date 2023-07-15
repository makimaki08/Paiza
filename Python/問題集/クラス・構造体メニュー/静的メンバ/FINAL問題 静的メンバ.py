class Customer:
	custmer_count = 0

	def __init__(self):
		self.sum_payment = 0

	def setFoodOder(self, price):
		self.sum_payment += price

	def setSoftdrinkOder(self, price):
		self.sum_payment += price

	# 大人のみ購入させる
	def setAlcoholOder(self):
		pass

	def getSumPayment(self):
		Customer.custmer_count += 1
		return self.sum_payment


class AdultCustomer(Customer):
	def __init__(self):
		super().__init__()
		self.alcohol_check = False

	def setAlcholCheck(self):
		self.alcohol_check = True

	def setAlcoholOder(self, price=500):
		self.sum_payment += price


	def setFoodOder(self, price):
		# 飲酒済みの場合
		if(self.getAlcoholCheck):
			self.sum_payment += price - 200

		else:
			self.sum_payment += price


customer_num, order_num = [int(x) for x in input().split()]
customer_arr = [None]*customer_num


for i in range(customer_num):
	age = int(input())
	if(age>=20):
		customer_arr[i] = AdultCustomer()
	else:
		customer_arr[i] = Customer()

for _ in range(order_num):
	input_arr = input().split()
	index = int(input_arr[0])-1
	order = input_arr[1]

	# お会計
	if(order == "A"):
		print(customer_arr[index].getSumPayment())

	# ビール
	elif(order == "0"):
		customer_arr[index].setAlcoholOder()
		customer_arr[index].setAlcholCheck()

	else:
		price = int(input_arr[2])

		if(order == "softdrink"):
			customer_arr[index].setSoftdrinkOder(price)

		elif(order == "alcohol"):
			customer_arr[index].setAlcoholOder(price)

		else:
			customer_arr[index].setFoodOder(price)

print(Customer.custmer_count)