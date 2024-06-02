# 邦邦控分机1.0 - BanGDream Pt Contorl Hepler 1.0

发现控分要去研究公式，虽然很简单，于是折腾了一下代码。

整个程序用python完成，ui使用pyside6，使用了[**QFluentWidgets**](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)风格组件库

公式来自[**这里**](https://www.bilibili.com/read/cv20061259/)

[**B站专栏**](https://www.bilibili.com/read/cv33421271)

**For English version, please see below.**

## 安装

直接下载zip包，启动exe

可能会被windows defender拦截，使用时关闭

## 源码使用

建议使用conda虚拟环境，python=3.11，需要安装pyside6以及QFluentWidgets对应版本；

运行mainUI.py

## 一把计算

* 任务live：加成倍率，其他人分数，支援乐队综合力
* CP活：加成倍率，其他人分数，是否清CP
* EX：加成倍率，其他人分数
* 5V5：输赢，精简mode
* 组曲：
* 对邦：精简模式

## 自动规划

必须输入的：目标，当前，平均分

* 任务live：加成倍率，支援乐队综合力（最后一把部分的加成为自动计算）
* CP活：加成倍率，是否清CP（最后一把部分加成为自动计算）
* EX：加成倍率（最后一把部分加成为自动计算）
* 5V5：输赢，排名（1到5都行，但是建议1或5），最后一把不能指定
* 组曲：曲数（只限定平均部分
* 对邦：对邦or自由，只指定平均部分，只是优先用哪种方式，不会只用那种方式（比如如果对邦算不出来，还是会去用自由算）。

## 简单的算法

* 用户输入期望的分数范围和最大分数 （下拉框选择）
* 然后计算出该分数的pt获取数 = ptPer
* 将所需pt数除ptPer，得到大致的游戏次数
* 如果不能整除：
  * 由于剩余的pt数 - ptLeft只要打过pt获取数的最低值就可以实现（同时不大于0加成队伍的最高分）
  * 即当剩余值大于最低值时，就可以完成
  * 若该值小于最低值，则整除pt数少打一把，剩余的数量为ptLeft + ptper；这时将这部分重新划分为最低值+差值，不断提高最低值（+1）同时差值下降，直到找到差值可以一把完成的分数，同时较小值的部分也不会太高
  * 若在第一种情况中，剩余值虽然大于最低值，但是对于0加成队伍来说过高，那么也按照上面的办法做

## In English

This is an English version, if you are English speaker and don't know what this program is, but you notice the name of this repo contains BanGDream, ok just let me briefly introduce it.

This repo make a program which can help bangdream player to control the event pt to some exact number you want, like 114514 or some, if you are curious about it, you can refer to this webpage(Chinese) [About what is pt control in bangdream](https://www.bilibili.com/read/cv20061259/). You can just provide the current pt and your target to this program, and select the event type, different event types will need different data to calculate the results.

The result will give how much fire you should use, and the score interval you should achieve.

To see the ui of the program, check [this article](https://www.bilibili.com/read/cv33421271)

If you really need an English version for this program, please send an issue in this repo, I will consider if there is someone ask me to do it :)
  
