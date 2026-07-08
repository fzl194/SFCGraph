---
id: UNC@20.15.2@MMLCommand@SET DDNSUPPRESSION
type: MMLCommand
name: SET DDNSUPPRESSION（设置DDN抑制功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DDNSUPPRESSION
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- DDN抑制管理
status: active
---

# SET DDNSUPPRESSION（设置DDN抑制功能）

## 功能

**适用NF：SGW-C**

该命令用于设置DDN抑制功能相关参数。DDN抑制功能是指“MONITORTIMER(监控时长)”内某用户的DDN流程失败，且收到MME返回Downlink Data Notification Failure Indication消息携带失败原因值“UE not responding”或者“Unable to page UE”，失败的次数达到“MONITORTIMES(DDN失败次数)”，该用户在接下来的“SUPPTIMER(抑制时长)”内，将对DDN流程进行抑制，收到UPF的DDN请求后直接回复失败，不再向MME发送DDN消息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SUPPSW | MONITORTIMER | MONITORTIMES | SUPPTIMER |
| --- | --- | --- | --- |
| DISABLE | 5 | 10 | 5 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUPPSW | DDN抑制功能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制DDN抑制功能是否开启。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |
| MONITORTIMER | 监控时长(分) | 可选必选说明：该参数在"SUPPSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置DDN抑制的监控时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNSUPPRESSION查询当前参数配置值。<br>配置原则：<br>当用户在配置的“监控时长(分)”内，DDN由于收到MME发送Downlink Data Notification Failure Indication消息携带失败原因值“UE not responding”或者“Unable to page UE”而失败次数达到配置的“DDN失败次数”时，系统启动DDN抑制功能。 |
| MONITORTIMES | DDN失败次数 | 可选必选说明：该参数在"SUPPSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置DDN失败次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~3000，单位是次。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNSUPPRESSION查询当前参数配置值。<br>配置原则：<br>当用户在配置的“监控时长(分)”内，DDN由于收到MME发送Downlink Data Notification Failure Indication消息携带失败原因值“UE not responding”或者“Unable to page UE”而失败次数达到配置的“DDN失败次数”时，系统启动DDN抑制功能。 |
| SUPPTIMER | 抑制时长(分) | 可选必选说明：该参数在"SUPPSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于配置DDN抑制的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNSUPPRESSION查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [DDN抑制功能配置（DDNSUPPRESSION）](configobject/UNC/20.15.2/DDNSUPPRESSION.md)

## 使用实例

设置使能开启DDN抑制功能，在DDN流程失败后的30分钟内，如果DDN失败次数达到10次，则启动DDN抑制，抑制时长20分钟：

```
SET DDNSUPPRESSION: SUPPSW=ENABLE, MONITORTIMER=30, MONITORTIMES=10, SUPPTIMER=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置DDN抑制功能（SET-DDNSUPPRESSION）_92686816.md`
