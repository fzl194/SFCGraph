# 激活SMS over GPRS/EDGE/WCDMA

- [操作场景](#ZH-CN_OPI_0184683740__1.3.1)
- [必备事项](#ZH-CN_OPI_0184683740__1.3.2)
- [操作流程](#ZH-CN_OPI_0184683740__1.3.3)
- [操作步骤](#ZH-CN_OPI_0184683740__1.3.4)
- [任务示例](#ZH-CN_OPI_0184683740__1.3.5)

## [操作场景](#ZH-CN_OPI_0184683740)

本操作指导介绍在运行网络中激活SMS over GPRS/EDGE/WCDMA特性的操作过程。

SMS over GPRS/EDGE/WCDMA是指SGSN通过分组域为移动用户提供收发短消息的业务。SMS（Short Message Service）是电信业务的一种，它允许用户通过SMC（Short Message Center）发送和接收字符信息。SMS可以由电路域或分组域进行承载。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0184683740)

前提条件

- 请仔细阅读[WSFD-106202 SMS over GPRS/EDGE/WCDMA特性概述](特性概述_85247546.md)。
- 完成加载License。
- 用户在HLR中已经签约PS短消息业务。
- 与UNC相连的CG的参数配置完成，可以在MML命令行-UNC窗口上执行命令 **[**LST CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/查询CG配置参数(LST CHGCG)_26145376.md)** 确认相关配置已经完成。
- MS设置通过PS域发短消息。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2SMS02 | 本端规划 | 打开本特性的License配置开关。 |
| [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 移动国家码（MCC） | 123 | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 移动网号（MNC） | 00 | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 国家码（CC） | 86 | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许SM业务（SM） | YES | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许SMS业务（SMS） | YES | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 是否允许纠正短消息中心（SMSCR） | YES | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md) | 纠正后的短消息中心（SMSCT） | 8613951996 | 全网规划 | 增加非漫游用户短信息归属PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 移动国家码（MCC） | 123 | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 移动网号（MNC） | 01 | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 匹配IMSI（MATCHIMSI） | 1234 | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 国家码（CC） | 86 | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 是否允许SMS业务（SMS） | YES | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 是否允许纠正短消息中心（SMSCR） | YES | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md) | 纠正后的短消息中心（SMSCT） | 8613951996 | 全网规划 | 增加漫游用户短信息互联PLMN配置信息。 |
| [**ADD SMSCBLACKLIST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/SMSC黑名单/增加SMSC黑名单记录(ADD SMSCBLACKLIST)_72225405.md) | SMSC地址（SMSCADDR） | 8613951701 | 全网规划 | 增加SMSC黑名单记录。 |
| [**ADD SMSCCONVERT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/SMSC转换/增加SMSC转换配置记录(ADD SMSCCONVERT)_72225407.md) | 请求SMSC地址（REQADDR） | 8613951702 | 全网规划 | 增加SMSC转换配置记录。 |
| [**ADD SMSCCONVERT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/SMSC转换/增加SMSC转换配置记录(ADD SMSCCONVERT)_72225407.md) | 转换SMSC地址（CORRADDR） | 8613951996 | 全网规划 | 增加SMSC转换配置记录。 |
| [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | CG的IPV4地址（IP） | 10.10.171.9 | 全网规划 | 增加一个CG。 |
| [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | GTP承载协议（PRO） | UDP | 全网规划 | 增加一个CG。 |
| [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | CG协议版本（CGR） | R6 | 全网规划 | 增加一个CG。 |
| [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | 缺省CG（DEFAULTCG） | YES | 全网规划 | 增加一个CG。 |
| [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | 优先级（GRD） | 0 | 全网规划 | 增加一个CG。 |
| [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | CG名（CGN） | abc | 全网规划 | 增加一个CG。 |
| [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 计费属性（CC） | NORMAL | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
| [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 生成S-SMO-CDR（SMOP） | YES | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
| [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | 生成S-SMT-CDR（SMTP） | YES | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
| [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md) | CG的IPv4地址（CGIP） | 10.10.171.9 | 全网规划 | 开启始发SMS和终止SMS计费功能。 |
| [**SET SMS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/短消息配置/设置SMS配置信息(SET SMS)_72345329.md) | 短消息最大试发次数（SMSMRT） | AFTERCORRECT | 全网规划 | 设置SMS配置信息。 |

## [操作流程](#ZH-CN_OPI_0184683740)

激活SMS over GPRS/EDGE/WCDMA操作流程如 [图1 激活SMS over GPRS/EDGE/WCDMA操作流程](#ZH-CN_OPI_0184683740__zh-cn_opi_0130429347_fig_01) 所示。

**图1** 激活SMS over GPRS/EDGE/WCDMA操作流程

<br>

![](激活SMS over GPRS_EDGE_WCDMA_84683740.assets/zh-cn_image_0207340555_2.png)

## [操作步骤](#ZH-CN_OPI_0184683740)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 增加短消息PLMN配置信息。
    - 增加非漫游用户短信息归属PLMN配置信息。
      [**ADD HPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/归属网络运营商管理/MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)
    - 增加漫游用户短信息互联PLMN配置信息。
      [**ADD CONNECTPLMN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/互联PLMN管理/增加互联PLMN(ADD CONNECTPLMN)_26305852.md)
4. **可选：**增加SMSC黑名单记录。
  [**ADD SMSCBLACKLIST**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/SMSC黑名单/增加SMSC黑名单记录(ADD SMSCBLACKLIST)_72225405.md)
  > **说明**
  > 为了禁止手机使用未经过授权的短消息服务中心进行短消息业务，可以将未经授权的短消息服务中心加入黑名单中。
5. **可选：**增加SMSC转换配置记录。
  [**ADD SMSCCONVERT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/SMSC转换/增加SMSC转换配置记录(ADD SMSCCONVERT)_72225407.md)
  > **说明**
  > 为避免HPLMN用户设置错误导致短消息业务失败，可以配置转换记录。
6. 配置短消息计费。
    a. 开启始发SMS和终止SMS计费功能。
      [**SET CHGCHAR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)
      > **说明**
      > - 参数“SMOP”（生成S-SMO-CDR）选择“YES”。
      > - 参数“SMTP”（生成S-SMT-CDR）选择“YES”。
    b. **可选：**设置SMS配置信息。
      [**SET SMS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/业务安全管理/短消息/短消息配置/设置SMS配置信息(SET SMS)_72345329.md)
7. 配置到SMC的数据，具体过程请参见 [配置到SMC的数据](../../../../../初始配置/UNC初始配置与调测/组网对接配置/配置AMF&MME&SGSN/配置SGSN/配置到SMC的数据_82467132.md) 。

## [任务示例](#ZH-CN_OPI_0184683740)

任务描述

激活以下PLMN用户的短消息业务：HPLMN 12300，国家码为86；互联PLMN 12301，附加的匹配IMSI为1234，国家码为86。

增加一条SMSC黑名单记录：SMC地址为8613951701。增加一条SMSC转换记录：请求SMSC地址为8613951702，转换SMSC地址为8613951996。

对用户的始发SMS和终止SMS进行计费，CG的IP地址为10.10.171.9。设置S-SMO-CDR中记录的短消息中心为纠正后的短消息中心。

脚本

//设置本特性License开关为“ENABLE”。

```
SET LICENSESWITCH: LICITEM="LKV2SMS02", SWITCH=ENABLE;
```

//激活以下PLMN用户的短消息业务：HPLMN 12300，国家码为86；互联PLMN 12301，附加的匹配IMSI为1234，国家码为86。

```
ADD HPLMN: MCC="123", MNC="00", CC="86", SM=YES, SMS=YES, SMSCR=YES, SMSCT="8613951996";
ADD CONNECTPLMN: MCC="123", MNC="01", MATCHIMSI="1234", CC="86", SMS=YES, SMSCR=YES, SMSCT="8613951996";
```

//可选：增加一条SMSC黑名单记录，SMSC地址为8613951701。

```
ADD SMSCBLACKLIST: SMSCADDR="8613951701";
```

//可选：增加SMSC转换配置记录。

```
ADD SMSCCONVERT: REQADDR="8613951702", CORRADDR="8613951996";
```

//增加一个CG，IP地址为"10.10.171.9"，等级为0，GTP承载协议为UDP，CG协议版本为R6，CG名为"abc"。

```
ADD CHGCG: IP="10.10.171.9", PRO=UDP, CGR=R6, DEFAULTCG=YES, GRD=0, CGN="abc";
```

//对用户的始发SMS和终止SMS进行计费：属性设为“NORMAL”，生成S-SMO-CDR和S-SMT-CDR，CG的IP地址设为“10.10.171.9”。

```
SET CHGCHAR: CC=NORMAL, SMOP=YES, SMTP=YES, CGIP="10.10.171.9";
```

//可选：设置S-SMO-CDR中记录的短消息中心为纠正后的短消息中心。

```
SET SMS: RSMSCT=AFTERCORRECT;
```
