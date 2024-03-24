import random
import csv
import pyinputplus as pyip
import tools

if __name__ == '__main__':
    csv_name = pyip.inputStr("放在指定資料夾中的檔案名稱全名:")
    get_name_cnt = pyip.inputInt("抽幾個人?")
    get_sbj_cnt = pyip.inputInt("放幾個科目?")

    #隨機抽n個人
    result = tools.getStudents(csv_name,get_name_cnt)

    #每個人隨機放n個分數(分數從0~100)
    data = tools.genScores(result, get_sbj_cnt)
        
    #設定column name
    sbjs = [f"科目{i+1}" for i in range(get_sbj_cnt)]
    title=["姓名"]
    title.extend(sbjs)

    #存檔
    fileName=pyip.inputFilename("請輸入檔案名稱(不用輸入副檔名)")

    #存1.CSV或是2.Excel
    fileType=pyip.inputChoice(["1","2"],"輸入1)存CSV\n輸入2)存CSV和Excel\n")

    try:
        if fileType == "1":
            tools.saveListToCSV(fileName,title,data)
        elif fileType == "2":
            tools.saveListToCSV(fileName,title,data)
            tools.saveListToXlsx(fileName,title,data)
            print("存檔成功")
        else:
            print("存檔失敗")
    except:
        print("存檔失敗")

    #讀取成list[dict]再重新用dict方法寫入csv/excel
    dictData = tools.getListOfDictFromCsv(fileName+".csv")
    dictTitle=list(dictData[0].keys())
    print(dictTitle)

    newFileName="_"+fileName
    
    tools.saveDictToCSV(newFileName,title,dictData,"Y")
    tools.saveDictToXlsx(newFileName,title,dictData,"Y")
        
    print("存檔成功")

    
