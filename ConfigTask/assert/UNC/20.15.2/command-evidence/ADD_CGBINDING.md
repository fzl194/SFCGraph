# 命令证据包：ADD CGBINDING
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG绑定/增加CG绑定关系（ADD CGBINDING）_09896874.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令用来增加CG绑定关系。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 用户选定CG Group后，CG优先级使用绑定CG到CG Group时指定的优先级，不使用配置CG时指定的优先级。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CGGRPID | CG组ID | local_planned | required | 无 | 整数类型，取值范围为1～32。 |
| CGIPVERSION | CG IP版本 | global_planned | required | IPV4 | 枚举类型。 |
| CGIPV4ADDR | CG IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| CGIPV6ADDR | CG IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。 |
| CGPORT | CG端口号 | global_planned | required | 无 | 整数类型，取值范围为1024～65535。 |
| PRIORITY | 等级 | local_planned | required | 无 | 整数类型，取值范围为0～100。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L44:
    > - [**ADD CG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG管理/配置CG（ADD CG）_09896845.md)
    > - [**ADD CGGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组/添加CG组（ADD CGGROUP）_09896879.md)
    > - [**ADD CGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG绑定/增加CG绑定关系（ADD CGBINDING）_09896874.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 操作步骤上下文（±2 行原文）：
  L86:
    >       > - 离线计费模板下未选择到CG组且没有配置全局CG组时，则使用全局CG。全局CG是该CG未绑定到任一CG组的CG，全局CG的优先级最低。
    >     d. **可选** ：配置CG组绑定CG。
    >       **ADD CGBINDING**
    >     e. **可选：**配置CG组绑定关系。
    >       **ADD CGGRPBINDING**

## ④ 自动比对
- 命令真相参数（6）：['CGGRPID', 'CGIPV4ADDR', 'CGIPV6ADDR', 'CGIPVERSION', 'CGPORT', 'PRIORITY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
