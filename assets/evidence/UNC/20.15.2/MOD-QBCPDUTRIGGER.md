# 修改QBC计费PDU会话级的trigger参数（MOD QBCPDUTRIGGER）

- [命令功能](#ZH-CN_MMLREF_0209652270__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652270__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652270__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652270__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652270)

**适用NF：PGW-C、SMF**

该命令用于修改QBC计费PDU会话级的trigger参数。

## [注意事项](#ZH-CN_MMLREF_0209652270)

该命令执行后只对新激活用户生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652270)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652270)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| ULCHG | 用户位置更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户位置更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| AMFCHG | AMF更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置AMF更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：<br>1）作为I-SMF/V-SMF/N11SMF的场景下，AMF的改变会触发AMFCHG（SERVING_NODE_CHANGE）的trigger。<br>2）作为N16aSMF/H-SMF的场景下，I-SMF/V-SMF的插入/改变/删除都会触发AMFCHG（SERVING_NODE_CHANGE）的trigger。 |
| PRACHG | 区域用户位置上报更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置区域用户位置上报更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| PSDATAOFFCHG | PS数据关闭状态更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PS数据关闭状态的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| UETZCHG | 用户时区更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户时区更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| PLMNCHG | PLMN更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PLMN更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| RATCHG | RAT更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置RAT更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| SESSAMBRCHG | 会话AMBR更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置会话AMBR更新的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| ADDUPF | 添加UPF | 可选必选说明：可选参数<br>参数含义：该参数用于指定添加UPF的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| TIMELIMIT | 时间阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PDU会话的数据时间阈值的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| VOLUMELIMIT | 流量阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PDU会话的数据流量阈值的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：无 |
| EVENTLIMIT | 事件阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置PDU会话的数据事件阈值的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：<br>QBC计费不支持EVENTLIMIT。 |
| MAXNUMCCC | 计费条件改变阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置计费条件改变阈值的trigger上报方式。<br>数据来源：全网规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：无<br>配置原则：<br>当前版本不支持配置为DEFERRED。当该参数配置为DEFERRED时，按照IMMEDIATE处理。 |

## [使用实例](#ZH-CN_MMLREF_0209652270)

修改绑定融合计费模板名称为“test”的QBC计费PDU会话级的trigger参数，用户位置更改trigger上报方式为延迟上报：

```
MOD QBCPDUTRIGGER: CCTMPLTNAME="test", ULCHG=DEFERRED;
```
