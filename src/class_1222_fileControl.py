
f = open("a.txt", "w", encoding="utf-8")
f.write("Hello\nWorld!")
f.close()

with open("a.txt", "w", encoding="utf-8") as f:
    f.write("Hello\nWorld!")

f = open("a.txt", "r", encoding="utf-8")
content = f.read()
f.close()
print(content)

with open("a.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)