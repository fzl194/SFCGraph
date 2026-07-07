# 命令证据包：SET ZEROCHGSKIPSW
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）_09896806.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于设置零流量计费事件忽略开关。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令仅当软参DWORD519 BIT4取值为1时生效。
- 该命令最大记录数为1。
- 忽略零流量计费事件会导致某些计费信息缺失（如RAT更新信息、ULI改变信息），需要确认影响后使能该功能。
- UNC当前暂不支持基于位置的计费订阅和取消，SKIPULIBASEDCHG无实际生效场景。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | Z

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| ZEROCHGSKIPSW | 零流量计费事件忽略总开关 | local_planned | required | 无 | 枚举类型。 |
| SKIPRATCHNG | 忽略RAT更新 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPSNCHNG | 忽略Serving Node地址改变 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPTMZONECHNG | 忽略MS时区改变 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPPLMNCHNG | 忽略Serving Node PLMN标识改变 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPTIMETHRESH | 忽略时间阈值 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPCCFH | 忽略CCFH | local_planned | conditional | 无 | 枚举类型。 |
| SKIPFINALCDR | 忽略去激活话单 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPPSFCI | 忽略PS-Furnish-Charging-Information改变 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPFOCGENCDR | 忽略强制生成话单 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPULIBASEDCHG | 忽略基于位置的计费订阅和取消 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPQOSCHNG | 忽略QoS改变 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPULICHNG | 忽略ULI改变 | local_planned | conditional | 无 | 枚举类型。 |
| SKIPTARIFFCHNG | 忽略费率切换 | local_planned | conditional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L41:
    > - [**SET CDRSTRGSTATUS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存目录/设置话单缓存目录状态（SET CDRSTRGSTATUS）_09897006.md)
    > - [**SET CDRSTORAGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存控制/设置话单存储控制参数（SET CDRSTORAGECTRL）_09897001.md)
    > - [**SET ZEROCHGSKIPSW**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）_09896806.md)
    > - [**ADD CG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG管理/配置CG（ADD CG）_09896845.md)
    > - [**ADD CGGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组/添加CG组（ADD CGGROUP）_09896879.md)

## ④ 自动比对
- 命令真相参数（14）：['SKIPCCFH', 'SKIPFINALCDR', 'SKIPFOCGENCDR', 'SKIPPLMNCHNG', 'SKIPPSFCI', 'SKIPQOSCHNG', 'SKIPRATCHNG', 'SKIPSNCHNG', 'SKIPTARIFFCHNG', 'SKIPTIMETHRESH', 'SKIPTMZONECHNG', 'SKIPULIBASEDCHG', 'SKIPULICHNG', 'ZEROCHGSKIPSW']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
