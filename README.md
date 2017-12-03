# 12306 爬虫
## 12306查询余票的爬虫
### 安装
- 下载代码
- 执行 python3 setup.py install
- 执行 tickets -h 或tickets --help 查看帮助
命令行火车票查看器

···

Usage:
    tickes [-gdtkz] <from> <to> <date>


Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
    
···
    
## 效果

![效果](/image/01.png)
