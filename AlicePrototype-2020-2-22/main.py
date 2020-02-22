# -*- coding:utf-8 -*-

# import Levenshtein

import weather
import news


def __analyse(raw_str):
    analyse_result = []
    weather_wors = ['天气', 'weather']
    news_words = ['新闻', 'news', "头条"]
    if any(word in raw_str for word in weather_wors):
        analyse_result.append('weather')
    if any(word in raw_str for word in news_words):
        analyse_result.append('news')
    return analyse_result

if __name__ == '__main__':
    while (True):
        raw_str = input()
        analyse_result = __analyse(raw_str)
        if 'weather' in analyse_result:
            weather.handle(raw_str)
        if 'news' in analyse_result:
            news.handle(raw_str)
        else:
            print('Alice没能听懂主人说的是什么哇……')

# Levenshtein.ratio(str, test_str) #可以尝试使用字符串匹配度来替代关键词检索
