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
    #對Student對象進行迭代操作時，例如在 for 迴圈中使用它，__iter__ 方法會被呼叫並返回self.root的迭代器。
    def __iter__(self):
        return iter(self.root)
    
    #可以通過索引訪問 Student 對象中的 Scores 對象
    def __getitem__(self, item):
        return self.root[item]
    
csv_url='https://raw.githubusercontent.com/roberthsu2003/python/master/pydantic/%E5%AD%B8%E7%94%9F%E5%88%86%E6%95%B8.csv'
web=requests.get(url=csv_url)
if web.ok:
    print('Downald successfully')
else:
    print('Downald failed')

#==========================================
csv_str:str=web.text
csv_file=io.StringIO(csv_str)
dict_reader=csv.DictReader(csv_file)
csv_data=list(dict_reader)
csv_stu=Student.model_validate(csv_data)
json_str=csv_stu.model_dump_json()
#==========================================

#create csv file
with open('new_student.csv', mode='w', encoding='utf-8', newline='') as student_csv_file:
    dict_writer=csv.DictWriter(student_csv_file, fieldnames=list(Scores.model_fields.keys()))
    dict_writer.writeheader()#寫入欄位名稱
    for score in csv_stu:
        dict_writer.writerow(score.model_dump())#model_dump()將資料轉為python的資料結構，以寫入檔案
    print('new_students.csv is created.')

#create json file
with open('new_students.json', mode='w', encoding='utf-8') as student_json_file:
    student_json_file.write(json_str)
    print('new_students.json is created.')