#coding=utf-8
#author:微信公众号：稻香开发测试
#查看代码讲解，视频教程，请微信添加好友搜索公众号[稻香开发测试]查看历史消息获取。
import json
import re
from pyecharts import Bar
from pyecharts import Grid
from pyecharts import WordCloud
from pyecharts import Pie
from pyecharts import Map
from collections import Counter
import jieba.analyse
import PIL.Image as Image
import os
import math
#import codecs
from PIL import ImageFile


def word_cloud(item_name, item_name_list, item_num_list, word_size_range):
    wordcloud = WordCloud(width=1400, height=900)

    wordcloud.add("", item_name_list, item_num_list, word_size_range=word_size_range, shape='pentagon')
    out_file_name = './analyse/' + item_name + '.html'
    wordcloud.render(out_file_name)


def get_tag(text,cnt):
    text = re.sub(r"[汝阳县|偃师]", "", text)
	#text是单个标题
    #print ('正在分析句子:',text)
    tag_list = jieba.analyse.extract_tags(text)
    #print(tag_list)
    for tag in tag_list:
        cnt[tag] += 1
def counter2list(_counter):
    name_list = []
    num_list = []

    for item in _counter:
        name_list.append(item[0])
        num_list.append(item[1])

    return name_list,num_list


def get_bar(item_name, item_name_list, item_num_list):
    subtitle = "洛阳市九县六区百姓呼声栏目帖子统计"
    bar = Bar(item_name, page_title=item_name, title_text_size=30, title_pos='center', \
              subtitle=subtitle, subtitle_text_size=25)

    bar.add("", item_name_list, item_num_list, title_pos='center', xaxis_interval=0, xaxis_rotate=27, \
            xaxis_label_textsize=20, yaxis_label_textsize=20, yaxis_name_pos='end', yaxis_pos="%50")
    bar.show_config()

    grid = Grid(width=1300, height=800)
    grid.add(bar, grid_top="13%", grid_bottom="23%", grid_left="15%", grid_right="15%")
    out_file_name = './analyse/' + item_name + '.html'
    grid.render(out_file_name)
if __name__ == '__main__':

    #in_file_name = './' + dxpath + 'data/friends.json'
    def xianqu(xian):
        with open("./lyddata/"+xian+".txt", 'r',encoding='utf-8') as f:
            a=f.readlines()

        # 待统计参数
        #print(a)
        words = Counter()  # 性别
        # Counter是一个简单的计数器，例如，统计字符出现的个数：

        for aone in a:
            get_tag(aone,words)
        #论坛标题关键词

        name_list, num_list = counter2list(words.most_common(300))
        print(len(name_list))
        word_cloud(xian+'百姓呼声关键词', name_list, num_list, [20, 100])
        """"""
    xian=["15_jianxiqu",
           "16_xigongqu",
           "17_laochengqu",
           "18_chanhehuizuqu",
           "19_luolongqu",
           "20_jiliqu",
           "21_yanshishi",
           "22_xinanxian",
           "23_yichuanxian",
           "24_mengjinxian",
           "25_luoningxian",
           #"26_ruyangxian",
           "27_luanchuanxian",
           "28_yiyangxian",
           "29_songxian",
           "59_longmenyuanquguanweihui",
           "108_gaoxinqu",
           "115_yibinqu"]
    '''这里是提取分析关键词的
    for onexian in xian:
        xiancon=onexian[0:12]+"title"
        print(xiancon)
        xianqu(xiancon)
    '''
    name_list=["涧西区","西工区","老城区","瀍河区","洛龙区","高新区","伊滨区","龙门","吉利区","偃师市","新安县","伊川县","汝阳县","孟津县","洛宁县","栾川县","宜阳县","嵩县"]
    num_list=[10848,6988,6428,5579,10777,5372,3723,980,875,2869,5584,5529,2254,10158,2912,830,5996,1430]
    get_bar('帖子数量统计', name_list, num_list)
