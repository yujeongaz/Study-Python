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