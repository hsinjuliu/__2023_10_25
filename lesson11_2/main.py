import random
import csv
import pyinputplus as pyip
from packageName.tools import getRandom,saveToCSV,putRandomInt

'''
main.py:
__name__ == '__main__' 代表主執行檔
要使用其他function就import
'''

if __name__ == '__main__':
    csv_name = pyip.inputStr("放在指定資料夾中的檔案名稱全名:")
    get_name_cnt = pyip.inputInt("抽幾個人?")
    get_sbj_cnt = pyip.inputInt("放幾個科目?")

    #隨機抽n個人
    result = getRandom(csv_name,get_name_cnt)
    print(f"隨機抽{get_name_cnt}個人結果:")
    print(result)

    #每個人隨機放n個分數
    data = putRandomInt(result, get_sbj_cnt)
        
    #設定column name
    '''測試存檔失敗
    title=None
    '''
    sbjs = [f"科目{i+1}" for i in range(get_sbj_cnt)]
    title=["姓名"]
    title.extend(sbjs)


    fileName=pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名)")

    if saveToCSV(fileName,title,data):
        print("存檔成功!")
    else:
        print("存檔失敗")
    



