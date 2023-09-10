# 21 ✅
letters = "python"
print(letters[0], letters[2])

# 22 ✅
license_plate = "24가 2210"
print(license_plate[-4:])

# 23 ✅
string = "홀짝홀짝홀짝"
print(string[::2])

# 24 ✅
string = "PYTHON"
print(string[::-1])

# 25 ✅
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 26 ✅
print(phone_number.replace("-", ""))

# 27 ✅
url = "http://sharebook.kr"
# print(url[-2:])
print(url.split(".")[1])

# 28 ✅
# 오류 발생

# 29 ✅
string = "abcdfe2a354a32a"
print(string.replace("a", "A"))

# 30 ✅
# "aBcd" ❌
# "abcd"

# 31 ✅
# "34"

# 32 ✅
# "HiHiHi"

# 33 ✅
print("-" * 80)

# 34 ✅
t1 = "python"
t2 = "java"
print((t1 + " " + t2 + " ") * 4)

# 35 ✅
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# 36 ✅
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))

# 37 ✅
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 38 ✅
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))
print(상장주식수, type(상장주식수))

# 39 ✅
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 40 ✅
data = "   삼성전자    "
print(data.strip())