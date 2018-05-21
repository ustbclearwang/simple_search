#encoding: utf-8
import os
import json
import time
import datetime
import logging
import traceback
import jieba
import jieba.analyse
from django.shortcuts import render_to_response,render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import *
from threading import Thread
from django.db.models import Q
from django.db import connection
from django.db.models import Count
'''
转发到搜索页面
'''
def index(request):
    return render(request,'index.html')

'''
切词
'''
def api_search(request):
    if request.method != 'POST':
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errMsg = 'Method not allowed',successResult=''))
    try:
        keyword_str = request.POST.get('name',None)
        flag = False
        tag_list = []
        if keyword_str:
            # 调用切词
            tag_list = keyword_cut(keyword_str)
            SearchData_info = SearchData.objects.filter(search_keyword__in=tag_list).values('task_data_id').order_by().annotate(Count('task_data_id'))
            task_data_id_list = []
            for _ in SearchData_info:
                task_data_id_list.append(_['task_data_id'])
            task_data = TaskData.objects.filter(id__in=task_data_id_list)
            flag = True
        else:
            task_data = TaskData.objects.all()
        #  没有数据
        if  not task_data:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errMsg = 'No data found',successResult=''))
        pages = request.GET.get('pagtor')
        if not pages:
            pg = '10'
        else:
            pg = pages
        paginator = Paginator(task_data, pg)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        pages_num = paginator.count
        in_tion_list = []
        if flag and len(tag_list) > 0:
            for i in contacts:
                date_time = i.time
                url = i.url
                article_title = i.article_title
                for tag in tag_list:
                    article_title = article_title.replace(tag,'<span style = "color:red">'+tag+'</span>')
                article_author = i.article_author
                views_count = i.views_count
                in_tion_data ={
                    'time':date_time,'url':url,'article_title':article_title,
                    'article_author':article_author,
                    'views_count':views_count
                }
                in_tion_list.append(in_tion_data)  
        else:
            for i in contacts:
                date_time = i.time
                url = i.url
                article_title = i.article_title
                article_author = i.article_author
                views_count = i.views_count
                in_tion_data ={
                    'time':date_time,'url':url,'article_title':article_title,
                    'article_author':article_author,
                    'views_count':views_count
                }
                in_tion_list.append(in_tion_data)  

        return get_json_response(request, dict(suc_id=0, ret_cd=200, ret_ts=long(time.time()),errMsg = '',successResult=in_tion_list,pages_num=pages_num))
    
    except Exception as e:
        print e
        return get_json_response(request, dict(suc_id=0, ret_cd=500, ret_ts=long(time.time()),errMsg = 'Server internal error,Please contact the administrator.',successResult=''))


'''
切词
'''
def keyword_cut(keyword_str):
    topK = 10
    PROJECT_ROOT = os.path.dirname(__file__)
    jieba.analyse.set_stop_words(PROJECT_ROOT+'/stop_words.txt')
    tags = jieba.analyse.extract_tags(keyword_str, topK=topK)
    result_tags = []
    for tag in tags:
        if tag not in result_tags:
            result_tags.append(tag)
    return result_tags

    

'''
    # json时间转换
'''
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj) 

'''
    # 通用函数返回json数据
'''
def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp,cls=DateEncoder), content_type='application/json')
