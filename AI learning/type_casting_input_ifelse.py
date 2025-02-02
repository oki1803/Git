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

# 10 mod 3 等於3餘1
#print (10 % 3)
# 11 mod 3 等於3餘2
#print (11 % 3)
# 12 mod 3 等於4餘0
#print (12 % 3)

#x = 1
#y = 2
#z = 3
#print (max (x,y,z))
#print (min(x,y,z))

#c = -4
#a = 4.6
#四捨五入
#print(round(a))
import math
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

#age = int(input("請輸入你的年齡:"))
#if age >= 100:
#    print("你年齡太大，無法註冊")
#elif age >= 18:
#    print("你可以註冊")
#elif age < 0:
#    print("你還未出生")
#else:
#    print("你必須年滿18歲才能註冊")

operator = input("請輸入運算符(加法:+，減法：-，乘法：*，除法：/")
num1 = float(input("請輸入第一個數字:"))
num2 = float(input("請輸入第二個數字:"))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    print(f"運算符號無效")
print(f"運算結果是{round(result)}")