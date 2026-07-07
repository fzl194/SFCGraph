# 命令证据包：ADD CGGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组/添加CG组（ADD CGGROUP）_09896879.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用来增加CG组，配置CG组描述信息。此命令为离线计费的基本配置，CG组用来绑定CG。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为32。
- 如果要使用该CG组则必须绑定到离线计费模板下或设置为全局CG组。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CGGRPID | CG组ID | local_planned | required | 无 | 整数类型，取值范围为1～32。 |
| DESCRIPTION | CG组描述 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L43:
    > - [**SET ZEROCHGSKIPSW**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费参数/设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）_09896806.md)
    > - [**ADD CG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG管理/配置CG（ADD CG）_09896845.md)
    > - [**ADD CGGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组/添加CG组（ADD CGGROUP）_09896879.md)
    > - [**ADD CGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG绑定/增加CG绑定关系（ADD CGBINDING）_09896874.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)

**md：`WSFD-011201/配置到CG的数据（GGSN_SGW-C_PGW-C）_95923479.md`**
- 操作步骤上下文（±2 行原文）：
  L79:
    >       **ADD CG**
    >     b. **可选** ：配置CG组。
    >       **ADD CGGROUP**
    >     c. **可选** ：配置全局CG组。
    >       **SET GLBCGGROUP**

## ④ 自动比对
- 命令真相参数（2）：['CGGRPID', 'DESCRIPTION']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
