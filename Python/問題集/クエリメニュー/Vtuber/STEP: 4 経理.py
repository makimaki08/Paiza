N, K = map(int, input().split())
departments = [input() for _ in range(N)]
# print(departments)

receipts = {}
for i in range(K):
	department_name, order_id, fee = input().split()
	receipts[order_id] = (department_name, int(fee))
	# print(department_name, order_id, fee)

# print(receipts)
# print(receipts.items())

for department in departments:
	print(department)
	for order_id, receipt_arr in receipts.items():
		if(department == receipt_arr[0]):
			print(order_id, receipt_arr[1])
	print("-----")