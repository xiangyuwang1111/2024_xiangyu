from pydantic import BaseModel,Field,RootModel


class Scores(BaseModel):
    姓名:str
    國文:int = Field(alias='科目1')
    英文:int = Field(alias='科目1')
    數學:int = Field(alias='科目1')
    地理:int = Field(alias='科目1')
    歷史:int = Field(alias='科目1')


class Student(RootModel):
    root:list[Scores]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]