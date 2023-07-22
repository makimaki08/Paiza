import numpy
""" 
	区間和の求め方。
	→numpyを利用して累積和を求める際に、配列の要素を制限した状態で渡してあげれば良いのでは？
		1.input配列を作る。（まずはここから）
		2.出力する最小値、最大値を取得する。
		3.numpy配列に、input_arr[最小値:最大値]となるように値を渡す。
	↓上記は実行タイムエラーにより、不可能
	
	→累積和を求めておいて、最大-[最小-1]の値を取ると良い
"""
N, K = map(int, input().split())
input_arr = [int(input()) for _ in range(N)]
input_arr.insert(0,0)
sum_arr = numpy.cumsum(input_arr)

for _ in range(K):
	min_value, max_value = map(int, input().split())
	print(sum_arr[max_value]- sum_arr[min_value-1])