# 激活 VoLTE紧急呼叫 （适用于SGW-C/PGW-C）

- [操作场景](#ZH-CN_OPI_0230394882__1.3.1)
- [必备事项](#ZH-CN_OPI_0230394882__1.3.2)
- [操作步骤](#ZH-CN_OPI_0230394882__1.3.3)
- [任务示例](#ZH-CN_OPI_0230394882__1.3.4)

## [操作场景](#ZH-CN_OPI_0230394882)

在SGW-C/PGW-C上激活VoLTE紧急呼叫功能。

紧急呼叫不需要进行鉴权，建议紧急APN的地址分配方式采用本地分配或DHCP分配，本文档以本地地址分配为例。

> **说明**
> VoLTE紧急呼叫和VoLTE普通呼叫使用不同的承载来传输，因此紧急呼叫的APN名称和相关数据需要分别规划，与普通呼叫的APN区分开。

## [必备事项](#ZH-CN_OPI_0230394882)

前提条件

- 请仔细阅读[WSFD-102101 VoLTE紧急呼叫](特性概述_70014691.md)。
- 完成加载License。
- 在MME、SGW-C、PGW-C、MSC、eNodeB等网元上完成VoLTE基本业务的数据配置。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md) | VPN实例名（VPNINSTANCE） | vpn1 | 本端规划 | 配置APN所属的VPN实例。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | APN名称（APN） | sos | 全网规划 | 使能紧急呼叫功能。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | 使能紧急呼叫功能。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 | 使能紧急呼叫功能。 |
| [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md) | 支持紧急呼叫（EMERGENCYSWITCH） | ENABLE | 本端规划 | 使能紧急呼叫功能。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 本地用户PCC功能（HOMEPCCSWITCH） | ENABLE | 本端规划 | 使能紧急APN的PCC功能。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 漫游用户PCC功能（ROAMPCCSWITCH） | INHERIT | 本端规划 | 使能紧急APN的PCC功能。 |
| [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md) | 拜访用户PCC功能（VISITPCCSWITCH） | INHERIT | 本端规划 | 使能紧急APN的PCC功能。 |
| [**ADD ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md) | 地址池名称（POOLNAME） | pool-op | 全网规划 | 添加本地地址池。 |
| [**ADD ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md) | 绑定VPN（HASVPN） | ENABLE | 本端规划 | 添加本地地址池。 |
| [**ADD ADDRPOOL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md) | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 | 添加本地地址池。 |
| [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) | 承载定时器(min)(BEARERTIMER) | 60 | 本端规划 | 配置紧急呼叫结束后释放缺省承载。<br>对于<br>“BEARERTIMER”<br>时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。 |

## [操作步骤](#ZH-CN_OPI_0230394882)

1. 进入 “MML命令行-UNC” 窗口。
2. 打开License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
3. 配置APN参数。
    a. 配置APN所属的VPN实例。
      [**ADD VPNINST**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/VPN/增加VPN实例（ADD VPNINST）_09653755.md)
    b. 创建APN实例，使能紧急呼叫功能。
      [**ADD APN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN/增加APN配置（ADD APN）_09653747.md)
      > **说明**
      > 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
    c. 使能APN的PCC功能。
      [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
4. 配置紧急呼叫结束后释放缺省承载。
  [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md)
  > **说明**
  > 紧急呼叫缺省承载创建以后，除非用户关机，否则缺省承载不会被删除。这样系统资源会被一直占用，为了回收系统资源，需要配置 [**SET APNIDLETIME**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/APN定时器属性/设置APN空闲上下文定时器配置（SET APNIDLETIME）_09653122.md) 命令来释放缺省承载，考虑到可能会有回呼的场景， “BEARERTIMER” 的时间不能设置为0，建议保持缺省值60分钟。

## [任务示例](#ZH-CN_OPI_0230394882)

任务描述

配置VoLTE用户的紧急呼叫功能，其中紧急APN为“sos”。

脚本

1. 打开本特性的License配置开关。
  ```
  SET LICENSESWITCH:LICITEM="LKV3W9ECAL11",SWITCH=ENABLE;
  ```
2. 使能紧急呼叫功能。
  //配置APN所属的VPN实例。
  ```
  ADD VPNINST:VPNINSTANCE="vpn1";
  ```
  //创建APN实例，使能紧急呼叫功能。
  ```
  ADD APN:APN="sos",HASVPN=ENABLE,VPNINSTANCE="vpn1",EMERGENCYSWITCH=ENABLE;
  ```
  //使能APN的PCC功能。
  ```
  SET APNPCCFUNC:APN="sos",HOMEPCCSWITCH=ENABLE,ROAMPCCSWITCH=INHERIT,VISITPCCSWITCH=INHERIT;
  ```
3. 配置紧急呼叫结束后释放缺省承载。
  ```
  SET APNIDLETIME: APN="sos", INHERIT=NO, SCTXCHKSW=ENABLE, PCTXCHKSW=ENABLE, GCTXCHKSW=ENABLE, HCTXCHKSW=ENABLE, ICTXCHKSW=ENABLE, GULTIMERLEVEL=BEARER, DFTBEARPOLICY=ONEDAY, BEARERTIMER=60;
  ```
