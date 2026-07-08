# 激活支持Routing Behind MS

- [操作场景](#ZH-CN_OPI_0274264904__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0274264904__1.3.2)
- [必备事项](#ZH-CN_OPI_0274264904__1.3.3)
- [操作步骤](#ZH-CN_OPI_0274264904__1.3.4)
- [任务示例](#ZH-CN_OPI_0274264904__1.3.5)

## [操作场景](#ZH-CN_OPI_0274264904)

当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个 MS/UE 接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活 UDG 的Routing Behind MS功能。

> **说明**
> 适用于PGW-U、UPF。

## [对系统的影响](#ZH-CN_OPI_0274264904)

如果APN配置了anti-spoofing功能，使能Routing Behind MS功能后，该APN的anti-spoofing功能自动关闭。

## [必备事项](#ZH-CN_OPI_0274264904)

前提条件

- 请仔细阅读[GWFD-110910 支持Routing Behind MS](../GWFD-110910 支持Routing Behind MS_74264898.md)。
- 完成加载license（如果有需求，请联系华为技术支持工程师处理）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/APN的地址分配属性配置/设置ApnAddressAttr配置（SET APNADDRESSATTR）_82837173.md) | APN名称（APN） | apn1 | 已配置数据中获取 | 规划使能Routing Behind MS功能的APN实例，已通过<br>[**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)<br>命令配置，可以使用<br>[查询APN配置（LST APN）](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/查询APN配置（LST APN）_82837017.md)<br>命令进行查询。 |
| [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/APN的地址分配属性配置/设置ApnAddressAttr配置（SET APNADDRESSATTR）_82837173.md) | 手机后路由（FRAMEDROUTE） | ENABLE | 本端规划 | 配置指定APN是否允许手机后路由用户接入。 |
| [**SET APNFLOWMAXNUM**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN最大五元组数/设置APN最大流数（SET APNFLOWMAXNUM）_82837010.md) | APN（APN） | apn1 | 已配置数据中获取 | 已通过<br>[**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)<br>命令配置，可以使用<br>[查询APN配置（LST APN）](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/查询APN配置（LST APN）_82837017.md)<br>命令进行查询。 |
| [**SET APNFLOWMAXNUM**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN最大五元组数/设置APN最大流数（SET APNFLOWMAXNUM）_82837010.md) | APN最大五元组节点数（FDMAXNUM） | 800 | 本端规划 | 某个APN下允许创建的五元组的最大数目，即单用户所有业务可以使用五元组个数上限。 |
| [**SET SRVCOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/业务公共参数/设置业务公共参数（SET SRVCOMMONPARA）_82837309.md) | 用户session的五元组节点最大数量（FDMAXNUM） | 600 | 本端规划 | 全局配置的单用户所有业务可以使用五元组个数上限。 |
| [**SET SRVCOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/业务公共参数/设置业务公共参数（SET SRVCOMMONPARA）_82837309.md) | 单用户最大流表数动态调整开关（USERFLOWADJSW） | ENABLE | 本端规划 | 全局配置的单用户所有业务可以使用五元组个数上限。 |

## [操作步骤](#ZH-CN_OPI_0274264904)

1. 打开本特性的License开关。
  [**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)
2. 使能该APN的Routing Behind MS功能。
  [**SET APNADDRESSATTR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/APN的地址分配属性配置/设置ApnAddressAttr配置（SET APNADDRESSATTR）_82837173.md)
  > **说明**
  > - 如果APN使能了L2TP功能，则无需开启Routing Behind MS功能。
  > - 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。
3. 配置APN下单用户所有业务允许创建的五元组的最大数目。
  [**SET APNFLOWMAXNUM**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN最大五元组数/设置APN最大流数（SET APNFLOWMAXNUM）_82837010.md)
4. 配置全局单用户所有业务可以使用五元组个数上限，并打开自动调整用户五元组上限功能开关。
  [**SET SRVCOMMONPARA**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/业务匹配策略/业务匹配公共配置/业务公共参数管理/业务公共参数/设置业务公共参数（SET SRVCOMMONPARA）_82837309.md)
  > **说明**
  > 单个用户的默认五元组个数为600，如果现网有超过该默认值的情况，需要配置该步骤。

## [任务示例](#ZH-CN_OPI_0274264904)

任务描述

使能APN“apn1”的Routing Behind MS功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5RBMS01",SWITCH=ENABLE;
```

//使能该APN的Routing Behind MS功能。

```
SET APNADDRESSATTR:APN="apn1",FRAMEDROUTE=ENABLE;
```

//配置APN下单用户所有业务可以使用五元组个数上限。

```
SET APNFLOWMAXNUM:APN="apn1",FDMAXNUM=800;
```

//配置全局单用户所有业务可以使用五元组个数上限，并打开自动调整用户五元组上限功能开关。

```
SET SRVCOMMONPARA:FDMAXNUM=800,USERFLOWADJSW=ENABLE;
```
