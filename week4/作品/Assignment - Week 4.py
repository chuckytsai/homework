# 載入模組
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from markupsafe import escape
import json 

# 建立Application物件
# 設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="accountLogin",  # 靜態檔案的資料匣名稱
    static_url_path="/"
)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin",methods=["POST"])
def signin():
    name = request.form["whatName"]
    if name == "test":
        name = request.form["whatPW"]
        if name == "test":
            return render_template("member.html")
    name = request.form["whatName"]
    if name != "test":
        return render_template("error.html")
    name = request.form["whatPW"]
    if name != "test":
        return render_template("error.html")
    if request.method == 'POST':
        session['whatName'] = request.form['whatName']
        return redirect(url_for('index'))
        
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

app.run(port=3000)



