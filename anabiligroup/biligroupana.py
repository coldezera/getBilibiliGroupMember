import pandas as pd

data = pd.read_csv('E://spider-progress//bilibiligroup//biliuser.csv')
df = pd.DataFrame(data)
totaldata = len(df) # 总数据条数

private = len(df[(df.PrivateProfile > 0)]) # 资料私密数
private_clean = len(df[(df.PrivateProfile > 0) & (df.VACBan < 1) & (df.GameBan < 1)])# 资料私密封禁记录空的
private_onlyvac = len(df[(df.PrivateProfile > 0) & (df.VACBan > 0) & (df.GameBan < 1)])
private_onlygameban = len(df[(df.PrivateProfile > 0) & (df.VACBan < 1) & (df.GameBan > 0)])
private_vacandgameban = len(df[(df.PrivateProfile > 0) & (df.VACBan > 0) & (df.GameBan > 0)])

vacban = len(df[df.VACBan > 0])# vacban的数目
gameban = len(df[df.GameBan > 0])
ban = len(df[(df.VACBan > 0) | (df.GameBan > 0)])# 有封禁记录数目（vac or gameban）
vacandgameban = len(df[(df.VACBan > 0) & (df.GameBan > 0)])# vac and gameban
notban = len(df[(df.VACBan < 1) & (df.GameBan < 1)])

havecsgo = len(df[df.CSGO > 0])
nocsgo = len(df[(df.CSGO < 1)])

csgo_ban = len(df[(df.CSGO > 0) & ((df.VACBan > 0) | (df.GameBan > 0))])
csgo_notban = len(df[(df.CSGO > 0) & ((df.VACBan < 1) & (df.GameBan < 1))])

nocsgo_ban = len(df[(df.CSGO < 1) & ((df.VACBan > 0) | (df.GameBan > 0))])
nocsgo_notban = len(df[(df.CSGO < 1) & ((df.VACBan < 1) & (df.GameBan < 1))])

private_ban = len(df[(df.PrivateProfile > 0) & ((df.VACBan > 0) | (df.GameBan > 0))])
private_notban = len(df[(df.PrivateProfile > 0) & ((df.VACBan < 1) & (df.GameBan < 1))])

print(totaldata)
# print(df[(df.PrivateProfile > 0)])# 资料私密
# print(df[(df.VACBan > 0) | (df.GameBan > 0)]) #有游戏封禁记录





