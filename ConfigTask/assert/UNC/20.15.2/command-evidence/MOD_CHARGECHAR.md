# 命令证据包：MOD CHARGECHAR
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）_09896810.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用来修改对本地用户、漫游用户、拜访用户所采用的计费属性。

计费属性指对用户所采用的计费类型，不同计费类型可以有不同的话单生成方式。用户的计费属性可以遵从SGSN/SGW上的属性配置，也可以遵从UNC上的属性配置。本地用户和漫游用户统称本PLMN（Public Land Mobile Network，运营商移动网络标识）的归属用户。UNC支
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCNAME | 计费属性名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| HOME | 本地用户计费属性 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| ROAM | 漫游用户计费属性 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| VISIT | 拜访用户计费属性 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| HOMESGSN | 本地用户使用Serving Node计费属性 | local_planned | optional | 无 | 枚举类型。 |
| ROAMSGSN | 漫游用户使用Serving Node计费属性 | local_planned | optional | 无 | 枚举类型。 |
| VISITSGSN | 拜访用户使用Serving Node计费属性 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011202

**md：`WSFD-011202/WSFD-011202 支持热计费功能（适用于GGSN、SGW-C、PGW-C）参考信息_28072079.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - **[增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/增加对本地用户、漫游用户、拜访用户所采用的计费属性（ADD CHARGECHAR）_09896809.md)**
    > - **[删除对本地用户、漫游用户、拜访用户所采用的计费属性（RMV CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/删除对本地用户、漫游用户、拜访用户所采用的计费属性（RMV CHARGECHAR）_09896811.md)**
    > - **[修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD CHARGECHAR）_09896810.md)**
    > - **[查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST CHARGECHAR）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/基本计费属性/查询对本地用户、漫游用户、拜访用户所采用的计费属性（LST CHARGECHAR）_09896812.md)**
    > - **[设置计费控制配置（SET CHARGECTRL）](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)**

## ④ 自动比对
- 命令真相参数（7）：['CCNAME', 'HOME', 'HOMESGSN', 'ROAM', 'ROAMSGSN', 'VISIT', 'VISITSGSN']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
