# 调测IPv6承载上下文特性（SGSN/GGSN）

- [操作场景](#ZH-CN_OPI_0248043374__1.3.1)
- [必备事项](#ZH-CN_OPI_0248043374__1.3.2)
- [操作步骤](#ZH-CN_OPI_0248043374__1.3.3)

## [操作场景](#ZH-CN_OPI_0248043374)

当运营商部署IPv6承载上下文特性时，需对该特性进行调测，确保本功能可以正常使用。

> **说明**
> 适用于SGSN、GGSN。

## [必备事项](#ZH-CN_OPI_0248043374)

前提条件

- 请仔细阅读[WSFD-104001 IPv6承载上下文特性概述（SGSN/GGSN）](特性概述_48043355.md)。

- 完成[激活IPv6承载上下文特性（SGSN/GGSN）](激活IPv6承载上下文特性（SGSN_GGSN）_48043366.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | 用户IMSI（IMSI） | 123000123456789 | 测试终端自带 | - |

工具

- 测试终端

## [操作步骤](#ZH-CN_OPI_0248043374)

1. 进入 “MML命令行-UNC” 窗口。
2. 执行 [**LST LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询IPv6承载上下文对应的License配置开关是否打开。
    - 如果“SWITCH”为“ENABLE”，流程结束。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
