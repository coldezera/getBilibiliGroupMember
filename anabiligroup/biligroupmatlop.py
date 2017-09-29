#coding:utf-8
from matplotlib import pyplot as plt
import biligroupana as data
import pltconfig

#-------------------------------------资料私密和不私密 饼状图--------------------------------------
# plt.figure(figsize=(6, 9))
#定义饼状图的标签，标签是列表
labels = [u'个人资料私密', u'个人资料公开']
#每个标签占多大，会自动去算百分比
fracs = [data.private/data.totaldata, 1-(data.private/data.totaldata)]
explode = [0, 0] # 0.1 表示凸出index部分
plt.pie(x=fracs, labels=labels, shadow=True, autopct='%3.1f %%', explode=explode,
        labeldistance=1.05, startangle=90, pctdistance=0.8)
plt.title('组内资料公开情况', bbox={'facecolor': '0.8', 'pad': 5})
plt.axis('equal')
plt.legend(loc=(0.75, 1))
plt.show()
'''
labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
shadow，饼是否有阴影
startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
pctdistance，百分比的text离圆心的距离
patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
'''
#-----------------------------------资料私密有封禁记录和没有的------------------------------------------------
