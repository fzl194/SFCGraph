---
id: UNC@20.15.2@MMLCommand@MOD NGAPLE
type: MMLCommand
name: MOD NGAPLE（修改NGAP本端实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGAPLE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP本端实体管理
status: active
---

# MOD NGAPLE（修改NGAP本端实体）

## 功能

**适用NF：AMF**

该命令用于修改NGAP本端实体配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPLEIDX | NGAP本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NGAP本端实体的索引，该索引作为NGAP本端实体的唯一标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |
| NGAPPARAIDX | NGAP参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NGAP本端实体的NGAP协议参数配置索引。NGAP协议参数存在系统默认配置，如果NGAP本端实体默认使用系统默认参数可不指定该参数。如果NGAP本端实体需要使用其他配置值，则可以引用对应配置的NGAP协议参数索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGAPLE]] · NGAP本端实体（NGAPLE）

## 使用实例

将本端实体标识为1的本端实体的NGAP参数索引改为5，执行如下命令：

```
MOD NGAPLE: NGAPLEIDX=1, NGAPPARAIDX=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NGAP本端实体（MOD-NGAPLE）_09653766.md`
