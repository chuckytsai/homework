
要求二：建立資料庫和資料表
透過任何方式 ( 建議練習使用終端機 Command Line 介面，為未來使用 Linux 系統打基礎 )，
連結到 MySQL 伺服器中進行管理，完成以下動作：
1. 建立一個新的資料庫，取名字為website。
2. 在資料庫中，建立資料表，取名字為user。資料表中必須包含以下欄位設定：
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/website.JPG)
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/usertable.JPG)

基本的 SQL 指令

● 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和
password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/INSERT%204%2B1.JPG)

● 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/INSERT%204%2B1.JPG)

● 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/COUNT.JPG)

● 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近
到遠排序。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/orderBy.JPG)

● 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近
到遠排序。

![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/where2-4.JPG)

● 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/wherePLY.JPG)

● 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/wherePLYandPW.JPG)

● 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位
改成【丁滿】。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/PLY丁滿.JPG)

● 使用 DELETE 指令刪除所有在 user 資料表中的資料。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/delete.JPG)

結合資料表 SQL JOIN 的操作 (Optional)

在資料庫中，建立新資料表，取名字為message。資料表中必須包含以下欄位設定：
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/messageTable.JPG)

使用 SELECT 搭配 JOIN 的語法，取得所有留言，資料中須包含留言會員的姓名。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/joincontent.JPG)

使用 SELECT 搭配 JOIN 的語法，取得 user 資料表中欄位 username 是 ply 的所有留
言，資料中須包含留言會員的姓名。
![image]( https://github.com/chuckytsai/homework/blob/main/week5/img/wherePLYJOIN.JPG)

