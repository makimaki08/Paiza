class Company:
	def __init__(self, name, pin, balance):
		self.name = name
		self.pin = pin
		self.balance = balance

	def get_balance(self, raq_pin, req_balance):
		if(self.pin == req_pin):
			self.set_balance(req_balance)
			return self.balance

	def set_balance(self, balance):
			self.balance -= balance
			

	def get_status(self):
		print(self.name, self.balance)


N, K = map(int, input().split())
companys = {}

for _ in range(N):
	name, pin, balance = input().split()
	companys[name] = Company(name, pin, int(balance))

for _ in range(K):
	company, req_pin, req_balance = input().split()
	companys[company].get_balance(req_pin, int(req_balance))

for company in companys.values():
	company.get_status()