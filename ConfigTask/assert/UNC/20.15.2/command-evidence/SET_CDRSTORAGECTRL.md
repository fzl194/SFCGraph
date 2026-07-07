# 命令证据包：SET CDRSTORAGECTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存控制/设置话单存储控制参数（SET CDRSTORAGECTRL）_09897001.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

命令用来配置缓存话单文件的超期时间，配置的天数加上周数乘以七为配置的超期总天数。如果一个话单文件被缓存的时间超过配置的超期时间，该话单不会再发往CG/CHF。当配置的超期时间为0时，所有缓存文件不进行超期检测且不上报超期话单缓存告警，CG/CHF状态恢复正常后，所有的缓存话单都将发往CG/CHF。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CDREXPIREDAY | CDREXPIREWEEK |
| --- | --- | --- |
| 初始值 | 2 | 4 |

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CDREXPIREDAY | 话单缓存超期天数 | local_planned | optional | 无 | 整数类型，取值范围为0～6，单位是天。 |
| CDREXPIREWEEK | 话单缓存超期周数 | local_planned | optional | 无 | 整数类型，取值范围为0～52。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L40:
    > - [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**SET CDRSTRGSTATUS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存目录/设置话单缓存目录状态（SET CDRSTRGSTATUS）_09897006.md)
    > - [**SET CDRSTORAGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存控制/设置话单存储控制参数（SET CDRSTORAGECTRL）_09897001.md)
    > - [**SET ZEROCHGSKIPSW**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）_09896806.md)
    > - [**ADD CG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG管理/配置CG（ADD CG）_09896845.md)

**md：`WSFD-011201/配置话单可选功能（GGSN_SGW-C_PGW-C）_95923448.md`**
- 数据规划表（该命令的参数行）：
  | **SET CDRSTORAGECTRL** | 话单缓存超期天数（CDREXPIREDAY） | 3 | 本端规划 | 配置缓存话单文件的超期时间 |
  | **SET CDRSTORAGECTRL** | 话单缓存超期周数（CDREXPIREWEEK） | 3 | 本端规划 | 配置缓存话单文件的超期时间 |
- 任务示例脚本（该命令行）：
  `SET CDRSTORAGECTRL: CDREXPIREDAY=3,CDREXPIREWEEK=3;`
- 操作步骤上下文（±2 行原文）：
  L56:
    >       **SET CDRSTRGSTATUS**
    >     b. 配置缓存话单的超期时间。
    >       **SET CDRSTORAGECTRL**
    >       > **说明**
    >       > 当话单缓存的时间超过配置的超期时间时，系统会产生告警 **ALM-81059 超期话单缓存** ，提醒操作维护人员尽快处理话单。话单长期超期得不到处理，会导致用户计费信息丢失。
  L95:
    >     b. 手动操作完毕后，配置解锁话单缓存主目录 **CHARGE1** 。
    >       ```
    >       SET CDRSTORAGECTRL: CDREXPIREDAY=3,CDREXPIREWEEK=3;
    >       ```

### WSFD-011206

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **SET CDRSTORAGECTRL** | CDREXPIREDAY（话单缓存超期天数） | 2 | 本端规划 | 配置缓存文件的超期时长，超期的缓存文件不再回放。 |
  | **SET CDRSTORAGECTRL** | CDREXPIREWEEK（话单缓存超期周数） | 4 | 本端规划 | 配置缓存文件的超期时长，超期的缓存文件不再回放。 |
- 任务示例脚本（该命令行）：
  `SET CDRSTORAGECTRL:CDREXPIREDAY=2,CDREXPIREWEEK=4;`
- 操作步骤上下文（±2 行原文）：
  L67:
    >   **SET GLBDFTCHFGROUP**
    > - 配置缓存文件的超期时长。
    >   **SET CDRSTORAGECTRL**
    > - 配置融合计费话单缓存告警上报的控制参数。
    >   ****SET STGALARMCTRL****
  L124:
    > 
    > ```
    > SET CDRSTORAGECTRL:CDREXPIREDAY=2,CDREXPIREWEEK=4;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（2）：['CDREXPIREDAY', 'CDREXPIREWEEK']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4}（多值→atom 应考虑 decision_driven）
