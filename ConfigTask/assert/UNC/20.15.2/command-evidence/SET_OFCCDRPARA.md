# 命令证据包：SET OFCCDRPARA
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md`
> 用该命令的特性数：8

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C、PGW-C、SMF**

![](配置离线计费话单参数（SET OFCCDRPARA）_09896905.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，配置SPCDRCONTROL=PGW_SGW_CDR后需检查流量容器占用率，防止资源耗尽引发用户激活成功率下降

该命令用于配置离线计费话单参数。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SPCDRCONTROL | PGWCDRLOTVSW | PGWCDRLOSDRATSW | PGWCDRLOSDAMBR | SRVNODEADDR | PSFCIFORMAT | CCFHCDRSW | R6EGCDRCCFHSW | LASTACTIVITYSW

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| GSNNODEIDPREFIX | gsn-node-id字段前缀 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～17。 |
| GNIDELIMITER | gsn-node-id字段分隔符 | local_planned | optional | 无 | 字符串类型，输入长度范围为1。 |
| SPCDRCONTROL | SP合一网关话单控制 | local_planned | optional | 无 | 枚举类型。 |
| PGWCDRLOTVSW | PGW-CDR携带List of Traffic Volume | local_planned | optional | 无 | 枚举类型。 |
| PGWCDRLOSDRATSW | PGW-CDR话单的List of Service Data携带RAT-Type | local_planned | optional | 无 | 枚举类型。 |
| PGWCDRLOSDAMBR | PGW-CDR话单List of Service Data容器携带APN-AMBR开关 | local_planned | optional | 无 | 枚举类型。 |
| SRVNODEADDR | GCDR话单的sgsnAddress值 | local_planned | optional | 无 | 枚举类型。 |
| PSFCIFORMAT | OCS故障导致用户离线后产生的话单pSFreeFormatData格式 | local_planned | optional | 无 | 枚举类型。 |
| CCFHCDRSW | CCFH强制产生话单开关 | local_planned | optional | 无 | 枚举类型。 |
| CCFHCDRCC | CCFH强制产生话单填充的Charging Characteristics值 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0 |
| R6EGCDRCCFHSW | R6 eGCRD支持CCFH强制生成话单 | local_planned | optional | 无 | 枚举类型。 |
| LASTACTIVITYSW | Last Activity功能开关 | local_planned | optional | 无 | 枚举类型。 |
| SGWLOTVQOSEXT | SGW-CDR流量容器携带扩展Qos参数开关 | 对端协商 | optional | 无 | 枚举类型。 |
| PGWLOTVQOSEXT | PGW-CDR流量容器携带扩展Qos参数开关 | 对端协商 | optional | 无 | 枚举类型。 |
| PGWLOSDQOSEXT | PGW-CDR业务容器携带扩展Qos参数开关 | 对端协商 | optional | 无 | 枚举类型。 |
| SGWLOTVCPEPS | SGW-CDR话单的LoTV携带CP CIoT EPS Optimisation Indicator | local_planned | optional | 无 | 枚举类型。 |
| SGWLOTVSPRATE | SGW-CDR话单的LoTV携带Serving PLMN Rate Control | local_planned | optional | 无 | 枚举类型。 |
| PGWLOSDSPRATE | PGW-CDR话单LoSD携带Serving PLMN Rate Control | local_planned | optional | 无 | 枚举类型。 |
| PGWLOSDAPNRATE | PGW-CDR话单的LoSD携带APN Rate Control | local_planned | optional | 无 | 枚举类型。 |
| PGWIPV6IFID | G-CDR/PGW-CDR中用户IPv6地址Interface Identifier填写方式 | global_planned | optional | 无 | 枚举类型。 |
| SGWIPV6IFID | SGW-CDR中用户IPv6地址Interface Identifier填写方式 | global_planned | optional | 无 | 枚举类型。 |
| CDRAFTERTCSW | 费率切换后强制产生话单开关 | local_planned | optional | 无 | 枚举类型。 |
| CDRAFTERTCCAUSE | 费率切换后强制产生话单的关闭原因 | local_planned | conditional | 无 | 枚举类型。 |
| STGENCRYPT | 话单缓存加密开关 | local_planned | optional | 无 | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-216104

**md：`WSFD-216104/WSFD-216104 基于APN的eMTC终端接入速率控制参考信息_75993426.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)
    > - [**LST CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)
    > - [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**LST OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)
    > - [**ADD DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/增加Diameter字典加载路径（ADD DIAMDICTPATH）_09897247.md)

**md：`WSFD-216104/激活基于APN的eMTC终端接入速率控制_77396887.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR中携带APN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277396887)

### WSFD-216105

**md：`WSFD-216105/WSFD-216105 基于服务PLMN的eMTC终端接入速率控制参考信息_75993431.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**RMV CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)
    > - [**LST CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)
    > - [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**LST OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)
    > - [**ADD DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/增加Diameter字典加载路径（ADD DIAMDICTPATH）_09897247.md)

**md：`WSFD-216105/激活基于服务PLMN的eMTC终端接入速率控制_77396889.md`**
- 操作步骤上下文（±2 行原文）：
  L46:
    >   [**ADD CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR或SGW-CDR中携带Serving PLMN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277396889)

