N, K = map(int, input().split())
departments = {input(): [] for _ in range(N)}
# print(departments)

for i in range(K):
	department_name, order_id, fee = input().split()
	departments[department_name].append([order_id, int(fee)])

print(departments)
print(departments.items())

# for department in departments:
# 	print(department)
# 	for order_id, receipt_arr in departments.items():
# 		if(department == receipt_arr[0]):
# 			print(order_id, receipt_arr[1])
# 	print("-----")