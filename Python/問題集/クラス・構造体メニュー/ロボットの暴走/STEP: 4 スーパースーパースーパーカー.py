class SuperCar:
	def __init__(self, fuel, mileage):
		self.fuel = fuel
		self.mileage = mileage
		self.total_distance = 0


	def run(self):
		# 燃料が0より上の場合
		if(self.fuel>0):
			self.total_distance += self.mileage
			self.fuel = max(self.fuel-1,0)

	def get_total_distance(self):
		return self.total_distance

class SuperSuperCar(SuperCar):
	def fly(self):
		# 燃料が5以上の場合
		if(self.fuel>=5):
			self.total_distance += self.mileage**2
			self.fuel = max(self.fuel-5,0)

		# 燃料が5未満の場合
		else:
			supre().run()


class SuperSuperSuperCar(SuperSuperCar):
	def fly(self):
		# 燃料が5以上の場合
		if(self.fuel>=5):
			self.total_distance += 2*(self.mileage**2)
			self.fuel = max(self.fuel-5,0)

		# 燃料が5未満の場合
		else:
			supre().run()

	def teleport(self):
		# 燃料が燃費の2乗以上の場合
		if(self.fuel>=self.mileage**2):
			self.total_distance += self.mileage**4
			self.fuel = max(self.fuel-self.mileage**2,0)

		# 燃料が燃費の2乗未満の場合
		else:
			self.fly()

car_num, action_num = [int(x) for x in input().split()]
car_arr = [None]*car_num

for i in range(car_num):
	input_arr = input().split()
	car_type = input_arr[0]
	fuel = int(input_arr[1])
	mileage = int(input_arr[2])


	if(car_type == "supercar"):
		car_arr[i] = SuperCar(fuel, mileage)

	elif(car_type == "supersupercar"):
		car_arr[i] = SuperSuperCar(fuel, mileage)

	elif(car_type == "supersupersupercar"):
		car_arr[i] = SuperSuperSuperCar(fuel, mileage)


for _ in range(action_num):
	input_arr = input().split()
	index = int(input_arr[0])-1
	action = input_arr[1]

	if(action == "run"):
		car_arr[index].run()

	elif(action == "fly"):
		car_arr[index].fly()

	elif(action == "teleport"):
		car_arr[index].teleport()

for car in car_arr:
	print(car.get_total_distance())
