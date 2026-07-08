---
id: UDG@20.15.2@MMLCommand@DSP PAEDISCARD
type: MMLCommand
name: DSP PAEDISCARD（显示PAE丢包统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAEDISCARD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 报文
status: active
---

# DSP PAEDISCARD（显示PAE丢包统计信息）

## 功能

该命令用于显示PAE模块丢包统计信息。

通过获取的信息，可了解通信是否正常，并进行故障诊断。

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

- [[UDG@20.15.2@ConfigObject@PAEDISCARD]] · PAE丢包统计信息（PAEDISCARD）

## 使用实例

显示所有资源PAE丢包统计信息：

```
DSP PAEDISCARD:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
微服务类型  微服务实例号  丢包类型                                  丢包数目                                  最近30分钟丢包数目      				
aa          aa            PAE_PKTCNT_DROP_TAPIF_LOOKUP_TBL          8                                         8         
aa          aa            PAE_PKTCNT_DROP_FAB_INVALID_PKT           2                                         2
bb          bb            PAE_PKTCNT_DROP_TAPIF_LOOKUP_TBL          8                                         8
bb          bb            PAE_PKTCNT_DROP_FAB_INVALID_PKT           2                                         2  
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PAEDISCARD.md`
