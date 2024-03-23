import random
import csv

def getRandom(txt_name:str='random.txt', get_cnt:int=1) -> list:
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


def putRandomInt(origData:list,randomCnt:int) -> list:
    #每個人隨機放n個分數
    data = []
    for name in origData:
        name_sbj = [name]
        for i in range(0,randomCnt):
            name_sbj.append(random.randint(0,100))
        data.append(name_sbj)
    print(data)
    return data
        

def saveToCSV(fileName:str,title:list[str],data:list[list]) ->list[list]:
    fileName += ".csv"
    print("檔案名稱",fileName)
    print(f"資料:{data}")

    try:
        with open(fileName,mode='w',encoding='utf-8',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(title)
            writer.writerows(data)
        return True
    except:
        return False
    else:
        return False