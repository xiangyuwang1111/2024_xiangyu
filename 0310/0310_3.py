import random
import pyinputplus as pyip
import csv
from pprint import pprint 

def get_student(n):
    students:list[dict]=[]
    for _ in range(n):
        student:dict[str:int]={}
        for subject in ['國文','英文','數學']:
            student[subject]=random.randint(50,100)
        students.append(student)
    return students
def save_file(filename:str,data:list[dict]):
    '''
    可以在這邊說明 
    數標移到function會出現說明
    '''
    with open(csvname,mode='w',encoding='utf-8',newline='') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=['國文','英文','數學'])
        writer.writeheader()
        writer.writerows(students)
    print(f'{csvname}存檔完成')
def main():
    num=pyip.inputNum('輸入多少學生: ')
    students=get_student(num)
    filename=input('輸入檔案名稱:')
    csvname=f'{filename}.csv'
    save_file(filename,students)

main()