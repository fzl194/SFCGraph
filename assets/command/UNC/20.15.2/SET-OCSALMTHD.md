---
id: UNC@20.15.2@MMLCommand@SET OCSALMTHD
type: MMLCommand
name: SET OCSALMTHD（设置OCS告警阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OCSALMTHD
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
- 计费管理
- 告警管理
- OCS告警阈值
status: active
---

# SET OCSALMTHD（设置OCS告警阈值）

## 功能

**适用NF：PGW-C、SMF**

该命令用于设置OCS告警相关配置。包括OCS链路告警阈值、OCS链路状态采样配置和OCS应用层告警阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CONNALMTHD | CONNALMCLRTHD | SAMPLEPERIOD | SAMPLETIMES | SAMPLEPRDNUM | APPALMTHD | APPALMCLRTHD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 50 | 80 | 5 | 12 | 15 | 0 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNALMTHD | OCS链路告警产生阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定“ALM-81023 OCS无响应”链路告警产生阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| CONNALMCLRTHD | OCS链路告警恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于指定“ALM-81023 OCS无响应”链路告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| SAMPLEPERIOD | OCS链路状态采样间隔 （秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS链路状态采样间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：无<br>配置原则：无 |
| SAMPLETIMES | OCS链路状态采样次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS链路状态采样次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～20。<br>默认值：无<br>配置原则：无 |
| SAMPLEPRDNUM | 连续检测周期数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定连续检测周期数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，5～30。<br>默认值：无<br>配置原则：无 |
| APPALMTHD | OCS应用层告警产生阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于控制CPU内连续超时的CCA消息数累加到多少时触发“ALM-81023 OCS无响应”的应用层告警。门限为零，表示无效值，即OCS无响应的应用层告警机制不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| APPALMCLRTHD | OCS应用层告警恢复阈值 | 可选必选说明：可选参数<br>参数含义：现网中经常由于OCS设备闪断，导致频繁上报告警，为防止告警过多，使用该参数进行控制。该参数用于CPU内控制连续收到CCA消息数累加到多少时恢复“ALM-81023 OCS无响应”的应用层告警。门限为零，表示收到CCA消息就立即恢复OCS无响应的应用层告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSALMTHD]] · OCS告警阈值（OCSALMTHD）

## 使用实例

配置OCS无响应的应用层告警产生阈值为20，告警恢复阈值为10：

```
SET OCSALMTHD:APPALMTHD=20,APPALMCLRTHD=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OCSALMTHD.md`
