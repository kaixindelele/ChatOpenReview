# ChatOpenReview
众筹开源项目：利用OpenReview的优质审稿数据，微调出一个专业的审稿和审稿回复GPT

## 进展

4.26 First domain: Reinforcement Learning Domain Fineturned model have a good result
     we decided to fineturn in difference domain, AI area first, expected will be:
          1. Reinforcment Learning
          2. Computer Vision
          3. NLP
          4. Robotics
          5. AI4S
     Any other suggestions please feel free to command in issue
     
     Sample Result:
'''
Input:  Optimization-Based Algebraic Multigrid Coarsening Using Reinforcement Learning
Output: 
Title: Optimization-Based Algebraic Multigrid Coarsening Using Reinforcement Learning
Authors: Ali Taghibakhshi, Scott MacLachlan, Luke Olson, Matthew West

This paper addresses the problem of grid coarsening for algebraic multigrid (AMG) methods by proposing a reinforcement learning (RL) method using graph neural networks (GNNs). The authors present a novel approach based on dueling double-DQN agents with topology adaptive convolution layers (TAGCN) that outperforms existing heuristic methods while preserving theoretical guarantees for convergence. Additionally, the proposed method demonstrates scalability with a linear graph-decomposition-based evaluation algorithm.

Strengths:

- The paper provides a clear background and motivation for the research, addressing shortcomings in existing methods and presenting a well-defined problem.
- The proposed RL method using GNNs shows promising results, outperforming existing heuristic methods and preserving theoretical convergence guarantees.
- The paper demonstrates the scalability of the proposed method, which is an essential aspect for the practical application of grid coarsening in AMG methods.

Weaknesses:

- The RL agent is specialized for solving Poisson's equation on 2D grids, limiting its applicability to other problems and requiring further research to generalize the approach.
- The paper does not provide a thorough comparison with other machine learning-based approaches or address their limitations.
-  While the paper demonstrates the scalability of the proposed method, it does not provide a detailed analysis of the computational cost associated with training the RL agent and the GNN. Understanding the trade-off between the time taken for training and the improvements achieved in grid coarsening would provide a more comprehensive assessment of the method's practicality.
- The paper does not discuss the robustness of the proposed method to noisy or imperfect input data. In real-world applications, it is crucial to understand how sensitive the RL-based GNN approach is to such variations and whether any pre-processing or additional steps are necessary to ensure its reliability.
- The paper tests the proposed method on the 2D Poisson problem with various unstructured grids. However, it would be beneficial to evaluate the method's performance on a wider range of benchmark problems to further validate its applicability and effectiveness.
- The paper does not provide details on the hyperparameter tuning process or model selection for the RL agent and GNN. Understanding how these choices were made and how sensitive the results are to different hyperparameter settings would help establish the robustness and generalizability of the proposed method.

Overall, the paper presents a well-motivated and innovative approach to grid coarsening for AMG methods, successfully addressing the problem and showing promising results. However, the paper could benefit from a broader discussion of related machine learning-based approaches and further investigation into generalizing the proposed method.
'''

4.25 敬请期待第一个微调小模型的发布

4.18 今天已经爬取了NIPS22的审稿数据，匹配好了审稿和审稿回复信息。下载链接如下：[NeurIPS_2022_reviews.json](https://www.aliyundrive.com/s/hqKrKxeUw5S) 提取码: xp21
如果大家有发现匹配不上的文章，欢迎及时报告！

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
3. 不注册也行：~~在openreview官网注册账号，报错用户邮箱和密码，填入get_reviewers.py的对应位置~~
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


## 项目引用：
Please cite the repo if you use the data or code in this repo.

```
@misc{ChatOpenReview,
  author={Yongle Luo, zhuhaojia, Shaocong Ma},
  title = {ChatOpenReview: A Language model for Paper Review and Response},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kaixindelele/ChatOpenReview}},
}
```
