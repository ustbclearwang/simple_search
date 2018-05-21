# 简易化的搜索引擎服务

开发系统：Deepin Linux 15.5

数据库：MySQL5.6

开发语言：Python2.7

web框架：Django1.8.18

分词：jieba0.39


## 开发思路

- 1.数据采集爬虫，爬虫对应网站的数据，我选择的是【简书】网站，数据为客户提供。

- 2.基于简书文章的标题进行分词提取tag，与该文章对应id然后存入数据库

- 3.数据检索利用分词得到tag,数据库查询tag对应的文章id


## 文件说明

- jianshu.sql 数据库结构以及测试数据

- stop_words.txt 结巴分词使用的[停用词](https://baike.baidu.com/item/停用词/4531676?fr=aladdin "https://baike.baidu.com/item/停用词/4531676?fr=aladdin")

- task_data_.xlsx 客户提供的测试数据

- jiashu django项目

## 演示结果

[![](https://github.com/0nise/simple_search/blob/master/images/images.png)](https://github.com/0nise/simple_search/blob/master/images/images.png "演示图片")

## 项目运行

- 1.修改[settings.py](https://github.com/0nise/simple_search/jianshu/jianshu/settings.py "https://github.com/0nise/simple_search/jianshu/jianshu/settings.py")文件数据库配置信息

- 2.运行[manage.py](https://github.com/0nise/simple_search/jianshu/manage.py "https://github.com/0nise/simple_search/jianshu/manage.py") runserver 0.0.0.0:8000

- 3.打开浏览器访问 http://localhost:8080/search/index/

## 更新日志

- 2018.5.21 更新