# 调测 NSA(Opt.3)双连接管理

- [操作场景](#ZH-CN_OPI_0193270613__1.3.1)
- [必备事项](#ZH-CN_OPI_0193270613__1.3.2)
- [操作步骤](#ZH-CN_OPI_0193270613__1.3.3)

## [操作场景](#ZH-CN_OPI_0193270613)

本操作指导介绍在运行网络中调测 NSA(Opt.3)双连接管理 特性的操作过程。

> **说明**
> 适用于MME。

## [必备事项](#ZH-CN_OPI_0193270613)

前提条件

- 请仔细阅读[WSFD-011502 NSA(Opt.3)双连接管理](../WSFD-011502 NSA(Opt.3)双连接管理_93270610.md)。
- 完成[激活NSA(Opt.3)双连接管理](激活NSA(Opt.3)双连接管理_93270612.md)。

数据

该操作无需准备数据。

工具

OM Portal跟踪。

## [操作步骤](#ZH-CN_OPI_0193270613)

在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：

- 验证安全参数传递功能。
    1. 在UNC上创建一个用户跟踪，参数“IMSI”填写被跟踪用户A的IMSI。
    2. 用户A附着到MME，查看用户跟踪。
      预期结果：

      a. Attach Request携带UE additional security capability信元。
          b. Security Mode Command消息携带Replayed UE additional security capability。
          c. MME发给eNodeB的Initial Context Setup Request消息中携带NR UE Security Capabilities，指示的算法和UE携带的相同。
- 验证流量上报功能。
    1. NSA用户附着到LTE网络。
    2. eNodeB发送Secondary RAT Data Usage Report上报5G流量，观察用户跟踪。
      预期结果：观察到MME给S-GW发送Change Notification Request消息上报流量统计报告。
- 验证5G用户信息对等网元间传递功能。
    1. 在UNC上创建用户跟踪，假设终端的IMSI为“123036901000001”。
    2. 终端开机附着。
    3. 触发Inter流程。
      预期结果：本端MME通过Forward Relocation Request消息将信元Extended Access Restriction Data携带给对端MME。
