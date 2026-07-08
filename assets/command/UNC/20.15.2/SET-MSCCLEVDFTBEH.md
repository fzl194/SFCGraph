---
id: UNC@20.15.2@MMLCommand@SET MSCCLEVDFTBEH
type: MMLCommand
name: SET MSCCLEVDFTBEH（设置DCC模板MSCC层缺省返回码动作）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MSCCLEVDFTBEH
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
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

# SET MSCCLEVDFTBEH（设置DCC模板MSCC层缺省返回码动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置DCC在线计费模板MSCC缺省返回码动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为101。
- MSCC层返回码DIAMETER_CREDIT_CONTROL_NOT_APPLICABLE（4011）的缺省处理动作为免费访问该业务，不受该命令控制。
- MSCC层返回码DIAMETER_SUCCESS（2001），DIAMETER_LIMITED_SUCCESS（2002）的缺省处理动作为成功，正常转发报文并计费，不受该命令控制。
- 当OCS在CCA消息中返回MSCC层非4012异常返回码和FUA信元时，如果软参BIT1738值为0，则忽略FUA信元，按照本命令配置的处理动作进行处理。
- 该命令设定后的数据，需要通过LST DCCTEMPLATE命令进行查看。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DCCTMPLTNAME | MSCCLEVDFTBEH | MSCCDFTBLKTM | MSCCREACTREQ |
| --- | --- | --- | --- | --- |
| 初始值 | global | BLOCK | 0 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | DCC模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作的DCC在线计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DCCTEMPLATE命令配置生成。<br>- 该命令基于此参数配置DCC在线计费模板的MSCC缺省返回码动作。 |
| MSCCLEVDFTBEH | MSCC层缺省处理动作 | 可选必选说明：必选参数<br>参数含义：该参数用于配置业务的执行类型，选择不同的枚举值将执行不同的业务功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BLOCK：阻断。<br>- BLCK_TRG_RPT：阻断后trigger触发上报。<br>- BLCK_IMMED_RPT：阻断后立即触发上报。<br>- BLCK_NO_RPT：阻断后不再触发上报。<br>- CONTINUE：业务继续进行。<br>- TERMINATE：去活。<br>- REDIRECT：重定向。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |
| MSCCDFTBLKTM | MSCC层缺省阻塞处理时间间隔（分） | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCLEVDFTBEH”配置为“BLCK_IMMED_RPT” 或 “BLCK_NO_RPT”时为可选参数。<br>参数含义：该参数用于配置业务阻塞的时间，从阻塞开始经过这段时间以后，业务再来时可以重新触发配额申请。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1440，单位是分钟。<br>默认值：无<br>配置原则：无 |
| MSCCDFTRDIPV4 | MSCC层缺省处理重定向IP | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCLEVDFTBEH”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于配置在线计费模板中MSCC层当前返回码的动作为将当前业务重定向到指定的虚拟IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| MSCCDFTRDIPV6 | MSCC层缺省处理重定向IPV6 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCLEVDFTBEH”配置为“REDIRECT”时为可选参数。<br>参数含义：该参数用于配置在线计费模板中MSCC层当前返回码的动作为将当前业务重定向到指定的虚拟IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| MSCCREACTREQ | MSCC层重新激活请求 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MSCCLEVDFTBEH”配置为“TERMINATE”时为可选参数。<br>参数含义：该参数用于指示当用户因MSCC层异常结果码被去活时，UNC是否通知用户重新激活。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCCLEVDFTBEH]] · DCC模板MSCC层缺省返回码动作（MSCCLEVDFTBEH）

## 使用实例

设置名为“DccTemplate”的DCC在线计费模板的MSCC层缺省返回码动作为阻断后立即触发上报：

```
SET MSCCLEVDFTBEH:DCCTMPLTNAME="DccTemplate",MSCCLEVDFTBEH=BLCK_IMMED_RPT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MSCCLEVDFTBEH.md`
