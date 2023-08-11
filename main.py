import os
from insert_ import insert_
from query_ import query_
from delete_ import delete_
from update_ import update_
while True:
    choice =input("(1)新增(2)查詢(3)刪除(4)更改(5)結束程式：")
    if choice =='1':
        name = input("請輸入病患的姓名：") 
        nid = input("請輸入病患的身分證字號：") 
        age = input("請輸入病患的年紀：")
        height = input("請輸入病患的身高(cm)：")
        weight = input("請輸入病患的體重(kg)：")
        insert_(name,nid,age,height,weight)
    elif choice=='2':
        query_()
    elif choice=='3':
        name = input("請輸入病患的姓名：") 
        nid = input("請輸入病患的身分證字號：")
        delete_(name,nid)
    elif choice=='4':
        update_()
    elif choice=='5':
        print("結束程式！")
        break
    else:
        print("無效指令！")
os.system('pause')