#!/usr/bin/python
# coding: utf-8

#将200个字符串存入MySQL中

from ActiveCodes import codes
import mysql.connector
from mysql.connector import errorcode

if __name__ == '__main__':
    active_codes = codes(200,15)
    # print active_codes
    cnx = mysql.connector.connect(user="root", password="root",host="127.0.0.1",database="ActiveCodesStore")
    cursor = cnx.cursor()
    # create table
    create_table = "CREATE TABLE `UsedCodes` (" \
        "`id` int(11) unsigned NOT NULL ," \
        "`activeCode` varchar(15) DEFAULT NULL, " \
        " PRIMARY KEY (`id`) " \
        " ) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;"
    try:
        cursor.execute(create_table)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("table already exists.")
        else:
            print(err.msg)

    # insert data
    for i in range(len(active_codes)):
        print i
        active_code = active_codes[i]
        insert_cmd = "Insert into UsedCodes (id, activeCode) values (%d, \"%s\")" % (i, active_code)
        #print insert_cmd
        try:
            cursor.execute(insert_cmd)
        except mysql.connector.Error as err:
            print(err.msg)
    # 没有下面这句，数据不会保存到数据库中
    cnx.commit()
    
    cursor.close()
    cnx.close()
