# 命令证据包：ADD CPCGBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG绑定/增加抄送CG绑定（ADD CPCGBINDING）_09896869.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来增加抄送CG绑定关系。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为32。
- 当前版本不支持此命令。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CPCGGRPID | 抄送CG组ID | local_planned | required | 无 | 整数类型，取值范围为1。整数1。 |
| CGIPVERSION | CG IP版本 | global_planned | required | IPV4 | 枚举类型。 |
| CGIPV4ADDR | CG IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| CGIPV6ADDR | CG IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。 |
| CGPORT | CG端口号 | global_planned | required | 无 | 整数类型，取值范围为1024～65535。 |
| PRIORITY | 等级 | local_planned | required | 无 | 整数类型，取值范围为0～100。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L48:
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD CPCGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG组/增加抄送CG组（ADD CPCGGRP）_09896864.md)
    > - [**ADD CPCGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG绑定/增加抄送CG绑定（ADD CPCGBINDING）_09896869.md)
    > - **[DSP SMPDPNUM](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文数/查询会话管理的PDP上下文数（DSP SMPDPNUM）_09653799.md)**
    > 

## ④ 自动比对
- 命令真相参数（6）：['CGIPV4ADDR', 'CGIPV6ADDR', 'CGIPVERSION', 'CGPORT', 'CPCGGRPID', 'PRIORITY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
