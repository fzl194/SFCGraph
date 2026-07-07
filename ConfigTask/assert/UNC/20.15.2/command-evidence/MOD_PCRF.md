# 命令证据包：MOD PCRF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

![](修改PCRF（MOD PCRF）_09897102.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改对端信息可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。

此命令用于修改PCRF的基本信息，修改特定的PCRF。

此命令为PCC策略控制的核心配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 修改特定的PCRF时，一定要输入指定PCRF主机名称。
- 可能导致PCRF链路闪断，影响PCC策略控制。
- PCRF绑定到PCRFGroup时，修改该PCRF的动态协商参数会同时修改该PCRFGROUP下所有其他PCRF的协商参数，如果该PCRFGROUP下的某个PCRF同时被其他PCRFGROUP绑定，那么该PCRFGROUP下的PCRF的协商参数也会被刷新。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOSTNAME | PCRF主机名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT150控制是否 |
| VPNINSTANCE | VPN实例 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，区分大小写。 |
| SUPFEANEGOSW | Supported-Features动态协商开关 | 对端协商 | optional | 无 | 枚举类型。 |
| CARRYSUPFEASW | Supported-Feature AVP携带开关 | global_planned | conditional | 无 | 枚举类型。 |
| FEATURELIST | Feature列表 | 对端协商 | optional | 无 | 位域类型。 |
| DSCPV | DSCP值 | global_planned | optional | 无 | 整数类型，取值范围为0～63，255。 |
| WALVALUE | wal值 | local_planned | optional | 无 | 整数类型，取值范围为0～4294967295。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109104

**md：`WSFD-109104/WSFD-109104 基于累计流量的策略控制参考信息_29056192.md`**
- 操作步骤上下文（±2 行原文）：
  L13:
    > 
    > - [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > - [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > - [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)
    > 

**md：`WSFD-109104/激活基于累计流量的策略控制_29056190.md`**
- 数据规划表（该命令的参数行）：
  | [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md) | PCRF主机名（HOSTNAME） | pcrf_01 | 已配置数据中获取 | 使用<br>[**ADD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)<br>定义的PCRF主机名。 |
  | [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md) | Supported-Features动态协商开关（SUPFEANEGOSW） | ENABLE | 与对端协商 | 使用样例值。 |
  | [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md) | Feature列表（FEATURELIST） | UMCH | 与对端协商 | PCRF需要支持UMCH功能。 |
- 任务示例脚本（该命令行）：
  `MOD PCRF: HOSTNAME="pcrf_01",SUPFEANEGOSW=ENABLE,FEATURELIST=UMCH-1;`
- 操作步骤上下文（±2 行原文）：
  L43:
    >   [**SET PCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
    > 4. 与PCRF通过Gx接口交互时，使能流量监控拥塞处理（UMCH）功能。
    >   [**MOD PCRF**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > 5. 配置将某类业务/应用的流量不统计到会话级流量。
    >   [**MOD PCCPOLICYGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务策略/PCC策略组/修改PCC策略组（MOD PCCPOLICYGRP）_09897174.md)
  L71:
    > 
    > ```
    > MOD PCRF: HOSTNAME="pcrf_01",SUPFEANEGOSW=ENABLE,FEATURELIST=UMCH-1;
    > ```
    > 

### WSFD-010802

**md：`WSFD-010802/WSFD-010802 周边网元过载保护（Gx_Gy_Ga_Gi接口流控功能）参考信息_30753122.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > [**ADD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    > 
    > [**MOD PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/修改PCRF（MOD PCRF）_09897102.md)
    > 
    > [**RMV PCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/删除PCRF（RMV PCRF）_09897103.md)

## ④ 自动比对
- 命令真相参数（7）：['CARRYSUPFEASW', 'DSCPV', 'FEATURELIST', 'HOSTNAME', 'SUPFEANEGOSW', 'VPNINSTANCE', 'WALVALUE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '与对端协商': 2}（多值→atom 应考虑 decision_driven）
