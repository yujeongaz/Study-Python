# 81 ✅
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a, b = scores
print(valid_score)

# 82 ✅
a, b, *valid_score = scores
print(valid_score)

# 83 ✅
a, *valid_score, b = scores
print(valid_score)

# 84 ✅
temp = {}
print(type(temp))

# 85 ✅
product = {
    "메로나": 1000,
    "폴라포": 1200,
    "빵빠레": 1800,
}
print(product)

# 86 ✅
product["죠스바"] = 1200
product["월드콘"] = 1500
print(product)

# 87 ✅
print(product["메로나"])

# 88 ✅
product["메로나"] = 1300
print(product["메로나"])

# 89 ✅
del product["메로나"]
print(product)

# 90 ✅
# icecream의 없는 키를 사용해서 인덱싱을 했기 때문이다.

# 91 ✅
inventory = {
    "메로나": [300, 20],
    "비비빅": [400, 3],
    "죠스바": [250, 100],
}

# 92 ✅
print(inventory["메로나"][0])

# 93 ✅
print(inventory["메로나"][1])

# 94 ✅
inventory["월드콘"] = [500, 7]

# 95 ✅
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
arr = list(icecream.keys())
print(arr)

# 96 ✅
arr = list(icecream.values())
print(arr)

# 97 ✅
print(sum(arr))

# 98 ✅
new_product = {
    "팥빙수": 2700,
    "아맛나": 1000,
}
icecream.update(new_product)
print(icecream)

# 99 ✅
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
print(dict(zip(keys, vals)))

# 100 ✅
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
print(dict(zip(date, close_price)))