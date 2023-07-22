N, K = map(int, input().split())
departments = {input(): [] for _ in range(N)}
# print(departments)

for i in range(K):
	department_name, order_id, fee = input().split()
	departments[department_name].append((order_id, int(fee)))

# print(departments)
# print(departments.items())

for department, receipts in departments.items():
	print(department)
	for order_id, fee in receipts:
		print(order_id, fee)
	print("-----")