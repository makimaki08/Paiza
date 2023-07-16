class Player:
	def __init__(self, hp, f_1, a_1, f_2, a_2, f_3, a_3):
		self.hp = hp
		self.f_1 = f_1
		self.a_1 = a_1
		self.f_2 = f_2
		self.a_2 = a_2
		self.f_3 = f_3
		self.a_3 = a_3

	# ダメージを受ける
	def set_damege(self, attack):
		self.hp -= attack
		# 0よりhpが下回った場合、0に強制的に変更
		if(self.hp<0):
			self.hp = 0

	# 入力値によって、異なる命令を出す
	def get_command_value(self,command):
		if(command==1): # f_1,a_1
			# 強化技かどうか判定（f_i == 0 and a_i == 0）
			if(get_is_enforce(self.f_1, self.a_1)):
				# 強化技の場合→全ての発生フレームをー3、attacを+5する
				set_enforce()
				# フレーム=0(f_i)を返す
				return self.f_1, self.a_1
			else:
				# 強化技ではない場合→f_1のフレームを返す
				return self.f_1, self.a_1

		elif(command==2): # f_2,a_2
			# 強化技かどうか判定（f_i == 0 and a_i == 0）
			if(get_is_enforce(self.f_2, self.a_2)):
				# 強化技の場合→全ての発生フレームをー3、attacを+5する
				set_enforce()
				# フレーム=0(f_i)を返す
				return self.f_2, self.a_2
			else:
				# 強化技ではない場合→f_2のフレームを返す
				return self.f_2, self.a_2

		elif(command==3): # f_3,a_3
			# 強化技かどうか判定（f_i == 0 and a_i == 0）
			if(get_is_enforce(self.f_3, self.a_3)):
				# 強化技の場合→全ての発生フレームをー3、attacを+5する
				set_enforce()
				# フレーム=0(f_i)を返す
				return self.f_3, self.a_3

			else:
				# 強化技ではない場合→f_3のフレームを返す
				return self.f_3, self.a_3


	# 強化技か判定するフラグを返す関数
	def get_is_enforce(self,f,a):
		# 強化技かTrue/Falseを返す
		if(f==0 and a==0):
			return True
		else:
			return False

	# 強化技を実行し、全ての発生フレームをー3、attacを+5する
	def set_enforce(self):
		# 1：f_1, a_1の強化（f_i, a_iが強化技ではない場合）
		if(get_is_enforce(self.f_1,self.a_1)==False):
			# f_i-3が1以上である場合
			self.f_1 = self.f_1 - 3 if self.f_1 - 3 >= 1 else 1
			self.a_1 += 5

		# 2：f_2, a_2の強化（f_i, a_iが強化技ではない場合）
		if(get_is_enforce(self.f_2,self.a_2)==False):
			# f_i-3が1以上である場合
			self.f_2 = self.f_2 - 3 if self.f_2 - 3 >= 1 else 1
			self.a_2 += 5

		# 3：f_3, a_3の強化（f_i, a_iが強化技ではない場合）
		if(get_is_enforce(self.f_3,self.a_3)==False):
			# f_i-3が1以上である場合
			self.f_3 = self.f_3 - 3 if self.f_3 - 3 >= 1 else 1
			self.a_3 += 5




player_num, attack_num =  map(int, input().split())
player_arr = [None]*player_num
for i in range(player_num):
	hp, f_1, a_1, f_2, a_2, f_3, a_3 = map(int, input().split())
	player_arr[i] = Player(hp, f_1, a_1, f_2, a_2, f_3, a_3)

for _ in range(attack_num):
	input_arr = [int(x) for x in input().split()]
	print(input_arr)


	# player1関係を初期化
	player_1 = player_arr[input_arr[0]-1]
	flame_1, attack_1 = player_1.get_command_value(input_arr[1])

	# player2関係を初期化
	player_2 = player_arr[input_arr[2]-1]
	flame_2, attack_2 = player_2.get_command_value(input_arr[3])


	# player達のhpが0では無いこと
	if(player_1.hp != 0 and player_2.hp != 0):
		# player_1の方が、コマンドフレームが速い場合→player_1の攻撃がplayer_2にヒット
		if(flame_1>flame_2):
			player_2.set_damege(attack_1)

		# player_2の方が、コマンドフレームが速い場合→player_2の攻撃がplayer_1にヒット
		elif(flame_1<flame_2):
			player_1.set_damege(attack_2)

		# player_1とplayer_2のコマンドフレームが同じ場合→動作なし
		else:
			pass

alive_p_count = 0
for player in player_arr:
	if(player.hp>0):
		alive_p_count+=1

print(alive_p_count)