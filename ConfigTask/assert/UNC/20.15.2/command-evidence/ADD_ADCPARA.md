# 命令证据包：ADD ADCPARA
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/ADC/ADC参数/增加ADC参数（ADD ADCPARA）_65996998.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置应用的流信息上报开关信息。

流信息的上报功能是指对于需要进行检测上报的应用，在上报应用开始/结束上报时，同时上报当前业务的流信息，便于PCRF/PCF能够获取到应用与流的对应关系，从而可以下发更精确地策略对业务进行控制。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为8000。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| FLOWFILTERNAME | 流过滤器名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 |
| FLOWINFORPT | 流信息上报标识 | local_planned | optional | DISABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109102

**md：`WSFD-109102/激活ADC基本功能_92582136.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD ADCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/ADC/ADC参数/增加ADC参数（ADD ADCPARA）_65996998.md) | 流过滤器名称（FLOWFILTERNAME） | flowfilter_ADC01 | 已配置数据中获取 | 使用<br>[**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)<br>命令定义的流过滤器名称。 |
  | [**ADD ADCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/ADC/ADC参数/增加ADC参数（ADD ADCPARA）_65996998.md) | 流信息上报开关（FLOWINFORPT） | ENABLE | 本端规划 | PCRF/PCF需要获取流信息时，设置为ENABLE。默认取值是DISABLE。 |
- 任务示例脚本（该命令行）：
  `ADD ADCPARA: FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L51:
    >       [**ADD FLOWFILTER**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务过滤器/流过滤器/增加流过滤器（ADD FLOWFILTER）_09897153.md)
    >     b. 配置ADC参数。
    >       [**ADD ADCPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/ADC/ADC参数/增加ADC参数（ADD ADCPARA）_65996998.md)
    > 3. PCRF/PCF要下发应用Start和Stop的两个Event Trigger，当PCRF/PCF不通过动态规则下发appid时，请执行本步骤。
    >     a. **可选：**配置SMF上的本地rule。
  L86:
    > 
    > ```
    > ADD ADCPARA: FLOWFILTERNAME="flowfilter_ADC01",FLOWINFORPT=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（2）：['FLOWFILTERNAME', 'FLOWINFORPT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 1}（多值→atom 应考虑 decision_driven）
