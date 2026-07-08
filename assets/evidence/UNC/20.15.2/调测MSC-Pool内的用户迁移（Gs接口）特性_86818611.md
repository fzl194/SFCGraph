# 调测MSC Pool内的用户迁移（Gs接口）特性

- [操作场景](#ZH-CN_OPI_0186818611__1.3.1)
- [必备事项](#ZH-CN_OPI_0186818611__1.3.2)
- [操作步骤](#ZH-CN_OPI_0186818611__1.3.3)

## [操作场景](#ZH-CN_OPI_0186818611)

本操作指导介绍在运行网络中调测MSC Pool内的用户迁移（Gs接口）特性的操作过程。

> **说明**
> 适用于 SGSN 。

## [必备事项](#ZH-CN_OPI_0186818611)

前提条件

- 请仔细阅读[WSFD-110001 MSC Pool内的用户迁移（Gs接口）特性概述](特性概述_86818608.md)。
- 完成[激活MSC Pool内的用户迁移（Gs接口）特性](激活MSC Pool内的用户迁移（Gs接口）特性_86818610.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0186818611)

在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常 ：

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0186818611__cmd1660314278334)。
    - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
3. 查询MSC/VLR迁移配置信息。
  [**LST VLROFFLOADINF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/MSC POOL管理/VLR迁移配置信息/查询VLR迁移配置信息(LST VLROFFLOADINF)_26145422.md) ;
4. 查询MSC/VLR的迁移状态。
  [**DSP VLR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/电路域联合业务/VLR管理/显示VLR迁移进度(DSP VLR)_26305256.md) : VN=VLR号 ;
  预期结果：如果是启动迁移的MSC/VLR，则显示 “迁移状态” 为 “手动迁移中” 。如果是未启动迁移的MSC/VLR或终止迁移的MSC/VLR，则显示 “迁移状态” 为 “正常” 。
  > **说明**
  > 启动迁移后，确认MSC/VLR的状态是否为“手动迁移中”。在手动迁移状态下，一共有三个阶段：手动迁移第一阶段，手动迁移第二阶段，迁移完成。
