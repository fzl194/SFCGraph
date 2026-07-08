# 激活 VoLTE基础语音业务 （适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0167930995__1.3.1)
- [必备事项](#ZH-CN_OPI_0167930995__1.3.2)
- [操作步骤](#ZH-CN_OPI_0167930995__1.3.3)
- [任务示例](#ZH-CN_OPI_0167930995__1.3.4)

## [操作场景](#ZH-CN_OPI_0167930995)

本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程。

## [必备事项](#ZH-CN_OPI_0167930995)

前提条件

- 请仔细阅读[WSFD-102001 VoLTE基础语音业务特性概述](特性概述_68374441.md)
- 本特性受License控制，请先完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md) | IMS开关（IMSSWITCH） | ENABLE | 全网规划 | 开启IMS功能开关。<br>业务处理过程中优先应用APN下的设置，只有当APN下配置为<br>“INHERIT”<br>时才应用全局下的设置。 |
| [**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md) | 信令空口增强开关（SIGNALRADIOPRE） | ENABLE | 全网规划 | 用于开启IMS信令空口增强功能。 |
| [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md) | 携带EBI（EBI） | Enable(使能) | 与对端协商 | 配置支持在Downlink Data Notification消息中携带EBI信元。<br>协议中Downlink Data Notification消息中的Bearer ID为可选信元，为确保MME能够通过Downlink Data Notification消息中的Bearer ID识别VoLTE语音被叫，需要配置此功能。 |
| [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md) | EBI值（EBIVALUE） | DEFAULTBEARER(缺省承载) | 与对端协商 | 配置支持在Downlink Data Notification消息中携带EBI信元。<br>协议中Downlink Data Notification消息中的Bearer ID为可选信元，为确保MME能够通过Downlink Data Notification消息中的Bearer ID识别VoLTE语音被叫，需要配置此功能。 |
| [**SET CONFCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话流程控制管理/会话流程冲突控制/设置冲突控制参数（SET CONFCTRL）_09651408.md) | EPS消息缓存重发的次数（EPSRETRYTIMES） | 3 | 本端规划 | 配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数。次数达到设置值时，消息将被丢弃。<br>说明：EPSRETRYTIMES建议默认值为3。 |
| [**SET CONFCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话流程控制管理/会话流程冲突控制/设置冲突控制参数（SET CONFCTRL）_09651408.md) | EPS消息缓存重发的时间间隔(s)（EPSTIMEOUT） | 2 | 本端规划 | 配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。 |

## [操作步骤](#ZH-CN_OPI_0167930995)

打开License配置开关。

1. 进入 “MML命令行-UNC” 窗口。
2. 打开License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

3. 开启全局缺省PCC开关。
  [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
4. 开启APN下的PCC开关。
  [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
5. 将指定的PCRF分组及号段信息绑定到指定APN。
  [**ADD PCRFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)

配置基于APN的IMS业务

6. 配置IMS使能开关和IMS信令空口增强开关，绑定到指定APN实例下。
  [**SET APNIMSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/IMS业务功能/基于APN的IMS属性/设置APN的IMS属性（SET APNIMSATTR）_33845576.md)
7. 配置支持在Downlink Data Notification消息中携带EBI信元。
  [**SET DDNATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/DDN消息携带的属性/设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）_09651485.md)
8. 配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数；配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。
  [**SET CONFCTRL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话流程控制管理/会话流程冲突控制/设置冲突控制参数（SET CONFCTRL）_09651408.md)

## [任务示例](#ZH-CN_OPI_0167930995)

任务描述

部署VoLTE基础语音业务。

脚本

**打开License开关**

// 进入 “MML命令行-UNC” 窗口。

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3W9IMSA12", SWITCH=ENABLE;
```

//开启全局缺省PCC开关。

```
SET PCCFUNC: HOMEPCCSWITCH=ENABLE;
```

//开启APN下的PCC开关。

```
SET APNPCCFUNC: APN="ims", HOMEPCCSWITCH=ENABLE;
```

//将指定的PCRF分组及号段信息绑定到指定APN。 参数 PCRFGRPNAME使用 **[ADD PCRFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)** 命令配置生成。执行该命令前请先通过 **[LST PCRFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/查询PCRF组（LST PCRFGROUP）_09897093.md)** 查询当前是否已添加该PCRF Group。 根据查询结果，选择是否配置该参数。

```
ADD PCRFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, PCRFGRPNAME="aaa";
```

**配置基于APN的IMS业务**

//配置IMS使能开关和IMS信令空口增强开关，绑定到指定APN实例下。

```
SET APNIMSATTR: APN="ims", IMSSWITCH=ENABLE, SIGNALRADIOPRE=ENABLE;
```

//配置支持在Downlink Data Notification消息中携带EBI信元。

```
SET DDNATTR: EBI=Enable, EBIVALUE=DefaultBearer;
```

//配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数；配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。

```
SET CONFCTRL: EPSRETRYTIMES=3, EPSTIMEOUT=2;
```
