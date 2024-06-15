# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
ans=random.randint(1,100)
count=0
while True:
    count+=1
    re=int(input("請輸入數字："))
    
    if re==ans:
        print("終於猜對了")
        print("猜第",count,"次")
        break
    elif re< ans:
        print("比答案小")
    else:
        print("比答案大")
    print("猜第",count,"次")