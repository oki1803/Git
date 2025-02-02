#AI learning
# integer 整數
#age = 30
# float 浮點數 
#gpa = 3.3
# string str
#name = 'Peter'
#boolean # ture, false
#is_online = True
#print(f"在線上嗎?{is_online}"),print(f"我的名字是{name}"),print(f"我的GPA{gpa},我今年{age}歲")

#顯示型別轉摸 & 隱藏型別轉摸
#age = 30
#gpa = 3.3
#student = True
#age = float(age)
#print(age)
#print(type(age))
#name  = input("請輸入名字:")
#print(f"你的名字是{name}")

#Length = float(input("長度"))
#Width = float(input("寬度"))
#Area = Length * Width
#print(f"面積為{Area}m2")

#item = input(")你想購買什麼物品")
#price = float(input("價格多少？"))
#quantity = int(input("你需要多少件？"))
#total = price * quantity
#print(f"你購買了{quantity}個 {item}，總價為 ${total}")

#加減乘除
#apples = 3
#apples += 1
#print(int(apples))
#apples -= 2
#print(int(apples))
#apples *= 3
#print(int(apples))
#apples /= 3
#print(int(apples))
#apples **= 2

#Mod 求餘數
# 10 mod 3 等於3餘1
#print (10 % 3)
# 11 mod 3 等於3餘2
#print (11 % 3)
# 12 mod 3 等於4餘0
#print (12 % 3)

#化簡
#x = 1
#y = 2
#z = 3
#print (max (x,y,z))
#print (min(x,y,z))

#c = -4
#a = 4.6
#四捨五入
#print(round(a))
#import math
#四捨五入進位
#print(math.ceil(a))
#四捨五入捨去
#print(math.floor(a))
# 絕對值
#print(abs(c))

#計算圓的周長 2πR
#radius = float(input("請輸入圓的半徑"))
#c = 2 * math.pi * radius
#print(f"圓的周長為{round (c,2)}")

# 計算圓的面積 πR2
#radius = float(input("請輸入圓的半徑"))
#area = math.pi * (radius ** 2)
#print(f"圓的面積為{round(area,2)}")

#if else and elif
#age = int(input("請輸入你的年齡:"))
#if age >= 100:
#    print("你年齡太大，無法註冊")
#elif age >= 18:
#    print("你可以註冊")
#elif age < 0:
#    print("你還未出生")
#else:
#    print("你必須年滿18歲才能註冊")

#operator = input("請輸入運算符(加法:+，減法：-，乘法：*，除法：/")
#num1 = float(input("請輸入第一個數字:"))
#num2 = float(input("請輸入第二個數字:"))
#if operator == '+':
#    result = num1 + num2
#elif operator == '-':
#    result = num1 - num2
#elif operator == '*':
#    result = num1 * num2
#elif operator == '/':
#    result = num1 / num2
#else:
#    print(f"運算符號無效")
#print(f"運算結果是{round(result)}")

# 單位轉換
#weight = float(input("請輸入你的體重："))
#unit = input("你的體重是公斤還是磅？(kg/Lb)").upper()
#if unit == 'KG':
#    weight *= 2.2
#    new_unit = '磅'
#elif unit == 'LB' :
#    weight /= 2.2
#    new_unit ="公斤"
#else:
#    print('單位不正確')
#    exit()
#print(f"你的體重是 {round(weight)}{new_unit}")


#name = "code shiba"
#length = int(len(name))
#print("你的全名共有", length, "個字元")
#space_pos = name.find(" ")
#print("第一個空格出現在第", space_pos, "個字元")
#name_capitalized = name.capitalize()
#print(name_capitalized)
#name_upper = name.upper()
#print(name_upper)
#name_lower = name.lower()
#print(name_lower)

#username = input("請輸入你的使用者名稱:")
#if (len(username) > 12 or len(username) <= 2):
#    print("你的使用者名稱不能超過12個字元或少過2個字元")
#elif " " in username:
#    print("你的使用者名稱不能包含空格")
#elif not username.isalpha():
#    print("你的使用者名稱不能包含數字")    
#else:
#    print("歡迎" + username)

#credit_number = "1234-5678-9876-5432"
#first_char = credit_number [0]
#print("第一個字元：",first_char)
#second_char = credit_number [1]
#print("第二個字元：",second_char)
#first_four = credit_number [0:4]
#print("前四個字元：",first_four)
#last_one = credit_number [-1]
#print("最後一個字元：",last_one)
#last_two = credit_number [-2]
#print("最後第 2個字元:",last_two)

#email = "codeshiba@gmail.com"
#index = email. index ("@")
#print (index)
#print(email[0:index])
#print(email[index:])
#print(email[(index+1):])

#price_1 = 3.321
#price_2 = -77
#price_3 = 15.11
#.2f 小數後2位, <^>10 對齊左中右第10位, >+ 加上正負號
#print(f"價格 1為{price_1:.2f}\n"
#f"價格2為{price_2:^10.2f}\n"
#f"價格 3為{price_3:>+.2f}")


#While 迴圈
#num = int(input("請輸入 1 到10之間的數字:"))
#while num < 1 or num > 10:
#    print(f"你輸入的數字 {num}是無效的")
#    num = int(input("請輸入 1 到 10 之間的數字:"))
#print(f"你輸入了 {num}")

#For 迴圈
#for x in range(1,11):
#    print(x)
#for y in reversed(range(1,11)):
#    print(y)

#credits_cards = "1234-5678-9012-3456"
#for z in credits_cards:
#    if z == '9':
#        continue
#    else:
#        print(z)
#or c in credits_cards:
#    if c == '9':
#        break
#    else:
#        print(c)

#for y in range(5):
#    for x in range(1,10):
#        print(x,end=" ")
#    print()    

#rows = int(input("請輸入行數:"))
#cols = int(input("請輸入列數:"))
#symbol = input("請輸入符號:")

#for i in range(rows):
#    for j in range(cols):
#        print(symbol, end=" ")
#    print()

#import time
#my_time = int(input("請輸入秒數:"))
#for x in range(my_time):
#    print(x)
#    time.sleep(1)
#print("時間到了!")

#for y in range(my_time, 0, -1):
#    print(y)
#    time.sleep(1)
#print("時間到了!")

#for z in range(my_time):
#    seconds = z % 60
#    minutes = z // 60 % 60
#    print(f"{minutes:02}:{seconds:02}")
#    time.sleep(1)
#print("時間到了!")


goods = []#列表
prices = []
while True:
    good = input("請輸入想購買的物器:")
    if good.lower() =="q":
        break

    price = float(input(f"請輸入{good}的價格:"))
    goods.append(good)
    prices.append(price)
print("商品:", goods)
print("價格:", prices)
for index, good in enumerate(goods):
#    print("索引 index: ", index)
#    print("商品名稱: ", good)
    print(f"第{index +1}商品是{good}, 價格:{prices[index]:.2f}")