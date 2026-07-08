---
id: UDG@20.15.2@MMLCommand@RTR PAEREASSEMBLEINFO
type: MMLCommand
name: RTR PAEREASSEMBLEINFO（清除PAE分片重组统计计数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: PAEREASSEMBLEINFO
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 报文
status: active
---

# RTR PAEREASSEMBLEINFO（清除PAE分片重组统计计数）

## 功能

该命令用于清除Fabric口分片重组统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PAEREASSEMBLEINFO]] · PAE分片重组统计信息（PAEREASSEMBLEINFO）

## 使用实例

清除微服务“aa” Fabric口分片重组统计信息：

```
RTR PAEREASSEMBLEINFO:CELLTYPE="aa", CELLINSTANCE="bb";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-PAEREASSEMBLEINFO.md`
