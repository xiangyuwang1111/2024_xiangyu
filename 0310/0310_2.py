students=[{'國文': 90, '數學': 88, '英文': 61},
            {'國文': 98, '數學': 85, '英文': 63},
            {'國文': 86, '數學': 99, '英文': 85},
            {'國文': 52, '數學': 52, '英文': 71},
            {'國文': 53, '數學': 58, '英文': 98},
            {'國文': 54, '數學': 66, '英文': 54},
            {'國文': 94, '數學': 67, '英文': 70},
            {'國文': 69, '數學': 87, '英文': 89},
            {'國文': 100, '數學': 75, '英文': 100},
            {'國文': 100, '數學': 100, '英文': 100}]
#自訂義檔案名稱
import csv
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
filename=input('輸入檔案名稱:')
csvname=f'{filename}.csv'
save_file(filename,students)