#猜數字的.py檔,用$ python lesson7_3.py 執行

import random

min = 1
max = 10
target = random.randint(1,10)
#target = random.rantrange(1,11)
print(f"target={target}")

count = 0
while(True):

    count+=1
    print(f"猜數字,第{count}次:")
    i = int(input(f"請輸入數字,範圍{min}~{max}:"))
    print(i)

    if(i == target):
        print("猜對了!")
        break
    elif(i >=1 and i <= 10):

        #pass #沒內容時可用pass
        if(i<target):
            print("提示:再大一點!")
        else:
            print("提示:再小一點!")
    else:
        print("超過範圍!請重新輸入!")
