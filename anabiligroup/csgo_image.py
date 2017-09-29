#coding:utf-8
from matplotlib import pyplot as plt
import biligroupana as data
import pltconfig

plt.figure(figsize=(6, 9))
labels = [u'拥有CSGO', u'没有CSGO', u'资料私密']
session1 = data.havecsgo/data.totaldata
session2 = data.nocsgo/data.totaldata
session3 = data.private/data.totaldata
fracs = [session1, session2, session3]
explode = [0, 0, 0]
plt.pie(x=fracs, labels=labels, shadow=True, autopct='%3.2f %%', explode=explode,
        labeldistance=1.1, startangle=90, pctdistance=0.8)
plt.title('组内拥有CSGO情况', bbox={'facecolor': '0.8', 'pad': 5})
plt.axis('equal')
plt.legend(loc=(0.85, 0.85))
plt.show()

