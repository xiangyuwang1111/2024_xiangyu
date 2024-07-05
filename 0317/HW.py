from pydantic import BaseModel,Field,RootModel
import requests
import io
import csv

class Scores(BaseModel):
    姓名:str
    國文:int = Field(alias='科目1')
    英文:int = Field(alias='科目2')
    數學:int = Field(alias='科目3')
    地理:int = Field(alias='科目4')
    歷史:int = Field(alias='科目5')

class Student(RootModel):
    root:list[Scores]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
    
csv_url='https://raw.githubusercontent.com/roberthsu2003/python/master/pydantic/%E5%AD%B8%E7%94%9F%E5%88%86%E6%95%B8.csv'
web=requests.get(url=csv_url)
if web.ok:
    print('Downald successfully')
else:
    print('Downald failed')

csv_str:str=web.text
csv_file=io.StringIO(csv_str)
dict_reader=csv.DictReader(csv_file)
csv_data=list(dict_reader)

csv_stu=Student.model_validate(csv_data)

with open('new_student.csv', mode='w', encoding='utf-8', newline='') as student_file:
    dict_writer=csv.DictWriter(student_file, fieldnames=list(Scores.model_fields.keys()))
    dict_writer.writeheader()
    for score in csv_stu:
        dict_writer.writerow(score.model_dump())
    print('new_student.csv is created.')


