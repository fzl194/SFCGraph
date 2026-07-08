---
id: UDG@20.15.2@MMLCommand@DSP PAEQUEUE
type: MMLCommand
name: DSP PAEQUEUE（显示PAE队列统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAEQUEUE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 端口
status: active
---

# DSP PAEQUEUE（显示PAE队列统计信息）

## 功能

该命令用于显示PAE队列统计信息。

通过该命令可查看指定资源上队列的状态和统计信息，可了解通信是否正常，并进行故障诊断。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| QUEUEID | 队列ID | 可选必选说明：可选参数<br>参数含义：队列ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～20。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAEQUEUE]] · PAE队列统计信息（PAEQUEUE）

## 使用实例

显示PAE队列统计信息：

```
DSP PAEQUEUE:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
队列ID        队列名称                接收报文数目    发送报文数目    接收报文速率（pps）    发送报文速率（pps）    重发次数    丢包统计

0x80000000    loop_vchannel_send_0    0               0               0                      0                      0           0
0x80000001    loop_vchannel_recv_0    8               0               0                      0                      0           0
0x80000002    loop_vchannel_send_1    0               0               0                      0                      0           0
0x80000003    loop_vchannel_recv_1    8               0               0                      0                      0           0
0x80000004    loop_vchannel_send_2    0               0               0                      0                      0           0
0x80000005    loop_vchannel_recv_2    0               0               0                      0                      0           0
0x80000006    loop_vchannel_send_3    0               0               0                      0                      0           0
0x80000007    loop_vchannel_recv_3    0               0               0                      0                      0           0
0x80000008    dp_to_dp_pkt            0               0               0                      0                      0           0
0x80000009    fei_to_dp_pkt           12              0               0                      0                      0           0
0x8000000A    fei_to_dp_msg           0               0               0                      0                      0           0
0x8000000B    extport_0_send_0        0               0               0                      0                      0           0
0x8000000C    extport_0_recv_0        0               0               0                      0                      0           0
0x8000000D    extport_0_send_1        0               0               0                      0                      0           0
0x8000000E    extport_0_recv_1        0               0               0                      0                      0           0
0x8000000F    extport_0_send_2        0               0               0                      0                      0           0
0x80000010    extport_0_recv_2        0               0               0                      0                      0           0
0x80000011    extport_0_send_3        0               0               0                      0                      0           0
0x80000012    extport_0_recv_3        0               0               0                      0                      0           0
0x80000013    fabport_1_send_0        0               0               0                      0                      0           0
0x80000014    fabport_1_recv_0        0               0               0                      0                      0           0
0x80000015    fabport_1_send_1        0               0               0                      0                      0           0
0x80000016    fabport_1_recv_1        0               0               0                      0                      0           0
0x80000017    fabport_1_send_2        0               0               0                      0                      0           0
0x80000018    fabport_1_recv_2        0               0               0                      0                      0           0
0x80000019    fabport_1_send_3        0               0               0                      0                      0           0
0x8000001A    fabport_1_recv_3        0               0               0                      0                      0           0
(结果个数 = 27)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE队列统计信息（DSP-PAEQUEUE）_92520046.md`
