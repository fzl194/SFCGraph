# 命令证据包：SET SGWCHGMETH
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C**

该命令用于设置SGW计费方式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为17。
- 不允许配置ChargeCharValue和掩码取与操作后的值不等于ChargeCharValue。
- 不允许配置ChargeCharValue和掩码取与后的值，与当前已有配置的ChargeCharValue和对应掩码取与后的值相等。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | CHARGECHA

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CHARGECHAR | 计费属性 | local_planned | required | 无 | 枚举类型。 |
| CHARGECHARVALUE | 计费属性值 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCMASK | 计费属性掩码 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCPRIORITY | 计费属性优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～65535。 |
| OFFLINEFLAG | 是否离线计费 | local_planned | required | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L20:
    > - [**SET SGWCHARGECFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW计费基础参数/SGW计费配置（SET SGWCHARGECFG）_09896989.md)
    > - [**SET SGWAPNCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW APN计费方式/设置SGW APN计费方式（SET SGWAPNCHGMETH）_09896992.md)
    > - [**SET SGWCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/计费属性控制/设置SGW Charge Method（SET SGWCHGMETH）_09896985.md)
    > - [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)
    > - [**SET OFCTHRESHOLD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **SET SGWCHGMETH** | 计费属性（CHARGECHAR） | DEFAULT | 全网规划 | 配置SGW-C计费方式。 |
  | **SET SGWCHGMETH** | 是否离线计费（OFFLINEFLAG） | ENABLE | 全网规划 | 配置SGW-C计费方式。 |
- 任务示例脚本（该命令行）：
  `SET SGWCHGMETH: CHARGECHAR=DEFAULT, OFFLINEFLAG=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L69:
    > 3. 配置使能SGW-C的离线计费方式。
    >     a. 基于用户计费属性使能SGW-C的离线计费方式。
    >       **SET SGWCHGMETH**
    >     b. 基于APN使能SGW-C的离线计费方式。
    >       **SET SGWAPNCHGMETH**
  L114:
    > 
    > ```
    > SET SGWCHGMETH: CHARGECHAR=DEFAULT, OFFLINEFLAG=ENABLE;
    > ```
    > 

## ④ 自动比对
- 命令真相参数（5）：['CCMASK', 'CCPRIORITY', 'CHARGECHAR', 'CHARGECHARVALUE', 'OFFLINEFLAG']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 2}（多值→atom 应考虑 decision_driven）
