# 命令证据包：ADD PDUSCACT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级结果码处理动作/增加PDU异常返回码动作（ADD PDUSCACT）_09652165.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加PDU异常返回码动作。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 最多可输入2000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| CODETYPE | 返回码类型 | local_planned | required | 无 | <br>- “DEFAULT（针对未指定的异常返回码设置处理动作）”：当收到配置指定之外的结果码时需 |
| STATUSCODE | 状态码 | local_planned | conditional | 无 | 整数类型，取值范围是300~999，65535。 |
| SCACT | 处理动作 | local_planned | required | 无 | <br>- “FAILOVER（进行Failover处理）”：进行Failover处理时，优先按照C |
| RDVIRTIP | 重定向IPV4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| RDVIRTIPV6 | 重定向IPV6地址 | global_planned | conditional | 无 | IPv6地址类型。 |
| BLKTIMER | 阻塞处理时间间隔 | local_planned | conditional | 无 | 整数类型，取值范围是0~1440，单位是分钟。 |
| GTPV01CAUSE | 原因值GtpV0-1 | local_planned | conditional | 无 | 整数类型，取值范围是0~255。 |
| GTPV2CAUSE | 原因值GtpV2 | local_planned | conditional | 无 | 整数类型，取值范围是0~255。 |
| REACTREQ | 重新激活请求 | local_planned | conditional | 无 | <br>- DISABLE（不使能） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/融合计费可靠性（未部署NCG）_75816427.md`**
- 操作步骤上下文（±2 行原文）：
  L42:
    > 场景二：当SMF超时（ **SET FAILHANDLING** 配置的TXTIMER定时器）未收到响应消息，向备CHF重发计费请求消息（ **SET FAILHANDLING** 配置FHACTION参数为CONTINUE或RETRY_AND_TERM）。备用CHF正常处理、正常返回计费响应消息。
    > 
    > 场景三：当SMF收到的响应消息携带异常响应码时，向备CHF重发计费请求消息（ **ADD PDUSCACT** 配置SCACT参数为FAILOVER）。备用CHF正常处理、正常返回计费响应消息。
    > 
    > P4：当SMF感知到主用CHF正常，会将计费消息发往主用CHF（ **SET FAILHANDLING** 配置AUTOFAILBACK），完成回切。

**md：`WSFD-011206/使用全局CCT模板进行融合计费实例_93029782.md`**
- 数据规划表（该命令的参数行）：
  | **ADD PDUSCACT** | CCTMPLTNAME（CCT名称） | cct-test | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。 |
  | **ADD PDUSCACT** | CODETYPE（返回码类型） | VALUE | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。 |
  | **ADD PDUSCACT** | STATUSCODE（状态码） | 404 | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。 |
  | **ADD PDUSCACT** | SCACT（处理动作） | CONTINUE | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。 |
- 任务示例脚本（该命令行）：
  `ADD PDUSCACT: CCTMPLTNAME="global", CODETYPE=VALUE, STATUSCODE=404, SCACT=CONTINUE;`
- 操作步骤上下文（±2 行原文）：
  L102:
    > 
    > ```
    > ADD PDUSCACT: CCTMPLTNAME="global", CODETYPE=VALUE, STATUSCODE=404, SCACT=CONTINUE;
    > ```
    > 

**md：`WSFD-011206/配置异常返回码和异常信元动作_93260161.md`**
- 数据规划表（该命令的参数行）：
  | ****ADD PDUSCACT**** | CCT名称（CCTMPLTNAME） | cct-test | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。 |
  | ****ADD PDUSCACT**** | 返回码类型（CODETYPE） | VALUE | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。 |
  | ****ADD PDUSCACT**** | 状态码（STATUSCODE） | 502 | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。 |
  | ****ADD PDUSCACT**** | 处理动作（SCACT） | FAILOVER | 本端规划 | 配置当SMF收到CHF的PDU级异常返回码时的动作。基于用户计费过程中的PDU会话进行处理。 |
- 任务示例脚本（该命令行）：
  `ADD PDUSCACT: CCTMPLTNAME="cct-test", CODETYPE=VALUE, STATUSCODE=502, SCACT=FAILOVER;`
- 操作步骤上下文（±2 行原文）：
  L49:
    >   ****SET FAILHANDLING****
    > 3. **可选：** 配置当SMF收到CHF的PDU级异常返回码时的动作。
    >   ****ADD PDUSCACT****
    > 4. **可选：** 配置当SMF收到CHF的响应的RG级异常返回码时的动作。
    >   ****ADD RGRCACT****
  L87:
    > 
    > ```
    > ADD PDUSCACT: CCTMPLTNAME="cct-test", CODETYPE=VALUE, STATUSCODE=502, SCACT=FAILOVER;
    > ```
    > 

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 操作步骤上下文（±2 行原文）：
  L57:
    >   **SET FAILHANDLING**
    > - 配置当SMF收到CHF的PDU级异常返回码时的动作。
    >   **ADD PDUSCACT**
    > - 配置计费消息缓存功能。
    >   **SET N40MSGSTG**

**md：`WSFD-011206/调测融合计费的缓存消息回放功能_90005269.md`**
- 操作步骤上下文（±2 行原文）：
  L39:
    > 2. 开启计费缓存功能。
    >     - [**SET FAILHANDLING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/设置融合计费模板故障处理动作（SET FAILHANDLING）_09654177.md)命令“FHACTION”参数配置为“CONTINUE”。
    >     - [**ADD PDUSCACT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级结果码处理动作/增加PDU异常返回码动作（ADD PDUSCACT）_09652165.md)命令“SCACT”参数配置为“FAILOVER”或“CONTINUE”。
    >     - [**SET N40MSGSTG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费消息缓存/设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.md)命令“STGSWITCH”参数配置为“ENABLE”。
    >     - [**SET CNVRGDCHGPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/全局配置/设置融合计费全局参数（SET CNVRGDCHGPARA）_09653056.md)命令“CHGDATAREFGEN”参数配置为“SMF”。

## ④ 自动比对
- 命令真相参数（10）：['BLKTIMER', 'CCTMPLTNAME', 'CODETYPE', 'GTPV01CAUSE', 'GTPV2CAUSE', 'RDVIRTIP', 'RDVIRTIPV6', 'REACTREQ', 'SCACT', 'STATUSCODE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 8}（多值→atom 应考虑 decision_driven）
