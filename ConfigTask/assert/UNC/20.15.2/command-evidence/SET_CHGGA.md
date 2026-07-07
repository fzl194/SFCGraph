# 命令证据包：SET CHGGA
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/设置计费Ga接口参数(SET CHGGA)_26145378.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：![](设置计费Ga接口参数(SET CHGGA)_26145378.assets/notice_3.0-zh-cn_2.png)

计费参数的错误修改可能导致计费中心无法正确计费，需谨慎修改。 本命令部分参数的修改需要复位CDP才能生效，部分参数需要复位SPP和GTP才能生效，详细请参见命令联机帮助。

**适用网元：SGSN**

该命令用于设置计费Ga接口参数，包括SGSN生成话单的协议版本
**notes（规格/上限→应投影 atom rule）**：
- - 系统初次运行时，会执行系统初始设置值。
- 如果设置“CDR重发间隔（ITVRES）”、“硬盘操作失败告警次数门限（HDDETH）”、“硬盘空间不足门限（HDDFSL）”、“重定向帧最大占用率（REDICTFRMMAXOCCRATE）”，则只有在CDP进程重启之后才生效。
- 如果设置“GPRS CDR协议版本（GCR）”、“UMTS CDR协议版本（UCR）”、“R98 CDR版本（CHGV

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GCR | GPRS CDR协议版本 | 整网规划 | optional |  | <br>- “R98(R98)” |
| UCR | UMTS CDR协议版本 | 整网规划 | optional |  | <br>- “R99(R99)” |
| CHGVER98 | R98 CDR版本 | 整网规划 | optional |  | <br>- “CMCCV130(中国移动计费网关规范V1.3.0)”：表示遵循中国移动计费网关规范V |
| CHGVER99 | R99 CDR版本 | 整网规划 | optional |  | <br>- “GPP32015V360(3GPP 32.015 V3.6.0)”：表示遵循3GPP  |
| CHGVER4 | R4 CDR版本 | 整网规划 | optional |  | <br>- “GPP32215V440(3GPP 32.215 V4.4.0)”：表示遵循3GPP  |
| CHGVER5 | R5 CDR版本 | 整网规划 | optional |  | <br>- “GPP32215V560(3GPP 32.215 V5.6.0)”：表示遵循3GPP  |
| CHGVER6 | R6 CDR版本 | 整网规划 | optional |  | <br>- “GPP32251V660(3GPP 32.251 V6.6.0)”：表示遵循3GPP  |
| CHGVER7 | R7 CDR版本 | 整网规划 | optional |  | <br>- “GPP32251V740(3GPP 32.251 V7.4.0)”：表示遵循3GPP  |
| CHGVER9 | R9 CDR版本 | 整网规划 | optional |  | <br>- “GPP32251V940(3GPP 32.251 V9.4.0)”：表示遵循3GPP  |
| ITVRES | CDR重发间隔（s） | 整网规划 | optional |  | 1～10 |
| RSNUM | CDR重发次数 | 整网规划 | optional |  | 1～10 |
| HDDETH | 硬盘操作失败告警次数门限 | 整网规划 | optional |  | 1～10 |
| HDDFSL | 硬盘空间不足门限（%） | 整网规划 | optional |  | 50～90 |
| REDICTFRMMAXOCCRATE | 重定向帧最大占用率（%） | 整网规划 | optional |  | 20～80 |
| QOSVER | 话单QoS最高版本 | 整网规划 | optional |  | <br>- “R5(R5)” |
| GASENDUDPCHECK | 发送消息UDP校验 | 整网规划 | optional |  | <br>- “DISABLE(不生效)” |
| GAREVUDPCHECK | 接收消息UDP校验 | 整网规划 | optional |  | <br>- “DISABLE(不生效)” |
| CDROVERWRITE | 覆盖硬盘上话单文件 | 整网规划 | optional |  | <br>- “NO(不覆盖)” |
| IPPLCY | IP地址选择策略 | 整网规划 | optional |  | 枚举类型。在IPv4网络中，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011005

