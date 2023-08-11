def insert_(name, nid, age, height, weight):
    with open(f"{nid}.txt", 'w') as f:
        f.write(name + "\n")
        f.write(nid + "\n")
        f.write(age + "\n")
        f.write(height + "\n")
        f.write(weight + "\n")

if __name__ == "__main__":
    print(1)
    name = input("請輸入病患的姓名：")
    nid = input("請輸入病患的身分證字號：")
    age = input("請輸入病患的年紀：")
    height = input("請輸入病患的身高(cm)：")
    weight = input("請輸入病患的體重(kg)：")
    insert_(name, nid, age, height, weight)
