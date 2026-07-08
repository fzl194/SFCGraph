---
id: UNC@20.15.2@MMLCommand@SET GLBRDSACCT
type: MMLCommand
name: SET GLBRDSACCT（设置全局RADIUS Accounting配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GLBRDSACCT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS计费管理
- RADIUS基础参数
status: active
---

# SET GLBRDSACCT（设置全局RADIUS Accounting配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用来设置全局RADIUS计费配置的信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令必须配置其中一个参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ONOFFADDITTIMES | TRANSTHRESHOLD |
| --- | --- | --- |
| 初始值 | 0 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ONOFFADDITTIMES | 发送RADIUS Accounting On/Off消息附加次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定发送RADIUS Accounting On/Off消息附加次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |
| TRANSTHRESHOLD | 每秒钟尝试发送Accounting Start消息的用户数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定每秒钟尝试发送Accounting Start消息的用户数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GLBRDSACCT]] · 全局RADIUS Accounting配置（GLBRDSACCT）

## 使用实例

修改PGW APN计费方式：ONOFFADDITTIMES为1，TRANSTHRESHOLD为10：

```
SET GLBRDSACCT: ONOFFADDITTIMES=1,TRANSTHRESHOLD=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-GLBRDSACCT.md`
