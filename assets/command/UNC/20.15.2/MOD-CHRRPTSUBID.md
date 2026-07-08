---
id: UNC@20.15.2@MMLCommand@MOD CHRRPTSUBID
type: MMLCommand
name: MOD CHRRPTSUBID（修改CHR本地存盘用户）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CHRRPTSUBID
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
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

# MOD CHRRPTSUBID（修改CHR本地存盘用户）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于修改指定IMSI本地存储CHR表单对应的流程模板索引。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指示用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| TMPLIDX | 流程模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指示流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。该参数需要在ADD SESSNCHRPRCTMPL命令中已配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHRRPTSUBID]] · CHR本地存盘用户（CHRRPTSUBID）

## 使用实例

修改指定IMSI为123030123456789的用户对应CHR表单的流程模板索引为1：

```
MOD CHRRPTSUBID: IMSI="123030123456789",TMPLIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改CHR本地存盘用户（MOD-CHRRPTSUBID）_36049943.md`
