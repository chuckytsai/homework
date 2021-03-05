

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
    sumM = 0
    for index in range(len(data["employees"])):
        #  若是employees有索引就會繼續幫大家總加salary
        sumM = sumM + data["employees"][index]["salary"]

    print('薪水平均:', sumM//len(data["employees"]))


# Tuple
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

# =====要求三：Python 演算法=====


def maxProduct(nums):
    sum = 0
    a = -float("inf")  # var a = -Infinity(javaScript)
    for test1 in range(0, len(nums)):
        for test2 in range(test1+1, len(nums)):
            sum = nums[test1] * nums[test2]
            a = max(a, sum)
    print('相成最大數', a)


maxProduct([5, 20, 2, 6])  # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3])  # 得到 30 因為 10 和 3 相乘得到最大值
maxProduct([-10, -20, 1, 2])  # 得到 200 因為 -20 和 -10 相乘得到最大值

# =====要求四：Python 演算法=====


def twoSum(nums, target):
    for test1 in range(0, len(nums)):
        for test2 in range(test1 + 1, len(nums)):
            if nums[test1] + nums[test2] == target:
                return [test1], [test2]


result = twoSum([2, 11, 7, 15], 9)
print('相加為9的2個數目索引', result)


# ========要求五：演算法========
def maxZeros(nums):
    add = 0
    max = 0
    for zeros in range(0, len(nums)):
        if nums[zeros] == 0:
            add = add+1  # add++;(JS)
        else:
            if add > max:
                max = add
            add = 0

    if add > max:
        max = add
    print('連續最多0的數目',max)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0


# # 排序名稱
# name_list = ["小雞", "兩大類", "小喵", "小蟲"]
# for name in name_list:
#     print(name)