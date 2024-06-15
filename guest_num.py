# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
start=input("請決定隨機數字範圍開始值:")
end=input("請決定隨機數字範圍結束值:")
start=int(start)
end=int(end)
ans=random.randint(start,end)
count=0
while True:
    count+=1
    re=int(input("請輸入數字："))
    
    if re==ans:
        print("你猜中了!")
        print("這是你猜的第",count,"次")
        break
    elif re< ans:
        print("比答案小")
    else:
        print("比答案大")
    print("這是你猜的第",count,"次")