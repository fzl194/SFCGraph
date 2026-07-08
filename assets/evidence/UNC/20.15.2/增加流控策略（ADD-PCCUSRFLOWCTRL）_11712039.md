# 增加流控策略（ADD PCCUSRFLOWCTRL）

- [命令功能](#ZH-CN_MMLREF_0211712039__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0211712039__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0211712039__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0211712039__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0211712039)

**适用NF：SMF**

该命令用于增加流控策略。

## [注意事项](#ZH-CN_MMLREF_0211712039)

- 该命令执行后立即生效。

- 如果一个更新流程匹配上多个流控策略，动作优先顺序为：TERMINATE、ROLLBACK、FLOWCTRL。不允许添加UPDTYPE相同的流控策略，ALL类型的UPDTYPE只能添加一个。

- 最多可输入10条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| USRFLOWCTRLNAME | UPDTYPE | CTRLACT | SAMPLEINVL | SAMPLECNT | ROLLBACK | FLOWCTRLINVL | FLOWCTRLCNT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| default_rule_qos_fail | RULE_INSTALL_FAIL-1&QOS_UPDATE_FAIL-1 | TERMINATE | 10 | 5 | LOCAL_PCC | 120 | 1 |

#### [操作用户权限](#ZH-CN_MMLREF_0211712039)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0211712039)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRFLOWCTRLNAME | Update流控策略名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update流控策略名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。区分大小写。<br>默认值：无<br>配置原则：无 |
| UPDTYPE | Update流控的类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update流控的类型。当ALL选定时表示包含所有更新流程。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（所有更新消息类型）”：所有更新消息类型。<br>- “USAGE_MONITOR_REPORT（流量上报消息）”：流量上报消息。<br>- “RULE_INSTALL_FAIL（Rule安装失败消息）”：Rule安装失败消息。<br>- “QOS_UPDATE_FAIL（QoS更新失败消息）”：QoS更新失败消息。<br>- “ULI_CHANGE（用户位置信息变化）”：用户位置信息变化。<br>默认值：无<br>配置原则：<br>只有默认记录允许配置为NULL，其他记录不允许为NULL。 |
| CTRLACT | 用于指定Update达到指定次数后执行的处理动作 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Update达到指定次数后执行的处理动作。<br>数据来源：本端规划<br>取值范围：<br>- “TERMINATE（去活会话）”：去活会话。<br>- “ROLLBACK（回滚为静态PCC用户）”：回滚为静态PCC用户。<br>- “FLOWCTRL（流控）”：流控。<br>默认值：无<br>配置原则：无 |
| SAMPLEINVL | 采样间隔 | 可选必选说明：该参数在"CTRLACT"配置为"ROLLBACK"、"TERMINATE"时为条件可选参数。<br>参数含义：该参数用于指定采样间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~1800，单位是秒。<br>默认值：120<br>配置原则：无 |
| SAMPLECNT | 采样次数 | 可选必选说明：该参数在"CTRLACT"配置为"ROLLBACK"、"TERMINATE"时为条件可选参数。<br>参数含义：该参数用于指定采样次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是3~120。<br>默认值：5<br>配置原则：无 |
| ROLLBACK | 回滚类型 | 可选必选说明：该参数在"CTRLACT"配置为"ROLLBACK"时为条件可选参数。<br>参数含义：该参数用于指定CTRLACT配置为ROLLBACK时的回滚类型。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL_PCC（回滚为静态PCC）”：回滚为静态PCC。<br>- “INHERIT_PCC（回滚为静态PCC，仍使用PCF策略）”：回滚为静态PCC，仍使用PCF策略。<br>默认值：LOCAL_PCC<br>配置原则：无 |
| FLOWCTRLINVL | Update消息流控间隔 | 可选必选说明：该参数在"CTRLACT"配置为"FLOWCTRL"时为条件可选参数。<br>参数含义：该参数用于指定Update消息流控间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~1800，单位是秒。<br>默认值：120<br>配置原则：无 |
| FLOWCTRLCNT | Update消息流控间隔内发送次数 | 可选必选说明：该参数在"CTRLACT"配置为"FLOWCTRL"时为条件可选参数。<br>参数含义：该参数用于指定Update消息流控间隔内发送次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~10。<br>默认值：1<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0211712039)

增加对应用量上报的更新消息流控策略，当每分钟发送消息数大于2次时进行流控。

```
ADD PCCUSRFLOWCTRL: USRFLOWCTRLNAME="flowctr1", UPDTYPE=USAGE_MONITOR_REPORT-1, CTRLACT=FLOWCTRL, FLOWCTRLINVL=60, FLOWCTRLCNT=2;
```
