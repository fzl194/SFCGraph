# 命令证据包：MOD SELECTCHFGBYCC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/修改基于CC选择CHF处理（MOD SELECTCHFGBYCC）_09651411.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于修改基于CC选择CHF处理。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTYPE | Charge Characteristic类型 | local_planned | required | 无 | <br>- DEFAULT（未指定Charge Characteristic的值） |
| CCVALUE | Charge Characteristic值 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| MASK | Charge Characteristic特定值掩码 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| PRIORITY | Charge Characteristic优先级 | local_planned | conditional | 无 | 整数类型，取值范围是1~65535。 |
| PRIMARYCHFGRP | 主CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~63。该参数输入空格或者null（不区分大小写）清空参数值。 |
| SECONDARYCHFGRP | 备CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是1~63。该参数输入空格或者null（不区分大小写）清空参数值。 |

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

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L64:
    >           - 如果有可用CHF，请执行[步骤 10](#ZH-CN_OPI_0289257219__step13334556133920)。
    >           - 如果没有可用CHF，请执行[步骤 9.b](#ZH-CN_OPI_0289257219__substep6959172620617)。
    >     b. 执行 [**SET GLBDFTCHFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/设置全局默认CHF组（SET GLBDFTCHFGROUP）_09651523.md) 、 [**MOD SELECTCHFGBYCC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/修改基于CC选择CHF处理（MOD SELECTCHFGBYCC）_09651411.md) 命令，按照规划配置当前用户可选择的CHF，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 10. 检查是否产生 [ALM-100072 目的NF服务不可达](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100072 目的NF服务不可达_26182301.md) 告警。
    >     a. 检查是否产生 [ALM-100072 目的NF服务不可达](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-100072 目的NF服务不可达_26182301.md) 告警，查询N40接口的通信是否存在故障。

## ④ 自动比对
- 命令真相参数（6）：['CCTYPE', 'CCVALUE', 'MASK', 'PRIMARYCHFGRP', 'PRIORITY', 'SECONDARYCHFGRP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
