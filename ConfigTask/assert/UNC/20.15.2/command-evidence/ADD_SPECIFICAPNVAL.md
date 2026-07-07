# 命令证据包：ADD SPECIFICAPNVAL
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户使用的APN与信令流程中使用的指定APN的映射关系。用户使用的APN包括：别名APN、虚拟APN或真实APN，信令流程包括：PCRF交互、PCF交互、CG话单、同AAA鉴权交互、计费交互以及同OCS和CHF交互。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 用户APN必须是在ADD APN或ADD APNALIAS命令中已配置过的APN或别名APN，上报APN不用预先在ADD APN或ADD APNALIAS命令中配置。
- 若执行了RMV APN或RMV APNALIAS命令删除APN或别名APN，也需删除本命令中的映射关系。若一条数据中的所有的映射APN都为NULL时，删除该条记录。
- 添加记录时上报

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBSCRIBERAPN | 用户APN | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| ONLYROAMSWITCH | 是否只对漫游用户生效开关 | local_planned | optional | DISABLE | <br>- DISABLE（不使能） |
| PCRFAPN | PCRF交互消息使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| CGAPN | CG话单使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| OCSAPN | OCS交互消息使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| AAAACCTAPN | AAA计费消息使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| AAAAUTHAPN | AAA鉴权消息使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| AAAAUTHAPNCASE | AAA鉴权消息使用的映射APN是否大小写敏感 | local_planned | optional | CASE_INSENSITIVE | <br>- “CASE_INSENSITIVE（大小写不敏感）”：大小写不敏感 |
| CHFAPN | CHF交互消息使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |
| PCFAPN | PCF交互消息使用的映射APN | local_planned | optional | 无 | 字符串类型，输入长度范围是0~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 操作步骤上下文（±2 行原文）：
  L129:
    >       [**SET APNPCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 8. **可选：**配置specific APN。
    >   [**ADD SPECIFICAPNVAL**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)
    >   > **说明**
    >   > GGSN/PGW-C向PCRF上报APN时，不仅能携带Request APN/Service APN，GGSN/PGW-C支持上报指定的APN，该APN可以是系统中配置的任一APN实例名称或者APN别名名称。

### WSFD-011306

**md：`WSFD-011306/WSFD-011306 Radius功能参考信息_15542176.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    > - **[SET RDSAUTHREQVSA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/鉴权管理/请求消息信元控制/设置RADIUS鉴权请求携带的私有扩展属性（SET RDSAUTHREQVSA）_28567662.md)**
    > - **[MOD RDSSVRGRP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器组/修改Radius服务器组（MOD RDSSVRGRP）_09896731.md)**
    > - **[**ADD SPECIFICAPNVAL**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)**
    > - [**ADD RULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则/增加规则（ADD RULE）_09897200.md)
    > - [**ADD USERPROFILE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/用户模板/增加用户模板（ADD USERPROFILE）_09897206.md)

**md：`WSFD-011306/配置RADIUS功能_32909765.md`**
- 操作步骤上下文（±2 行原文）：
  L141:
    >   > - 通过**[SET FHBYPASS](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/失败旁路处理/设置失败旁路处理（SET FHBYPASS）_09896714.md)**“HOLDINGTIME”控制故障恢复后对放通用户的后续处理，即永久在线或去激活。
    > 8. **可选：** 配置Specific APN。
    >   [**ADD SPECIFICAPNVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)
    >   > **说明**
    >   > 其中 “ONLYROAMSWITCH” 为可选参数，配置 [**ADD SPECIFICAPNVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md) 命令的生效范围：仅对漫游用户生效。
  L143:
    >   [**ADD SPECIFICAPNVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md)
    >   > **说明**
    >   > 其中 “ONLYROAMSWITCH” 为可选参数，配置 [**ADD SPECIFICAPNVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/周边接口呈现APN策略管理/指定上报的APN/增加用户APN与消息交互使用APN的映射关系（ADD SPECIFICAPNVAL）_09653027.md) 命令的生效范围：仅对漫游用户生效。
    >   >
    >   > 在上报APN时，不仅能携带Request APN/Service APN， UNC 支持上报指定的APN，该APN可以是系统中配置的任一APN实例名称或者APN别名的名称。

## ④ 自动比对
- 命令真相参数（10）：['AAAACCTAPN', 'AAAAUTHAPN', 'AAAAUTHAPNCASE', 'CGAPN', 'CHFAPN', 'OCSAPN', 'ONLYROAMSWITCH', 'PCFAPN', 'PCRFAPN', 'SUBSCRIBERAPN']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
