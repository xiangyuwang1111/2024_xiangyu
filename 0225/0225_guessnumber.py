import random
import pyinputplus as pyip
print("========猜數字遊戲========\n")
x=random.randint(1,100)
count=0
m=1
M=100
while(1):
    ans=pyip.inputInt(f"猜數字({m}-{M}):",min=m,max=M)
    count+=1
    if(ans<x):
        print("大一點!")
        m=ans
    elif(ans>x):
        print("小一點!")
        M=ans
    else:
        print(f"猜中了!猜了{count}次\n")
        break