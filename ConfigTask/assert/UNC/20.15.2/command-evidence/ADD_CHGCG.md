# 命令证据包：ADD CHGCG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用于配置与本端SGSN对接的CG需满足的相关参数。

SGSN与CG对接时，需要配置该命令。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 此表最大记录数为16。
- “GTP承载协议（PRO）”、“CG的IP地址（IP）”和“CG接收端口号（SPN）”唯一确定一条记录。
- 只有在本命令中配置的CG，才能在[**SET CHGCHAR**](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)、[**ADD CHGBEHA**](../计费行为参数配置/增加计费

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| IPT | IP地址类型 | global_planned | optional | “IPV4(IPV4地址)” | <br>- “IPV4(IPV4地址)” |
| IP | CG的IPV4地址 | 整网规划 | conditional | 无 | 0.0.0.0~255.255.255.255 |
| IPV6 | CG的IPV6地址 | global_planned | conditional | 无 | ::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF |
| GRD | 优先级 | 整网规划 | conditional | 0 | 0~11 |
| PRO | GTP承载协议 | 整网规划 | required | 无 | <br>- “UDP(UDP)”：表示SGSN和CG之间通过UDP/IP进行通讯。 |
| CGR | CG协议版本 | 整网规划 | required | 无 | <br>- “R98(R98)”：表示CG支持的协议版本为R98。 |
| SPN | CG接收端口号 | 整网规划 | optional | 3386 | 1024~65535 |
| DEFAULTCG | 缺省CG | 整网规划 | optional | <br>“YES（是）” | <br>- “NO（否）” |
| CGN | CG名 | 整网规划 | optional | noname | 1~32位字符串 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-106202

**md：`WSFD-106202/激活SMS over GPRS_EDGE_WCDMA_84683740.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | CG的IPV4地址（IP） | 10.10.171.9 | 全网规划 | 增加一个CG。 |
  | [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | GTP承载协议（PRO） | UDP | 全网规划 | 增加一个CG。 |
  | [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | CG协议版本（CGR） | R6 | 全网规划 | 增加一个CG。 |
  | [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | 缺省CG（DEFAULTCG） | YES | 全网规划 | 增加一个CG。 |
  | [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | 优先级（GRD） | 0 | 全网规划 | 增加一个CG。 |
  | [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) | CG名（CGN） | abc | 全网规划 | 增加一个CG。 |
- 任务示例脚本（该命令行）：
  `ADD CHGCG: IP="10.10.171.9", PRO=UDP, CGR=R6, DEFAULTCG=YES, GRD=0, CGN="abc";`
- 操作步骤上下文（±2 行原文）：
  L141:
    > 
    > ```
    > ADD CHGCG: IP="10.10.171.9", PRO=UDP, CGR=R6, DEFAULTCG=YES, GRD=0, CGN="abc";
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/配置离线计费参数（SGSN）_01731207.md`**
- 操作步骤上下文（±2 行原文）：
  L82:
    >   **SET CHGCHAR**
    >   > **说明**
    >   > - 只有**ADD CHGCG**命令配置的CG，才能在**SET CHGCHAR**命令中生效。
    >   > - 根据实际场景的不同选择性配置计费属性功能。用户计费属性的优先级由低到高的顺序如下：
    >   >     - **SET CHGCDR**命令配置的计费属性。

### WSFD-011202

**md：`WSFD-011202/调测支持热计费功能_85008162.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > > 1. 用户在HLR中已签约GPRS业务，PDP计费属性为HOTBILLING。
    > > 2. 设置UMTS话单版本，以及UMTS CDR协议版本与CG的协议版本一致。
    > >   在SGSN MML窗口上执行命令 [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) 设置CG的协议版本。
    > >   在SGSN MML窗口上执行命令 [**SET CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/设置计费Ga接口参数(SET CHGGA)_26145378.md) 设置UMTS话单版本为32.015 V3.a.0，以及UMTS CDR协议版本与CG的协议版本一致。
    > > 3. SGSN与支持32.015 V3.a.0话单版本的CG连接正常。

## ④ 自动比对
- 命令真相参数（9）：['CGN', 'CGR', 'DEFAULTCG', 'GRD', 'IP', 'IPT', 'IPV6', 'PRO', 'SPN']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 6}（多值→atom 应考虑 decision_driven）
