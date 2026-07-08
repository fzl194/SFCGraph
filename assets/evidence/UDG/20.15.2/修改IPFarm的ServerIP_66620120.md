# 修改IPFarm的ServerIP

- [操作场景](#ZH-CN_OPI_0166620120__1.3.1)
- [必备事项](#ZH-CN_OPI_0166620120__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166620120__1.3.3)
- [任务示例](#ZH-CN_OPI_0166620120__1.3.4)

## [操作场景](#ZH-CN_OPI_0166620120)

IPFarm的ServerIP不允许被修改，配置不同的IP会新增一个ServerIP。如果需要修改ServerIP，可以先删除原来的ServerIP，再配置一个新的ServerIP。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0166620120)

前提条件

- 请仔细阅读[GWFD-110281 用户Portal](../../GWFD-110281 用户Portal_66620113.md)。
- 完成[配置用户Portal](../配置用户Portal_66620114.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**RMV IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/删除IPFarmServer（RMV IPFARMSERVER）_86526415.md)<br>[**ADD IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/增加IPFarmServer（ADD IPFARMSERVER）_82837056.md) | IP-Farm名称（IPFARMNAME） | farm_test | 已配置数据中获取 | 配置的IPFarm名称，已通过<br>[**ADD IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/增加IPFarm（ADD IPFARM）_82837050.md)<br>命令配置完成，可以使用<br>[**LST IPFARM**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm参数/查询IPFarm（LST IPFARM）_82837053.md)<br>命令进行查询。 |
| [**RMV IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/删除IPFarmServer（RMV IPFARMSERVER）_86526415.md)<br>[**ADD IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/增加IPFarmServer（ADD IPFARMSERVER）_82837056.md) | IP协议版本（IPVERSION） | IPV4 | 本端规划 | - |
| [**RMV IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/删除IPFarmServer（RMV IPFARMSERVER）_86526415.md)<br>[**ADD IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/增加IPFarmServer（ADD IPFARMSERVER）_82837056.md) | 服务器IPv4地址（SERVERIPV4） | 10.10.253.251<br>10.10.253.252 | 本端规划 | - |

## [操作步骤](#ZH-CN_OPI_0166620120)

1. 删除原来的类型为IPV4的ServerIP。
  [**RMV IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/删除IPFarmServer（RMV IPFARMSERVER）_86526415.md)
2. 新增IPFarm的类型为IPV4的ServerIP。
  [**ADD IPFARMSERVER**](../../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/IP Farm 管理/IP Farm服务器/增加IPFarmServer（ADD IPFARMSERVER）_82837056.md)

## [任务示例](#ZH-CN_OPI_0166620120)

任务描述

把IPFarm为farm_test的ServerIP由10.10.253.251修改为10.10.253.252。

脚本

```
RMV IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="10.10.253.251";
```

```
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="10.10.253.252";
```
