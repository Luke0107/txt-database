import os
def delete_(name,nid):
    # name = input("請輸入病患的姓名：") 
    # nid = input("請輸入病患的身分證字號：")
    if os.path.exists(f'{nid}.txt'):
        with open(f"{nid}.txt",'r') as f:
            l = f.readline()
            l = l.strip()
            if l==name:
                f.close()
                os.remove(f'{nid}.txt')
    else:
        print("查無此人")


if __name__ == "__main__":
    name = input("請輸入病患的姓名：") 
    nid = input("請輸入病患的身分證字號：")
    delete_(name,nid)