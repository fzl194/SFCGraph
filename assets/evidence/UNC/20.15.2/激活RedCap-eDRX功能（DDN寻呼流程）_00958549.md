# 激活RedCap eDRX功能（DDN寻呼流程）

- [操作场景](#ZH-CN_OPI_0000001600958549__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001600958549__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001600958549__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001600958549__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001600958549)

本操作指导介绍在5G eDRX模式时，UE不在寻呼窗口时的DDN寻呼流程。

> **说明**
> 适用于SMF。

## [必备事项](#ZH-CN_OPI_0000001600958549)

前提条件

- 请仔细阅读[WSFD-990005 支持5G eDRX功能特性概述](WSFD-990005 支持RedCap eDRX功能特性概述_50693596.md)。
- 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/设置全局终端接入eDRX模式属性（SET GLBEDRXATTR）_82741713.md) | 支持eDRX模式开关 | ENABLE | 固定取值 | 当eDRX模式开关关闭时，请确保AMF上已经没有eDRX用户，否则存量eDRX用户的下行数据包，可能会被丢弃。 |
| [**SET GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/设置全局终端接入eDRX模式属性（SET GLBEDRXATTR）_82741713.md) | 下行包缓存数获取优先级 | DLBUFFPKTCNT | 固定取值 | 无特殊情况，保持初始值。 |
| [**SET GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/设置全局终端接入eDRX模式属性（SET GLBEDRXATTR）_82741713.md) | 下行包缓存数 | 10 | 固定取值 | 无特殊情况，保持初始值。 |
| [**SET GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/设置全局终端接入eDRX模式属性（SET GLBEDRXATTR）_82741713.md) | 下行包缓存额外时长 | 10 | 固定取值 | 无特殊情况，保持初始值。 |
| [**ADD APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/增加APN的终端接入eDRX模式属性（ADD APNEDRXATTR）_32381428.md) | APN名称 | test | 固定取值 | - |
| [**ADD APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/增加APN的终端接入eDRX模式属性（ADD APNEDRXATTR）_32381428.md) | 支持eDRX模式开关 | ENABLE | 本端规划 | - 当eDRX模式开关关闭时，请确保AMF上已经没有eDRX用户，否则存量eDRX用户的下行数据包，可能会被丢弃。<br>- 此参数优先级大于**SET GLBEDRXATTR**。根据不同APN的主要业务模型，可以针对性地配置下行包缓存数获取优先级和下行包缓存数。例如，物流监控类业务，建议优先使用本地签约数据，配置本地缓存最大包数为10。<br>- 若有此类APN定制的业务需求，**EDRXSW**需配置为“ENABLE“。若无针对性的业务需求，此参数也可配置为“INHERIT“，继承全局下行包缓存参数。 |
| [**ADD APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/增加APN的终端接入eDRX模式属性（ADD APNEDRXATTR）_32381428.md) | 下行包缓存数获取优先级 | DLBUFFPKTCNT | 全网规划 | - 当eDRX模式开关关闭时，请确保AMF上已经没有eDRX用户，否则存量eDRX用户的下行数据包，可能会被丢弃。<br>- 此参数优先级大于**SET GLBEDRXATTR**。根据不同APN的主要业务模型，可以针对性地配置下行包缓存数获取优先级和下行包缓存数。例如，物流监控类业务，建议优先使用本地签约数据，配置本地缓存最大包数为10。<br>- 若有此类APN定制的业务需求，**EDRXSW**需配置为“ENABLE“。若无针对性的业务需求，此参数也可配置为“INHERIT“，继承全局下行包缓存参数。 |
| [**ADD APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/增加APN的终端接入eDRX模式属性（ADD APNEDRXATTR）_32381428.md) | 下行包缓存数 | 10 | 全网规划 | - 当eDRX模式开关关闭时，请确保AMF上已经没有eDRX用户，否则存量eDRX用户的下行数据包，可能会被丢弃。<br>- 此参数优先级大于**SET GLBEDRXATTR**。根据不同APN的主要业务模型，可以针对性地配置下行包缓存数获取优先级和下行包缓存数。例如，物流监控类业务，建议优先使用本地签约数据，配置本地缓存最大包数为10。<br>- 若有此类APN定制的业务需求，**EDRXSW**需配置为“ENABLE“。若无针对性的业务需求，此参数也可配置为“INHERIT“，继承全局下行包缓存参数。 |
| [**ADD APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/增加APN的终端接入eDRX模式属性（ADD APNEDRXATTR）_32381428.md) | 下行包缓存额外时长 | 10 | 固定取值 | - |
| [**SET PFCPCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md) | 是否支持BAR信元 | SUPPORT | 固定取值 | - |

## [操作步骤](#ZH-CN_OPI_0000001600958549)

1. 进入 “MML命令行-UNC” 窗口。
2. （可选）以全局粒度配置下行包缓存参数：
  [**SET GLBEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/设置全局终端接入eDRX模式属性（SET GLBEDRXATTR）_82741713.md)
3. 以APN为粒度配置下行包缓存参数：
  [**ADD APNEDRXATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/eDRX模式管理/增加APN的终端接入eDRX模式属性（ADD APNEDRXATTR）_32381428.md)
4. 配置PFCP接口兼容性：
  [**SET PFCPCMPT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/PFCP接口兼容性/设置PFCP接口兼容性参数（SET PFCPCMPT）_96243192.md)
5. 打开本功能的License配置开关：
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)

## [任务示例](#ZH-CN_OPI_0000001600958549)

任务描述

支持eDRX功能的UE接入核心网后，发起DDN寻呼流程，且UE不在寻呼窗口。SMF基于APN”test”配置下行包缓存参数。

脚本

//打开SMF上的全局eDRX开关，配置SMF优先获取本地配置的下行包缓存数，下行包缓存数为10，并额外增加20的下行包缓存时长。

```
SET GLBEDRXATTR: EDRXSW=ENABLE, PKTCNTPRIORITY=DLBUFFPKTCNT, DLBUFFPKTCNT=10, EXTDLBUFFTIME=20; 
ADD APNEDRXATTR: APN="test", EDRXSW=ENABLE, PKTCNTPRIORITY=DLBUFFPKTCNT, DLBUFFPKTCNT=10, EXTDLBUFFTIME=20;
```

//配置PFCP接口兼容性参数。

```
SET PFCPCMPT: BAR=SUPPORT;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2RCEDRXSM01", SWITCH=ENABLE;
```
