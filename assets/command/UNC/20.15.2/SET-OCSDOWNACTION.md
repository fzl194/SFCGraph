---
id: UNC@20.15.2@MMLCommand@SET OCSDOWNACTION
type: MMLCommand
name: SET OCSDOWNACTION（设置DCC模板OCS状态Down动作）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OCSDOWNACTION
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 101
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 信用控制模板
status: active
---

# SET OCSDOWNACTION（设置DCC模板OCS状态Down动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置DCC在线计费模板OCS状态Down动作。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为101。
- 该命令设定后的数据，需要通过LST DCCTEMPLATE命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DCCTMPLTNAME | OCSDNACTION | HOLDINGTMFLAG |
| --- | --- | --- | --- |
| 初始值 | global | PERMIT | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 该命令基于此参数配置DCC在线计费模板的OCS状态Down动作。 |
| OCSDNACTION | OCS断用户处理动作 | 可选必选说明：必选参数<br>参数含义：该参数用于配置在线计费模板中配置用户激活时Gy对端状态为Down时的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PERMIT：通过。<br>- FORBIDDEN：禁止。<br>- BLOCK：阻塞业务一段时间后去活用户，阻塞时间受DCCTEMPLATE下的BLOCKTIMER控制。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：OCSDnAction参数为PERMIT时，需要首先通过SET HOLDINGTIME命令配置HoldingTime参数。 |
| HOLDINGTMFLAG | OCS断用户允许在线时间控制开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“OCSDNACTION”配置为“PERMIT”时为可选参数。<br>参数含义：该参数用于指定OCS状态为DOWN时允许用户激活后，是否使用HoldingTime控制允许用户访问的时间。如果使用HoldingTime控制用户访问时间，HoldingTime超时后用户将被去活。HoldingTime时间通过参数HoldingTime配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能OCS断用户允许在线时间控制。<br>- ENABLE：使能OCS断用户允许在线时间控制。<br>- INHERIT：继承全局DCC模板。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSDOWNACTION]] · DCC模板OCS状态Down动作（OCSDOWNACTION）

## 使用实例

设置名为“DccTemplate”的DCC在线计费模板的OCS断用户处理动作为通过，并打开OCS断用户允许在线时间控制开关：

```
SET OCSDOWNACTION:DCCTMPLTNAME="DccTemplate",OCSDNACTION=PERMIT,HOLDINGTMFLAG=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OCSDOWNACTION.md`
