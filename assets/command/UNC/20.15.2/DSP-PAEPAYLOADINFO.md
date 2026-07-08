---
id: UNC@20.15.2@MMLCommand@DSP PAEPAYLOADINFO
type: MMLCommand
name: DSP PAEPAYLOADINFO（显示PAE负载信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEPAYLOADINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 系统资源
status: active
---

# DSP PAEPAYLOADINFO（显示PAE负载信息）

## 功能

该命令用于显示指定资源上PAE模块转发线程的负载信息。

在需要查询PAE转发线程的CPU使用率、以及当时的转发速率时，可以使用此命令查询。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [PAE负载信息（PAEPAYLOADINFO）](configobject/UNC/20.15.2/PAEPAYLOADINFO.md)

## 使用实例

显示所有资源上PAE负载信息：

```
DSP PAEPAYLOADINFO:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
微服务类型  微服务实例号 线程ID    线程类型      绑核ID    CPU使用率（%）    外联口发送速率（pps）    外联口接收速率（pps）    Fabric发送速率（pps）    Fabric接收速率（pps）    Loop口发送速率（pps）    Loop口接收速率（pps）    Channel发送速率（pps）    Channel接收速率（pps）    Control发送速率（pps）    Control接收速率（pps） 
		
aa          aa           1         转发线程      2         31                0                        0                        2                        5                        0                        0                        0                         0                         0                         0
aa          aa           2         转发线程      3         31                0                        0                        8                        13                       0                        0                        0                         0                         0                         0                   
aa          aa           64        非转发线程    0         0                 0                        0                        0                        0                        0                        0                        0                         0                         0                         0
bb          bb           1         转发线程      2         29                0                        0                        2                        6                        0                        0                        0                         0                         0                         0
bb          bb           2         转发线程      3         30                0                        0                        8                        12                       0                        0                        0                         0                         0                         0
bb          bb           64        非转发线程    0         0                 0                        0                        0                        0                        0                        0                        0                         0                         0                         0
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PAE负载信息（DSP-PAEPAYLOADINFO）_92520024.md`
