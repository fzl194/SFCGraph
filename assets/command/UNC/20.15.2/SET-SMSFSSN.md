---
id: UNC@20.15.2@MMLCommand@SET SMSFSSN
type: MMLCommand
name: SET SMSFSSN（设置SMSF本局SSN号）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSFSSN
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SMSFOPC本局SSN号
status: active
---

# SET SMSFSSN（设置SMSF本局SSN号）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF对接SMSC网元时，SCCP层主叫地址中携带的SSN号。

## 注意事项

- 该命令执行后立即生效。
- 该命令目前适用于SMSF和SMSC短信中心对接时使用。在修改该命令前请通过 [**ADD SCCPSSN**](../../SCCP管理/SCCP子系统/增加SCCP子系统(ADD SCCPSSN)_26306144.md) 命令配置本局信令点需要配置的子系统号。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSN | 子系统号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统号。<br>数据来源：本端规划<br>取值范围：<br>- “VLR(7)”<br>- “MSC(8)”<br>- “SGSN(149)”<br>默认值：无<br>初始系统默认值为“SGSN(149)”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFSSN]] · SMSF本局SSN号（SMSFSSN）

## 使用实例

设置SMSFSSN号为“MSC”。

```
SET SMSFSSN: SSN=MSC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SMSFSSN.md`
