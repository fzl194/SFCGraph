# 命令证据包：MOD APNCHGMODE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费模式/修改基于APN的计费接口选择方式（MOD APNCHGMODE）_72001549.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：![](修改基于APN的计费接口选择方式（MOD APNCHGMODE）_72001549.assets/notice_3.0-zh-cn_2.png)

修改基于APN的计费接口选择方式不当可能选错计费策略接口，相应计费策略接口未配置时会导致计费相关流程失败，进而影响用户使用业务，比如用户无法正常激活。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于修改不同的APN在
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后只对新激活用户生效。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字 |
| TMACCTYPE | 指定终端和接入类型 | local_planned | required | 无 | <br>- “UE5G_RAT4G（5G终端4G接入）”：5G终端4G接入是指在4G接入的PDN激活 |
| BY5GSIWKI | 按5GS互操作指示选择计费接口 | local_planned | conditional | 无 | <br>- False（否） |
| FORCED | 指定的计费接口 | local_planned | conditional | 无 | <br>- “GaGyMode（GaGy模式）”：GaGy模式 |
| FORSGWONLY | 作为SGW计费模式 | local_planned | conditional | 无 | <br>- GaGyMode（GaGy模式） |
| FORVSMFONLY | 作为V-SMF计费模式 | global_planned | conditional | 无 | <br>- “GaGyMode（GaGy模式）”：GaGy模式 |
| ISMFCHGSW | I-SMF是否支持计费 | global_planned | conditional | 无 | <br>- DISABLE（不使能） |
| BY5GCNRI | 按5GC无限制接入标识选择计费接口 | local_planned | conditional | 无 | <br>- False（否） |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/调测融合计费的计费会话创建功能_89257219.md`**
- 操作步骤上下文（±2 行原文）：
  L49:
    >           - 如果计费模式选择为N40接口，请执行[步骤 7](#ZH-CN_OPI_0289257219__step382183311511)。
    >           - 如果计费模式选择为GaGy接口，请执行[步骤 6.b](#ZH-CN_OPI_0289257219__substep359365010164)。
    >     b. 执行 [**SET CHGMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费模式/设置计费接口选择方式（SET CHGMODE）_09651465.md) / [**MOD APNCHGMODE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费模式/修改基于APN的计费接口选择方式（MOD APNCHGMODE）_72001549.md) 命令，配置指定用户计费接口采用N40接口，即 “FORCED” 参数取值为 “NchfMode” ，请再次执行 [步骤 3](#ZH-CN_OPI_0289257219__step2585105420194) 。
    > 7. 检查用户N40接口融合计费是否使能。
    >     a. 执行 [**LST CHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/用户属性计费控制/查询计费控制配置（LST CHARGECTRL）_09896793.md) 命令，查询当前用户漫游、拜访、本地属性是否使能了N40接口融合计费；执行 [**LST USRPROFCHARGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/User Profile计费控制/查询User Profile的计费配置（LST USRPROFCHARGE）_09896815.md) 、 [**LST APNCHARGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/APN计费配置/查询APN的计费配置（LST APNCHARGECTRL）_09896818.md) 、 [**LST CHARGEMETHOD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费控制/计费属性计费控制/查询计费方式（LST CHARGEMETHOD）_09896798.md) 命令，查看当前用户是否按预期规划基于User Profile或DNN或CC使能了融合计费。

## ④ 自动比对
- 命令真相参数（8）：['APN', 'BY5GCNRI', 'BY5GSIWKI', 'FORCED', 'FORSGWONLY', 'FORVSMFONLY', 'ISMFCHGSW', 'TMACCTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
