# fruits = ["apple", "banana", "chisato", "chisato"]
# print(fruits)
# print(set(fruits))
# print(list(set(fruits)))
# print(fruits[2])

# set は重複削除して、{}になる

# sort
# データ型違うとソートできない

fruits = ["apple", "chisato", "banana", "chisato", "5"]
print(fruits)
print(sorted(fruits))
sorted_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)

# 0番目を基準として右はプラス、左はマイナス(PC上はプラス実行)
# numbers = [1, 2, 3, 4]
# print(numbers[-1])
# # 配列の最後番目を取りたいときは-1を使う
# print(numbers[3])
# numbers.insert(-1, 5)
# print(numbers)
# numbers.append(6)
# print(sorted(numbers))
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[0:5])
print(numbers[:5])
print(numbers[-3:-1])
print(numbers[3:])
print(numbers[-3:])
# print(numbers[-1(5):3])
# print(numbers[5:3])
