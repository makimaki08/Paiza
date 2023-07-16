class Player:
	def __init__(self, hp, f_1, a_1, f_2, a_2, f_3, a_3):
		self.hp = hp
		self.f = [f_1, f_2, f_3]
		self.a = [a_1, a_2, a_3]

	# 強化技を実行し、全ての発生フレームをー3、attacを+5する
	def set_enhance(self):
		# f_i, a_iの強化（f_i, a_iが強化技ではない場合）
		for i in range(len(self.f)):
			if self.f[i] == 0 and self.a[i] == 0:
				continue

			# 最小値が1となるように、max関数を利用
			self.f[i] = max(self.f[i]-3, 1)
			self.a[i] += 5


	# ダメージを受ける
	def set_damege(self, damage):
		self.hp -= damage
		# 0よりhpが下回った場合、0に強制的に変更
		if(self.hp<=0):
			self.hp = 0

	# 入力値によって、異なる命令を出す
	def get_command_value(self,index):
		# 対応する値を返す
		return (self.f[index], self.a[index])






player_num, attack_num =  map(int, input().split())
player_arr = [None]*player_num
for i in range(player_num):
	hp, f_1, a_1, f_2, a_2, f_3, a_3 = map(int, input().split())
	player_arr[i] = Player(hp, f_1, a_1, f_2, a_2, f_3, a_3)


for _ in range(attack_num):
	input_arr = [int(x) for x in input().split()]


	# player1関係を初期化
	player_1 = player_arr[input_arr[0]-1]
	flame_1, attack_1 = player_1.get_command_value(input_arr[1]-1)

	# player2関係を初期化
	player_2 = player_arr[input_arr[2]-1]
	flame_2, attack_2 = player_2.get_command_value(input_arr[3]-1)

	# player達のhpが0では無いこと
	if(player_1.hp != 0 and player_2.hp != 0):
		if((flame_1 == 0 and attack_1 == 0) and (flame_2 == 0 and attack_2 == 0)):
			player_1.set_enhance()
			player_2.set_enhance()

		elif(flame_1 == 0 and attack_1 == 0):
			player_1.set_enhance()
			player_1.set_damege(attack_2)

		elif(flame_2 == 0 and attack_2 == 0):
			player_2.set_enhance()
			player_2.set_damege(attack_2)

		else:
			# player_1の方が、コマンドフレームが速い場合→player_1の攻撃がplayer_2にヒット
			if(flame_1<flame_2):
				player_2.set_damege(attack_1)


			# player_2の方が、コマンドフレームが速い場合→player_2の攻撃がplayer_1にヒット
			elif(flame_1>flame_2):
				player_1.set_damege(attack_2)

			# player_1とplayer_2のコマンドフレームが同じ場合→動作なし
			else:
				continue

alive_p_count = 0
for player in player_arr:
	if(player.hp>0):
		alive_p_count+=1

print(alive_p_count)