### WSFD-215204

**md：`WSFD-215204/WSFD-215204 基于APN的NB-IoT终端接入速率控制参考信息（PGW-C）_77673131.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**RMV CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)
    > - [**LST CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)
    > - [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**LST OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)
    > - [**ADD DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/增加Diameter字典加载路径（ADD DIAMDICTPATH）_09897247.md)

**md：`WSFD-215204/激活基于APN的NB-IoT终端接入速率控制（PGW-C）_77673129.md`**
- 操作步骤上下文（±2 行原文）：
  L45:
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR中携带APN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277673129)

### WSFD-215205

**md：`WSFD-215205/WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制参考信息（S_PGW-C）_77673138.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**RMV CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)
    > - [**LST CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)
    > - [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**LST OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)
    > - [**ADD DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/增加Diameter字典加载路径（ADD DIAMDICTPATH）_09897247.md)

**md：`WSFD-215205/激活基于服务PLMN的NB-IoT终端接入速率控制（S_PGW-C）_77673136.md`**
- 操作步骤上下文（±2 行原文）：
  L47:
    >   [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
    > 6. **可选：**配置PGW-CDR或SGW-CDR中携带Serving PLMN Rate Control字段。
    >   [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0277673136)

### WSFD-011511

**md：`WSFD-011511/WSFD-011511 NSA用户数据话单生成和上报参考信息_28784144.md`**
- 操作步骤上下文（±2 行原文）：
  L17:
    > - **[**LST CDRFIELDTEMP**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)**
    > - **[**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)**
    > - **[**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)**
    > - **[**LST OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)**
    > 

**md：`WSFD-011511/激活NSA用户数据话单生成和上报_28784142.md`**
- 数据规划表（该命令的参数行）：
  | [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md) | SGW-CDR流量容器携带扩展Qos参数开关（SGWLOTVQOSEXT） | ENABLE | 与对端协商 | 可选配置，配置SGW-CDR和PGW-CDR话单中携带扩展Qos参数 |
  | [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md) | PGW-CDR流量容器携带扩展Qos参数开关（PGWLOTVQOSEXT） | ENABLE | 与对端协商 | 可选配置，配置SGW-CDR和PGW-CDR话单中携带扩展Qos参数 |
  | [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md) | PGW-CDR业务容器携带扩展Qos参数开关（PGWLOSDQOSEXT） | ENALBE | 与对端协商 | 可选配置，配置SGW-CDR和PGW-CDR话单中携带扩展Qos参数 |
- 任务示例脚本（该命令行）：
  `SET OFCCDRPARA:SGWLOTVQOSEXT=ENABLE,PGWLOTVQOSEXT=ENABLE,PGWLOSDQOSEXT=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L45:
    >   [**SET OFCTHRESHOLD**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/设置离线计费阈值（SET OFCTHRESHOLD）_09896910.md)
    > 4. （可选配置）配置SGW-CDR和PGW-CDR话单中携带扩展Qos参数。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0228784142)
  L70:
    > 
    > ```
    > SET OFCCDRPARA:SGWLOTVQOSEXT=ENABLE,PGWLOTVQOSEXT=ENABLE,PGWLOSDQOSEXT=ENABLE;
    > ```

### WSFD-011521

**md：`WSFD-011521/WSFD-011521 NSA 用户QoS管理参考信息_27675788.md`**
- 操作步骤上下文（±2 行原文）：
  L12:
    > 本特性相关的MML命令如下：
    > 
    > - [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**MOD DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/修改Diameter字典加载路径（MOD DIAMDICTPATH）_09897248.md)
    > - [**LOD DIAMDICT**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载字典/加载Diameter字典（LOD DIAMDICT）_09897254.md)

**md：`WSFD-011521/激活NSA用户QoS管理_27675786.md`**
- 数据规划表（该命令的参数行）：
  | [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md) | SGW-CDR流量容器携带扩展Qos参数开关（SGWLOTVQOSEXT） | ENABLE | 与对端协商 | 配置离线计费话单参数 |
  | [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md) | PGW-CDR流量容器携带扩展Qos参数开关（PGWLOTVQOSEXT） | ENABLE | 与对端协商 | 配置离线计费话单参数 |
  | [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md) | PGW-CDR业务容器携带扩展Qos参数开关（PGWLOSDQOSEXT） | ENABLE | 与对端协商 | 配置离线计费话单参数 |
- 任务示例脚本（该命令行）：
  `SET OFCCDRPARA:SGWLOTVQOSEXT=ENABLE,PGWLOTVQOSEXT=ENABLE,PGWLOSDQOSEXT=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L53:
    > 1. 进入 “MML命令行-UNC” 窗口。
    > 2. 配置PGW-CDR/SGW-CDR容器携带扩展QoS参数。
    >   [**SET OFCCDRPARA**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > 3. 设置Diameter字典加载路径。
    >   [**MOD DIAMDICTPATH**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/修改Diameter字典加载路径（MOD DIAMDICTPATH）_09897248.md)
  L78:
    > 
    > ```
    > SET OFCCDRPARA:SGWLOTVQOSEXT=ENABLE,PGWLOTVQOSEXT=ENABLE,PGWLOSDQOSEXT=ENABLE;
    > ```
    > 

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于GGSN_SGW-C_PGW-C）_29423866.md`**
- 操作步骤上下文（±2 行原文）：
  L38:
    > - [**SET GLBCDRFLDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/全局话单字段模板/设置全局话单模板（SET GLBCDRFLDTEMP）_09896895.md)
    > - [**FOC GENERATECDR**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费维护/强制生成话单/强制生成话单（FOC GENERATECDR）_09897016.md)
    > - [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
    > - [**SET CDRSTRGSTATUS**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存目录/设置话单缓存目录状态（SET CDRSTRGSTATUS）_09897006.md)
    > - [**SET CDRSTORAGECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/计费缓存/缓存控制/设置话单存储控制参数（SET CDRSTORAGECTRL）_09897001.md)

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **SET OFCCDRPARA** | SP合一网关话单控制（SPCDRCONTROL） | PGW_SGW_CDR | 本端规划 | 配置SP合一用户产生SGW话单。 |
- 操作步骤上下文（±2 行原文）：
  L80:
    >       **ADD SGWSEGGCHGMETH**
    > 5. **可选** ：配置SP合一用户产生SGW话单。
    >   **SET OFCCDRPARA**
    > 
    > ## [任务示例](#ZH-CN_OPI_0302167102)

**md：`WSFD-011201/配置话单可选功能（GGSN_SGW-C_PGW-C）_95923448.md`**
- 数据规划表（该命令的参数行）：
  | **SET OFCCDRPARA** | CCFH强制产生话单开关（CCFHCDRSW） | ENABLE | 本端规划 | 用户进行在线计费发生CCFH动作处理后，可在话单中增加CCFH标识。 |
  | **SET OFCCDRPARA** | CCFH强制产生话单填充的Charging Characteristics值（CCFHCDRCC） | 0x1000 | 本端规划 | 用户进行在线计费发生CCFH动作处理后，可在话单中增加CCFH标识。 |
- 任务示例脚本（该命令行）：
  `SET OFCCDRPARA: CCFHCDRSW=ENABLE,CCFHCDRCC="0x1000";`
- 操作步骤上下文（±2 行原文）：
  L51:
    >       > 该命令可基于用户（IMSI、MSISDN）强制产生话单。
    >     b. 配置在线计费CCFH处理时是否强制产生话单，以及强制产生话单时话单中charging characteristic字段的取值、R6版本的eG-CDR是否支持CCFH处理。
    >       **SET OFCCDRPARA**
    > 2. 配置话单缓存功能。
    >     a. 配置锁定话单缓存目录。
  L80:
    >     b. 配置在线计费CCFH处理时是否强制产生话单。
    >       ```
    >       SET OFCCDRPARA: CCFHCDRSW=ENABLE,CCFHCDRCC="0x1000";
    >       ```
    > 2. 配置话单缓存功能。

**md：`WSFD-011201/配置话单字段（GGSN_SGW-C_PGW-C）_95923364.md`**
- 数据规划表（该命令的参数行）：
  | **SET OFCCDRPARA** | List of Traffic Volume | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR是否携带流量容器（ListOfTrafficVolume）。 |
  | **SET OFCCDRPARA** | RAT Type | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR的业务容器（ListOfServiceData）是否携带RAT Type。 |
  | **SET OFCCDRPARA** | APN-AMBR | 配置PGW-CDR的字段携带方式。可以控制PGW-CDR的业务容器（ListOfServiceData）是否携带APN-AMBR。 |

### WSFD-109001

**md：`WSFD-109001/配置DCC处理动作_95923447.md`**
- 操作步骤上下文（±2 行原文）：
  L73:
    >       **SET TXTIMER**
    >     6. 配置在线计费CCFH处理时是否强制产生话单，强制产生话单时话单中charging characteristic字段的取值；配置R6版本的eG-CDR是否支持CCFH处理。
    >       **SET OFCCDRPARA**
    >     7. 配置业务持续时长。
    >       **SET HOLDINGTIME**

## ④ 自动比对
- 命令真相参数（24）：['CCFHCDRCC', 'CCFHCDRSW', 'CDRAFTERTCCAUSE', 'CDRAFTERTCSW', 'GNIDELIMITER', 'GSNNODEIDPREFIX', 'LASTACTIVITYSW', 'PGWCDRLOSDAMBR', 'PGWCDRLOSDRATSW', 'PGWCDRLOTVSW', 'PGWIPV6IFID', 'PGWLOSDAPNRATE', 'PGWLOSDQOSEXT', 'PGWLOSDSPRATE', 'PGWLOTVQOSEXT', 'PSFCIFORMAT', 'R6EGCDRCCFHSW', 'SGWIPV6IFID', 'SGWLOTVCPEPS', 'SGWLOTVQOSEXT', 'SGWLOTVSPRATE', 'SPCDRCONTROL', 'SRVNODEADDR', 'STGENCRYPT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'与对端协商': 6, '本端规划': 3}（多值→atom 应考虑 decision_driven）
