# 命令证据包：ADD RGRCACT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/RG级结果码处理动作/增加RG级异常返回码处理动作（ADD RGRCACT）_09654186.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加RG级异常返回码的处理动作配置。当CHF返回的Charging Data Response消息携带RG级异常返回码时，根据此配置进行处理。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 当异常返回码处理动作配置为重定向时，RDVIRTIP和RDVIRTIPV6之间至少配置一个参数。

- 最多可输入707条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CCTMPLTNAME | RCCODE | RCACT | BLKTIMER | RDVIRTIP | RDVIRTIPV6 | REACTREQ | HOLDI

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | global_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| RCCODE | RG级异常返回码 | global_planned | required | 无 | <br>- “DEFAULT（缺省值）”：当收到配置指定之外的结果码时需要执行的动作。 |
| RCACT | RG级异常返回码动作 | global_planned | required | 无 | <br>- BLCK_TRG_RPT（阻塞业务，后续有Trigger触发时，上报Charging D |
| BLKTIMER | RG级阻塞处理时间间隔(分钟) | global_planned | conditional | 无 | 整数类型，取值范围是0~1440，单位是分钟。 |
| RDVIRTIP | RG级重定向处理重定向IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| RDVIRTIPV6 | RG级重定向处理重定向IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。 |
| REACTREQ | RG级重新激活请求 | global_planned | conditional | 无 | 不配置此参数时值默认为DISABLE（0）。 |
| HOLDINGTIME | 用户保持时长(分钟) | global_planned | conditional | 无 | 整数类型，取值范围是0~2880，单位是分钟。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **ADD RGRCACT** | CCTMPLTNAME（在线计费模板名称） | cct-test | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。 |
  | **ADD RGRCACT** | RCCODE（RG级异常返回码） | QUOTAMNOTAPPL | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。 |
  | **ADD RGRCACT** | RCACT（RG级异常返回码动作） | BLCK_IMMED_RPT | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。 |
  | **ADD RGRCACT** | BLKTIMER（RG级阻塞处理时间间隔） | 30 | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。 |
- 任务示例脚本（该命令行）：
  `ADD RGRCACT: CCTMPLTNAME="global", RCCODE=QUOTAMNOTAPPL, RCACT=BLCK_IMMED_RPT, BLKTIMER=30;`
- 操作步骤上下文（±2 行原文）：
  L108:
    > 
    > ```
    > ADD RGRCACT: CCTMPLTNAME="global", RCCODE=QUOTAMNOTAPPL, RCACT=BLCK_IMMED_RPT, BLKTIMER=30;
    > ```

**md：`WSFD-011206/配置异常返回码和异常信元动作_93260161.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD RGRCACT**** | 在线计费模板名称（CCTMPLTNAME） | cct-test | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。 |
  | ****ADD RGRCACT**** | RG级异常返回码（RCCODE） | QUOTAMNOTAPPL | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。 |
  | ****ADD RGRCACT**** | RG级异常返回码动作（RCACT） | BLCK_IMMED_RPT | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。 |
  | ****ADD RGRCACT**** | RG级阻塞处理时间间隔（BLKTIMER） | 30 | 全网规划 | 配置当SMF收到CHF的响应的RG级异常返回码时的动作。基于计费过程中PDU会话下的RG进行处理。 |
- 任务示例脚本（该命令行）：
  `ADD RGRCACT: CCTMPLTNAME="cct-test", RCCODE=QUOTAMNOTAPPL, RCACT=BLCK_IMMED_RPT, BLKTIMER=30;`
- 操作步骤上下文（±2 行原文）：
  L51:
    >   ****ADD PDUSCACT****
    > 4. **可选：** 配置当SMF收到CHF的响应的RG级异常返回码时的动作。
    >   ****ADD RGRCACT****
    > 5. **可选：** 配置忽略CHF响应消息的信元列表。
    >   ****SET CNVRGDCHGPARA****
  L58:
    >   >
    >   > - 当“IGNORERSPAVP”参数配置为“INVOCATIONNUM”时，表示忽略CHF响应消息中的Invocation Sequence Number，不检查是否跟请求消息一致。
    >   > - 当“IGNORERSPAVP”参数配置为“FUI”时，表示当CHF返回RG级异常返回码和FUI时，忽略CHF响应消息中的FinalUnitIndication，按照对应****ADD RGRCACT****配置的“RCACT”动作执行。当**ADD RGRCACT**未配置时，执行默认动作。
    >   > - 当“IGNORERSPAVP”参数配置为“SESSIONFAILOVER”时，表示忽略CHF响应消息中的SessionFailover，使用对应CCT模板通过****SET FAILHANDLING****配置的“FAILOVERSUP”动作，“FAILOVERSUP”表示主CHF故障时，向备CHF发送计费消息进行处理。
    >   > - 当“IGNORERSPAVP”参数配置为“FAILUREHANDLING”时，表示忽略CHF响应消息中的FailureHandling，使用对应CCT模板通过**SET FAILHANDLING**配置的“FHACTION”动作。
  L93:
    > 
    > ```
    > ADD RGRCACT: CCTMPLTNAME="cct-test", RCCODE=QUOTAMNOTAPPL, RCACT=BLCK_IMMED_RPT, BLKTIMER=30;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（8）：['BLKTIMER', 'CCTMPLTNAME', 'HOLDINGTIME', 'RCACT', 'RCCODE', 'RDVIRTIP', 'RDVIRTIPV6', 'REACTREQ']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 8}（多值→atom 应考虑 decision_driven）
