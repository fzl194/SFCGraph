# 调测LTE和UMTS PS网络之间的切换

- [操作场景](#ZH-CN_OPI_0227489130__1.3.1)
- [必备事项](#ZH-CN_OPI_0227489130__1.3.2)
- [操作步骤](#ZH-CN_OPI_0227489130__1.3.3)

## [操作场景](#ZH-CN_OPI_0227489130)

本操作指导用于验证LTE和UMTS网络之间的切换业务功能。

> **说明**
> 适用于 SGSN、 GGSN、 MME、SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0227489130)

前提条件

- 请仔细阅读[WSFD-104503 LTE和UMTS PS网络之间的切换](../WSFD-104503 LTE和UMTS PS网络之间的切换_91285432.md)。
- 已完成[激活LTE和UMTS网络之间的重选](激活LTE和UMTS PS网络之间的切换_91285433.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪。

## [操作步骤](#ZH-CN_OPI_0227489130)

- 此处举例验证 UNC 能正确处理用户从LTE到UMTS发起的位置更新。
  在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：
    1. 用户在HSS中已签约EPS业务。
    2. 在 UNC 的操作维护台上建立S1接口跟踪，用户跟踪，GTPC接口跟踪。
    3. 用户从eNodeB的覆盖区移动到RNC的覆盖区，触发切换流程。
      预期结果：MME正常处理eNodeB发起的HO Required流程。
    4. 进入 “MML命令行-UNC” 窗口。
    5. 查询用户状态信息。
      [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) : QUERYOPT=BYIMSI, IMSI="IMSI";
      预期结果： “MM状态” 为 “ECM-CONNECTED” 。
    6. 查询用户承载信息。
      [**DSP SMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/系统管理/用户数据库管理/显示承载上下文(DSP SMCTX)_72226033.md) : QUERYOPT=BYIMSI, IMSI="IMSI", IDTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=*;
      预期结果：可观察到用户的签约的承载上下文信息，没有动态信息。
