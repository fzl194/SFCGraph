---
id: UNC@20.15.2@MMLCommand@SET STGTRIGGER
type: MMLCommand
name: SET STGTRIGGER（设置融合计费消息缓存期间融合计费消息生成的trigger）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: STGTRIGGER
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费消息缓存
status: active
---

# SET STGTRIGGER（设置融合计费消息缓存期间融合计费消息生成的trigger）

## 功能

**适用NF：SMF**

该命令用于设置融合计费消息缓存期间融合计费消息生成的trigger。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TIMELIMIT | PDUTIMELIMIT | VOLUMELIMIT | PDUVOLUMELIMIT | RATCHG | SRVNDCHG | QOSCHG | ULCHG |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IMMEDIATE | 30 | IMMEDIATE | 500 | IMMEDIATE | DEFERRED | DEFERRED | DEFERRED |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMELIMIT | 时间阈值 | 可选必选说明：可选参数<br>参数含义：用于设置用户业务放通期间，时间阈值trigger的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- NONREPORT（不上报）<br>- IMMEDIATE（立即上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| PDUTIMELIMIT | PDU时长阈值(分钟) | 可选必选说明：可选参数<br>参数含义：指定PDU级别触发生成缓存消息的时长阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| VOLUMELIMIT | 流量阈值 | 可选必选说明：可选参数<br>参数含义：用于设置用户业务放通后，流量阈值trigger的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- NONREPORT（不上报）<br>- IMMEDIATE（立即上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| PDUVOLUMELIMIT | PDU流量阈值(MB) | 可选必选说明：可选参数<br>参数含义：指定PDU级别触发生成缓存消息的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2147483647，单位是兆字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| RATCHG | RAT更新 | 可选必选说明：可选参数<br>参数含义：设置用户业务放通后，RAT更新trigger的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- NONREPORT（不上报）<br>- IMMEDIATE（立即上报）<br>- DEFERRED（延迟上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| SRVNDCHG | 服务节点更新 | 可选必选说明：可选参数<br>参数含义：设置用户业务放通后，服务节点更新trigger的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- NONREPORT（不上报）<br>- IMMEDIATE（立即上报）<br>- DEFERRED（延迟上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| QOSCHG | QoS更新 | 可选必选说明：可选参数<br>参数含义：设置用户业务放通后，QoS更新trigger的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- NONREPORT（不上报）<br>- IMMEDIATE（立即上报）<br>- DEFERRED（延迟上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |
| ULCHG | 用户位置更新 | 可选必选说明：可选参数<br>参数含义：设置用户业务放通后，用户位置更新trigger的处理方式。<br>数据来源：本端规划<br>取值范围：<br>- NONREPORT（不上报）<br>- IMMEDIATE（立即上报）<br>- DEFERRED（延迟上报）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STGTRIGGER查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STGTRIGGER]] · 融合计费消息缓存期间融合计费消息生成的trigger（STGTRIGGER）

## 使用实例

设置融合计费消息缓存期间融合计费消息生成的trigger：

```
SET STGTRIGGER: TIMELIMIT=IMMEDIATE, PDUTIMELIMIT=30, VOLUMELIMIT=IMMEDIATE, PDUVOLUMELIMIT=500, RATCHG=IMMEDIATE, SRVNDCHG=DEFERRED, QOSCHG=DEFERRED, ULCHG=DEFERRED;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置融合计费消息缓存期间融合计费消息生成的trigger（SET-STGTRIGGER）_34667406.md`
