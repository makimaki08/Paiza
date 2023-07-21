idol_num, event_num = map(int,input().split())
idols = [str(input()) for _ in range(idol_num)]
# print(idols)
for _ in range(event_num):
	input_arr = input().split()
	if(input_arr[0] == "handshake"):
		idols.sort()
		for idol in idols:
			print(idol)

	elif(input_arr[0] == "join"):
		idols.append(input_arr[1])

	elif(input_arr[0] == "leave"):
		for j in range(len(idols)):
			if(idols[j] == input_arr[1]):
				idols.pop(j)
				

