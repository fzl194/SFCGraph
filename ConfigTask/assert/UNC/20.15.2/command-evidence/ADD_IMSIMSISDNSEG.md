# 命令证据包：ADD IMSIMSISDNSEG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于配置IMSI/MSISDN号码段。设置号段后，可以通过ADD SUBSCRIBERIDSEGGRP命令配置到号段组。最终可以达到根据号段组选择USERPROFILE作为本地策略、根据号段选择OCS、根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等业务功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为12000。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SEGMENTNAME | IMSI/MSISDN号段名称 | global_planned | required | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| SEGMENTTYPE | IMSI/MSISDN号段类型 | global_planned | required | 无 | 枚举类型。 |
| SEGSTART | 号段起始字符串 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～17。 |
| SEGEND | 号段结束字符串 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～17。 |
| WILDCARDSEG | 通配号段字符串 | global_planned | conditional | 无 | 字符串类型，输入长度范围为1～47。仅支持“*”、“?”和数字。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L30:
    > - [**ADD RULEBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/规则绑定/增加用户模板和规则的绑定关系（ADD RULEBINDING）_09897216.md)
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD PCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    > - [**ADD PCRFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD IMSIMSISDNSEG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md) | IMSI/MSISDN号段名称（SEGMENTNAME） | msisdnseg1<br>msisdnseg2 | 本端规划 | 配置IMSI/MSISDN号码段 |
  | [**ADD IMSIMSISDNSEG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md) | IMSI/MSISDN号段类型（SEGMENTTYPE） | MSISDN | 全网规划 | 配置IMSI/MSISDN号码段 |
  | [**ADD IMSIMSISDNSEG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md) | 号段起始字符串（SEGSTART） | 18900000000<br>18950000000 | 全网规划 | 配置IMSI/MSISDN号码段 |
  | [**ADD IMSIMSISDNSEG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md) | 号段结束字符串（SEGEND） | 18949999999<br>18999999999 | 全网规划 | 配置IMSI/MSISDN号码段 |
- 任务示例脚本（该命令行）：
  `ADD IMSIMSISDNSEG:SEGMENTNAME="msisdnseg1",SEGMENTTYPE=MSISDN,SEGSTART="18900000000",SEGEND="18949999999";`
  `ADD IMSIMSISDNSEG:SEGMENTNAME="msisdnseg2",SEGMENTTYPE=MSISDN,SEGSTART="18950000000",SEGEND="18999999999";`
