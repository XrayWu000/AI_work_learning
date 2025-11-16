print("Hello World")
a = 1
b = 3
c = a + b
print(c)
s = "Henry"
print(s[::-1])
print(s[:3])
print(s[:3] * 3)
print("this is a test for format:\n{0} {s} {c}".format('first', s = s, c = 32.2))
ans = input("how are you?\n")
print(ans)
stack = [12,4,7,26]
d = stack.pop()
stack.append(int(input("some number: ")))
#print(d + " " + *stack) 這是錯的
print(d, *stack)
dic = {3: 10, 1: 20, 2: 30}
# 1. items(): 同時取 key / value
print("items:", list(dic.items()))
# 2. 預設排序：依 key 排序（因為 tuple 先比第一個元素）
print("sort by key:", sorted(dic.items()))
# 3. 指定依 value 排序
print("sort by value:", sorted(dic.items(), key=lambda x: x[1]))
# 4. get() 找不到 key → 回傳 None
print("get missing:", dic.get(99))
# 5. get() 找不到 key，給預設值
print("get missing with default:", dic.get(99, "not found"))