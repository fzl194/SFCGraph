# 调测支持Direct Tunnel功能

- [操作场景](#ZH-CN_OPI_0226375781__1.3.1)
- [必备事项](#ZH-CN_OPI_0226375781__1.3.2)
- [操作步骤](#ZH-CN_OPI_0226375781__1.3.3)

## [操作场景](#ZH-CN_OPI_0226375781)

本操作指导介绍在运行网络中调测支持Direct Tunnel功能的操作过程。

> **说明**
> 适用于 SGSN、 GGSN 。

## [必备事项](#ZH-CN_OPI_0226375781)

前提条件

- 请仔细阅读[WSFD-104506 支持Direct Tunnel 功能特性概述](特性概述_91527822.md)。
- 完成[激活支持Direct Tunnel功能](激活支持Direct Tunnel功能_26375780.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪。

## [操作步骤](#ZH-CN_OPI_0226375781)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令查询License配置开关是否已打开。
    - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0226375781__step586775134816)。
    - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
3. 执行ping命令，分别ping对应的RNC、GGSN的IP地址，查看是否可以ping通。
    - 如果是，请执行[4](#ZH-CN_OPI_0226375781__step11538312515)。
    - 如果否，请参考[激活支持Direct Tunnel功能](激活支持Direct Tunnel功能_26375780.md)页面重新配置RNC和GGSN。
4. 创建接口跟踪，查看Iu、Gn接口消息跟踪，查看是否有数据上报。
    - 如果是，调测结束。
    - 如果否，请执行[5](#ZH-CN_OPI_0226375781__step16896454185916)。
5. 收集信息并联系华为技术支持解决。
