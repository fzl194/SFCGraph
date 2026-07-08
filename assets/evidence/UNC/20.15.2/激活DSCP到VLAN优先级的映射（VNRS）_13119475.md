# 激活DSCP到VLAN优先级的映射 （VNRS）

- [操作场景](#ZH-CN_OPI_0213119475__1.3.1)
- [对系统的影响](#ZH-CN_OPI_0213119475__1.3.2)
- [必备事项](#ZH-CN_OPI_0213119475__1.3.3)
- [操作步骤](#ZH-CN_OPI_0213119475__1.3.4)
- [验证方法](#ZH-CN_OPI_0213119475__1.3.5)
- [任务示例](#ZH-CN_OPI_0213119475__1.3.6)

## [操作场景](#ZH-CN_OPI_0213119475)

本操作指导介绍，基于简单流分类，在运行网络配置DSCP和VLAN优先级映射关系。在需要配置DSCP和VLAN优先级映射关系的场景中使用此命令，此命令全局生效，将对出口报文中DSCP值按预期配置映射修改802.1p的值。

## [对系统的影响](#ZH-CN_OPI_0213119475)

该操作对系统正常运行无影响。

## [必备事项](#ZH-CN_OPI_0213119475)

前提条件

操作人员已经登录华为网络管理系统NMS（Network Management System）。

数据

需要准备本端规划的数据，无需准备与对端网元协商的数据，如 [表1](#ZH-CN_OPI_0213119475__zh-cn_opi_0134584220_tab_1) 所示。

*表1 需要准备的数据*

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| DSCPMAP | DSCP值（DSCP） | 62 | 本端规划 | [**ADD_DSCPMAP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DSCP映射VLAN优先级/添加DSCP值到VLAN优先级的映射（ADD DSCPMAP）_00865545.md) |
| DSCPMAP | 优先级类型（TYPE） | 8201p | 本端规划 | [**ADD_DSCPMAP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DSCP映射VLAN优先级/添加DSCP值到VLAN优先级的映射（ADD DSCPMAP）_00865545.md) |
| DSCPMAP | 优先级数值（VALUE） | 5 | 本端规划 | [**ADD_DSCPMAP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DSCP映射VLAN优先级/添加DSCP值到VLAN优先级的映射（ADD DSCPMAP）_00865545.md) |

## [操作步骤](#ZH-CN_OPI_0213119475)

1. 配置DSCP到VLAN优先级的映射。
  在 “MML命令行-UNC” 窗口上执行：
  [**ADD DSCPMAP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DSCP映射VLAN优先级/添加DSCP值到VLAN优先级的映射（ADD DSCPMAP）_00865545.md) : DSCP=DSCP值,TYPE=优先级类型,VALUE=优先级数值;

## [验证方法](#ZH-CN_OPI_0213119475)

- 查询DSCP到VLAN优先级的映射是否与配置一致。
  在 “MML命令行-UNC” 窗口上执行：
  [**LST DSCPMAP**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/安全管理/QoS管理/DSCP映射VLAN优先级/查询DSCP值到VLAN优先级的映射（LST DSCPMAP）_50121842.md) :;
  **预期结果：** 查询结果与配置结果一致。
  ```
  LST DSCPMAP:
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  DSCP值   优先级类型   优先级数值 
   62         exp          5 
   63         8021p        7 
  (结果个数 = 2)
  ---    END
  ```
  **异常结果：** 查询不到配置信息，请重新配置。

## [任务示例](#ZH-CN_OPI_0213119475)

任务描述

路由器与VNF2配置VLAN连接，通过在路由上配置DSCP到VLAN优先级的映射，使路由器上到VNF2的指定DSCP值的报文VLAN优先级为预期结果。

**图1** DSCP到VLAN优先级映射示意图

<br>

![](激活DSCP到VLAN优先级的映射（VNRS）_13119475.assets/zh-cn_image_0262797676_2.png)

脚本

//激活DSCP到VLAN优先级的映射。

```
ADD DSCPMAP
: DSCP=62,VALUE=5,TYPE=8021p;
```
