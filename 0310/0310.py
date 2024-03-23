import random
import pyinputplus as pyip
from pprint import pprint 
num=pyip.inputNum('How many students?')
students:list[dict]=[]
for _ in range(num):
    student:dict[str:int]={}
    for subject in ['Chinese','English','Math']:
        student[subject]=random.randint(50,100)
    students.append(student)
pprint(students)