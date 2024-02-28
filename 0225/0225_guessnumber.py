#自定義function
import random
import pyinputplus as pyip
def playgame():
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
def main():
    while(1):
        playgame()
        menu_value=pyip.inputMenu(["yes","no"],prompt="還要繼續嗎?\n",numbered=True)
        if(menu_value=="no"):break
    print("遊戲結束")
#main()

#python專案的主執行檔
if(__name__=="__main__"):
    main()