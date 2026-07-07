# 命令证据包：SET CDRTRIGGER
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用来配置离线计费话单产生开关。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 只有ADD OFCTemplate后才能配置该命令。
- 优先级的默认值255表示该开关采用默认优先级。默认优先级由高到低顺序为计费条件改变、Serving Node更新、MS时区更新、CDR RAT更新、Serving Node PLMN标识更新，用户配置优先级的开关比使用默认优先级的开关优先级高，未配置优先级的开关保持默认优先级顺

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| OFCTEMPLATENAME | 离线计费模板名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| CDRTRIGRATCHNG | CDR RAT更新 | local_planned | optional | 无 | 枚举类型。 |
| CDRTRIGRATPRIOR | RAT更新优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～100。 |
| CDRTRIGSNCHNG | Serving Node更新 | local_planned | optional | 无 | 枚举类型。 |
| CDRTRIGSNPRIOR | Serving Node更新优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～100。 |
| CDRTRIGTIMEZONE | MS时区更新 | local_planned | optional | 无 | 枚举类型。 |
| CDRTRIGMAXCHNG | 计费条件改变 | local_planned | optional | 无 | 枚举类型。 |
| CDRTRIMAXCHGPRI | 计费条件改变优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～100。 |
| CDRTRIGTZPRIOR | MS时区优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～100。 |
| CDRTRIGPLMNCHNG | Serving Node PLMN标识更新 | local_planned | optional | 无 | 枚举类型。 |
| CDRTRIGPLMNPRIO | Serving Node PLMN标识优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～100。 |
| CDRTRIGMOEXC | CDR MO Exception Data Counter更新 | local_planned | optional | 无 | 枚举类型。 |
| CDRTRIGMOEXCPRI | MO Exception Data Counter更新优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～100。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD OFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/增加离线计费模板（ADD OFCTEMPLATE）_09896908.md)
    > - [**SET OFCTHRESHOLD**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
    > - [**SET CDRTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **SET CDRTRIGGER** | 离线计费模板名（OFCTEMPLATENAME） | offlinecharge-test | 已配置数据中获取 | 话单产生条件 |
  | **SET CDRTRIGGER** | CDR RAT更新（CDRTRIGRATCHNG） | DISABLE | 本端规划 | 话单产生条件 |
  | **SET CDRTRIGGER** | Serving Node更新（CDRTRIGSNCHNG） | ENABLE | 本端规划 | 话单产生条件 |
  | **SET CDRTRIGGER** | 计费条件改变（CDRTRIGMAXCHNG） | ENABLE | 本端规划 | 话单产生条件 |
  | **SET CDRTRIGGER** | MS时区更新（CDRTRIGTIMEZONE） | DISABLE | 本端规划 | 话单产生条件 |
  | **SET CDRTRIGGER** | Serving Node PLMN标识更新（CDRTRIGPLMNCHNG） | ENABLE | 本端规划 | 话单产生条件 |
- 任务示例脚本（该命令行）：
  `SET CDRTRIGGER: OFCTEMPLATENAME="offlinecharge-test",CDRTRIGRATCHNG=DISABLE,CDRTRIGTIMEZONE=DISABLE,CDRTRIGPLMNCHNG=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L86:
    >       **SET OFCTHRESHOLD**
    >     c. 配置话单产生条件。
    >       **SET CDRTRIGGER**
    >     d. 配置话单容器产生条件。
    >       **SET CONTAINERTRIGGER**
  L143:
    >   ```
    >   ```
    >   SET CDRTRIGGER: OFCTEMPLATENAME="offlinecharge-test",CDRTRIGRATCHNG=DISABLE,CDRTRIGTIMEZONE=DISABLE,CDRTRIGPLMNCHNG=ENABLE;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（13）：['CDRTRIGMAXCHNG', 'CDRTRIGMOEXC', 'CDRTRIGMOEXCPRI', 'CDRTRIGPLMNCHNG', 'CDRTRIGPLMNPRIO', 'CDRTRIGRATCHNG', 'CDRTRIGRATPRIOR', 'CDRTRIGSNCHNG', 'CDRTRIGSNPRIOR', 'CDRTRIGTIMEZONE', 'CDRTRIGTZPRIOR', 'CDRTRIMAXCHGPRI', 'OFCTEMPLATENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 5}（多值→atom 应考虑 decision_driven）
