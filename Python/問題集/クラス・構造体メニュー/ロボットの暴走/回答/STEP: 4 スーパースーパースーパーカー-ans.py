class superCar:
    def __init__(self, f, f_c):
        self.fuel = f
        self.fuel_consumption = f_c
        self.mileage = 0

    def run(self):
        if self.fuel <= 0:
            return

        self.fuel -= 1
        self.mileage += self.fuel_consumption

    def get_mileage(self):
        return self.mileage


class superSuperCar(superCar):
    def fly(self):
        if self.fuel < 5:
            super().run()
        else:
            self.fuel -= 5
            self.mileage += self.fuel_consumption ** 2


class superSuperSuperCar(superCar):
    def fly(self):
        if self.fuel < 5:
            super().run()
        else:
            self.fuel -= 5
            self.mileage += 2 * self.fuel_consumption ** 2

    def teleport(self):
        if self.fuel < self.fuel_consumption ** 2:
            self.fly()
        else:
            self.fuel -= self.fuel_consumption ** 2
            self.mileage += self.fuel_consumption ** 4


n, k = [int(x) for x in input().split()]

cars = [None] * n
for i in range(n):
    values = input().split()

    car_type = values[0]
    fuel = int(values[1])
    fuel_consumption = int(values[2])

    if car_type == "supercar":
        cars[i] = superCar(fuel, fuel_consumption)
    elif car_type == "supersupercar":
        cars[i] = superSuperCar(fuel, fuel_consumption)
    else:
        cars[i] = superSuperSuperCar(fuel, fuel_consumption)

for _ in range(k):
    values = input().split()

    index = int(values[0]) - 1
    func = values[1]

    if func == "run":
        cars[index].run()
    elif func == "fly":
        cars[index].fly()
    else:
        cars[index].teleport()

for car in cars:
    print(car.get_mileage())