- 操作步骤上下文（±2 行原文）：
  L96:
    >   [**SET LICENSESWITCH**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. **可选：**配置IMSI或MSISDN号码段。
    >   [**ADD IMSIMSISDNSEG**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    >   > **说明**
    >   > 规划特定号段的用户触发PCC功能时需要配置。
  L169:
    > 2. 配置MSISDN号段。
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="msisdnseg1",SEGMENTTYPE=MSISDN,SEGSTART="18900000000",SEGEND="18949999999";
    >   ```
    >   ```
  L172:
    >   ```
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="msisdnseg2",SEGMENTTYPE=MSISDN,SEGSTART="18950000000",SEGEND="18999999999";
    >   ```
    > 3. 配置PCRF分组信息，设置pcrf_group_1组内的PCRF按配置比例进行负荷分担，pcrf_group_2组内的PCRF之间为主备备份。

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**SET CDRTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费话单产生开关（SET CDRTRIGGER）_09896911.md)
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
  L26:
    > - [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD CGGRPBINDING**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/GTPP信令/CG组管理/CG组绑定/增加CG组绑定关系（ADD CGGRPBINDING）_09896884.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **ADD IMSIMSISDNSEG** | IMSI/MSISDN号段名称（SEGMENTNAME） | testmsisdn1 | 本端规划 | 配置IMSI/MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | IMSI/MSISDN号段类型（SEGMENTTYPE） | IMSI | 本端规划 | 配置IMSI/MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | 号段起始字符串（SEGSTART） | 13900100100 | 本端规划 | 配置IMSI/MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | 号段结束字符串（SEGEND） | 13900100199 | 本端规划 | 配置IMSI/MSISDN号码段。 |
- 任务示例脚本（该命令行）：
  `ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn1",SEGMENTTYPE=IMSI,SEGSTART="13900100100",SEGEND="13900100199";`
- 操作步骤上下文（±2 行原文）：
  L74:
    > 4. 设置SGW-C基于号段组的计费方式。
    >     a. 配置IMSI及MSISDN号码段。
    >       **ADD IMSIMSISDNSEG**
    >     b. 配置IMSI/MSISDN/IMEISV号码段组。
    >       **ADD SUBSCRIBERIDSEGGRP**
  L124:
    > 
    > ```
    > ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn1",SEGMENTTYPE=IMSI,SEGSTART="13900100100",SEGEND="13900100199";
    > ```
    > 

### WSFD-104003

**md：`WSFD-104003/WSFD-104003 IPv6在线计费参考信息_29019969.md`**
- 操作步骤上下文（±2 行原文）：
  L47:
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)

### WSFD-109001

**md：`WSFD-109001/WSFD-109001 Gy_Diameter在线计费参考信息_29035079.md`**
- 操作步骤上下文（±2 行原文）：
  L47:
    > - [**ADD TARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/费率切换组/配置费率切换组（ADD TARIFFGROUP）_09896836.md)
    > - [**SET GLBTARIFFGROUP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/费率切换/全局费率切换组/配置全局费率切换组（SET GLBTARIFFGROUP）_09896840.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD SUBSCRIBERIDSEGGRP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN IMEISV号段组/增加IMSI_MSISDN_IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）_65997002.md)
    > - [**ADD VIRTUALAPNRULE**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/虚拟APN映射管理/虚拟APN映射策略/增加虚拟APN映射策略配置（ADD VIRTUALAPNRULE）_09652380.md)

**md：`WSFD-109001/配置OCS负荷分担_95923468.md`**
- 数据规划表（该命令的参数行）：
  | **ADD IMSIMSISDNSEG** | IMSI/MSISDN号段名称（SEGMENTNAME） | testmsisdn1<br>testmsisdn2 | 本端规划 | 配置MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | IMSI/MSISDN号段类型（SEGMENTTYPE） | MSISDN | 本端规划 | 配置MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | 号段起始字符串（SEGSTART） | 13900100100<br>13900100200 | 本端规划 | 配置MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | 号段结束字符串（SEGEND） | 13900100199<br>13900100299 | 本端规划 | 配置MSISDN号码段。 |
- 任务示例脚本（该命令行）：
  `ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn1",SEGMENTTYPE=MSISDN,SEGSTART="13900100100",SEGEND="13900100199";`
  `ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn2",SEGMENTTYPE=MSISDN,SEGSTART="13900100200",SEGEND="13900100299";`
- 操作步骤上下文（±2 行原文）：
  L82:
    >       **ADD OCS**
    >     b. 配置IMSI及MSISDN号码段。
    >       **ADD IMSIMSISDNSEG**
    >     c. 配置IMSI及MSISDN号码段组。
    >       **ADD SUBSCRIBERIDSEGGRP**
  L234:
    >   //配置号段，此处以MSISDN为例，如果需要也可以使用IMSI。
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn1",SEGMENTTYPE=MSISDN,SEGSTART="13900100100",SEGEND="13900100199";
    >   ```
    >   ```
  L240:
    >   ```
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn2",SEGMENTTYPE=MSISDN,SEGSTART="13900100200",SEGEND="13900100299";
    >   ```
    >   ```

**md：`WSFD-109001/配置基于CC+用户号段选择OCS_95923602.md`**
- 数据规划表（该命令的参数行）：
  | **ADD IMSIMSISDNSEG** | IMSI/MSISDN号段名称（SEGMENTNAME） | testmsisdn1<br>testmsisdn2 | 本端规划 | 配置MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | IMSI/MSISDN号段类型（SEGMENTTYPE） | MSISDN | 本端规划 | 配置MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | 号段起始字符串（SEGSTART） | 13900100100<br>13900100200 | 本端规划 | 配置MSISDN号码段。 |
  | **ADD IMSIMSISDNSEG** | 号段结束字符串（SEGEND） | 13900100199<br>13900100299 | 本端规划 | 配置MSISDN号码段。 |
- 任务示例脚本（该命令行）：
  `ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn1",SEGMENTTYPE=MSISDN,SEGSTART="13900100100",SEGEND="13900100199";`
  `ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn2",SEGMENTTYPE=MSISDN,SEGSTART="13900100200",SEGEND="13900100299";`
- 操作步骤上下文（±2 行原文）：
  L74:
    >       **ADD OCS**
    >     b. 配置IMSI及MSISDN号码段。
    >       **ADD IMSIMSISDNSEG**
    >     c. 配置IMSI及MSISDN号码段组。
    >       **ADD SUBSCRIBERIDSEGGRP**
  L145:
    >   //配置号段，此处以MSISDN为例，如果需要也可以使用IMSI。
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn1",SEGMENTTYPE=MSISDN,SEGSTART="13900100100",SEGEND="13900100199";
    >   ```
    >   ```
  L151:
    >   ```
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="testmsisdn2",SEGMENTTYPE=MSISDN,SEGSTART="13900100200",SEGEND="13900100299";
    >   ```
    >   ```

### WSFD-102202

**md：`WSFD-102202/WSFD-102202 P-CSCF故障时IMS业务恢复参考信息_26216213.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - **[RMV PCSCFIP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/删除P-CSCF地址配置（RMV PCSCFIP）_09653290.md)**
    > - **[LST PCSCFIP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/查询P-CSCF地址配置（LST PCSCFIP）_09653781.md)**
    > - **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
    > - **[MOD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/修改IMSI和MSISDN号段（MOD IMSIMSISDNSEG）_09897129.md)**
    > - **[LST IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/查询IMSI和MSISDN号段（LST IMSIMSISDNSEG）_09897131.md)**

### WSFD-102701

**md：`WSFD-102701/WSFD-102701 VoNR基础语音业务参考信息_11685430.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - **[**RMV PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/删除P-CSCF地址配置（RMV PCSCFIP）_09653290.md)**
    > - **[**LST PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/查询P-CSCF地址配置（LST PCSCFIP）_09653781.md)**
    > - **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
    > - **[**MOD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/修改IMSI和MSISDN号段（MOD IMSIMSISDNSEG）_09897129.md)**
    > - **[**LST IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/查询IMSI和MSISDN号段（LST IMSIMSISDNSEG）_09897131.md)**

### WSFD-102702

**md：`WSFD-102702/WSFD-102702 EPS Fallback参考信息_82764866.md`**
- 操作步骤上下文（±2 行原文）：
  L23:
    > - **[**RMV PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/删除P-CSCF地址配置（RMV PCSCFIP）_09653290.md)**
    > - **[**LST PCSCFIP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/IMS管理/P-CSCF管理/P-CSCF的IP地址/查询P-CSCF地址配置（LST PCSCFIP）_09653781.md)**
    > - **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
    > - **[**MOD IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/修改IMSI和MSISDN号段（MOD IMSIMSISDNSEG）_09897129.md)**
    > - **[**LST IMSIMSISDNSEG**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/查询IMSI和MSISDN号段（LST IMSIMSISDNSEG）_09897131.md)**

### WSFD-011132

**md：`WSFD-011132/激活Gx over DRA（静态路由+BFD组网）_29368407.md`**
- 任务示例脚本（该命令行）：
  `ADD IMSIMSISDNSEG:SEGMENTNAME="imsi_msisdn_segment_1",SEGMENTTYPE=MSISDN,SEGSTART="13800000000",SEGEND="13849999999";`
  `ADD IMSIMSISDNSEG:SEGMENTNAME="imsi_msisdn_segment_1",SEGMENTTYPE=MSISDN,SEGSTART="13800000000",SEGEND="13849999999";`
- 操作步骤上下文（±2 行原文）：
  L180:
    > 11. 开启全局缺省PCC开关并设置域名绑定。
    >     a. 配置IMSI或MSISDN号码段。
    >       **[ADD IMSIMSISDNSEG](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)**
    >     b. 使能全局PCC开关。
    >       **[SET PCCFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)**
  L270:
    >   //配置全局缺省的PCC开关，将PCRF域pcrf.huawei.com和用户号段imsi_msisdn_segment_1绑定。
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="imsi_msisdn_segment_1",SEGMENTTYPE=MSISDN,SEGSTART="13800000000",SEGEND="13849999999";
    >   ```
    >   ```
  L388:
    >   //配置全局缺省的PCC开关，将PCRF域pcrf.huawei.com和用户号段imsi_msisdn_segment_1绑定。
    >   ```
    >   ADD IMSIMSISDNSEG:SEGMENTNAME="imsi_msisdn_segment_1",SEGMENTTYPE=MSISDN,SEGSTART="13800000000",SEGEND="13849999999";
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（5）：['SEGEND', 'SEGMENTNAME', 'SEGMENTTYPE', 'SEGSTART', 'WILDCARDSEG']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 13, '全网规划': 3}（多值→atom 应考虑 decision_driven）
