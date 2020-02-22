# -*- coding:utf-8 -*-

from urllib.parse import quote
import configparser
import requests
import json
import os


class Tag:
    name = ''
    props = {}

    def __init__(self, name, props):
        self.name = name
        self.props = props


__config = configparser.ConfigParser()
__config.read(os.getcwd() + "/config.ini", encoding='utf-8')

__news_api_url = __config.get("news", "api")
__news_api_key = __config.get("news", "key")
__news_default_type = __config.get("news", "default_type")


def __analyse(raw_str):
    analyse_result = []
    news_query_words = ['?', '有什么', '如何', '呢？', '告诉我', '来点']
    if any(word in raw_str for word in news_query_words):
        news_type_words_map = {"社会": "shehui", "国内": "guonei", "国际": "guoji", "娱乐": "yule", "体育": "tiyu",
                               "军事": "junshi", "科技": "keji", "财经": "caijing", "时尚": "shishang"}
        query_props = {'type': news_type_words_map[__news_default_type]}
        for key, value in news_type_words_map.items():
            if key in raw_str:
                query_props['type'] = value
                break
        analyse_result.append(Tag('news-query', query_props))
    else:
        analyse_result.append(Tag('news-talk', None))
    return analyse_result


def handle(raw_str):
    analyse_result = __analyse(raw_str)
    for tag in analyse_result:
        if tag.name == 'news-talk':
            print("Alice也觉得最近世界上发生了好多事情呢……")
        if tag.name == 'news-query':
            news_complete_api = __news_api_url + "?type=" + tag.props['type'] + "&key=" + __news_api_key
            news_response = json.loads(requests.get(news_complete_api).content)
            error_code = news_response['error_code']
            if error_code == 0:
                print("嘀哩哩~数据接收完成，下面为主人播报新闻——")
                for index, news in enumerate(news_response['result']['data']):
                    print("\n" + str(index + 1) + ".标题：" + news['title'] + "\n发布时间：" + news['date'] + "\n链接：" + news['url'])
            else:
                print("发生了Alice也不清楚的错误呢(๑Ő௰Ő๑)……要不主人帮忙看一下\n错误代码：[News-API:" + error_code + "]")
