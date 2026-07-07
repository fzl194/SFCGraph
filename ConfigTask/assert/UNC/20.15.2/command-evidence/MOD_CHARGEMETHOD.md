# 命令证据包：MOD CHARGEMETHOD
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/修改计费方式（MOD CHARGEMETHOD）_09896796.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

MOD CHARGEMETHOD命令用来基于用户计费属性修改在线计费、离线计费和融合计费方式。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后只对新激活用户生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CHARGECHARACT | 计费属性 | global_planned | required | 无 | 枚举类型。 |
| CCVALUE | 计费属性值 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| MASK | 计费属性掩码 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| PRIORITY | 计费属性优先级 | global_planned | conditional | 无 | 整数类型，取值范围为1～65535。 |
| ONLINE | 在线计费开关 | global_planned | optional | 无 | 枚举类型。 |
| OFFLINE | 离线计费开关 | global_planned | optional | 无 | 枚举类型。 |
| CONVERGED | 融合计费开关 | global_planned | optional | 无 | 枚举类型。 |
| RGAPPLIED | 业务申请上报模式 | global_planned | conditional | 无 | 枚举类型。 |
| QBCSW | QBC计费开关 | global_planned | conditional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L54:
    >           - 如果使能融合计费，请执行[步骤 8](#ZH-CN_OPI_0289257219__step261013496208)。
    >           - 如果未使能融合计费，请执行[步骤 7.b](#ZH-CN_OPI_0289257219__substep1784820385463)。
    >     b. 执行 [**SET CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/设置计费控制配置（SET CHARGECTRL）_09896792.md) 命令，配置当前用户漫游、拜访、本地属性使能N40接口融合计费；执行 [**SET USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/设置User Profile的计费配置（SET USRPROFCHARGE）_09896814.md) 、 [**SET APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/设置APN的计费配置（SET APNCHARGECTRL）_09896817.md) 、 [**MOD CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/修改计费方式（MOD CHARGEMETHOD）_09896796.md) 命令，配置当前用户按照规划基于User Profile或DNN或CC使能融合计费，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 8. 检查用户N40接口是否开启了用户激活创建计费会话功能。
    >     a. 执行 [**LST CCT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/融合计费模板/查询融合计费模板（LST CCT）_09653820.md) 命令，查询与当前用户所使用的融合计费模板对应的 “CHF交互使能开关” 是否为 “激活发送” 。

## ④ 自动比对
- 命令真相参数（9）：['CCVALUE', 'CHARGECHARACT', 'CONVERGED', 'MASK', 'OFFLINE', 'ONLINE', 'PRIORITY', 'QBCSW', 'RGAPPLIED']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
