# TrainSearch

主要参考的是实验楼里的一个教程，但是那个教程太过久远，正如教程的作者所言，12306的网站接口会不断的发生变化，如果不及时更新，数据当然就爬取不到。

果然！12306变聪明了，query返回的数据格式，已经不再是教程里说的那种高度格式化的类似JSON的数据，以我浅薄的经验来看：

> 它被加密了！

不仅如此，12306的网站架构并不是REST风格的，多数的数据刷新是通过AJAX实现的，所以，我放弃了。

怎么办？正当我感到绝望的时候，柳暗花明，灵机一闪，想：能不能曲线救国呢？

[携程火车票](http://trains.ctrip.com/TrainBooking/SearchTrain.aspx?&mkt_header=bdkx&allianceID=106225&sid=550027&ouid=956893351-alading_tit-###)

这个神奇的网站拯救了我！不必考虑携程是怎么拿到的火车数据，这不重要，重要的是，你也利用它，拿到你想要的数据，这就够了。

只是数据源变了，整个思路还是和那篇教程一致的，只不过访问网站我用了`Selenium`这个Python的库，因为我发现携程网站的刷新有延迟，应该也是用到了AJAX技术，因此`Selenium+PhantomJS`组合就是最强大的工具。

不得不说，那篇教程写的相当不错，跟着做了一遍，收获很大，思路大体相同，但是实现细节上会有所出入，具体用到的库有：`docopt`, `colorama`, `BeautifulSoup`和`pypinyin`。详细过程看源码。

- master分支是控制命令行程序
- usr分支是用户操作程序

打包工具使用`pyinstaller`，对文件进行了裁剪，并添加readme.txt帮助文档。裁剪的不是很到位，由于要模拟Python整个全部的运行环境，因此依赖项很多，压缩文件甚至达到了98M，有兴趣可以当个工具玩！

[可执行文件在这里](https://github.com/plantree/TrainSearch/releases/tag/v1.0-beta)

简单截图：
![screenshot.png](https://github.com/plantree/TrainSearch/blob/master/screenshot.png?raw=true)

##### References:

1. [Python 实现火车票查询工具](https://www.shiyanlou.com/courses/623/labs/2072/document)
2. 《Python网络数据采集》，【美】米切尔，人民邮电出版社。

