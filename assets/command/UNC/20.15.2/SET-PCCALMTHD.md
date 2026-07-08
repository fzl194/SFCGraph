---
id: UNC@20.15.2@MMLCommand@SET PCCALMTHD
type: MMLCommand
name: SET PCCALMTHD（设置PCC告警阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCCALMTHD
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
- 告警管理
- PCC告警门限
status: active
---

# SET PCCALMTHD（设置PCC告警阈值）

## 功能

**适用NF：PGW-C、SMF**

此命令支持Gx接口消息交互超时告警，对于PCRF由于性能问题回响应慢，或者PCRF的应用层发生故障不回响应的情况，可以进行更好的监控。使用该命令可以控制连续超时的CCA消息数累加到门限值时触发告警，连续收到CCA消息数累加到门限值时恢复告警。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PCRFALMVAL | PCRFALMRSTVAL |
| --- | --- | --- |
| 初始值 | 0 | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFALMVAL | 应用层PCRF无响应告警阈值 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定的Gx应用层上报告警门限，表示连续超时的CCA消息数累加到门限值时触发告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：参数值为0时，表示不开启应用层上报PCRF无响应告警功能。 |
| PCRFALMRSTVAL | 应用层PCRF无响应告警恢复阈值 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定的Gx应用层恢复告警门限，表示连续收到CCA消息数累加到门限值时恢复告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCCALMTHD]] · PCC告警阈值（PCCALMTHD）

## 使用实例

为了更好得监控PCRF由于性能问题回响应慢，或者PCRF的应用层发生故障不回响应的情况，配置Gx接口消息交互超时告警的上报告警门限为100，恢复告警门限为50：

```
SET PCCALMTHD:PCRFALMVAL=100,PCRFALMRSTVAL=50;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PCCALMTHD.md`
