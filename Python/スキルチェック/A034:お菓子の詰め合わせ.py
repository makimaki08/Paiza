# 入力値の受け取り
N, max_value = map(int,input().split())
prices = [int(input()) for _ in range(N)]
# print(N, max_value)
# print(prices)

# 種類の最大数を求める処理
from itertools import combinations

def find_max_value_combination(prices, target):
    max_value = 0
    max_combination = []

    for i in range(1, len(prices) + 1):
        for combo in combinations(prices, i):
            combo_sum = sum(combo)
            if combo_sum <= target and combo_sum > max_value:
                max_value = combo_sum
                max_combination = combo

    return max_combination


max_value_combination = find_max_value_combination(prices, max_value)

# print("最大合計金額を持つ組み合わせ:")
# print(max_value_combination)



# 種類の最大数を購入した場合、お釣りを最小にする処理
print(max_value-sum(max_value_combination))