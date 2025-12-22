import random

def generate_winning_number(count = 6, lo = 1, hi = 49):
    win_num = set()

    while len(win_num) < count:
        win_num.add(random.randint(lo, hi))
    return win_num

LOW, HIGH = 1, 49

prize = generate_winning_number()
while True:
    special = random.randint(LOW, HIGH)
    if special not in prize:
        break
i = 0
while True:
    points = 0
    my_ticket = generate_winning_number()
    if special in my_ticket:
        points += 1
    points += len(prize & my_ticket) * 2
    i += 1
    if(points >= 11):
        break
    

print("point:", points)
print(prize)
print("{" + str(special) + "}")
print(my_ticket)
print("times:", i)
print("money(NTD$):", i * 50)