---
id: UNC@20.15.2@MMLCommand@SET IMSBYPASSFUNC
type: MMLCommand
name: SET IMSBYPASSFUNC（设置语音PCF/PCRF故障Bypass场景功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IMSBYPASSFUNC
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 语音PCF_PCRF Bypass管理
status: active
---

# SET IMSBYPASSFUNC（设置语音PCF/PCRF故障Bypass场景功能）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置语音PCF/PCRF故障Bypass场景功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ACTNODEDBEARER | ACTWITDEDBEARER | FAILLOCPCC | TSTUPDATEREQSW | REACTREQ |
| --- | --- | --- | --- | --- |
| INHERIT | INHERIT | LOCAL_PCC | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACTNODEDBEARER | 无语音专载时的故障非预期Bypass场景的异常处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用来配置无语音专载时的激活或更新流程故障非预期Bypass场景的异常处理动作。<br>数据来源：本端规划<br>取值范围：<br>- INHERIT（继承）<br>- TERMINATE（去活）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。<br>配置原则：<br>该参数仅适用于非预期Bypass场景，包括：1. 更新流程Gx接口不支持Failover场景、2. 直连场景Failover后收到备PCRF/PCF返回异常码场景、3. 非直连场景Failover后收到DRA返回非RESULTCODEDRA配置的异常码场景、4. 非直连场景Failover后收到SCP返回非RESULTCODESCP配置的异常码场景。参数取值为“INHERIT”时，继承原有的PCCTEMPLATE、PCCFAILACTION、RESULTCODECTRL等响应超时或异常码配置动作处理；参数取值为“TERMINATE”时，去活会话。 |
| ACTWITDEDBEARER | 存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用来配置存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作。<br>数据来源：本端规划<br>取值范围：<br>- INHERIT（继承）<br>- FASTROLLBACK（短暂回滚）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。<br>配置原则：<br>该参数仅适用于非预期Bypass场景，包括：1. 更新流程Gx接口不支持Failover场景、2. 直连场景Failover后收到备PCRF/PCF返回异常码场景、3. 非直连场景Failover后收到DRA返回非RESULTCODEDRA配置的异常码场景、4. 非直连场景Failover后收到SCP返回非RESULTCODESCP配置的异常码场景。参数取值为“INHERIT”时，继承原有的PCCTEMPLATE、PCCFAILACTION、RESULTCODECTRL等响应超时或异常码配置动作处理；参数取值为“FASTROLLBACK”时，短暂回滚本地PCC。 |
| FAILLOCPCC | 存在语音专载时更新流程故障回滚为Local PCC用户类型 | 可选必选说明：该参数在"ACTWITDEDBEARER"配置为"FASTROLLBACK"时为条件可选参数。<br>参数含义：该参数用于指定存在语音专载时更新流程故障回滚为Local PCC用户类型。<br>数据来源：全网规划<br>取值范围：<br>- LOCAL_PCC（回滚PCC用户为本地PCC用户）<br>- INHERIT_PCC（回滚PCC用户为本地PCC用户并且继续使用PCRF/PCF策略）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。<br>配置原则：无 |
| TSTUPDATEREQSW | 非直连场景下退出Bypass发送探测消息开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置非直连场景下退出Bypass时是否需要发送探测消息。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不发送探测消息）<br>- ENABLE（发送探测消息）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。<br>配置原则：无 |
| REACTREQ | 重新激活请求 | 可选必选说明：可选参数<br>参数含义：该参数用于指示当语音用户因Holdingtime超时去活时，UNC是否通知用户重新激活。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。<br>配置原则：<br>该参数使能时需要同时打开语音用户ADD APN命令的REACWITHDEL参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMSBYPASSFUNC]] · 语音PCF/PCRF故障Bypass场景功能（IMSBYPASSFUNC）

## 使用实例

配置无语音专载时的故障非预期Bypass场景的异常处理动作为“去活”：

```
SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IMSBYPASSFUNC.md`
