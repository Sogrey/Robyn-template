#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

def sqlite3_connect(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor

def sqlite3_close(conn, cursor):
    cursor.close()
    conn.close()

def sqlite3_execute(dbPath, sql, params):
    conn, cursor = sqlite3_connect(dbPath)
    cursor.execute(sql, params)
    values = cursor.fetchall()
    sqlite3_close(conn, cursor)
    return values

def sqlite3_execute_no_result(dbPath, sql, params):
    conn, cursor = sqlite3_connect(dbPath)
    cursor.execute(sql, params)
    conn.commit()
    sqlite3_close(conn, cursor)

def insert1(userId,userName):
    sql = "create table user (id varchar(20) primary key, name varchar(20))"    
    sqlite3_execute_no_result("test.db", sql, '')

    sql = "insert into user (id, name) values ('?', '?')"  
    sqlite3_execute_no_result("test.db", sql, userId, userName)

def insert2():
    sql = "select * from user where id=?"   
    res = sqlite3_execute("test.db", sql, '1')
    print(res)



# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect("test.db")
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
# cursor.execute("create table user (id varchar(20) primary key, name varchar(20))")
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute("insert into user (id, name) values ('1', 'Michael')")
# # 通过rowcount获得插入的行数:
# print("rowcount =", cursor.rowcount)
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()

# # 查询记录：
# conn = sqlite3.connect("test.db")
# cursor = conn.cursor()
# # 执行查询语句:
# cursor.execute("select * from user where id=?", "1")
# # 获得查询结果集:
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()
