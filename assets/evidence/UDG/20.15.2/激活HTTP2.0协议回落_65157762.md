# 激活HTTP2.0协议回落

- [操作场景](#ZH-CN_OPI_0165157762__1.3.1)
- [必备事项](#ZH-CN_OPI_0165157762__1.3.2)
- [操作步骤](#ZH-CN_OPI_0165157762__1.3.3)
- [任务示例](#ZH-CN_OPI_0165157762__1.3.4)

## [操作场景](#ZH-CN_OPI_0165157762)

当运营商部署的网关设备不具备HTTP2.0处理能力或者网关设备需要与不具备HTTP2.0处理能力的周边网元配合共同完成业务部署时，需要开启HTTP2.0协议回落功能，对业务实施计费与策略控制。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0165157762)

前提条件

- 请仔细阅读[GWFD-110202 HTTP2.0协议回落](../GWFD-110202 HTTP2.0协议回落_68597362.md)。
- UDG已完成与周边网元的对接。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET SRVCOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/业务公共参数/设置业务公共参数（SET SRVCOMMONPARA）_82837309.md) | HTTP2.0协议回落开关（HTTP2DEGRADESW） | ENABLE | 本端规划 | 开启全局HTTP2.0协议回落功能。 |
| [**SET APNHTTP2DGRD**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/APN HTTP2协议回落开关/设置APN HTTP2.0协议回落开关（SET APNHTTP2DGRD）_82837306.md) | APN名称（APN） | apn-test | 已配置数据中获取 | 开启基于APN的HTTP2.0协议回落功能。 |
| [**SET APNHTTP2DGRD**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/APN HTTP2协议回落开关/设置APN HTTP2.0协议回落开关（SET APNHTTP2DGRD）_82837306.md) | APN HTTP2协议回落开关（HTTP2DEGRADESW） | ENABLE | 本端规划 | 开启基于APN的HTTP2.0协议回落功能。 |
| [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_86528530.md) | PCC策略组名称（PCCPOLICYGRPNM） | pcc-test | 已配置数据中获取 | 开启基于rule级别的HTTP2.0协议回落功能。 |
| [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_86528530.md) | HTTP2.0协议回落开关（HTTP2DEGRADESW） | ENABLE | 本端规划 | 开启基于rule级别的HTTP2.0协议回落功能。 |

> **说明**
> UDG 进行HTTP2.0协议回落的优先级顺序为：基于rule级别的HTTP2.0协议回落>基于APN的HTTP2.0协议回落>全局HTTP2.0协议回落。在高优先级HTTP2.0协议回落功能未配置的情况下，默认继承上一层级低优先级HTTP2.0协议回落功能的配置。

## [操作步骤](#ZH-CN_OPI_0165157762)

1. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
2. 开启全局HTTP2.0协议回落功能开关。
  [**SET SRVCOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/业务公共参数/设置业务公共参数（SET SRVCOMMONPARA）_82837309.md)
3. 当运营商需要基于APN级别进行控制时，开启基于APN级别的HTTP2.0协议回落功能开关。
  [**SET APNHTTP2DGRD**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/APN HTTP2协议回落开关/设置APN HTTP2.0协议回落开关（SET APNHTTP2DGRD）_82837306.md)
4. 当运营商需要基于rule级别进行控制时，开启基于rule级别的HTTP2.0协议回落功能开关。
  [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务控制策略/PCC控制策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_86528530.md)

## [任务示例](#ZH-CN_OPI_0165157762)

任务描述

场景1：当 UDG 与SP Server配合共同完成业务部署时，若所有SP Server都不具备HTTP2.0处理能力，则需要开启全局HTTP2.0协议回落功能。

场景2：当 UDG 与SP Server配合共同完成业务部署时，若部分SP Server不具备HTTP2.0处理能力，且这部分SP Server规划为通过同一个APN（apn-test）接入，则需要开启基于APN级别的HTTP2.0协议回落功能。

场景3：当 UDG 与SP Server配合共同完成业务部署时，若部分SP Server不具备HTTP2.0处理能力，且无法通过APN进行区分，则需要开启基于rule的HTTP2.0协议回落功能。

脚本

//场景1：

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3G5H2PF01", SWITCH=ENABLE;
```

//开启全局HTTP2.0协议回落功能开关。

```
SET SRVCOMMONPARA: HTTP2DEGRADESW=ENABLE;
```

//配置基于APN级别的HTTP2.0协议回落功能开关，APN级别的与上一级（全局级别）回落开关相同。默认值为INHERIT。

```
SET APNHTTP2DGRD: APN="apn-test", HTTP2DEGRADESW=INHERIT;
```

//配置基于rule级别的HTTP2.0协议回落功能开关，rule级别的与上一级（APN级别）回落开关相同。默认值为INHERIT。

```
MOD PCCPOLICYGRP: PCCPOLICYGRPNM="pcc-test", HTTP2DEGRADESW=INHERIT;
```

//场景2：

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3G5H2PF01", SWITCH=ENABLE;
```

//关闭全局HTTP2.0协议回落功能开关。

```
SET SRVCOMMONPARA: HTTP2DEGRADESW=DISABLE;
```

//开启基于APN级别的HTTP2.0协议回落功能开关。

```
SET APNHTTP2DGRD: APN="apn-test", HTTP2DEGRADESW=ENABLE;
```

//场景3：

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV3G5H2PF01", SWITCH=ENABLE;
```

//关闭全局HTTP2.0协议回落功能开关。

```
SET SRVCOMMONPARA: HTTP2DEGRADESW=DISABLE;
```

// **某一APN下仅少数PCC策略组需要开启HTTP2.0协议回落功能开关。**

//关闭基于APN级别的HTTP2.0协议回落功能开关。

```
SET APNHTTP2DGRD: APN="apn-test", HTTP2DEGRADESW=DISABLE;
```

//开启基于rule级别的HTTP2.0协议回落功能开关。

```
MOD PCCPOLICYGRP: PCCPOLICYGRPNM="pcc-test", HTTP2DEGRADESW=ENABLE;
```

// **某一APN下仅少数PCC策略组不需要开启HTTP2.0协议回落功能开关。**

//开启基于APN级别的HTTP2.0协议回落功能开关。

```
SET APNHTTP2DGRD: APN="apn-test", HTTP2DEGRADESW=ENABLE;
```

//关闭基于rule级别的HTTP2.0协议回落功能开关。

```
MOD PCCPOLICYGRP: PCCPOLICYGRPNM="pcc-test", HTTP2DEGRADESW=DISABLE;
```
