# 命令证据包：SET GLBCDRFLDTEMP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/全局话单字段模板/设置全局话单模板（SET GLBCDRFLDTEMP）_09896895.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

该命令是用来为全局绑定话单字段模板。

使用该命令可以为不同种类的话单类型绑定不同的话单字段模板（CDRFIELDTEMP）。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 设置全局计费属性，执行SET GLBCDRFLDTEMP命令前，需要执行ADD CDRFIELDTEMP添加话单字段模板。
- 输入空格表示解除全局话单字段模板的绑定关系。
- 全局绑定的话单字段优先级较低，如果APN下没有绑定某类型的话单字段模板时，才会使用全局绑定的该话单类型的话单字段模板，如果全局也没有绑定该类型的话单字段时，会使用

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GCDRTEMPLATE | G-CDR话单字段模板名 | global_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| PGWCDRTEMPLATE | PGW-CDR话单字段模板名 | global_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |
| SGWCDRTEMPLATE | SGW-CDR话单字段模板名 | global_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > - [**SET GLBTARIFFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > - [**SET GLBCDRFLDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/全局话单字段模板/设置全局话单模板（SET GLBCDRFLDTEMP）_09896895.md)
    > - [**FOC GENERATECDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/强制生成话单/强制生成话单（FOC GENERATECDR）_09897016.md)
    > - [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)

**md：`WSFD-011201/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md`**
- 数据规划表（该命令的参数行）：
  | **SET GLBCDRFLDTEMP** | PGW-CDR话单字段模板名（PGWCDRTEMPLATE） | cdrfield-test | 全网规划 | 配置全局绑定话单字段模板 |
- 任务示例脚本（该命令行）：
  `SET GLBCDRFLDTEMP: PGWCDRTEMPLATE="cdrfield-test";`
- 操作步骤上下文（±2 行原文）：
  L98:
    >       | **ADD CDRFIELDTEMP** | PSFCI字段 | 该字段记录运营商或设备制造商定义的信息。 |
    > 2. 配置全局话单字段模板。
    >   **SET GLBCDRFLDTEMP**
    > 3. 配置APN实例的话单字段模板。
    >     a. 配置APN实例。如已配置APN，请跳过该步骤。
  L122:
    > 
    > ```
    > SET GLBCDRFLDTEMP: PGWCDRTEMPLATE="cdrfield-test";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（3）：['GCDRTEMPLATE', 'PGWCDRTEMPLATE', 'SGWCDRTEMPLATE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 1}（多值→atom 应考虑 decision_driven）
