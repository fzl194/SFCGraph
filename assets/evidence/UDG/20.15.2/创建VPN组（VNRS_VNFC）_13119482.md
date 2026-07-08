# 创建VPN组 （VNRS_VNFC）

- [操作场景](#ZH-CN_OPI_0213119482__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0213119482__1.3.2)
- [必备事项](#ZH-CN_OPI_0213119482__1.3.3)
- [操作步骤](#ZH-CN_OPI_0213119482__1.3.4)
- [验证方法](#ZH-CN_OPI_0213119482__1.3.5)
- [任务示例](#ZH-CN_OPI_0213119482__1.3.6)

## [操作场景](#ZH-CN_OPI_0213119482)

在网络部署时，通常用户会创建很多VPN实例，当配置将报文重定向到指定的VPN时，如果逐个配置报文重定向，会增加配置的复杂度，通过增加VPN组，将报文重定向到指定的VPN组，实现批量操作，可以使配置操作更加便捷。

> **说明**
> NP卡场景下，不支持创建VPN组。

## [对系统的影响](#ZH-CN_OPI_0213119482)

该操作对系统正常运行无影响。

## [必备事项](#ZH-CN_OPI_0213119482)

前提条件

设备加电并正常启动。

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如 [表1](#ZH-CN_OPI_0213119482__zh-cn_opi_0171965992_tab_1) 所示

*表1 需要准备的数据*

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| 增加VPN组 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **[ADD SQOSVPNGROUP](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组/增加VPN组（ADD SQOSVPNGROUP）_00600349.md)** |
| 增加VPN组成员 | VPN组名称（VPNGROUPNAME） | test1 | 本端规划 | **[ADD SQOSVPNGROUPMEM](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组成员/增加VPN组成员（ADD SQOSVPNGROUPMEM）_50280994.md)** |
| 增加VPN组成员 | VPN名称（VPNNAME） | vpn1 | 本端规划 | **[ADD SQOSVPNGROUPMEM](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组成员/增加VPN组成员（ADD SQOSVPNGROUPMEM）_50280994.md)** |
| 增加VPN组成员 | VPN优先级（VPNPRIORITY） | 2 | 本端规划 | **[ADD SQOSVPNGROUPMEM](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组成员/增加VPN组成员（ADD SQOSVPNGROUPMEM）_50280994.md)** |

## [操作步骤](#ZH-CN_OPI_0213119482)

1. 增加VPN组
  在 “MML命令行-UDG” 窗口上执行：
  **[ADD SQOSVPNGROUP](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组/增加VPN组（ADD SQOSVPNGROUP）_00600349.md)** : VPNGROUPNAME="VPN组名称";
2. 增加VPN组成员
  在 “MML命令行-UDG” 窗口上执行：
  **[ADD SQOSVPNGROUPMEM](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组成员/增加VPN组成员（ADD SQOSVPNGROUPMEM）_50280994.md)** : VPNGROUPNAME="VPN组名称", VPNNAME="VPN名称", VPNPRIORITY="VPN优先级";

## [验证方法](#ZH-CN_OPI_0213119482)

查询VPN组的信息是否与数据规划表中一致。

- 查询VPN组配置
  在 “MML命令行-UDG” 窗口上执行：
  **[LST SQOSVPNGROUP](../../../../../../../../OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/VPN组/查询VPN组（LST SQOSVPNGROUP）_50280654.md)** : VPNGROUPNAME="VPN组名称";
  **预期结果：** 查询结果与规划值一致。

  ```
  RETCODE = 0  操作成功。                                                                                                                                结果如下                                                         
  ------------------------                                                         
  VPN组名称 = test1   
    VPN名称 = vpn1  
  VPN优先级 = 2                                                              
  (结果个数 = 1)                                                          
  ---    END
  ```

## [任务示例](#ZH-CN_OPI_0213119482)

任务描述

创建VPN组并增加VPN组成员。

脚本

//创建VPN组。

```
ADD SQOSVPNGROUP:VPNGROUPNAME="test1";
```

//增加VPN组成员。

```
ADD SQOSVPNGROUPMEM:VPNGROUPNAME="test1",VPNNAME="vpn1",VPNPRIORITY=2;
```
