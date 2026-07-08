---
id: UNC@20.15.2@MMLCommand@RMV CHRRPTSUBID
type: MMLCommand
name: RMV CHRRPTSUBID（删除CHR本地存盘用户）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHRRPTSUBID
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- CHR本地存盘用户
status: active
---

# RMV CHRRPTSUBID（删除CHR本地存盘用户）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除用户本地存储CHR表单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指示删除记录时的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SPECIFIC_IMSI（指定IMSI）”：删除指定IMSI记录<br>- “ALL（所有）”：删除所有记录<br>默认值：SPECIFIC_IMSI<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"RANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指示用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHRRPTSUBID]] · CHR本地存盘用户（CHRRPTSUBID）

## 使用实例

删除指定用户本地存储CHR表单的配置，用户的IMSI为460030123456789： 删除所有指定用户本地存储CHR表单配置：

```
RMV CHRRPTSUBID: RANGE=SPECIFIC_IMSI, IMSI="460030123456789";
RMV CHRRPTSUBID,RANGE=ALL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHRRPTSUBID.md`
