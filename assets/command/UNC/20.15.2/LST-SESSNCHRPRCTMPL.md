---
id: UNC@20.15.2@MMLCommand@LST SESSNCHRPRCTMPL
type: MMLCommand
name: LST SESSNCHRPRCTMPL（查询会话CHR流程控制模板）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SESSNCHRPRCTMPL
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- CHR管理
- 会话CHR流程模板配置
status: active
---

# LST SESSNCHRPRCTMPL（查询会话CHR流程控制模板）

## 功能

**适用NF：PGW-C、SGW-C、SMF、GGSN**

该命令用于查询会话CHR流程控制模板。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMPLIDX | 流程模板索引 | 可选必选说明：可选参数<br>参数含义：流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SESSNCHRPRCTMPL]] · 会话CHR流程控制模板（SESSNCHRPRCTMPL）

## 使用实例

查询系统配置的所有会话CHR流程控制模板。

```
LST SESSNCHRPRCTMPL:;
RETCODE = 0  操作成功

结果如下
--------
流程模板索引  NG会话CHR成功流程上报选项  NG会话CHR失败流程上报选项                                                                                                                                                                                                                                                       GUL CHR成功流程上报选项  GUL CHR失败流程上报选项                                                                                                                                                                                                                                                                                                                                                                                                                               SMF成功信令事件上报选项  SMF失败信令事件上报选项  扩展CHR成功流程上报选项  扩展CHR失败流程上报选项                                                                                                                                                                                           

0             NULL                       Other&UE Initial Create SM Context&PDU Session Modification&PDU Session Release&Activation User Plane&Deactivation User Plane&Registration Update&Xn HO&N2 HO&Inter System Change&N4 Report&AMF Event Notification&RESERVED1&RESERVED2&RESERVED3&RESERVED4&RESERVED5&RESERVED6  NULL                     Create Session&Delete Session&Modify Bearer&Create Bearer&Update Bearer&Delete Bearer&Bearer Resource Command&Modify Bearer Command&Delete Bearer Command&Release Access Bearers&Create Indirect Data Forwarding Tunnel&Delete Indirect Data Forwarding Tunnel&Suspend Notification&Resume Notification&Downlink Data Notification&Change Notification&PGW Downlink Triggered Notification&PGW Restart Notification&Create PDP&Update PDP&Delete PDP  NULL                     NULL                     NULL                     Gy Re-Auth&Gy Abort-Session&Gy Credit-Control&Gx Credit-Control&Gx Re-Auth&Gx Abort-Session&Gx ADC Credit-Control&Authentication Access&Radius Accounting Start Stop&Radius Accounting Interim&Radius Disconnect  
1             NULL                       Other&UE Initial Create SM Context&PDU Session Modification&PDU Session Release&Activation User Plane&Deactivation User Plane&Registration Update&Xn HO&N2 HO&Inter System Change&N4 Report&AMF Event Notification&RESERVED1&RESERVED2&RESERVED3&RESERVED4&RESERVED5&RESERVED6  NULL                     Create Session&Delete Session&Modify Bearer&Create Bearer&Update Bearer&Delete Bearer&Bearer Resource Command&Modify Bearer Command&Delete Bearer Command&Release Access Bearers&Create Indirect Data Forwarding Tunnel&Delete Indirect Data Forwarding Tunnel&Suspend Notification&Resume Notification&Downlink Data Notification&Change Notification&PGW Downlink Triggered Notification&PGW Restart Notification&Create PDP&Update PDP&Delete PDP  NULL                     NULL                     NULL                     Gy Re-Auth&Gy Abort-Session&Gy Credit-Control&Gx Credit-Control&Gx Re-Auth&Gx Abort-Session&Gx ADC Credit-Control&Authentication Access&Radius Accounting Start Stop&Radius Accounting Interim&Radius Disconnect  
(结果个数 = 2)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SESSNCHRPRCTMPL.md`
