class Hero:
	def __init__(self, level, hp, attack, defense, speed, inte, luck):
		self.level = level
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.inte = inte
		self.luck = luck

	def Levelup(self, hp, attack, defense, speed, inte, luck):
		self.level += 1
		self.hp += hp
		self.attack += attack
		self.defense += defense
		self.speed += speed
		self.inte += inte
		self.luck += luck

	def Muscle_training(self, hp, attack):
		self.hp += hp
		self.attack += attack

	def Running(self, defense, speed):
		self.defense += defense
		self.speed += speed

	def Study(self, inte):
		self.inte += inte

	def Pray(self, luck):
		self.luck += luck

	def display_Status(self):
		print(self.level, self.hp, self.attack, self.defense, self.speed, self.inte, self.luck)

def get_fixArr(fix_arr):
		return [int(x) for x in fix_arr]

hero_num, event_num = map(int, input().split())
hero_arr = [None]*hero_num
for i in range(hero_num):
	level, hp, attack, defense, speed, inte, luck = map(int, input().split())
	hero_arr[i] = Hero(level, hp, attack, defense, speed, inte, luck)

for _ in range(event_num):
	input_arr = input().split()
	index = int(input_arr.pop(0))-1
	event = input_arr.pop(0)

	if(event == "levelup"):
		hp, attack, defense, speed, inte, luck = get_fixArr(input_arr)
		hero_arr[index].Levelup(hp, attack, defense, speed, inte, luck)

	elif(event == "muscle_training"):
		hp, attack = get_fixArr(input_arr)
		hero_arr[index].Muscle_training(hp, attack)

	elif(event == "running"):
		defense, speed = get_fixArr(input_arr)
		hero_arr[index].Running(defense, speed)

	elif(event == "study"):
		inte = int(input_arr.pop(0))
		hero_arr[index].Study(inte)

	elif(event == "pray"):
		luck = int(input_arr.pop(0))
		hero_arr[index].Pray(luck)

for j in range(hero_num):
	hero_arr[j].display_Status()