import random
from pydantic import BaseModel
class Person(BaseModel):
    name:str
    height:int
    weight:int
    bmi:int=0
    suggestion:str='None'
def get_BMI_suggestion(bmi:float)->str:
    if(bmi<18.5):
        return "體重過輕"
    elif(bmi>=18.5 and bmi<24):
        return "正常範圍"
    elif(bmi>=24 and bmi<27):
        return "輕度肥胖"
    elif(bmi>=27 and bmi<30):
        return"中度肥胖"
    else:
        return "重度肥胖"

people:list[Person]=[]
with open('names.txt', encoding='utf-8') as namesfile:
    names_str=namesfile.read()
    names:list[str]=names_str.split(sep='\n')
    num=int(input('輸入所需人數: '))
    randomnames:list[str]=random.choices(names, k=num)
    for name in randomnames:
        p=Person(name=name, height=random.randint(120,190), weight=random.randint(30,120))
        p.bmi=p.weight/(p.height/100)**2        
        p.suggestion=get_BMI_suggestion(p.bmi)
        people.append(p)
    for person in people:
        print(f'姓名: {person.name:>3}, 身高: {person.height:>3}cm, 體重: {person.weight:>3}kg, BMI: {person.bmi:>5.2f}, 建議: {person.suggestion:>4}')