# 设置SMSF本局SSN号（SET SMSFSSN）

- [命令功能](#ZH-CN_MMLREF_0279926770__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0279926770__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0279926770__1.3.3)
- [使用实例](#ZH-CN_MMLREF_0279926770__1.3.4)

## [命令功能](#ZH-CN_MMLREF_0279926770)

**适用NF：SMSF**

该命令用于设置SMSF对接SMSC网元时，SCCP层主叫地址中携带的SSN号。

## [注意事项](#ZH-CN_MMLREF_0279926770)

- 该命令执行后立即生效。
- 该命令目前适用于SMSF和SMSC短信中心对接时使用。在修改该命令前请通过 [**ADD SCCPSSN**](../../SCCP管理/SCCP子系统/增加SCCP子系统(ADD SCCPSSN)_26306144.md) 命令配置本局信令点需要配置的子系统号。

## [参数说明](#ZH-CN_MMLREF_0279926770)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSN | 子系统号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子系统号。<br>数据来源：本端规划<br>取值范围：<br>- “VLR(7)”<br>- “MSC(8)”<br>- “SGSN(149)”<br>默认值：无<br>初始系统默认值为“SGSN(149)”。 |

## [使用实例](#ZH-CN_MMLREF_0279926770)

设置SMSFSSN号为“MSC”。

```
SET SMSFSSN: SSN=MSC;
```
