建立資料庫和資料表
透過任何方式 ( 建議練習使用終端機 Command Line 介面，為未來使用 Linux 系統打基礎 )，
連結到 MySQL 伺服器中進行管理，完成以下動作：
1. 建立一個新的資料庫，取名字為website。
2. 在資料庫中，建立資料表，取名字為user。資料表中必須包含以下欄位設定：


基本的 SQL 指令
● 使用 INSERT 指令新增一筆資料到 user 資料表中，這筆資料的 username 和
password 欄位必須是 ply。接著繼續新增至少 4 筆隨意的資料。

● 使用 SELECT 指令取得所有在 user 資料表中的使用者資料。

● 使用 SELECT 指令取得 user 資料表中總共有幾筆資料。

● 使用 SELECT 指令取得所有在 user 資料表中的使用者資料，並按照 time 欄位，由近
到遠排序。

● 使用 SELECT 指令取得 user 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近
到遠排序。

● 使用 SELECT 指令取得欄位 username 是 ply 的使用者資料。

● 使用 SELECT 指令取得欄位 username 是 ply、且欄位 password 也是 ply 的資料。

● 使用 UPDATE 指令更新欄位 username 是 ply 的使用者資料，將資料中的 name 欄位
改成【丁滿】。

● 使用 DELETE 指令刪除所有在 user 資料表中的資料。

