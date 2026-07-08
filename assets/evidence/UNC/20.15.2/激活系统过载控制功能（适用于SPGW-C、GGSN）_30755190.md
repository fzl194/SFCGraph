# 激活系统过载控制功能（适用于SPGW-C、GGSN）

- [操作场景](#ZH-CN_OPI_0230755190__1.3.1)
- [必备事项](#ZH-CN_OPI_0230755190__1.3.2)
- [操作步骤](#ZH-CN_OPI_0230755190__1.3.3)
- [任务示例](#ZH-CN_OPI_0230755190__1.3.4)

## [操作场景](#ZH-CN_OPI_0230755190)

本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。

在系统过载时， UNC 通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。

> **说明**
> 适用于 GGSN、 SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0230755190)

前提条件

请仔细阅读 [WSFD-010801系统过载控制功能特性概述（适用于SPGW-C、GGSN）](WSFD-010801系统过载控制功能特性概述（适用于SPGW-C、GGSN）_30755109.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **[**SET FCSWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/服务通信管理/流控管理/设置流控开关（SET FCSWITCH）_09587940.md)** | 开关（SWITCH） | ENABLE | 本端规划 | 设置基于CPU过载的流控开关。 |
| [**SET APNACCESSWAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN接入速率/设置APN接入速率（SET APNACCESSWAL）_09652087.md) | APN名称（APN） | apn-test | 本端规划 | 设置APN下用户的接入速率。 |
| [**SET APNACCESSWAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN接入速率/设置APN接入速率（SET APNACCESSWAL）_09652087.md) | 用户的接入速率（WALNUMBER） | 30 | 本端规划 | 设置APN下用户的接入速率。 |
| **[SET GTPCFIXEDFC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/GTP-C接口配置管理/GTP-C固定速率流控管理/设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）_35636465.md)** | 流控消息类型（MSGTYPE） | REGISTER | 全网规划 | 设置GTPC接口上指定消息类型固定速率流控信息。 |
| **[SET GTPCFIXEDFC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/GTP-C接口配置管理/GTP-C固定速率流控管理/设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）_35636465.md)** | 固定速率流控开关（FCSWITCH） | On | 全网规划 | 设置GTPC接口上指定消息类型固定速率流控信息。 |
| **[SET GTPCFIXEDFC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/GTP-C接口配置管理/GTP-C固定速率流控管理/设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）_35636465.md)** | 流控速率门限(个/秒)（THRESHOLD） | 4000 | 全网规划 | 设置GTPC接口上指定消息类型固定速率流控信息。 |
| **[SET OVERLOADCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/信令抑制/设置信令抑制功能开关以及老化定时器时长（SET OVERLOADCTRL）_82122531.md)** | 信令抑制功能开关（CTRLENABLE） | ENABLE | 本端规划 | 设置信令抑制功能开关以及老化定时器时长。 |
| **[SET OVERLOADCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/信令抑制/设置信令抑制功能开关以及老化定时器时长（SET OVERLOADCTRL）_82122531.md)** | 信令抑制记录的老化定时器时长(秒)（AGINGTIME） | 34 | 本端规划 | 设置信令抑制功能开关以及老化定时器时长。 |
| **[SET OVERLOADCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/信令抑制/设置信令抑制功能开关以及老化定时器时长（SET OVERLOADCTRL）_82122531.md)** | OCS CCR-I去活是否开启信令抑制（SRVTRIGCCRI） | ENABLE | 本端规划 | 设置信令抑制功能开关以及老化定时器时长。 |
| **[SET OVERLOADCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/信令抑制/设置信令抑制功能开关以及老化定时器时长（SET OVERLOADCTRL）_82122531.md)** | ACCT去活是否开启信令抑制（SRVTRIGACCT） | ENABLE | 本端规划 | 设置信令抑制功能开关以及老化定时器时长。 |

## [操作步骤](#ZH-CN_OPI_0230755190)

1. 进入 “MML命令行-UNC” 窗口。
2. 设置基于CPU过载流控开关。
  **[SET FCSWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/服务通信管理/流控管理/设置流控开关（SET FCSWITCH）_09587940.md)**
3. 设置APN下用户接入速率。
  [**SET APNACCESSWAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN接入速率/设置APN接入速率（SET APNACCESSWAL）_09652087.md)
4. 设置GTPC接口指定消息类型固定流控速率。
  **[SET GTPCFIXEDFC](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/GTP-C接口配置管理/GTP-C固定速率流控管理/设置指定消息类型固定速率流控信息（SET GTPCFIXEDFC）_35636465.md)**
5. 设置信令抑制功能开关以及老化定时器时长。
  **[SET OVERLOADCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/流控管理/信令抑制/设置信令抑制功能开关以及老化定时器时长（SET OVERLOADCTRL）_82122531.md)**

## [任务示例](#ZH-CN_OPI_0230755190)

任务描述

系统中度或者重度过载时，启动自保流控。

脚本

//设置基于CPU过载流控开关。

```
SET FCSWITCH: SWITCH=ENABLE;
```

//设置APN接入速率。

```
SET APNACCESSWAL
:APN="huawei.com",WALNUMBER=300;
```

//设置GTPC接口接收消息流控功能。

```
SET GTPCFIXEDFC:MSGTYPE=CREATESESSIONREQUEST,FCSWITCH=ON,THRESHOLD=4000;
```

//设置信令抑制功能开关以及老化定时器时长。

```
SET OVERLOADCTRL: CTRLENABLE=ENABLE,AGINGTIME=34,SRVTRIGCCRI=ENABLE,SRVTRIGACCT=ENABLE;
```
