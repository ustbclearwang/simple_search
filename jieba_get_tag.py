#!/usr/bin/python
#-*- coding:UTF-8 -*-
#coding=utf-8
import os
import sys
import xlrd
import jieba
import jieba.analyse
import json
import MySQLdb
from DBUtils.PooledDB import PooledDB
pool_db = PooledDB(MySQLdb,20,host='127.0.0.1',user='root',passwd='root',db='jianshu',port=3306,charset='utf8')
connection = pool_db.connection()
cursor = connection.cursor()
"""
excle文件加
"""
def load_excel(filename, byindex=0):
    test_data = xlrd.open_workbook(filename,encoding_override='utf-8')
    sheet = test_data.sheets()[byindex]
    return sheet

"""
获取简书内容信息
"""
def get_task_data():
    sql = "SELECT id,article_title FROM task_data"
    result_dict = {}
    cursor.execute(sql)
    all_data = cursor.fetchall()
    for data in all_data:
        result_dict[data[0]] = data[1]
    return result_dict

"""
分词
"""
def cut():
    task_dict = get_task_data()
    topK = 10
    jieba.analyse.set_stop_words('stop_words.txt')
    for task_id in task_dict:
        tags = jieba.analyse.extract_tags(task_dict[task_id], topK=topK)
        print task_dict[task_id]
        for tag in tags:
            sql = "INSERT INTO search_data(id,search_keyword,task_data_id)VALUES(DEFAULT,'"+tag+"','"+str(task_id)+"')"
            cursor.execute(sql)
            connection.commit()
            print tag
        #print(",".join(tags))

if __name__ == '__main__':
    cut()