---
id: UDG@20.15.2@MMLCommand@DSP UFPLATENCY
type: MMLCommand
name: DSP UFPLATENCY（显示UFP时延度量统计结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UFPLATENCY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 时延统计
status: active
---

# DSP UFPLATENCY（显示UFP时延度量统计结果）

## 功能

该命令用于显示UFP逐包转发时延统计信息，包括最大值、最小值、平均值、包数以及分段统计结果。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLID | Cell ID | 可选必选说明：可选参数<br>参数含义：该参数表示PAE调试消息发送的CELLID，可以通过使用命令<br>[**DSP PAENODE**](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UFPLATENCY]] · UFP时延度量统计结果（UFPLATENCY）

## 使用实例

显示UFP逐包转发时延度量统计信息：

```
+++    UEG/*MEID:0 MENAME:UEG_1822*/        2024-03-20 10:55:47
O&M    #434
%%DSP UFPLATENCY: CELLID="isu-pod-0__103__0";%%
RETCODE = 0  操作成功

结果如下
--------
 Cell ID  =  isu-pod-0__103__0
统计信息  =  Max: 4013258us, Min: 22us, Avg: 1491240us, TotalPktNum: 5071439
Stat:
Latency		PktNum
0
~
100us 	98956
100
~
200us 	451734
200
~
300us 	149005
300
~
400us 	36907
400
~
500us 	23191
500
~
600us 	17044
600
~
700us 	14212
700
~
800us 	13365
800
~
900us 	13405
900
~
1000us 	13839
1
~
100ms 	803583
100
~
1000ms	800692
1
~
10s 		2635506
>10s		0

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UFPLATENCY.md`
