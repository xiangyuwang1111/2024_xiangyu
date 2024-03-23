import random
import pyinputplus as pyip
from pprint import pprint 

def get_student(n):
    students:list[dict]=[]
    for _ in range(n):
        student:dict[str:int]={}
        for subject in ['Chinese','English','Math']:
            student[subject]=random.randint(50,100)
        students.append(student)
    return students

num=pyip.inputNum('How many students: ')
stus=get_student(num)
pprint(stus)