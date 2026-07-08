---
id: UNC@20.15.2@MMLCommand@MOD IPEN7SUFFIX
type: MMLCommand
name: MOD IPEN7SUFFIX（修改智能业务后缀）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPEN7SUFFIX
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 智能双N7会话
status: active
---

# MOD IPEN7SUFFIX（修改智能业务后缀）

## 功能

**适用NF：SMF、PGW-C**

该命令用于修改智能业务后缀。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTELLISUFFIX | 智能业务后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于设置智能业务后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>不支持空格，不区分大小写。 |
| INTELLINAME | 智能业务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置智能业务名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPEN7SUFFIX]] · 智能业务后缀（IPEN7SUFFIX）

## 使用实例

修改智能业务后缀为“intelligent”配置的智能业务名称为“video”：

```
MOD IPEN7SUFFIX: INTELLISUFFIX="intelligent",INTELLINAME="video";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改智能业务后缀（MOD-IPEN7SUFFIX）_16631861.md`
