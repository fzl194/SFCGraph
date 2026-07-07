# 命令证据包：RMV PCRF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

![](删除PCRF（RMV PCRF）_09897103.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除对端信息可能导致Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

此命令用于删除PCRF的基本信息，删除特定的PCRF。

此命令为PCC策略控制的核心配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 如果PCRF被绑定在PCRF组中，并且该PCRF组只有一个PCRF，删除PCRF的同时，删除PCRF组；如果PCRF被绑定在PCRF组中，并且该PCRF组不是只有一个PCRF，删除PCRF的同时，该PCRF也在PCRF组中删除。
- 如果本设备是最后一个使用该HOSTNAME的diameter应用的设备，则同时删除该HostName对应的Diameter对端地址。


**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOSTNAME | PCRF主机名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否 |
| FORCED | 是否强制删除 | global_planned | optional | 无。执行命令并不输入该参数时，默认按照False执行命令。 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/调测到PCRF的数据_31422954.md`**
- 操作步骤上下文（±2 行原文）：
  L115:
    >     - 如果配置不一致，请执行[步骤 4](#ZH-CN_OPI_0231422954__stp3)。
    > 4. 修改GGSN/PGW-C上PCRF设备标识。
    >     a. 执行[**RMV PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令，删除原有配置。
    >     b. 执行[**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)命令，按照规划数据和PCRF上的数据重新配置GGSN/PGW-C的PCRF信息。
    >     c. 再次执行[步骤 2](#ZH-CN_OPI_0231422954__stp1)，查看PCRF状态。

### WSFD-010802

**md：`WSFD-010802/WSFD-010802 周边网元过载保护（Gx_Gy_Ga_Gi接口流控功能）参考信息_30753122.md`**
- 操作步骤上下文（±2 行原文）：
  L16:
    > [**MOD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > 
    > [**RMV PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)
    > 
    > [**LST PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/查询PCRF（LST PCRF）_09897104.md)

### WSFD-011132

**md：`WSFD-011132/特性概述_29315043.md`**
- 操作步骤上下文（±2 行原文）：
  L68:
    > - GGSN/PGW-C上开启DRA功能后，如果Gx、Gy应用配置相同的本端主机名，则同一台DRA设备不能同时为Gx、Gy应用提供路由服务。
    > - 如果是直连路径改造或经DRA的非直连路径改造的场景，需要注意以下事项：
    >     - 如果是从直连路径改造成经DRA的非直连路径，且直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，并将已经对接好的DRA绑定到对应的APN下（**[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**），再解锁APN。
    >     - 如果是从直连路径改造成直连路径与经DRA的非直连路径共存的场景，当后续直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，再解锁APN。
    >     - 如果是从经DRA的非直连路径改造成直连路径与经DRA的非直连路径共存的场景，当后续直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，再解锁APN。
  L69:
    > - 如果是直连路径改造或经DRA的非直连路径改造的场景，需要注意以下事项：
    >     - 如果是从直连路径改造成经DRA的非直连路径，且直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，并将已经对接好的DRA绑定到对应的APN下（**[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**），再解锁APN。
    >     - 如果是从直连路径改造成直连路径与经DRA的非直连路径共存的场景，当后续直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，再解锁APN。
    >     - 如果是从经DRA的非直连路径改造成直连路径与经DRA的非直连路径共存的场景，当后续直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，再解锁APN。
    > 
  L70:
    >     - 如果是从直连路径改造成经DRA的非直连路径，且直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，并将已经对接好的DRA绑定到对应的APN下（**[ADD REALMBINDAPN](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter Realm/Realm绑定APN/增加APN与Diameter Realm关联关系（ADD REALMBINDAPN）_09897285.md)**），再解锁APN。
    >     - 如果是从直连路径改造成直连路径与经DRA的非直连路径共存的场景，当后续直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，再解锁APN。
    >     - 如果是从经DRA的非直连路径改造成直连路径与经DRA的非直连路径共存的场景，当后续直连路径不再使用需要删除时，则需要先执行锁定对应APN并去活用户操作，用户去活完成后再执行[**RMV PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)命令删除直连路径，再解锁APN。
    > 
    > #### [原理概述](#ZH-CN_CONCEPT_0229315043)

## ④ 自动比对
- 命令真相参数（2）：['FORCED', 'HOSTNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
