import random

#輸入，准許一模一樣、純字和純數
while 1 :
    player = input("輸入: 0.剪刀 1.石頭 2.布\n")
    if player == "0.剪刀" or player == "剪刀" or player == "0":
        player = "0"
    elif player == "1.石頭" or player == "石頭" or player == "1":
        player = '1'
    elif player == "2.布" or player == "布" or player == "2":
        player = '2'
    else:
        print("錯誤輸入")
        continue
    player = int(player)
    break

com = random.randint(0, 2)
trans = ["剪刀", "石頭", "布"]
print("電腦出:", trans[com])

resultCom = (com + 1) % 3
resultPla = (player + 1) % 3
if(player == resultCom):
    print("你贏了")
elif(com == resultPla):
    print("你輸了")
else:
    print("平手")