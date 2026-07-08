---
id: UNC@20.15.2@MMLCommand@MOD PCCUSRFLOWCTRL
type: MMLCommand
name: MOD PCCUSRFLOWCTRL（修改流控策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PCCUSRFLOWCTRL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 更新流控策略
status: active
---

# MOD PCCUSRFLOWCTRL（修改流控策略）

## 功能

**适用NF：SMF**

该命令用于修改流控策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRFLOWCTRLNAME | Update流控策略名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update流控策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：无 |
| UPDTYPE | Update流控的类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Update流控的类型。当ALL选定时表示包含所有更新流程。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（所有更新消息类型）”：所有更新消息类型。<br>- “USAGE_MONITOR_REPORT（流量上报消息）”：流量上报消息。<br>- “RULE_INSTALL_FAIL（Rule安装失败消息）”：Rule安装失败消息。<br>- “QOS_UPDATE_FAIL（QoS更新失败消息）”：QoS更新失败消息。<br>- “ULI_CHANGE（用户位置信息变化）”：用户位置信息变化。<br>默认值：无<br>配置原则：<br>只有默认记录允许配置为NULL，其他记录不允许为NULL。 |
| CTRLACT | 用于指定Update达到指定次数后执行的处理动作 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update达到指定次数后执行的处理动作。<br>数据来源：本端规划<br>取值范围：<br>- “TERMINATE（去活会话）”：去活会话。<br>- “ROLLBACK（回滚为静态PCC用户）”：回滚为静态PCC用户。<br>- “FLOWCTRL（流控）”：流控。<br>默认值：无<br>配置原则：无 |
| SAMPLEINVL | 采样间隔 | 参数含义：该参数用于指定采样间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~1800，单位是秒。<br>默认值：无<br>配置原则：无 |
| SAMPLECNT | 采样次数 | 参数含义：该参数用于指定采样次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~120。<br>默认值：无<br>配置原则：无 |
| ROLLBACK | 回滚类型 | 参数含义：该参数用于指定CTRLACT配置为ROLLBACK时的回滚类型。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL_PCC（回滚为静态PCC）”：回滚为静态PCC。<br>- “INHERIT_PCC（回滚为静态PCC，仍使用PCF策略）”：回滚为静态PCC，仍使用PCF策略。<br>默认值：无<br>配置原则：无 |
| FLOWCTRLINVL | Update消息流控间隔 | 参数含义：该参数用于指定Update消息流控间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~1800，单位是秒。<br>默认值：无<br>配置原则：无 |
| FLOWCTRLCNT | Update消息流控间隔内发送次数 | 参数含义：该参数用于指定Update消息流控间隔内发送次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCUSRFLOWCTRL]] · 流控策略（PCCUSRFLOWCTRL）

## 使用实例

修改流控策略。

```
MOD PCCUSRFLOWCTRL: USRFLOWCTRLNAME="flowctr1", UPDTYPE=USAGE_MONITOR_REPORT-1, CTRLACT=FLOWCTRL, FLOWCTRLINVL=60, FLOWCTRLCNT=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-PCCUSRFLOWCTRL.md`
