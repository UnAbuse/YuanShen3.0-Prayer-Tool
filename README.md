# 原神3.0版本祈愿工具
本工具需要有一定的电脑基础的人来操作,内含教程  
## 前置准备，相关库安装
首先工具用到了python内置的轻量级数据库sqlite3，外置库为requests,rich.  
安装requests库:  
>pip install requests  
>pip install rich
## 操作教学
原神在3.0版本取消了祈愿日志输出的功能,作为一个经常写爬虫的人怎么可能自己去一个个数.  
于是,我决定用抓包的方式来分析解决这个问题,对于提交数据的分析,只需要抓取到一个参数便可使用本工具进行查询.  
这里我使用的工具是*fiddler*这个抓包工具,抓包开始可以发现一个向*hk4e-api.mihoyo.com*发送的请求.  
![图片1](https://github.com/UnAbuse/YuanShen3.0-Prayer-Tool/blob/main/%5D42O6D6PKKES9IA3_$~%25%7DES.png)  
在提交的数据中找到*authkey*,这个就是我们需要的参数了.
![图片2](https://github.com/UnAbuse/YuanShen3.0-Prayer-Tool/blob/efa4cef5c203ce7a3dbe00aac4a913b0f7e4cb9b/1.png)  
这时候来到我们代码文件的目录下(目前只有命令行版本，其他后面应该会写),右键打开*Windows Shell*,便能开始使用工具了.  
![图片3](https://github.com/UnAbuse/YuanShen3.0-Prayer-Tool/blob/a0cfdfab564374e9c926950b3c1d70352d5510bf/2.png)  
