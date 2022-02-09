# sduwhnews

[![GitHub issues](https://img.shields.io/github/issues/kxxt/sduwhnews)](https://github.com/kxxt/sduwhnews/issues)
[![GitHub forks](https://img.shields.io/github/forks/kxxt/sduwhnews)](https://github.com/kxxt/sduwhnews/network)
[![GitHub stars](https://img.shields.io/github/stars/kxxt/sduwhnews)](https://github.com/kxxt/sduwhnews/stargazers)
[![GitHub license](https://img.shields.io/github/license/kxxt/sduwhnews)](https://github.com/kxxt/sduwhnews/blob/master/LICENSE)
![Python](https://img.shields.io/badge/python-3.10-blue)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fkxxt%2Fsduwhnews)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fkxxt%2Fsduwhnews)

山东大学（威海） 新闻聚合

## 目前支持的网站

- [数学与统计学院](https://math.wh.sdu.edu.cn/index.htm) 仅爬取重要通知
- [教务处](https://jwc.wh.sdu.edu.cn/) 仅爬取工作通知
- [新闻网](https://xinwen.wh.sdu.edu.cn/) 仅爬取校园要闻

## 目前支持的推送方式

### Telegram

设置环境变量 `TG_CHAT_ID` 和 `TG_TOKEN`

然后运行 `src/tgbot.py`

（注意脚本会在工作目录下生成 `crawled.set` 来保存已经推送过的新闻的网址，请确保程序在工作目录有读写权限）

推荐设置定时任务运行此脚本

## 开发

安装依赖

```bash
poetry install
```

欢迎提交 PR!
