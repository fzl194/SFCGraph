# 命令证据包：SET AMFPLCYFUNC
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：AMF**

该命令用于设置AMF策略功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| AMNOTIFYSW | UENOTIFYSW | OLDAMPLCY | DYNRFSPSW | RFSPCLRMODE | DFTRFSP | DYNNISW | OVERLAPAREAPLCY | NEIGHBORLOCSW | HRAMAGINGSW | HRAMAGINGTMR | OLD

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| AMNOTIFYSW | AM策略关闭实时通知PCF开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| UENOTIFYSW | UE策略关闭实时通知PCF开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| OLDAMPLCY | N14接口是否传递AM策略 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| DYNRFSPSW | 灵活选频功能开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| RFSPCLRMODE | RFSP清除方式 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- WITHOUT_RFSP（未携带RFSP） |
| DFTRFSP | 默认RFSP | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | 整数类型，取值范围是0~256。 |
| DYNNISW | 是否开启动态NI功能 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| FULLNAME | 默认运营商全称 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | 字符串类型，输入长度范围是0~255。 |
| SHORTNAME | 默认运营商简称 | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | 字符串类型，输入长度范围是0~255。 |
| OVERLAPAREAPLCY | 重叠区域生效策略 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- PUBLIC_AREA（公网区域） |
| NEIGHBORLOCSW | 相邻位置区域处理开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| HRAMAGINGSW | 高铁AM偶联老化开关 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |
| HRAMAGINGTMR | 高铁AM偶联老化时长(min) | global_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | 整数类型，取值范围是1~1440，单位是分钟。 |
| OLDUEPLCY | N14接口是否传递UE策略 | global_planned | optional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFP | <br>- “NO（否）”：否 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-230001

**md：`WSFD-230001/WSFD-230001 动态UE Logo下发参考信息_45929684.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [ADD NGPRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA标识管理/增加5G PRA（ADD NGPRA）_44006470.md)
    > - [ADD NGPRAMEM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA位置成员管理/增加PRA位置区成员（ADD NGPRAMEM）_44006471.md)
    > - [SET AMFPLCYFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > - [ADD MECAREA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/本地特色业务区域管理/本地特色业务区域标识管理/增加5G MEC区域信息（ADD MECAREA）_34412856.md)
    > - [ADD MECAREAGNB](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/本地特色业务区域管理/本地特色业务区域gNodeB成员管理/增加5G MEC gNodeB信息（ADD MECAREAGNB）_34732056.md)
  L27:
    > - [SET AMFSBICMPT](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/AMF服务化接口兼容性参数管理/设置AMF服务化接口兼容性参数（SET AMFSBICMPT）_98011756.md)
    > - [SET NGMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/MM协议参数管理/5G移动性管理/设置5G移动性管理功能（SET NGMMFUNC）_09653748.md)
    > - [SET AMFPLCYFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0000002145929684)

### WSFD-230002

**md：`WSFD-230002/WSFD-230002 支持RFSP选频选网参考信息_81170597.md`**
- 操作步骤上下文（±2 行原文）：
  L14:
    > - [ADD NGPRA](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA标识管理/增加5G PRA（ADD NGPRA）_44006470.md)
    > - [ADD NGPRAMEM](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/网络开放管理/5G PRA管理/5G PRA位置成员管理/增加PRA位置区成员（ADD NGPRAMEM）_44006471.md)
    > - [SET AMFPLCYFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > 
    > #### [告警](#ZH-CN_TOPIC_0000002181170597)

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - [**ADD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/增加AM策略和UE策略控制参数（ADD AMUEPLCYCTRL）_09652143.md)
    > - [**MOD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)
    > - [**SET AMFPLCYFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > - [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)
    > - [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 操作步骤上下文（±2 行原文）：
  L126:
    >           - 修改应用网络侧规划的AM策略/UE策略的用户范围。
    >     6. （可选）执行 [步骤 5](#ZH-CN_OPI_0172467890__substep11273101124010) 后，设置实时通知PCF删除AM/UE偶联。默认不实时通知PCF删除AM/UE偶联，即用户下次激活时使用本地配置的AM策略/UE策略。
    >       [**SET AMFPLCYFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    >           - 实时通知PCF删除AM偶联时，将“AMNOTIFYSW”设置为“YES”。AMF通知PCF后，会同步删除AM偶联及从网络侧下发的AM策略。
    >           - 实时通知PCF删除UE偶联时，将“UENOTIFYSW”设置为“YES”。AMF通知PCF后，会同步删除UE偶联及从网络侧下发的UE策略。

## ④ 自动比对
- 命令真相参数（14）：['AMNOTIFYSW', 'DFTRFSP', 'DYNNISW', 'DYNRFSPSW', 'FULLNAME', 'HRAMAGINGSW', 'HRAMAGINGTMR', 'NEIGHBORLOCSW', 'OLDAMPLCY', 'OLDUEPLCY', 'OVERLAPAREAPLCY', 'RFSPCLRMODE', 'SHORTNAME', 'UENOTIFYSW']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
