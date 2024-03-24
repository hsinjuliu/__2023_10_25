import random
import csv

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
        

def saveListToCSV(fileName:str,title:list[str],data:list[list]) ->list[list]:
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