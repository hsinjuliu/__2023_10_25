import random
import csv
from openpyxl import Workbook

def getStudents(txt_name:str='random.txt', get_cnt:int=1) -> list:
    '''
    getRandom
    txt_name: file name with format .txt, default is random.txt
    get_cnt: need get how much random info, default is 1
    '''

    #open file
    src_file = open(txt_name,mode='r',encoding='utf-8')
    src_str = src_file.read()
    src_file.close()
    
    print()
    print("file content:" , src_str)
    print()

    #split file to list
    datalist = src_str.split('\n')
    max =len(datalist)

    print('data size:',max)
    print() 


    if get_cnt > max:
        return random.sample(datalist,max)
    else:
        return random.sample(datalist,get_cnt)


def genScores(origData:list,randomCnt:int) -> list:
    #每個人隨機放n個分數(分數0~100)
    data = []
    for name in origData:
        name_sbj = [name]
        for i in range(0,randomCnt):
            name_sbj.append(random.randint(0,100))
        data.append(name_sbj)
    print(data)
    return data

def getListOfDictFromCsv(fileName):
    #讀取CSV存成list[dict]
    dictKeys = []
    dictData = []
    with open(fileName, mode="r", encoding="utf-8") as f:
        dictReader = csv.DictReader(f)
        fieldnames=dictReader.fieldnames
        for row in dictReader:
            dictData.append(row)

    print("讀取出的list[dict]")
    print(dictData)
    return dictData


def saveListToCSV(fileName:str,title:list[str], data:list[list]) ->list[list]:
    fileName += ".csv"
    print(f"檔案名稱:{fileName}")
    print(f"欄位名稱:{title}")
    print(f"資料:{data}")

    try:
        with open(fileName,mode='w',encoding='utf-8',newline='') as file:
            writer=csv.writer(file)

            if title != None:
                writer.writerow(title)

            writer.writerows(data)
        return True
    except:
        return False
    else:
        return False
    
def saveDictToCSV(fileName:str,title:list[str],data:list[dict],isWriteHeader:str):
    fileName += ".csv"
    print(f"檔案名稱:{fileName}")
    print(f"欄位名稱:{title}")
    print(f"資料:{data}")

    try:
        with open(fileName,mode='w',encoding='utf-8',newline='') as file:
            dicWriter=csv.DictWriter(file,title)
            if isWriteHeader == "Y":
                dicWriter.writeheader()
            dicWriter.writerows(data)
        return True
    except:
        return False
    else:
        return False


def saveListToXlsx(fileName:str,title:list[str],data:list[list]) ->list[list]:
    fileName += ".xlsx"
    print(f"檔案名稱:{fileName}")
    print(f"欄位名稱:{title}")
    print(f"資料:{data}")

    wb = Workbook()

    #預設的Sheet
    ws = wb.active 

    #寫入title
    ws.append(title)

    #從wb目前的row index開始寫
    for row in data:
        ws.append(row)

    #存檔
    wb.save(fileName)


def saveDictToXlsx(fileName:str,title:list[str],data:list[dict],isWriteHeader:str):
    fileName += ".xlsx"
    print(f"檔案名稱:{title}")
    print(f"欄位名稱:{fileName}")
    print(f"資料:{data}")

    wb = Workbook()

    #預設的Sheet
    ws = wb.active 

    #寫入title
    if isWriteHeader == "Y":
        ws.append(title)

    
    #從list[dict]分離資料
    rowdata = []
    for dictData in data:
        rowdata.append(list(dictData.values()))

    #從wb目前的row index開始寫
    for row in rowdata:
        ws.append(row)

    #存檔
    wb.save(fileName)
