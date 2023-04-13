# ChatOpenReview
众筹开源项目：利用OpenReview的优质审稿数据，微调出一个专业的审稿和审稿回复GPT

## 进展
4.14 今天已经尝试爬取NIPS22的审稿数据

## 爬取数据教程：
1. 查阅官网文档：https://docs.openreview.net/getting-started/using-the-api/installing-and-instantiating-the-python-client
2. 安装python库：
进入一个新的虚拟环境，比如chatreview, python3.8
```python
git clone git@github.com:openreview/openreview-py.git
cd openreview-py
pip3 install -e .
```
3. 在openreview官网注册账号，报错用户邮箱和密码，填入get_reviewers.py的对应位置
4. 设置网络，如果在国内，需要魔法，且需要将网络设置为tun模式：参考这个链接：[tun设置](https://github.com/kaixindelele/chatpaper#%E4%B8%80%E4%BB%A5%E8%84%9A%E6%9C%AC%E6%96%B9%E5%BC%8F%E8%BF%90%E8%A1%8C)
5. 注意，数据保存格式需要仔细查看，当前的txt格式可能后期不好提取；官方文档推荐的是csv：[export to csv](https://docs.openreview.net/getting-started/using-the-api/notes/exporting-all-reviews-into-a-csv)
6. 目前的格式前几个审稿content是审稿的，后面几个是作者的回复，大家后期可以做数据清洗时注意下。

## 数据来源
openreview官方提供数据批量下载：https://docs.openreview.net/getting-started/using-the-api/notes/exporting-all-reviews-into-a-csv
以及之前ACL的这篇杰出工作：[A Meta-Review Dataset for Controllable Text Generation](https://github.com/Shen-Chenhui/MReD)

## 准备工作：
0. 阅读meta-review的论文，梳理这篇工作解决的问题，借鉴他们的思路--需要一位同学看完，给大家做汇报；
1. 下载和分析meta-review的数据，分析格式和效果；--需要一位会python的同学做梳理。 
2. OpenReview的其他会议的数据爬取和清洗；--需要一位会python或者jave的同学爬取，还需要一定的存储能力。我之前试过爬取简单的爬取，但是没有拿到审稿信息；
3. 挑选一个文本输出长度不低于4K token的开源LLM模型--需要一位熟悉LLM的同学，最好是微调过LLM的同学。
4. 设计一个方案，实现PDF论文的长文本+审稿prompt的压缩，或者滑动输入。--需要一个懂NLP和LLM的同学
5. 制备指令微调数据集--同上

希望大家领取任务后，自己评估一下任务周期，咱们尽量一两天同步一次进度。


## 团队招募：
1. 做过LLMs微调工作的大佬 or 其他代码能力强的同学
2. 有计算资源的带佬，哈哈
3. 对这个项目感兴趣，且愿意投入时间和精力的同学

## 联系方式：
主页有我的QQ邮箱，欢迎对项目感兴趣的大佬们加QQ好友，或者邮件联系！

最近加的人比较多，敬请附上学校/公司，技术栈，以及动机，麻烦大家了!

明天准备和meta-review的作者团队联系
