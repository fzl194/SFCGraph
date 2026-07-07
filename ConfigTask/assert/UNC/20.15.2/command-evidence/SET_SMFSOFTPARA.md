# 命令证据包：SET SMFSOFTPARA
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md`
> 用该命令的特性数：4

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF**

该命令用于设置SMF的软件参数信息。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| DT | DWORDNUM | DWORDVALUE | BITNUM | BITVALUE | BYTENUM | BYTEVALUE | STRINGNUM | STRINGVALUE |
| --- 

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| DT | 数据类型 | local_planned | required | 无。 | <br>- Dw（双字） |
| DWORDNUM | Dword索引 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是1~1500。 |
| DWORDVALUE | Dword值 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是0~4294967295。 |
| BITNUM | Bit索引 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是1~4000。 |
| BITVALUE | Bit值 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是0~1。 |
| BYTENUM | Byte索引 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是1~1200。 |
| BYTEVALUE | Byte值 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是0~255。 |
| STRINGNUM | String索引 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 整数类型，取值范围是1~30。 |
| STRINGVALUE | String值 | local_planned | conditional | 无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFS | 字符串类型，输入长度范围是1~64。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-215501

**md：`WSFD-215501/激活支持Category NB2接入（S_PGW-C）_77673142.md`**
- 任务示例脚本（该命令行）：
  `SET SMFSOFTPARA:DT=Bit,BITNUM=717,BITVALUE=1;`
- 操作步骤上下文（±2 行原文）：
  L32:
    >   [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
    > 3. 打开本特性的软参配置开关。
    >   [**SET SMFSOFTPARA**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277673142)
  L51:
    > 
    > ```
    > SET SMFSOFTPARA:DT=Bit,BITNUM=717,BITVALUE=1;
    > ```

### WSFD-201301

**md：`WSFD-201301/激活E-UTRAN和WLAN互操作_76948724.md`**
- 数据规划表（该命令的参数行）：
  | **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | 数据类型（DT） | Bit | 本端规划 | BIT719 该软参用于控制用户在non-3GPP和3GPP网络间切换时，是否允许双栈和单栈之间进行切换。 |
  | **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | Bit索引（BITNUM） | 719 | 本端规划 | BIT719 该软参用于控制用户在non-3GPP和3GPP网络间切换时，是否允许双栈和单栈之间进行切换。 |
  | **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | Bit值（BITVALUE） | 1 | 本端规划 | BIT719 该软参用于控制用户在non-3GPP和3GPP网络间切换时，是否允许双栈和单栈之间进行切换。 |
- 任务示例脚本（该命令行）：
  `SET SMFSOFTPARA: DT=Bit, BITNUM=719, BITVALUE=1;`
- 操作步骤上下文（±2 行原文）：
  L46:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置用户在non-3GPP和3GPP网络间切换时，允许双栈与单栈之间进行切换。
    >   **[SET SMFSOFTPARA](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)**
    > 3. 配置E-UTRAN和WLAN互操作控制属性。
    >     - 设置全局E-UTRAN和WLAN互操作控制属性。
  L74:
    > 
    > ```
    > SET SMFSOFTPARA: DT=Bit, BITNUM=719, BITVALUE=1;
    > ```
    > 

### WSFD-109101

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 任务示例脚本（该命令行）：
  `SET SMFSOFTPARA: DT=BIT, BITNUM=1202, BITVALUE=1;`
- 操作步骤上下文（±2 行原文）：
  L66:
    > 5. **可选：**如果PCRF不支持热备份功能，GGSN/PGW-C上需要开启failover增强功能。
    >     a. GGSN/PGW-C上开启failover增强功能。
    >       [**SET SMFSOFTPARA**](../../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)
    >       详细描述请参见 [BIT1202 控制Gx Failover增强功能是否生效](../../../../../../../OM参考/软件参数/UNC软件参数/业务软件参数/软件参数（SMF_GGSN_SGW-C_PGW-C）/PCC策略控制管理/BIT1202 控制Gx Failover增强功能是否生效_98644179.md) 。
    >     b. 配置GGSN/PGW-C发送的CCR-U消息中携带信元Called-Station-ID、User-Equipment-Info、Framed-IP-Address、Framed-IPv6-Prefix，Subscription-Id-Type和Subscription-Id携带MSISDN开关。
  L114:
    > 5. PCRF不支持热备时，开启failover增强功能并配置上报[步骤 5.b](#ZH-CN_OPI_0231422950__substep826311974175816)和[步骤 5.c](#ZH-CN_OPI_0231422950__substep1922626752175816)描述的需携带的参数。
    >   ```
    >   SET SMFSOFTPARA: DT=BIT, BITNUM=1202, BITVALUE=1;
    >   SET PCCMSGATTR: MSGTYPE=CCRU, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE, USREQUIPINFO=ENABLE, FRAMEDIPADDRESS=ENABLE, FRAMEDIPV6PREF=ENABLE;
    >   SET PCCMSGATTR: MSGTYPE=CCRT, MSISDN=ENABLE, CALLEDSTATIONID=ENABLE;

### WSFD-010802

**md：`WSFD-010802/激活Gx_Gy_Ga_Gi接口流控功能_30753120.md`**
- 数据规划表（该命令的参数行）：
  | **[SET SMFSOFTPARA](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | 数据类型（DT） | BYTE | 与对端协商 | 配置Gx接口是否支持基于Gx集中点的WAL流控功能，以及流控阈值。 |
  | **[SET SMFSOFTPARA](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | Byte索引（BYTENUM） | 863 | 与对端协商 | 配置Gx接口是否支持基于Gx集中点的WAL流控功能，以及流控阈值。 |
  | **[SET SMFSOFTPARA](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)** | Byte值（BYTEVALUE） | 40 | 与对端协商 | 配置Gx接口是否支持基于Gx集中点的WAL流控功能，以及流控阈值。 |
- 任务示例脚本（该命令行）：
  `SET SMFSOFTPARA:DT=BYTE,BYTENUM=863,BYTEVALUE=40;`
- 操作步骤上下文（±2 行原文）：
  L61:
    >   **[ADD RDSSVR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/RADIUS管理/连接管理/Radius服务器/增加RADIUS服务器（ADD RDSSVR）_09896756.md)**
    > 6. **可选：**通过软参BYTE863配置Gx接口是否支持基于Gx集中点的WAL流控功能，以及流控阈值。
    >   **[SET SMFSOFTPARA](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/软件参数管理/设置SMF软参（SET SMFSOFTPARA）_09653002.md)**
    > 
    > ## [任务示例](#ZH-CN_OPI_0230753120)
  L98:
    > 
    > ```
    > SET SMFSOFTPARA:DT=BYTE,BYTENUM=863,BYTEVALUE=40;
    > ```

## ④ 自动比对
- 命令真相参数（9）：['BITNUM', 'BITVALUE', 'BYTENUM', 'BYTEVALUE', 'DT', 'DWORDNUM', 'DWORDVALUE', 'STRINGNUM', 'STRINGVALUE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3, '与对端协商': 3}（多值→atom 应考虑 decision_driven）
