# 辞書型では、キーだけ取得「.keys()」、値だけ取得「.values()」、keyとvalueを同時に取得「.items()」がある。

group_num, event_num = map(int,input().split())
group_member = {input() for _ in range(group_num)}

historys = {}
for i in range(event_num):
	year, name = input().split()
	historys[int(year)] = name

# print(historys.keys()) # dict_keys([645, 593, 2058, 29484, 374759])
# print(historys.values()) # dict_values(['nao', 'hiro', 'yuki', 'nao', 'nao'])
# print(historys.items()) # dict_items([(645, 'nao'), (593, 'hiro'), (2058, 'yuki'), (29484, 'nao'), (374759, 'nao')])


for year, name in sorted(historys.items()):
	print(name)

# 参考： https://magazine.techacademy.jp/magazine/19309