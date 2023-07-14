class Client(object):
	"""docstring for Client"""
	def __init__(self,old):
		self.old = old
		self.drink = 0
		self.food = 0
		self.alcohol_check = False
		self.payment = 0

	# 支払い金額を合算する関数
	def setPayment(self,fee):
		self.payment = self.payment+fee

	# 支払い金額を返すする関数
	def getPayment(self):
		return self.payment

	# アルコールを頼んだ場合、飲酒フラグをTrueにする関数
	def setAlcoholCheck(self):
		self.alcohol_check = True

	# アルコールを頼んだか返す関数
	def getAlcoholCheck(self):
		return self.alcohol_check

	# 成人か未成年か返す関数
	def getAuditCheck(self):
		if(self.old>=20):
			return True
		else:
			return False


client_num, order_num = map(int,input().split())
client_arr = []
for i in range(client_num):
	client_arr.append(Client(int(input())))

for j in range(order_num):
	input_line = input().split()
	order_human = client_arr[int(input_line[0])-1] # 注文を頼んだ人
	order = input_line[1] # 注文内容
	fee = int(input_line[2]) # 料金

	if(order=="food"):
		# アルコールを頼んでいる時、200円引きした注文料金を、支払い合計に追加
		if(order_human.getAlcoholCheck()):
			order_human.setPayment(fee-200)
		# アルコールを頼んでいない時、注文料金を支払い合計に追加
		else:
			order_human.setPayment(fee)

	# 注文が食事以外の時（提供するものは、食事とアルコール・ソフトドリンクのみ）
	else:
		if(order=="alcohol"):
			# 注文者が成人の場合
			if(order_human.getAuditCheck()):
				# 支払い料金にアルコールの料金を追加し、飲酒フラグを設定
				order_human.setPayment(fee)
				order_human.setAlcoholCheck()
		else:
			order_human.setPayment(fee)

for client in client_arr:
	print(client.getPayment())