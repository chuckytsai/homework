from flask import Flask  # 載入模組
from flask import request
from flask import redirect
from flask import render_template
import json

# 建立Application物件
# 設定靜態檔案的路徑處理 #圖片也是用靜態
app = Flask(
    __name__,
    static_folder="accountLogin",  # 靜態檔案的資料匣名稱
    static_url_path="/"  # 靜態對應的網址名稱改成空白
    #所有的static資料下的檔案,都對應到網址路徑 /static/檔案名稱
)



# 建立路徑 /getSum對應的處理函式
# 要求字串 getSum?min=最小數字&max=最大數字
# @app.route("/getSum")
# def getSum():
#     maxNumber=request.args.get("max",100)
#     maxNumber=int(maxNumber)
#     minNumber=request.args.get("min",1)
#     minNumber=int(minNumber)

#     result=0
#     for n in range(minNumber,maxNumber+1):
#         result += n
#     return "結果: "+ str(result)

# 建立網站路徑
@app.route("/") 
def index(): 
    return render_template("index.html")


#處理路徑 /error的對應函式
@app.route("/Error")
def error():
    return render_template("error.html")

#後端按鈕寫法
@app.route("/show")
def show():
    data=request.args.get("data","")
    return "歡迎光臨 ,"+ data

#後端按鈕寫法
@app.route("/caluculate")
def caluculate():
    math=request.args.get("math","")
    math=int(math)  #轉為數字
    result=0
    for n in range(1,math+1):
        result+=n
    return "結果為: "+ str(result)



# 建立網站路徑對應的處理方式(用英文或中文的語言偏好做區分)
# @app.route("/en/") 
# def index_english(): 
#     return json.dumps({
#         "status": "ok",
#         "text": "Hello"
#     })

# @app.route("/zh/")  
# def index_chinese(): 
#     return json.dumps({
#         "status": "ok",
#         "text": "您好"
#     }, ensure_ascii=False)  # 指示不用ASCII編碼處理中文

# @app.route("/")
# def index():
#     lang = request.headers.get("accept-language")  # 抓取語系
#     if lang.startswith("en"):
#         return redirect("/en/")
#     else:
#         return redirect("/zh/")

    # 回傳網站首頁的內容

    # print("請求方法",request.method)
    # print("通訊協定",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))





# @app.route("/data")  #data路徑
# def handleData():
#     return "My Data"


# # 動態路由:建立路徑/user/使用者名稱 對應的處理函式
# @app.route("/user/<username>")
# def handleUser(username):
#     if username=="chucky":
#         return "你好 "+username
#     else:
#         return "Hello " +username
# 啟動網站伺服器 指定port參數指定埠號
app.run(port=3000)
