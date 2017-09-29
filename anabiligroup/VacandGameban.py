#coding:utf-8
from matplotlib import pyplot as plt
import biligroupana as data
import numpy as np
import pltconfig

pos = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
plt.figure(figsize=(6, 9))
labels = [u'①有封禁记录', u'②有封禁记录', u'①没有封禁记录',
          u'②没有封禁记录', u'资料私密有封禁记录', u'资料私密无封禁记录' ]
session1 = data.csgo_ban/data.totaldata
session2 = data.nocsgo_ban/data.totaldata
session3 = data.csgo_notban/data.totaldata
session4 = data.nocsgo_notban/data.totaldata
session5 = data.private_ban/data.totaldata
session6 = data.private_notban/data.totaldata
fracs = [session1, session2, session3, session4, session5, session6]
explode = [0, 0, 0, 0, 0, 0]
a, l_text, p_text = plt.pie(x=fracs, labels=labels, shadow=True, autopct='%3.2f %%', explode=explode,
        labeldistance=1.1, startangle=90, pctdistance=0.6)

l_text[0].set_position([0.2, 1.15])
p_text[0].set_position([0, 0.75])
plt.title('组内所有人封禁情况(①:有CSGO,②:没CSGO)', bbox={'facecolor': '0.8', 'pad': 5})
plt.axis('equal')
plt.legend(loc=(0.85, 0.85))
plt.show()

