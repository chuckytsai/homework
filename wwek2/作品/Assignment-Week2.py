# =====#要求一：函式與流程控制 =====
def calculate(min, max):
    sum = 0
    for x in range(min, max+1):
        sum = sum+x
    print('數字總加為: ', sum)


calculate(1, 3)  # 程式要能夠計算 1+2+3，最後印出 6

calculate(4, 8)  # 程式要能夠計算 4+5+6+7+8，最後印出 30


# =====要求二：Python 字典與列表物件與陣列=====
# 正確計算出員工的平均薪資，並考慮員工數量會變動的情況

def avg(data):
    # sumM = 0
    # for index in range(len(data[employees]):
    # #  若是employees有索引就會繼續幫大家總加salary
    #     sumM=sumM+data.employees[index].salary
    #     sumM//len(data.employees)
    # print(sumM)
    print("大家平均薪水",len(data))
    

avg({
    "count": 3,
    "employees": [
        {
            "name": "John",
            "salary": 30000,
        },
        {
            "name": "Bob",
            "salary": 60000,
        },
        {
            "name": "Jenny",
            "salary": 50000,
        }
    ]
})


