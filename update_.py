import os
from insert_ import insert_
from delete_ import delete_
def update_():
    name = input("請輸入病患的姓名：")
    nid = input("請輸入病患的身分證字號：")
    delete_(name,nid)
    age = input("請輸入病患的年紀：")
    height = input("請輸入病患的身高(cm)：")
    weight = input("請輸入病患的體重(kg)：")
    insert_(name,nid,age,height,weight)

if __name__ == "__main__":
    update_()