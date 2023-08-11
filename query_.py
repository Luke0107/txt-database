import os

def query_():
    name = input("請輸入病患的姓名：")
    nid = input("請輸入病患的身分證字號：")
    if os.path.exists(f'{nid}.txt'):
        with open(f'{nid}.txt',mode='r',encoding='UTF-8') as f:
            l = f.readlines()
            for i in range(len(l)):
                l[i] = l[i].strip()
            if l[0]==name:
                print("查詢成功！")
                print("姓名:",f"{name}")
                print("身分證字號:",f"{nid}")
                print("年齡:",f"{l[2]}")
                print("身高:",f"{l[3]}")
                print("體重:",f"{l[4]}")
            else:
                print("查詢失敗！")
    else:
        print("查無此人")


if __name__ == "__main__":
    query_()