---
id: UNC@20.15.2@MMLCommand@SET PCCFAILACTION
type: MMLCommand
name: SET PCCFAILACTION（设置PCC故障处理）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCCFAILACTION
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
- PCC管理
- 基本功能
- PCC公共参数
status: active
---

# SET PCCFAILACTION（设置PCC故障处理）

## 功能

**适用NF：PGW-C、SMF**

该命令用来设置PCC故障处理动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- LOCAL_PCC代表本地PCC用户，有PCC功能，占用PCC基本功能的License，但不与PCRF/PCF交互，EPS场景下的本地PCC用户支持业务触发的QoS保证功能。
- 对于Gx接口的回滚策略，当SET FHBYPASS的GXERRRC参数配置为ENABLE时，SET FHBYPASS命令优先级高于此命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SELPEERFAILACT | SELPEERLOCPCC | SELPEERRDSPCC | INITIALFAILACT | INITFAILLOCPCC | INITFAILRDSPCC | UPDATEFAILACT | UPDFAILLOCPCC | UMRFAILACT | SCPFAILOVERSW |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DEFAULT | LOCAL_PCC | LOCAL_PCC | FORBIDDEN | LOCAL_PCC | LOCAL_PCC | CONTINUE | LOCAL_PCC | INHERIT_UPDATEFAILACT | SCP_NOT_FAILOVER |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELPEERFAILACT | 选择PCRF/PCF失败动作 | 可选必选说明：可选参数<br>参数含义：该参数用于配置激活过程中根据号段匹配选择PCRF/PCF-Group和realm失败情况下系统执行的动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DEFAULT：表示如果配置了缺省的PCRF/PCF组和Realm，则选择缺省的PCRF/PCF组和Realm；如果没有配置缺省的PCRF/PCF组和Realm，若能获取到有效的本地或Radius策略，则激活为本地PCC用户，否则激活失败。<br>- ROLLBACK：表示进行回滚处理。<br>- FORBIDDEN：表示按照激活失败处理。<br>默认值：无<br>配置原则：无 |
| SELPEERLOCPCC | 选择PCRF/PCF失败回滚为Local PCC用户类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SELPEERFAILACT”配置为“ROLLBACK”时为可选参数。<br>参数含义：该参数用于指定激活号段匹配失败回滚为Local PCC用户类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_PCC：表示回滚PCC用户为本地PCC用户。<br>默认值：无<br>配置原则：无 |
| SELPEERRDSPCC | 选择PCRF/PCF失败回滚为RADIUS PCC用户类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SELPEERFAILACT”配置为“ROLLBACK”时为可选参数。<br>参数含义：该参数用于指定激活号段匹配失败回滚为RADIUS PCC用户类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_PCC：表示回滚RADIUS PCC用户为本地PCC用户。<br>默认值：无<br>配置原则：无 |
| INITIALFAILACT | Initial流程故障处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于配置激活过程中Gx/N7链路故障、流控丢消息或响应超时情况下系统执行的动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FORBIDDEN：表示按照激活失败处理。<br>- ROLLBACK：表示进行回滚处理。<br>默认值：无<br>配置原则：无 |
| INITFAILLOCPCC | Initial流程故障回滚为Local PCC用户类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INITIALFAILACT”配置为“ROLLBACK”时为可选参数。<br>参数含义：该参数用于指定Initial流程故障回滚为Local PCC用户类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_PCC：表示回滚PCC用户为本地PCC用户。<br>默认值：无<br>配置原则：无 |
| INITFAILRDSPCC | Initial流程故障回滚为RADIUS PCC用户类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INITIALFAILACT”配置为“ROLLBACK”时为可选参数。<br>参数含义：该参数用于指定Initial流程故障回滚为RADIUS PCC用户类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_PCC：表示回滚RADIUS PCC用户为本地PCC用户。<br>默认值：无<br>配置原则：无 |
| UPDATEFAILACT | Update流程故障处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于配置更新过程中Gx/N7链路故障、流控丢消息或响应超时情况下系统执行的动作。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- ROLLBACK：表示进行回滚处理。<br>- TERMINATE：表示去活用户。<br>- CONTINUE：表示继续与PCRF/PCF交互。<br>默认值：无<br>配置原则：无 |
| UPDFAILLOCPCC | Update流程故障回滚为Local PCC用户类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UPDATEFAILACT”配置为“ROLLBACK”时为可选参数。<br>参数含义：该参数用于指定Update流程故障回滚为Local PCC用户类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_PCC：表示Update流程故障回滚PCC用户为本地PCC用户。<br>- INHERIT_PCC：表示Update流程故障回滚PCC用户为本地PCC用户并且继续使用PCRF/PCF策略。<br>默认值：无<br>配置原则：无 |
| UMRFAILACT | 流量上报失败时处理动作 | 可选必选说明：可选参数<br>参数含义：控制流量上报流程中，当PCF状态异常或回复响应超时时，是否去活整个用户。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- INHERIT_UPDATEFAILACT：流量上报流程中，当对端状态异常或回复响应超时时，使用UPDATEFAILACT参数配置处理。<br>- TERMINATE：流量上报流程中，当对端状态异常或回复响应超时时，去活整个用户。<br>默认值：无<br>配置原则：无 |
| SCPFAILOVERSW | SCP故障重选开关 | 可选必选说明：可选参数<br>参数含义：SMF和PCF采用Model C/D通信模式时，SCP故障是否进行SCP重选。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SCP_NOT_FAILOVER：表示SCP故障时不进行SCP重选。<br>- SCP_FAILOVER：表示SCP故障时进行SCP重选。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCFAILACTION]] · PCC故障处理（PCCFAILACTION）

## 使用实例

设置PCC故障处理：选择PCRF/PCF失败动作为回滚，Initial流程故障处理动作为回滚，Update流程故障处理动作为回滚：

```
SET PCCFAILACTION:SELPEERFAILACT=ROLLBACK,INITIALFAILACT=ROLLBACK,UPDATEFAILACT=ROLLBACK;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PCC故障处理（SET-PCCFAILACTION）_09897058.md`
