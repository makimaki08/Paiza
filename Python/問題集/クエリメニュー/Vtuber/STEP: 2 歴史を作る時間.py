group_num, event_num = map(int,input().split())
group_member = {input() for _ in range(group_num)}

historys = {}
for i in range(event_num):
	year, name = input().split()
	historys[int(year)] = name

# print(historys)
# print(historys[593])
# print(sorted(historys))
for history_num in sorted(historys):
	print(historys[history_num])