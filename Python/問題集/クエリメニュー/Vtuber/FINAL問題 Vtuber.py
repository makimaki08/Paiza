N = int(input())
superchats = {}
memberships = []

for i in range(N):
	input_arr = input().split()
	name = input_arr[0]
	act = input_arr[1]

	if act == "give":
		superchats[int(input_arr[2])] = name

	elif act == "join":
		memberships.append(name)

# print(sorted(superchats, reverse=False))
# print(superchats.items())
for money, name in sorted(superchats.items(), reverse = True):
	print(name)

for member in sorted(memberships):
	print(member)