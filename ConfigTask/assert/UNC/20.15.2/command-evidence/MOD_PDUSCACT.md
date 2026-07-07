# 命令证据包：MOD PDUSCACT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/PDU级结果码处理动作/修改PDU异常返回码动作（MOD PDUSCACT）_09652181.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于修改PDU异常返回码动作。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

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

**md：`WSFD-011206/配置计费消息缓存_31702748.md`**
- 数据规划表（该命令的参数行）：
  | **MOD PDUSCACT** | CCTMPLTNAME（CCT名称） | cct-test | 本端规划 | 融合计费模板名称，<br>[配置融合计费模板](配置融合计费模板_93400212.md)<br>已经配置。 |
  | **MOD PDUSCACT** | CODETYPE（返回码类型） | VALUE | 本端规划 | - |
  | **MOD PDUSCACT** | STATUSCODE（状态码） | 502 | 本端规划 | - |
  | **MOD PDUSCACT** | SCACT（处理动作） | FAILOVER | 本端规划 | SCACT需配置为FAILOVER或CONTINUE，开启计费消息缓存的前提条件。 |
- 任务示例脚本（该命令行）：
  `MOD PDUSCACT: CCTMPLTNAME="cct-test", CODETYPE=VALUE, STATUSCODE=502, SCACT=FAILOVER;`
- 操作步骤上下文（±2 行原文）：
  L94:
    > 
    > ```
    > MOD PDUSCACT: CCTMPLTNAME="cct-test", CODETYPE=VALUE, STATUSCODE=502, SCACT=FAILOVER;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（10）：['BLKTIMER', 'CCTMPLTNAME', 'CODETYPE', 'GTPV01CAUSE', 'GTPV2CAUSE', 'RDVIRTIP', 'RDVIRTIPV6', 'REACTREQ', 'SCACT', 'STATUSCODE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4}（多值→atom 应考虑 decision_driven）
