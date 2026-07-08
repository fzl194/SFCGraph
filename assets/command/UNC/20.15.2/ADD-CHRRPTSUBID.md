---
id: UNC@20.15.2@MMLCommand@ADD CHRRPTSUBID
type: MMLCommand
name: ADD CHRRPTSUBID（增加CHR本地存盘用户）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD CHRRPTSUBID（增加CHR本地存盘用户）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于增加指定某个用户本地存储CHR表单。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入64条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指示用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：无 |
| TMPLIDX | 流程模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指示流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。该参数需要在ADD SESSNCHRPRCTMPL命令中已配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHRRPTSUBID]] · CHR本地存盘用户（CHRRPTSUBID）

## 使用实例

指定某个用户本地存储CHR表单，用户的IMSI为123030123456789：

```
ADD CHRRPTSUBID: IMSI="123030123456789", TMPLIDX=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CHRRPTSUBID.md`
