total = 0
i = 0
while i < 100:
    if(i == 0):
        i += 1
        continue
    j = 1
    t = 1
    while j < i:
        t *= j
        j += 1
    total += (1 / t)
    i += 1
print(total)