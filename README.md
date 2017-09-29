# getBilibiliGroupMember
抓取bilibili的Steam用户组的所有组员的游戏封禁情况

****

## 下载之前请确保满足以下条件

* **支持版本:Python3.6**
* **需要安装的库 scrapy requests numpy pandas matplotlib**
* **你已经申请了一个可用的Steam Web Api Key**

### 如何申请一个Steam Web Api Key
你必须有一个自己的域名，然后[点击这里](http://steamcommunity.com/dev),进去登录自己的Steam账号输入按照提示输入你的域名获取你的Key

****
## 下载完毕运行之前
将你申请得到的Key填入到代码中去，有__两处__地方需要填写，分别是

### 1. bilibiligroup\spiders\bili.py line 98
```python
get64url = 'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={Your Steam API key}&vanityurl={}'# {Your Steam API key}中间填入你的key，两个花括号要删掉
```

### 2. bilibiligroup\spiders\bili.py line 150
```python
nexturl = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={Your Steam API key}&steamid={}&format=json'# {Your Steam API key}中间填入你的key，两个花括号要删掉
```

****

## 运行代码

我是在Windows的环境运行的代码，先用CMD CD到你存放代码的根目录下输入

    scrapy crawl bili -o csvname.csv
__csvname.csv你可以随意输入你想要的文件名__，它是爬取下来的信息的保存文件
接下来就是等待程序爬去完毕。因为信息太多，爬取时间很长（__反正我是爬了差不多3天才爬完的。。。__）
