#外面是list 要用rootmodel
from pydantic import BaseModel, RootModel, Field, ValidationError
import requests
import pandas as pd
from requests import Response
youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
try:
    response:Response=requests.get(youbike_url)
except:
    print('INTERNET ERROR')
else:
    print('INTERNET OKAY!')

if response.status_code==200:
    print('DOWNALD SUCCESSFULLY')
else:
    print('DOWNALD FAILED')

class Site(BaseModel):
    站點名稱:str=Field(alias='sna')
    行政區:str=Field(alias='sarea')
    日期:str=Field(alias='mday')
    總車輛數:int=Field(alias='tot')
    可借:int=Field(alias='sbi')
    可還:int=Field(alias='bemp')

class Sites(RootModel):
    root:list[Site]

    def __iter__(self):
        return iter(self.root)
    def __getitem__(self, item):
        return self.root[item]


response.encoding='utf-8'
#取出純文字的json
response.text
#取出python的資料結構
data:list[dict]=response.json()
sites:Sites=Sites.model_validate(data)
source_data:list[dict]=sites.model_dump()['root']
df1=pd.DataFrame(source_data)