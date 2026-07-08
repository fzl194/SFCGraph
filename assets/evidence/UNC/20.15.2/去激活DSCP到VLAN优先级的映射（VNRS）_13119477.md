# 去激活DSCP到VLAN优先级的映射 （VNRS）

- [操作场景](#ZH-CN_OPI_0213119477__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0213119477__1.3.2)
- [必备事项](#ZH-CN_OPI_0213119477__1.3.3)
- [操作步骤](#ZH-CN_OPI_0213119477__1.3.4)
- [任务示例](#ZH-CN_OPI_0213119477__1.3.5)

## [操作场景](#ZH-CN_OPI_0213119477)

本操作指导介绍，在运行网络中，去激活DSCP到VLAN优先级映射功能的操作过程。

## [对系统的影响](#ZH-CN_OPI_0213119477)

无

## [必备事项](#ZH-CN_OPI_0213119477)

前提条件

- 操作人员已经登录网络管理系统NMS（Network Management System）。
- 已经激活DSCP到VLAN优先级映射功能。

数据

无需准备数据。

## [操作步骤](#ZH-CN_OPI_0213119477)

1. 删除对应的DSCPMAP。
  在 “MML命令行-UNC” 窗口上执行：
  [**RMV DSCPMAP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DSCP映射VLAN优先级/删除DSCP值到VLAN优先级的映射（RMV DSCPMAP）_00866185.md) : DSCP=DSCP值,TYPE=优先级类型,VALUE=优先级数值;

## [任务示例](#ZH-CN_OPI_0213119477)

任务描述

- 删除已配置的DSCPMAP。

脚本

//删除已配置的DSCPMAP。

```
RMV DSCPMAP:DSCP=8,VALUE=6,TYPE=8021p;
```
