# 命令证据包：MOD AMUEPLCYCTRL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于修改指定的AM策略和UE策略的控制参数。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 | global_planned | required | 无 | <br>- “ALL_USER（所有用户）”：所有用户 |
| IMSIPRE | IMSI前缀 | global_planned | conditional | 无 | 字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。 |
| MSISDNPRE | MSISDN前缀 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。 |
| NSGRPID | 网络切片群组标识 | global_planned | conditional | 无 | 整数类型，取值范围是0~16。0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进 |
| ISAMASSOC | 是否建立AM策略偶联 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| ISUEASSOC | 是否建立UE策略偶联 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| AMFAILPLCY | AM策略建立/更新失败处理策略 | global_planned | optional | 无 | <br>- “LOCAL_OR_SUB_AMPLCY（使用本地配置或签约的AM策略）”：AMF向PC |
| UEFAILPLCY | UE策略建立/更新失败处理策略 | global_planned | optional | 无 | <br>- “NOPROCESS（不处理异常）”：忽略UE策略创建/更新失败，不进行异常处理，用户移 |
| AMTERPLCY | AM策略终止处理策略 | global_planned | optional | 无 | <br>- “LOCAL_OR_SUB_AMPLCY（使用本地配置或签约的AM策略）”：AMF向PC |
| UETERPLCY | UE策略终止处理策略 | global_planned | optional | 无 | <br>- “NOPROCESS（不处理异常）”：忽略UE策略创建/更新失败，不进行异常处理，用户移 |
| MECTOMALLSW | 是否支持MECToMall | local_planned | optional | 无 | <br>- “NO（否）”：否 |
| NEARBYACCSW | 是否支持就近接入 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| NEARBYKEYWD | 就近接入关键字 | global_planned | conditional | 无 | 字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只 |
| NEARBYHPCFSW | 就近接入是否发现H-PCF | local_planned | conditional | 无 | <br>- “NO（否）”：否 |
| DNNAMPLCYSW | 基于DNN的创建AM策略偶联开关 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| DNNAMPLCYKEYWD | DNN关键字 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只 |
| REGPDUREASW | INTER注册场景PDU会话重建开关 | local_planned | conditional | 无 | <br>- “NO（否）”：否 |
| LOCAMPLCYSW | 跨省漫游用户是否支持MECToMall | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| DNNUEPLCYSW | 基于DNN的创建UE策略偶联开关 | global_planned | optional | 无 | <br>- “NO（否）”：否 |
| DNNUEPLCYKEYWD | UE策略的DNN关键字 | global_planned | conditional | 无 | 字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只 |
| DESC | 描述信息 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~32。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-230001

**md：`WSFD-230001/WSFD-230001 动态UE Logo下发参考信息_45929684.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [ADD MECAREAGNB](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/本地特色业务区域管理/本地特色业务区域gNodeB成员管理/增加5G MEC gNodeB信息（ADD MECAREAGNB）_34732056.md)
    > - [ADD MECAREATAI](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/本地特色业务区域管理/本地特色业务区域TAI成员管理/增加5G MEC TAI信息（ADD MECAREATAI）_34892004.md)
    > - [MOD AMUEPLCYCTRL](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)
    > - [ADD NGUSRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组标识管理/增加5G用户群（ADD NGUSRGRP）_44006475.md)
    > - [ADD NGUSRGRPMEM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/通用配置管理/用户群组成员管理/增加5G用户群成员（ADD NGUSRGRPMEM）_44006476.md)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L22:
    > - [**ADD PCFSELPLCY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/NF发现和选择管理/PCF选择策略管理/增加PCF选择策略（ADD PCFSELPLCY）_44006528.md)
    > - [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
    > - [**MOD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)
    > - [**SET AMFPLCYFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > - [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L121:
    >           - 应用网络侧规划的UE策略时，将“ISUEASSOC”设置为“YES”。
    >     5. （可选）修改应用网络侧规划的AM策略/UE策略的用户群，使其应用本地配置的AM策略/UE策略。
    >       [**MOD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)
    >           - 应用本地配置的AM策略时，将“ISAMASSOC”设置为“NO”。
    >           - 应用本地配置的UE策略时，将“ISUEASSOC”设置为“NO”。

## ④ 自动比对
- 命令真相参数（21）：['AMFAILPLCY', 'AMTERPLCY', 'DESC', 'DNNAMPLCYKEYWD', 'DNNAMPLCYSW', 'DNNUEPLCYKEYWD', 'DNNUEPLCYSW', 'IMSIPRE', 'ISAMASSOC', 'ISUEASSOC', 'LOCAMPLCYSW', 'MECTOMALLSW', 'MSISDNPRE', 'NEARBYACCSW', 'NEARBYHPCFSW', 'NEARBYKEYWD', 'NSGRPID', 'REGPDUREASW', 'SUBRANGE', 'UEFAILPLCY', 'UETERPLCY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
