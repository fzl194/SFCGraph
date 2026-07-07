# 命令证据包：MOD TNFBINDGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/修改目标NF实例绑定组（MOD TNFBINDGRP）_09652550.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、NCG、SMSF**

该命令用于修改目标NF实例绑定目标NF组的配置。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| TNFGRPINDEX | 目标NF组索引 | local_planned | required | 无 | 整数类型，取值范围是0~511。 |
| TNFINSINDEX | 目标NF实例索引 | local_planned | required | 无 | 整数类型，取值范围是0~2047。 |
| PRIORITY | 优先级 | global_planned | optional | 无 | 整数类型，取值范围是1~255。值越小优先级越高。 |
| WEIGHT | 权重 | global_planned | optional | 无 | 整数类型，取值范围是1~65535。值越大表示权重越大。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/调测融合计费的主备CHF的可靠性_89257222.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > 5. 如果通过本地配置基于CC选择CHF，执行 [**LST SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/查询基于CC选择CHF处理（LST SELECTCHFGBYCC）_09653040.md) 、 [**LST TNFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/查询目标NF实例绑定组（LST TNFBINDGRP）_09651395.md) 、 [**LST TNFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/查询目标NF组（LST TNFGRP）_09652113.md) 、 [**LST TNFINSIP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/查询目标NF实例IP地址（LST TNFINSIP）_09651383.md) 、 [**LST TNFINS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/查询目标NF实例（LST TNFINS）_09652356.md) 命令，查看SMF本地是否配置备CHF组，且备用CHF配置了IP地址等信息。
    >     - 如果已配置，请执行[步骤 6](#ZH-CN_OPI_0289257222__step1321124813497)。
    >     - 如果未配置，请执行[**ADD TNFINSIP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例IP地址管理/增加目标NF实例IP地址（ADD TNFINSIP）_09654443.md)、[**MOD TNFINS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例管理/修改目标NF实例（MOD TNFINS）_09651413.md)、[**ADD TNFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF组管理/增加目标NF组（ADD TNFGRP）_09651791.md)、[**MOD TNFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/服务化接口管理/注册与服务发现/本地NRF功能管理/目标NF实例绑定组管理/修改目标NF实例绑定组（MOD TNFBINDGRP）_09652550.md)、[**MOD SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/修改基于CC选择CHF处理（MOD SELECTCHFGBYCC）_09651411.md)命令，根据规划配置基于CC绑定主备CHF组，并再次执行[步骤 3](#ZH-CN_OPI_0289257222__step2585105420194)。
    > 6. 查看用户跟踪消息，打开CHF给SMF发送的 Charging Data Response [initial] /Charging Data Response [update]消息，查看是否携带sessionFailover信元，且该信元为FAILOVER_NOT_SUPPORTED，即主用CHF故障时不支持向备用CHF发送计费消息。
    >     - 如果CHF下发了sessionFailover信元，且取值为FAILOVER_NOT_SUPPORTED，那么主用CHF故障时，SMF未向备用CHF发送计费消息是正常的。如果需要修改，则联系CHF端技术支持修改相关配置。

## ④ 自动比对
- 命令真相参数（4）：['PRIORITY', 'TNFGRPINDEX', 'TNFINSINDEX', 'WEIGHT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
