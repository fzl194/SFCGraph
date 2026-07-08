---
id: UNC@20.15.2@MMLCommand@DSP PAECHANNEL
type: MMLCommand
name: DSP PAECHANNEL（显示PAE通道统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAECHANNEL
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

# DSP PAECHANNEL（显示PAE通道统计信息）

## 功能

该命令用于显示PAE Channel状态和统计信息。

Channel是同资源内应用进程和PAE之间的通信通道。通过此命令可查看Channel的状态和统计信息，可了解通信是否正常，并进行故障诊断。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| CHANNELNAME | 通道名称 | 可选必选说明：可选参数<br>参数含义：通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～11。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAECHANNEL]] · PAE通道统计信息（PAECHANNEL）

## 使用实例

- 显示微服务类型为“CCellCpcSrv”微服务实例为“2491301”的PAE Channel统计信息：
  ```
  DSP PAECHANNEL:CELLTYPE="CCellCpcSrv", CELLINSTANCE="2491301";
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  TP        通道索引    通道ID    通道调度权重    逻辑进程ID           节点ID              通道的接收使能标志    通道对应的用户是否重启    通道下的队列总数    队列ID        队列优先级    队列QoS    数据类型      通道名称    通道类型    QoS映射模式    队列写满次数    队列的单元总个数    队列的当前使用个数    接收报文数目    发送报文数目    接收报文速率（pps）    发送报文速率（pps）    应用侧的发包统计    应用侧的收包统计    丢包统计    重发次数

  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x8000000C    0             NULL       队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x8000000B    0             0,1        队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x8000000E    0             NULL       队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x8000000D    1             2,3        队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x80000010    0             NULL       队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x8000000F    2             4,5        队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x80000012    0             NULL       队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     1                   0x80000011    3             6,7        队列统计      extport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1001    0           0         10              1                    0                   TRUE                  FALSE                     8                   0x0           0             NULL       通道统计      extport     透传        全局           0               32760               0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000014    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000013    0             0,1        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000016    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000015    1             2,3        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000018    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000017    2             4,5        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x8000001A    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000019    3             6,7        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     8                   0x0           0             NULL       通道统计      fabport     默认        私有           0               32760               0                     0               0               0                      0                      0                   0                   0           0
  (结果个数 = 18)
  ---    END
  ```
- 显示指定PAE Channel统计信息：
  ```
  DSP PAECHANNEL: CELLTYPE="CCellCpcSrv", CELLINSTANCE="2491301",CHANNELNAME="fabport";
  ```
  ```
  RETCODE = 0  操作成功。

  结果如下
  -------------------------
  TP        通道索引    通道ID    通道调度权重    逻辑进程ID           节点ID              通道的接收使能标志    通道对应的用户是否重启    通道下的队列总数    队列ID        队列优先级    队列QoS    数据类型      通道名称    通道类型    QoS映射模式    队列写满次数    队列的单元总个数    队列的当前使用个数    接收报文数目    发送报文数目    接收报文速率（pps）    发送报文速率（pps）    应用侧的发包统计    应用侧的收包统计    丢包统计    重发次数

  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000014    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000013    0             0,1        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000016    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000015    1             2,3        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000018    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000017    2             4,5        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x8000001A    0             NULL       队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     1                   0x80000019    3             6,7        队列统计      fabport     NULL        NULL           0               4095                0                     0               0               0                      0                      0                   0                   0           0
  0x1002    1           1         10              1                    0                   TRUE                  FALSE                     8                   0x0           0             NULL       通道统计      fabport     默认        私有           0               32760               0                     0               0               0                      0                      0                   0                   0           0
  (结果个数 = 9)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE通道统计信息（DSP-PAECHANNEL）_92520031.md`
