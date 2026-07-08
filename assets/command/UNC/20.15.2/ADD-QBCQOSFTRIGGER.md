---
id: UNC@20.15.2@MMLCommand@ADD QBCQOSFTRIGGER
type: MMLCommand
name: ADD QBCQOSFTRIGGER（增加QBC计费QoS Flow级的trigger参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: QBCQOSFTRIGGER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费QoS Flow级Trigger
status: active
---

# ADD QBCQOSFTRIGGER（增加QBC计费QoS Flow级的trigger参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加QBC计费QoS Flow级的trigger参数。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入101条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | QOSCHG | QFLOWTIMELIMIT | QFLOWVOLLIMIT | QFLOWEND |
| --- | --- | --- | --- | --- |
| global | DEFERRED | DEFERRED | DEFERRED | DEFERRED |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| QOSCHG | QoS更新 | 可选必选说明：可选参数<br>参数含义：该参数用于设置QoS更新的trigger上报方式。<br>数据来源：本端规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：DEFERRED<br>配置原则：无 |
| QFLOWTIMELIMIT | QoS流时间阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置QoS流时间阈值的trigger上报方式。<br>数据来源：本端规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：DEFERRED<br>配置原则：无 |
| QFLOWVOLLIMIT | QoS流流量阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置QoS流流量阈值的trigger上报方式。<br>数据来源：本端规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：DEFERRED<br>配置原则：无 |
| QFLOWEND | QoS流结束 | 可选必选说明：可选参数<br>参数含义：该参数用于设置QoS流结束的trigger上报方式。<br>数据来源：本端规划<br>取值范围：<br>- “NONREPORT（不上报）”：事件发生，不生成容器，不上报CHF。<br>- “IMMEDIATE（立即上报）”：事件发生，按Immediate上报，对已经产生的用量生成用量容器，向CHF发送Charging Data Request Update消息携带所有生成的用量容器，并开始新的用量计量。<br>- “DEFERRED（延迟上报）”：事件发生，按Deferred上报，对已经产生的用量生成用量容器，并开始新的用量计量。<br>默认值：DEFERRED<br>配置原则：<br>当前版本不支持配置为NONREPORT。当该参数配置为NONREPORT时，按照DEFERRED处理。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QBCQOSFTRIGGER]] · QBC计费QoS Flow级的trigger参数（QBCQOSFTRIGGER）

## 使用实例

新增QBC计费QoS Flow级的trigger参数绑定名称为“test”的CCT融合计费模板，QoS更新trigger上报方式为立即上报：

```
ADD QBCQOSFTRIGGER: CCTMPLTNAME="test", QOSCHG=IMMEDIATE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加QBC计费QoS-Flow级的trigger参数（ADD-QBCQOSFTRIGGER）_09653288.md`
