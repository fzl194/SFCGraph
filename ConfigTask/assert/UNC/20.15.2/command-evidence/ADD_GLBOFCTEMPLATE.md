# 命令证据包：ADD GLBOFCTEMPLATE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/全局离线计费模板/增加全局离线计费模板（ADD GLBOFCTEMPLATE）_09896916.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

此命令用来配置全局离线计费配置，分GLOBAL类型和Charge Characteristic类型的全局离线模板。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为17。
- 整机最多可以配置16条Charge Characteristic类型的离线模板，外加1条全局类型的离线计费模板。
- 配置全局离线计费模板时，必须配置离线模板。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GLOBALFLAG | 全局记录 | local_planned | required | 无 | 枚举类型。 |
| CCVALUE | Charge Characteristic值 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCMASK | Charge Characteristic特定值掩码 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| CCPRIORITY | Charge Characteristic优先级 | local_planned | conditional | 无 | 整数类型，取值范围为0～65535。 |
| PGWTEMPLATE | PGW离线计费模板名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| SGWTEMPLATE | SGW离线计费模板名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| GGSNTEMPLATE | GGSN离线计费模板名 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**ADD CGGRPBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md)
    > - [**ADD SGWSEGGCHGMETH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW IMSI_MSISDN号段组计费方式/增加SGW IMSI_MSISDN Group Charge Method（ADD SGWSEGGCHGMETH）_09896995.md)
    > - [**ADD GLBOFCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/全局离线计费模板/增加全局离线计费模板（ADD GLBOFCTEMPLATE）_09896916.md)
    > - [**ADD FESTIVAL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/节假日/增加计费节假日表（ADD FESTIVAL）_09896827.md)
    > - [**ADD WEEKDAY**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/工作日/配置计费星期表（ADD WEEKDAY）_09896831.md)

**md：`WSFD-011201/配置离线计费参数（GGSN_SGW-C_PGW-C）_95923590.md`**
- 数据规划表（该命令的参数行）：
  | **ADD GLBOFCTEMPLATE** | 全局记录（GLOBALFLAG） | CHARGE_CHARACT | 本端规划 | 配置Charge Characteristic类型的全局离线模板 |
  | **ADD GLBOFCTEMPLATE** | Charge Characteristic值（CCVALUE） | 0x0003 | 本端规划 | 配置Charge Characteristic类型的全局离线模板 |
  | **ADD GLBOFCTEMPLATE** | PGW离线计费模板名（PGWTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置Charge Characteristic类型的全局离线模板 |
  | **ADD GLBOFCTEMPLATE** | SGW离线计费模板名（SGWTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置Charge Characteristic类型的全局离线模板 |
  | **ADD GLBOFCTEMPLATE** | 全局记录（GLOBALFLAG） | GLOBAL | 本端规划 | 配置GLOBAL类型的全局离线模板 |
  | **ADD GLBOFCTEMPLATE** | PGW离线计费模板名（PGWTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置GLOBAL类型的全局离线模板 |
  | **ADD GLBOFCTEMPLATE** | SGW离线计费模板名（SGWTEMPLATE） | offlinecharge-test | 已配置数据中获取 | 配置GLOBAL类型的全局离线模板 |
- 任务示例脚本（该命令行）：
  `ADD GLBOFCTEMPLATE:GLOBALFLAG=CHARGE_CHARACT,CCVALUE="0x3",CCMASK="0x3",CCPRIORITY=1,PGWTEMPLATE="offlinecharge-test",SGWTEMPLATE="offlinecharge-test";`
  `ADD GLBOFCTEMPLATE:GLOBALFLAG=GLOBAL,PGWTEMPLATE="offlinecharge-test",SGWTEMPLATE="offlinecharge-test";`
- 操作步骤上下文（±2 行原文）：
  L109:
    >       **ADD CHARGECHAR**
    >     b. 配置计费属性CC绑定OFCTemplate模板。
    >       **ADD GLBOFCTEMPLATE**
    > 5. 配置OFCTemplate模板绑定全局。
    >   **ADD GLBOFCTEMPLATE**
  L111:
    >       **ADD GLBOFCTEMPLATE**
    > 5. 配置OFCTemplate模板绑定全局。
    >   **ADD GLBOFCTEMPLATE**
    > 
    > ## [任务示例](#ZH-CN_OPI_0295923590)
  L167:
    >   ```
    >   ```
    >   ADD GLBOFCTEMPLATE:GLOBALFLAG=CHARGE_CHARACT,CCVALUE="0x3",CCMASK="0x3",CCPRIORITY=1,PGWTEMPLATE="offlinecharge-test",SGWTEMPLATE="offlinecharge-test";
    >   ```
    > 5. 任务四：配置全局的离线计费参数。

## ④ 自动比对
- 命令真相参数（7）：['CCMASK', 'CCPRIORITY', 'CCVALUE', 'GGSNTEMPLATE', 'GLOBALFLAG', 'PGWTEMPLATE', 'SGWTEMPLATE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3, '已配置数据中获取': 4}（多值→atom 应考虑 decision_driven）
