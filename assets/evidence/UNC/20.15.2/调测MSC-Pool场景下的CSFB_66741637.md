# 调测MSC Pool场景下的CSFB

- [操作场景](#ZH-CN_OPI_0166741637__1.3.1)
- [必备事项](#ZH-CN_OPI_0166741637__1.3.2)
- [操作步骤](#ZH-CN_OPI_0166741637__1.3.3)

## [操作场景](#ZH-CN_OPI_0166741637)

本操作介绍了通过调测手段检查 UNC 是否正确配置该功能的过程。

> **说明**
> 适用于MME

## [必备事项](#ZH-CN_OPI_0166741637)

前提条件

MSC Pool场景下的CSFB功能已经激活。

数据

该操作无需准备数据。

## [操作步骤](#ZH-CN_OPI_0166741637)

1. 验证MSC Pool场景下CSFB的主叫语音业务。
    a. 在MME网元上创建这两个用户的用户消息跟踪和S1-MME、S6a、SGs、GTPC接口消息跟踪任务。
    b. UE使用联合附着接入调测MME。
    c. 查询用户MM上下文的用户状态信息。
      进入 “MML命令行-UNC” 窗口。 [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) : QUERYOPT=BYIMSI, IMSI="IMSI";
      预期结果： “MM状态” 为 “ECM-CONNECTED” ； “VLR可靠性” 为 “可靠” ； “SGs关联状态” 为 “关联已建立” 。
    d. 被测UE主动发起语音业务，语音业务执行成功。
2. 验证MSC Pool场景下CSFB的被叫语音业务。
    a. 在MME网元上创建这两个用户的用户消息跟踪和S1-MME、S6a、SGs、GTPC接口消息跟踪任务。
    b. UE使用联合附着接入调测MME。
    c. 查询用户MM上下文的用户状态信息。
      进入 “MML命令行-UNC” 窗口。 [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) : QUERYOPT=BYIMSI, IMSI="IMSI";
      预期结果： “MM状态” 为 “ECM-CONNECTED” ； “VLR可靠性” 为 “可靠” ； “SGs关联状态” 为 “关联已建立” 。
    d. 被叫UE接收语音业务，被叫语音业务执行成功。
