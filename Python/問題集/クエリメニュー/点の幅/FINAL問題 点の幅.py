N, K = map(int, input().split())
box = [int(input()) for _ in range(N)]
box.insert(0,0)

for _ in range(K):
	A_l, A_r, B_l, B_r = map(int, input().split())
	calc_A = max(box[A_l:A_r+1]) - min(box[A_l:A_r+1])
	calc_B = max(box[B_l:B_r+1]) - min(box[B_l:B_r+1])
	if calc_A>calc_B:
		print("A")
	elif calc_A<calc_B:
		print("B")
	else:
		print("DRAW")