**md：`WSFD-011005/WSFD-011005 支持R98_R99_R4_R5_R6_R7的话单格式参考信息_92180152.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET CHGGA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/设置计费Ga接口参数(SET CHGGA)_26145378.md)
    > - [**LST CHGGA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/查询计费Ga接口参数(LST CHGGA)_72225059.md)
    > - [**DSP CHGGA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/显示计费Ga接口参数状态(DSP CHGGA)_26305194.md)

**md：`WSFD-011005/WSFD-011005 支持R98_R99_R4_R5_R6_R7的话单格式特性概述_92180151.md`**
- 操作步骤上下文（±2 行原文）：
  L66:
    > #### [原理概述](#ZH-CN_CONCEPT_0192180151)
    > 
    > UNC 支持R98、R99、R4、R5、R6、R7格式的话单，通过执行 [**SET CHGGA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/设置计费Ga接口参数(SET CHGGA)_26145378.md) 命令，可以分别给2G和3G用户指定一种话单格式，该命令还可以对各种话单格式所遵循的标准进行设置，关于话单的分类及各版本话单的详细介绍，请参见 [离线计费话单（SGSN）](../../../../业务专题/5G Core 计费解决方案/计费解决方案概述/计费原理/Ga_Gy接口离线_在线计费/Ga接口离线计费原理/离线计费话单（SGSN）_01_10018.md) 。
    > 
    > 举例来说，如果将参数 “GPRS CDR协议版本” 设置为 “R98” ，参数 “ UMTS CDR协议版本” 设置为 “R99” ，则：

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/设置计费Ga接口参数(SET CHGGA)_26145378.md)
    > - [**LST CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/查询计费Ga接口参数(LST CHGGA)_72225059.md)
    > - [**DSP CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/显示计费Ga接口参数状态(DSP CHGGA)_26305194.md)

**md：`WSFD-011201/离线计费话单（SGSN）_02556787.md`**
- 操作步骤上下文（±2 行原文）：
  L361:
    >     - 当硬盘占用量超过99％时，硬盘状态迁移为硬盘满状态。
    >     - 当硬盘占用量减少到95％以下时，硬盘状态从硬盘满迁移到硬盘空间不足。
    >   以硬盘空间不足告警门限配置为70％（即执行命令 **SET CHGGA** : HDDFSL=70;）时的实例说明硬盘空闲空间的状态变迁过程：
    >     1. 硬盘占用量处于上升时，硬盘空间从硬盘空间正常 -> 硬盘空间不足 -> 硬盘满状态迁移变化，如 [图17](#ZH-CN_TOPIC_0302556787__fig1658251784811) 所示。
    >       **图17** 硬盘空间不足时的状态迁移变化
  L381:
    >       ![](离线计费话单（SGSN）_02556787.assets/zh-cn_image_0302611122_2.png)
    >   **硬盘话单文件覆盖功能**
    >   大量缓存到硬盘上的话单文件使硬盘剩余空间逐渐减少，当硬盘使用空间达到配置的告警门限时，会触发硬盘剩余空间不足告警，此时，如果硬盘话单文件覆盖功能开关已打开（即已执行命令 **SET CHGGA** : CDROVERWRITE=YES;），系统会自动删除最早生成的话单文件，保留最新的话单文件。
    >   SGSN保证本特性中每次删除的话单文件是当前硬盘上最旧的话单文件，但是该文件不一定是整系统中最旧的文件。
    >   如果运营商通过SFTP功能把本地的话单文件上传到硬盘资源上，由于操作系统只提供了文件的最后修改时间，而没有办法获取文件创建时间，即此场景下，硬盘覆盖功能生效，但无法保证删除的话单文件是最旧的话单文件。

**md：`WSFD-011201/配置话单可靠性保证（SGSN）_01731121.md`**
- 数据规划表（该命令的参数行）：
  | **SET CHGGA** | 硬盘空间不足门限(%)（HDDFSL） | 90 | 全网规划 | 硬盘话单文件覆盖功能 |
  | **SET CHGGA** | 覆盖硬盘上话单文件（CDROVERWRITE） | YES | 全网规划 | 硬盘话单文件覆盖功能 |
- 任务示例脚本（该命令行）：
  `SET CHGGA:HDDFSL=90,CDROVERWRITE=YES;`
- 操作步骤上下文（±2 行原文）：
  L40:
    >   > 参数 “LRSNP” （配置本地话单序列号）固定选择 “PRESENT” （有）。
    > 3. 配置硬盘话单文件覆盖功能。
    >   **SET CHGGA**
    >   > **说明**
    >   > 参数 “CDROVERWRITE” （覆盖硬盘上话单文件）固定选择 “YES” （覆盖）。
  L61:
    > 
    > ```
    > SET CHGGA:HDDFSL=90,CDROVERWRITE=YES;
    > ```

### WSFD-011202

**md：`WSFD-011202/调测支持热计费功能_85008162.md`**
- 操作步骤上下文（±2 行原文）：
  L37:
    > > 2. 设置UMTS话单版本，以及UMTS CDR协议版本与CG的协议版本一致。
    > >   在SGSN MML窗口上执行命令 [**ADD CHGCG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) 设置CG的协议版本。
    > >   在SGSN MML窗口上执行命令 [**SET CHGGA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/计费Ga接口参数/设置计费Ga接口参数(SET CHGGA)_26145378.md) 设置UMTS话单版本为32.015 V3.a.0，以及UMTS CDR协议版本与CG的协议版本一致。
    > > 3. SGSN与支持32.015 V3.a.0话单版本的CG连接正常。
    > 

## ④ 自动比对
- 命令真相参数（19）：['CDROVERWRITE', 'CHGVER4', 'CHGVER5', 'CHGVER6', 'CHGVER7', 'CHGVER9', 'CHGVER98', 'CHGVER99', 'GAREVUDPCHECK', 'GASENDUDPCHECK', 'GCR', 'HDDETH', 'HDDFSL', 'IPPLCY', 'ITVRES', 'QOSVER', 'REDICTFRMMAXOCCRATE', 'RSNUM', 'UCR']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'全网规划': 2}（多值→atom 应考虑 decision_driven）
