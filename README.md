# getBilibiliGroupMember
抓取bilibili的Steam用户组的所有组员的游戏封禁情况

__(程序存在一定的BUG，在结果图后列出)__

****

## 下载之前请确保满足以下条件

* **支持版本:Python3.6**
* **需要安装的库 scrapy requests numpy pandas matplotlib**
* **你已经申请了一个可用的Steam Web Api Key**
 
### 如何申请一个Steam Web Api Key
你必须有一个自己的域名，然后[点击这里](http://steamcommunity.com/dev),进去登录自己的Steam账号输入按照提示输入你的域名获取你的Key

****
## 下载完毕运行之前

将你申请得到的Key填入到代码中去，有 __两处__ 地方需要填写，分别是

### 1. bilibiligroup\bilibiligroup\spiders\bili.py line 98
```python
get64url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={Your Steam API key}&vanityurl={}'# {Your Steam API key}中间填入你的key，两个花括号要删掉
```

### 2. bilibiligroup\bilibiligroup\spiders\bili.py line 150
```python
nexturl = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={Your Steam API key}&steamid={}&format=json'# {Your Steam API key}中间填入你的key，两个花括号要删掉
```

****

## 运行代码

我是在Windows的环境运行的代码，先用CMD CD到你存放代码的根目录下输入

    scrapy crawl bili -o csvname.csv
__csvname.csv你可以随意输入你想要的文件名__，它是爬取下来的信息的保存文件
接下来就是等待程序爬去完毕。因为信息太多，爬取时间很长（__反正我是爬了差不多3天才爬完的。。。__）

****

## 数据表格的格式说明


| user_url  | PrivateProfile  | CSGO  | VACBan  | GameBan |
| --------- | --------- | --------- | --------- | --------- |
|           |           |           |           |           |
|           |           |           |           |           |

### 列名解释
    user_url: 64位链接
    PrivateProfile: 个人主页私密与否 1: 个人资料私密  0: 个人资料公开
    CSGO: 是否拥有CSGO这款游戏 1: 拥有  0: 没有  NaN(空): 因为个人资料私密，无法知道是否拥有
    VACBan: 是否被VACBan 1: 有  0: 没有
    GameBan: 是否被GameBan 1: 有  0: 没有

****

## 数据抓取完毕

数据将会被保存.csv后缀的excel表格中去，通过 __anabiligroup/biligroupana.py__ 去统计需要求得的数据，
然后通过 __biligroupmatlop.py|__ __csgo_image.py|__ __private_iamge.py|__ __VacandGameban.py__ 使得数据可视化（饼状图）

__进行数据分析之前，将anabiligroup/biligroupana.py line 3 的路径改为存放数据的路径__

```python
data = pd.read_csv('E://spider-progress//bilibiligroup//biliuser.csv')
```

### 结果图

#### ①
 
 ![](https://github.com/coldezera/getBilibiliGroupMember/blob/master/resultimage/Profiles.jpg)
     
#### ②

![](https://github.com/coldezera/getBilibiliGroupMember/blob/master/resultimage/CSGO.jpg)

#### ③

![](https://github.com/coldezera/getBilibiliGroupMember/blob/master/resultimage/Private.jpg)

#### ④

![](https://github.com/coldezera/getBilibiliGroupMember/blob/master/resultimage/Ban.jpg)

****
## 目前存在的BUG：

requests.get在一定时间内调用的Api过于频繁，导致了10054和10060的错误，远程主机强迫关闭了链接或者长时间未应答使得页面读取失败。丢失数据。目前正在编写代理IP池，估计建立的稳定的代理IP之后，变着代理IP去爬取，应该就不会触发10054或10060的错误了

（第一次写README，肯定有不足之处，还请指出 QQ：616775154）




