#coding:utf-8
from matplotlib import pyplot as plt
import biligroupana as data
import pltconfig

plt.figure(figsize=(6, 9))
labels = [u'没有封禁记录', u'只有VAC', u'只有Gameban', u'VAC和Gameban']
session1 = data.private_clean/data.private
session2 = data.private_onlyvac/data.private
session3 = data.private_onlygameban/data.private
session4 = data.private_vacandgameban/data.private
fracs = [session1, session2, session3, session4]
explode = [0, 0, 0., 0.]
a, l_text, p_text = plt.pie(x=fracs, labels=labels, shadow=True, autopct='%3.2f %%', explode=explode,
        labeldistance=1.1, startangle=90, pctdistance=0.6)
p_text[1].set_position([0, 0.8])
p_text[2].set_position([0.07, 0.7])
p_text[3].set_position([0.17, 0.6])
l_text[1].set_position([-0.1, 1.12])
l_text[2].set_position([0.01, 1.06])
l_text[3].set_position([0.17, 1])
plt.title('组内个人资料私密的封禁情况', bbox={'facecolor': '0.8', 'pad': 5})
plt.axis('equal')
plt.legend(loc=(0.85, 0.85))
plt.show()

