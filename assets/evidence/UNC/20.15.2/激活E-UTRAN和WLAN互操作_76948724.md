# 激活E-UTRAN和WLAN互操作

- [操作场景](#ZH-CN_OPI_0276948724__1.3.1)
- [必备事项](#ZH-CN_OPI_0276948724__1.3.2)
- [操作步骤](#ZH-CN_OPI_0276948724__1.3.3)
- [任务示例](#ZH-CN_OPI_0276948724__1.3.4)

## [操作场景](#ZH-CN_OPI_0276948724)

E-UTRAN和WLAN互操作，也称作WL互操作网络，是指WL双模终端可接入EPC网络，使用基本的数据业务，并可在WLAN网络和LTE网络之间移动。部署WL互操作网络的配置同单独部署一种网络（WLAN或LTE）接入的配置基本一致。

E-UTRAN和WLAN（Wireless Local Area Network）互操作指用户可以在3GPP LTE网络和非3GPP WLAN间进行切换，而无需中断业务。

> **说明**
> 适用于SGW-C、PGW-C。

具体组网请参见E-UTRAN和WLAN互操作的 [网络结构](特性概述_76948718.md#ZH-CN_CONCEPT_0276948718__section2049984219491) 。

## [必备事项](#ZH-CN_OPI_0276948724)

前提条件

- 请仔细阅读[WSFD-201301 E-UTRAN和WLAN互操作特性概述](特性概述_76948718.md)。
- 操作员了解本特性组网涉及的各类接口并已完成组网中涉及的各接口配置。配置S6b接口时如果PGW-C与3GPP AAA Server直连，请参考WSFD-010102 Untrusted Non-3GPP网络用户接入中的[配置到3GPP AAA Server的数据](../../基本接入功能/WSFD-010102 Untrusted Non-3GPP网络用户接入/激活Untrusted Non-3GPP网络用户接入功能/配置到3GPP AAA Server的数据_80511835.md)；PGW-C通过DRA与3GPP AAA Server相连请参考WSFD-011134 S6b over DRA中的[激活S6b over DRA（静态路由+BFD组网）](../../逻辑接口功能/WSFD-011134 S6b over DRA/激活S6b over DRA（静态路由+BFD组网）_75821602.md)。
- 已完成特性License“82209418 LKV3WPHOLW11 E-UTRAN和WLAN互操作”加载，可以通过**[DSP LICENSE](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET GLOBALWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/全局E-UTRAN和WLAN互操作控制/设置全局E-UTRAN和WLAN互操作控制属性（SET GLOBALWIFILTEHO）_35962940.md) | 忽略消息中HI开关(IGNOREHIFLAG) | ENABLE | 本端规划 | Create Session Request消息已携带HI标记位但PGW-C上未选到合适上下文时，按照新激活处理。 |
| [**SET GLOBALWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/全局E-UTRAN和WLAN互操作控制/设置全局E-UTRAN和WLAN互操作控制属性（SET GLOBALWIFILTEHO）_35962940.md) | S2b接口切换开关(S2BHANDOVER) | ENABLE | 本端规划 | Create Session Request消息未携带HI标记位但PGW-C上有符合切换条件的上下文时，E-UTRAN和WLAN相关S2b接口的互操作按照切换处理。 |
| [**ADD APNWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/基于APN的E-UTRAN和WLAN互操作控制/增加基于APN的E-UTRAN和WLAN互操作控制属性（ADD APNWIFILTEHO）_82122523.md) | APN 名称(APN) | ims | 本端规划 | 增加基于APN的E-UTRAN和WLAN互操作控制属性。 |
| [**ADD APNWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/基于APN的E-UTRAN和WLAN互操作控制/增加基于APN的E-UTRAN和WLAN互操作控制属性（ADD APNWIFILTEHO）_82122523.md) | S2b接口切换开关(S2BHANDOVER) | INHERIT | 本端规划 | 增加基于APN的E-UTRAN和WLAN互操作控制属性。 |
| **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | 数据类型（DT） | Bit | 本端规划 | BIT719 该软参用于控制用户在non-3GPP和3GPP网络间切换时，是否允许双栈和单栈之间进行切换。 |
| **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | Bit索引（BITNUM） | 719 | 本端规划 | BIT719 该软参用于控制用户在non-3GPP和3GPP网络间切换时，是否允许双栈和单栈之间进行切换。 |
| **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | Bit值（BITVALUE） | 1 | 本端规划 | BIT719 该软参用于控制用户在non-3GPP和3GPP网络间切换时，是否允许双栈和单栈之间进行切换。 |
| **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)** | 已存在PDU会话建立使能开关（EXTPDUEST） | SUPPORT | 全网规划 | AMF支持从ePDG向5GS的PDU切换。 |

## [操作步骤](#ZH-CN_OPI_0276948724)

以下步骤在SMF上执行

1. 进入 “MML命令行-UNC” 窗口。
2. 配置用户在non-3GPP和3GPP网络间切换时，允许双栈与单栈之间进行切换。
  **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)**
3. 配置E-UTRAN和WLAN互操作控制属性。
    - 设置全局E-UTRAN和WLAN互操作控制属性。
      [**SET GLOBALWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/全局E-UTRAN和WLAN互操作控制/设置全局E-UTRAN和WLAN互操作控制属性（SET GLOBALWIFILTEHO）_35962940.md)
    - 增加基于APN的E-UTRAN和WLAN互操作控制属性。
      [**ADD APNWIFILTEHO**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入控制/E-UTRAN和WLAN互操作控制/基于APN的E-UTRAN和WLAN互操作控制/增加基于APN的E-UTRAN和WLAN互操作控制属性（ADD APNWIFILTEHO）_82122523.md)
4. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

以下步骤在AMF上执行

1. 进入 “MML命令行-UNC” 窗口。
2. 配置AMF支持从ePDG向5GS的PDU切换。“已存在PDU会话建立使能开关”设置为“SUPPORT（支持）”。
  **[SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)**

## [任务示例](#ZH-CN_OPI_0276948724)

任务描述

配置E-UTRAN和WLAN互操作功能。

脚本

//以下步骤在SMF上执行。

//配置用户在non-3GPP和3GPP网络间切换时，允许双栈与单栈之间进行切换。

```
SET SMFSOFTPARA: DT=Bit, BITNUM=719, BITVALUE=1;
```

//配置E-UTRAN和WLAN互操作控制属性。

```
SET GLOBALWIFILTEHO:IGNOREHIFLAG=ENABLE, S2BHANDOVER=ENABLE; 
ADD APNWIFILTEHO:APN="ims",S2BHANDOVER=INHERIT;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WPHOLW11",SWITCH=ENABLE;
```

//以下步骤在AMF上执行。

//配置AMF支持从ePDG向5GS的PDU切换。 “已存在PDU会话建立使能开关” 设置为 “SUPPORT（支持）” 。

```
SET NGMMFUNC: EXTPDUEST=SUPPORT;
```
