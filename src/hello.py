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