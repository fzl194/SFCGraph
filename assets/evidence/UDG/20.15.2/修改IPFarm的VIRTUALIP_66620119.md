# 修改IPFarm的VIRTUALIP

- [操作场景](#ZH-CN_OPI_0166620119__1.3.1)
- [必备事项](#ZH-CN_OPI_0166620119__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166620119__1.3.3)
- [任务示例](#ZH-CN_OPI_0166620119__1.3.4)

## [操作场景](#ZH-CN_OPI_0166620119)

该IPFarm被用于重定向时，修改该IPFarm的VIRTUALIP。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0166620119)

前提条件

- 请仔细阅读[GWFD-110281 用户Portal](../../GWFD-110281 用户Portal_66620113.md)。
- 完成[配置用户Portal](../配置用户Portal_66620114.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**MOD IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/修改IPFarm（MOD IPFARM）_82837051.md) | IP-Farm名称（IPFARMNAME） | farm_test | 已配置数据中获取 | 配置的IPFarm名称，已通过<br>[**ADD IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/增加IPFarm（ADD IPFARM）_82837050.md)<br>命令配置完成，可以使用<br>[**LST IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/查询IPFarm（LST IPFARM）_82837053.md)<br>命令进行查询。 |
| [**MOD IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/修改IPFarm（MOD IPFARM）_82837051.md) | IP协议版本（IPVERSION） | IPV4 | 本端规划 | - |
| [**MOD IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/修改IPFarm（MOD IPFARM）_82837051.md) | 虚拟IP地址（VIRTUALIP） | 10.1.2.3 | 本端规划 | - |

## [操作步骤](#ZH-CN_OPI_0166620119)

1. 修改IPFARM对应的VIRTUALIP。
  [**MOD IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/修改IPFarm（MOD IPFARM）_82837051.md)

## [任务示例](#ZH-CN_OPI_0166620119)

任务描述

将farm_test的虚拟IP地址修改为10.1.2.3。

脚本

//修改IPFARM对应的VIRTUALIP。

```
RMV RULE:RULENAME="rule_test1";
```

```
MOD IPFARM:IPFARMNAME="farm_test",IPVERSION=IPV4,VIRTUALIP="10.1.2.3";
```

```
ADD RULE:RULENAME="rule_test1",POLICYTYPE=SMARTREDIRECT,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_test1",PRIORITY=10,POLICYNAME="farm_test";
```
