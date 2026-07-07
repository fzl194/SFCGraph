# 命令证据包：SET SGWCHARGECFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C**

![](SGW计费配置（SET SGWCHARGECFG）_09896989.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改配置可能导致无可用CG，SGW话单无法被正常处理，从而导致用户无法计费。

SET SGWCHARGECFG命令用来修改SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用P
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | HOMEOFFLINE | ROAMOFFLINE | VISITOFFLINE | SGWCGFLAG |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | ENABLE | ENABLE | USE_LOC

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| HOMEOFFLINE | 本地用户离线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| ROAMOFFLINE | 漫游用户离线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| VISITOFFLINE | 拜访用户离线计费开关 | local_planned | optional | 无 | 枚举类型。 |
| SGWCGFLAG | SGW CG IP选择 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L18:
    > - [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md)
    > - [**ADD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/增加计费方式（ADD CHARGEMETHOD）_09896795.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**SET SGWAPNCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md)
    > - [**SET SGWCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md)
  L45:
    > - [**ADD CGGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组/添加CG组（ADD CGGROUP）_09896879.md)
    > - [**ADD CGBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG绑定/增加CG绑定关系（ADD CGBINDING）_09896874.md)
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**ADD LOGICINF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/逻辑接口/增加逻辑接口（ADD LOGICINF）_09896723.md)
    > - [**ADD CPCGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/抄送CG组/增加抄送CG组（ADD CPCGGRP）_09896864.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **SET SGWCHARGECFG** | 本地用户离线计费开关（HOMEOFFLINE） | DISABLE | 本端规划 | 该命令仅适用于UNC产品用作S-GW网元。<br>SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。<br>一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。 |
  | **SET SGWCHARGECFG** | 漫游用户离线计费开关（ROAMOFFLINE） | ENABLE | 本端规划 | 该命令仅适用于UNC产品用作S-GW网元。<br>SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。<br>一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。 |
  | **SET SGWCHARGECFG** | 拜访用户离线计费开关（VISITOFFLINE） | ENABLE | 本端规划 | 该命令仅适用于UNC产品用作S-GW网元。<br>SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。<br>一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。 |
  | **SET SGWCHARGECFG** | SGW CG IP选择（SGWCGFLAG） | USE_LOCAL | 本端规划 | 该命令仅适用于UNC产品用作S-GW网元。<br>SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。<br>一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。 |
- 任务示例脚本（该命令行）：
  `SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;`
  `SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;`
  `SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;`
  `SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;`
- 操作步骤上下文（±2 行原文）：
  L60:
    > 
    > 1. 基于用户归属属性（本地用户、漫游用户、拜访用户）使能SGW-C的离线计费方式。
    >   **SET SGWCHARGECFG**
    >   > **说明**
    >   > 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。
  L96:
    > 
    > ```
    > SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;
    > ```
    > 
  L110:
    > 
    > ```
    > SET SGWCHARGECFG:HOMEOFFLINE=DISABLE,ROAMOFFLINE=ENABLE,VISITOFFLINE=ENABLE,SGWCGFLAG=USE_LOCAL;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（4）：['HOMEOFFLINE', 'ROAMOFFLINE', 'SGWCGFLAG', 'VISITOFFLINE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 4}（多值→atom 应考虑 decision_driven）
