---
id: UDG@20.15.2@MMLCommand@SET AES128
type: MMLCommand
name: SET AES128（设置aes128加密算法的IV值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: AES128
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- AES128加密算法的IV值
status: active
---

# SET AES128（设置aes128加密算法的IV值）

## 功能

**适用NF：PGW-U、UPF**

该命令用来设置aes128加密算法的IV值。当重定向或者头增强配置需要进行aes128加密处理时，使用该数值作为加密算法的IV值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RDRCTRANDOMIV | HEADENRANDOMIV |
| --- | --- | --- |
| 初始值 | ENABLE | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDRCTRANDOMIV | 重定向随机IV值开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向加密是否使用随机生成的IV值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭），有安全风险，不建议使用。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议配置为ENABLE。 |
| REDIRECTIV | 重定向动作AES128的IV值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RDRCTRANDOMIV”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于设置AES128的IV值。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～16。本参数输入长度必须为16位的字符串，不支持空格。<br>默认值：无<br>配置原则：<br>- 设置时，输入的为明文，长度为16。<br>- 显示时，显示为“*****”。<br>- 输入单空格将删除该参数已有配置项。 |
| REDIRECTIVCONFIRM | 确认重定向动作AES128的IV值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RDRCTRANDOMIV”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于确认AES128的IV值。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～16。本参数输入长度必须为16位的字符串，不支持空格。<br>默认值：无<br>配置原则：<br>- 设置时，输入的为明文，长度为16。<br>- 显示时，显示为“*****”。<br>- 输入单空格将删除该参数已有配置项。 |
| HEADENRANDOMIV | 头增强随机IV值开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置头增强加密是否使用随机生成的IV值。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭），有安全风险，不建议使用。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：为了保证更好的安全性，建议配置为ENABLE。 |
| HEADENIV | 头增强动作AES128的IV值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEADENRANDOMIV”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于设置头增强动作执行AES128加密的IV值。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～16。本参数输入长度必须为16位的字符串，不支持空格。<br>默认值：无<br>配置原则：<br>- 设置时，输入的为明文，长度为16。<br>- 显示时，显示为“*****”。<br>- 输入单空格将删除该参数已有配置项。 |
| HEADENIVCONFIRM | 确认头增强动作AES128的IV值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEADENRANDOMIV”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于确认头增强动作执行AES128加密的IV值。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～16。本参数输入长度必须为16位的字符串，不支持空格。<br>默认值：无<br>配置原则：<br>- 设置时，输入的为明文，长度为16。<br>- 显示时，显示为“*****”。<br>- 输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AES128]] · aes128加密算法的IV值（AES128）

## 使用实例

假如运营商想要设置aes128加密算法的IV值为1234567890123456，配置如下：

```
SET AES128: RDRCTRANDOMIV=DISABLE, REDIRECTIV="1234567890123456", REDIRECTIVCONFIRM="1234567890123456", HEADENRANDOMIV=DISABLE, HEADENIV="1234567890123456", HEADENIVCONFIRM="1234567890123456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-AES128.md`
