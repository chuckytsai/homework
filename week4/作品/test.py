# 載入模組
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from markupsafe import escape
import os
import json

# 儲存檔案
with open("material\\vip\\np.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello\n沒意義的第二行")

# 讀取帳號密碼Json檔案
with open("material\\vip\\np.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)


inputNameValue = "test"
inputPWValue = "test"


for psycho in range(0, len(data["nightwalker"])):
    if data["nightwalker"][psycho]["name"]== inputNameValue:
        if data["nightwalker"][psycho]["password"]== inputPWValue:
            x=inputNameValue
            print(x)
     
