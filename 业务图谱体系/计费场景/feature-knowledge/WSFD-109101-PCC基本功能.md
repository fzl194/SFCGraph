# WSFD-109101 PCC基本功能（SMF/PGW-C/AMF侧）知识文档

## 概述

### 定义

PCC（Policy and Charging Control）基本功能是UNC（SMF/PGW-C/AMF）侧的策略和计费控制功能。UNC作为策略控制执行功能（PCEF-C），通过Gx接口（2G/3G/4G）或N7/N15/N28服务化接口（5G）与PCRF/PCF交互，接收并执行动态策略规则；同时UNC也支持本地静态策略（本地PCC）模式。本特性与UDG侧的GWFD-020351 PCC基本功能配合，构成完整的PCC策略执行体系：UNC负责策略决策接收和规则管理，UDG负责用户面策略执行。

### 适用NF

| 网元 | 角色 | 适用场景 | 最低版本 |
|------|------|----------|----------|
| SMF | 策略控制执行功能（PCEF-C） | 5G SM策略偶联、N7接口 | UNC 20.0.0 |
| PGW-C | 策略控制执行功能（PCEF-C） | 2G/3G/4G Gx接口 | UNC 20.3.0 |
| AMF | 接入和移动性策略执行 | 5G AM策略偶联、UE策略偶联 | UNC 20.0.0 |
| GGSN | 策略控制执行功能（PCEF-C） | 2G/3G Gx接口 | UNC 20.3.0 |
| UPF/PGW-U/GGSN-U | 用户面策略执行 | 配合UNC执行策略 | UDG 20.0.0/20.3.0 |

### 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 5G PCC基本功能首次发布（AMF+SMF）。 |
| 01 | 20.3.0 | 2G/3G/4G PCC基本功能（Gx接口）首次发布（PGW-C/GGSN）。 |

### License要求

| NF | License控制项 | 说明 |
|----|--------------|------|
| AMF | 82209964 LKV2PCCBF01 PCC基本功能 | AM策略、UE策略 |
| SMF/PGW-C/GGSN | 82207979 LKV3W9SPCC11 PCC基本功能 | SM策略、Gx策略 |

### 前置条件

- 完成UNC初始配置。
- 完成加载License。
- UDG侧已完成GWFD-020351 PCC基本功能配置（用户面策略执行）。
- 2G/3G/4G场景：完成WSFD-104508 SCTP配置。
- 5G场景：完成NRF发现配置。

### 规格限制

| 参数 | 规格 |
|------|------|
| 每个PCRF组内PCRF数（2/3/4G） | 32 |
| 系统PCRF总数（2/3/4G） | 100 |
| PCRF组总数（2/3/4G） | 100 |
| UserProfile模板数 | 5000 |
| 每QoS Flow规则数（5G） | 50 |

### 遵循标准

| 标准编号 | 标准名称 | 适用范围 |
|----------|----------|----------|
| 3GPP 23.203 | Policy and Charging Control Architecture | 2G/3G/4G |
| 3GPP 29.212 | Policy and Charging Control over Gx Reference Point | 2G/3G/4G Gx接口 |
| 3GPP 29.213 | Policy and Charging Control signalling flows and QoS parameter mapping | 2G/3G/4G |
| 3GPP 29.229 | Cx and Dx Interfaces Based on the Diameter Protocol | Diameter协议 |
| 3GPP 23.214 | Architecture enhancements for control and user plane separation | CU分离 |
| 3GPP 29.244 | Interface between the Control Plane and the User Plane Nodes | N4接口 |
| 3GPP 23.501 | System Architecture for the 5G System; Stage 2 | 5G |
| 3GPP 23.502 | Procedures for the 5G System; Stage 2 | 5G |
| 3GPP 23.503 | Policy and Charging Control Framework for the 5G System; Stage 2 | 5G |
| 3GPP 29.507 | Access and Mobility Policy Control Service; Stage 3 | 5G AM策略 |
| 3GPP 29.512 | Session Management Policy Control Service; Stage 3 | 5G SM策略 |
| 3GPP 29.513 | Policy and Charging Control signalling flows and QoS parameter mapping | 5G |

---

## 核心概念

### 1. CU分离架构下的PCC

PCC基本功能采用CU分离架构：
- **UNC（控制面）**：SMF/PGW-C/GGSN作为PCEF-C，负责与PCRF/PCF的信令交互、规则管理和策略决策。
- **UDG（用户面）**：UPF/PGW-U/GGSN-U作为PCEF-U，负责业务数据流检测、流量统计、QoS执行、重定向等。

规则和UserProfile可以指定下发目标：
- **主锚点UPF**：默认下发到主锚点UPF。
- **辅锚点UPF**：通过DNAI绑定，下发到指定辅锚点UPF。
- **两者同时**：同时下发到主锚点和辅锚点UPF。

### 2. 策略分类（5G）

5G PCC包含三种策略类型：

| 策略类型 | NF | 内容项 | 说明 |
|----------|-----|--------|------|
| AM策略 | AMF | SAR（Service Area Restrictions） | 服务区域限制 |
| AM策略 | AMF | RFSP Index | RAT/Frequency Selection Priority |
| UE策略 | AMF | ANDSP | Access Network Discovery and Selection Policy |
| UE策略 | AMF | URSP | UE Route Selection Policy |
| SM策略 | SMF | Session Rules（会话规则） | Session-AMBR、缺省QoS |
| SM策略 | SMF | PCC Rules（PCC规则） | SDF级QoS/计费控制 |

### 3. 规则类型

| 规则类型 | 定义来源 | 存储位置 | 下发方式 | 适用场景 |
|----------|----------|----------|----------|----------|
| 动态规则 | PCRF/PCF动态生成 | UNC仅临时存储 | PCRF/PCF主动下发或RAR推送 | PCRF/PCF实时策略控制 |
| 预定义规则 | PCRF/PCF仅发送规则名 | UNC和UDG均有预配置 | PCRF/PCF通过名称引用 | 固定策略、高性能场景 |
| 预定义规则组（UserProfile） | PCRF/PCF发送UserProfile名 | UNC和UDG均有预配置 | PCRF/PCF通过名称引用 | 多规则打包下发 |
| 本地规则 | UNC本地配置 | UNC和UDG均有预配置 | 无PCRF/PCF，本地安装 | 无PCRF/PCF部署的场景 |

### 4. 规则优先级

- 每条规则有全局优先级值（Priority），值越小优先级越高。
- 动态规则与预定义规则优先级相同时，动态规则优先。
- PCRF/PCF可为动态规则指定优先级；本地预定义规则的优先级通过ADD RULE命令配置。

### 5. IP-CAN会话（2G/3G/4G Gx）

IP-CAN会话是Gx接口上的策略控制基本单元，生命周期包含三个阶段：

| 阶段 | UNC→PCRF消息 | PCRF→UNC消息 | 触发条件 |
|------|-------------|-------------|----------|
| 建立 | CCR-I（Credit-Control-Request Initial） | CCA-I（Credit-Control-Answer Initial） | 用户激活 |
| 更新 | CCR-U（Update）或接收RAR | CCA-U或发送RAA | 事件触发/策略更新 |
| 终止 | CCR-T（Terminate） | CCA-T（Terminate） | 用户去激活 |

### 6. 专有承载管理（2G/3G/4G Gx）

| 操作 | 触发条件 | 方向 |
|------|----------|------|
| 专有承载激活 | PCRF下发新QoS/ARP规则 | PCRF→UNC→UDG |
| 专有承载更新 | 规则QoS/ARP变化 | PCRF→UNC→UDG |
| 专有承载去激活 | 规则去激活/删除 | PCRF→UNC→UDG或UNC主动触发 |

### 7. PCRF/PCF冗余与负荷分担

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| 主备模式 | 主用PCRF故障时切换到备用 | 高可靠性场景 |
| 轮询模式 | 按轮询方式分配会话 | 简单负荷分担 |
| 百分比模式 | 按配置权重分配会话 | 精细化负荷分担 |

PCRF组（PCRFGROUP）用于管理冗余和负荷分担，组内可配置各PCRF的百分比权重。5G N7接口支持GROUPID或PRIORITY两种负荷分担模式。

### 8. 迟滞时间

规则激活/去激活时间切换的迟滞时间，默认10分钟。用于避免规则在短时间内频繁切换激活状态。

### 9. PCF发现与选择（5G）

**AMF侧PCF发现：**
- 从旧AMF获取PCF信息（切换场景）
- 本地配置（AMFPCFSELPARAM）
- 通过NRF查询

**SMF侧PCF选择因素：**
- AMF提供的PCF信息（首选）
- 本地策略配置
- NRF查询
- 选择维度：SUPI号段、DNN、S-NSSAI、SUPI范围（PCF Serving Scope）

### 10. 接口模式选择（5G N7 vs 2/3/4G Gx）

当同一UNC同时支持5G和4G用户时，接口模式选择优先级：
1. **PCF实例级**：通过ADD PCCCHGMODEBYPCFID配置，指定PCF实例使用N7。
2. **APN/DNN级**：通过ADD APNPOLICYMODE配置，指定APN使用Gx或N7。
3. **全局级**：通过SET POLICYMODE配置默认接口模式。

---

## 原理与流程

### 1. 2G/3G/4G Gx接口信令流程

#### 1.1 IP-CAN会话建立

```
UE → GGSN/PGW-C(UNC) → PCRF
1. 用户发起PDP/PDN激活
2. UNC发送CCR-I到PCRF（携带IMSI、APN、UE-IP、RAT-Type等）
3. PCRF返回CCA-I（携带PCC规则、事件触发、QoS信息）
4. UNC将规则下发到UDG，建立承载
```

#### 1.2 IP-CAN会话更新

两种触发方式：
- **UNC主动上报（CCR-U）**：事件触发条件满足时，UNC发送CCR-U到PCRF。
- **PCRF主动推送（RAR）**：PCRF发送Re-Auth-Request到UNC，UNC响应RAA。

#### 1.3 IP-CAN会话终止

```
1. 用户去激活
2. UNC发送CCR-T到PCRF
3. PCRF返回CCA-T
4. UNC通知UDG删除规则和承载
```

#### 1.4 Supported Features动态协商

Gx接口支持能力协商：
1. CCR-I中携带Supported-Features AVP
2. CCA-I中PCRF返回支持的Feature列表
3. 双方取交集确定可用Feature
4. 通过ADD PCRF命令配置Supported-Features动态协商开关和Feature列表

### 2. 5G策略偶联流程

#### 2.1 AM策略偶联

**建立流程：**
1. UE注册到AMF
2. AMF发送Npcf_AMPolicyControl_Create Request到PCF（携带SUPI、GPSI、接入类型、PEI等）
3. PCF返回Npcf_AMPolicyControl_Create Response（携带SAR策略、RFSP Index等）
4. AMF通知RAN/UE

**修改流程（三种触发场景）：**
- 触发条件满足（如位置变化、RFSP变化）
- AMF变化（可复用原PCF）
- PCF策略变化（PCF通过UpdateNotify通知）

**终止流程：**
- UE去注册、PCF变更、PCF主动终止

#### 2.2 UE策略偶联

**建立流程：**
1. AMF发送Npcf_UEPolicyControl_Create Request到PCF
2. PCF返回Response（携带ANDSP、URSP策略）
3. AMF通过MANAGE UE POLICY COMMAND下发到UE

**修改流程：**与AM策略类似，三种触发场景。

**终止流程：**Npcf_UEPolicyControl_Delete Request/Response。

#### 2.3 SM策略偶联

**建立流程：**
1. UE发起PDU会话建立
2. SMF发送Npcf_SMPolicyControl_Create Request到PCF
3. PCF返回Response（携带Session Rules + PCC Rules）
4. SMF将规则下发到UPF

**SM策略内容：**
- **Session Rules**：Session-AMBR、缺省QoS（5QI/ARP）
- **PCC Rules**：SDF模板、QoS参数（5QI/ARP/GBR/MBR）、计费参数、门控状态

### 3. Event Triggers（事件触发/PCR Triggers）

#### 3.1 Gx接口Event Triggers（2/3/4G）

| Event Trigger ID | 描述 | 上报条件 |
|-----------------|------|----------|
| SGSN_CHANGE | SGSN变化 | 用户移动 |
| QOS_CHANGE | QoS变化 | 承载QoS修改 |
| RAI_CHANGE | 路由区变化 | 用户移动 |
| TAI_CHANGE | 跟踪区变化 | 用户移动 |
| ECGI_CHANGE | ECGI变化 | 用户移动 |
| RAT_CHANGE | RAT类型变化 | 用户切换 |
| USER_LOCATION_CHANGE | 用户位置变化 | 用户移动 |
| REVALIDATION_TIMEOUT | 重验证超时 | 定时器超时 |
| UE_IP_CHANGE | UE IP变化 | IP地址变更 |
| DEFAULT_EPS_BEARER_QOS_CHANGE | 缺省承载QoS变化 | HSS签约变更 |
| AN_GW_CHANGE | 接入网关变化 | 网关切换 |
| RESOURCE_MODIFICATION_REQUEST | 资源修改请求 | UE请求资源 |
| PLMN_CHANGE | PLMN变化 | 用户漫游 |
| DEFAULT_ACCESS_CHANGE | 缺省接入变化 | 接入变更 |
| CGI_CHANGE | CGI变化 | 用户移动 |
| MAX_MBR_CHANGED | 最大MBR变化 | 签约变更 |
| REMOVE_MBR_ENFORCEMENT | 移除MBR执行 | 签约变更 |
| PO_C_AVAILABILITY_CHANGE | PO-C可用性变化 | 网关变化 |
| USAGE_REPORT | 使用量报告 | 用量阈值 |

#### 3.2 N7接口PCR Triggers（5G SMF）

5G SM策略支持25+种PCR Triggers，上报条件分三类：
- **SMF默认上报**：SMF主动上报的事件
- **PCF订阅上报**：PCF通过策略订阅的事件
- **PCF订阅+请求上报**：PCF订阅且需请求报告的事件

关键PCR Triggers包括：LOC_CH（位置变化）、PRA_CH（Presence Reporting Area变化）、SERV_AREA_CH（服务区变化）、RFSP_CH（RFSP变化）、ALLOWED_NSSAI_CH（允许的NSSAI变化）、USAGE_REPORT（使用量报告）等。

#### 3.3 N15接口PCR Triggers（5G AMF）

AMF侧PCR Triggers：LOC_CH、PRA_CH、SERV_AREA_CH、RFSP_CH、ALLOWED_NSSAI_CH。

### 4. QoS映射（2G/3G/4G Gx）

Gx接口支持GPRS/UMTS QoS与EPC QoS的映射：

| GPRS/UMTS参数 | EPC Gx AVP | 说明 |
|---------------|-----------|------|
| Traffic Class | QoS-Class-Identifier | 业务类型映射 |
| Maximum Bit Rate (UL/DL) | Maximum-Requested-Bandwidth-UL/DL | 最大比特率 |
| Guaranteed Bit Rate (UL/DL) | Guaranteed-Bitrate-UL/DL | 保证比特率 |
| Delivery Order | 不直接映射 | 通过5QI间接表达 |
| Maximum SDU Size | 不直接映射 | 通过5QI间接表达 |
| SDU Error Ratio | 不直接映射 | 通过5QI间接表达 |

### 5. Gx Failover功能

#### 5.1 基本Failover

**前提条件：**
- PCRF配置为主备或负荷分担模式
- UNC本地支持Failover
- PCRF间使用相同的LOCALHOSTNAME（同一Diameter链路组）
- PCRF支持CC-Session-Failover AVP
- PCRF支持热备（Hot Standby）

**触发机制：**
1. UNC发送Diameter消息后启动Tx定时器
2. Tx定时器超时未收到响应
3. UNC切换到备用PCRF重新发送

**配置命令：**
- ADD PCRF（配置PCRF信息）
- ADD PCRFGROUP（FAILOVERSW=ENABLE）
- SET PCCTIMER（APPRETRYTIMEOUT参数）
- SET PCCMSGATTR（消息属性配置）

#### 5.2 增强Failover（BIT1202）

当PCRF不支持热备时，启用增强Failover：
- 备用PCRF从CCR-U消息重建会话
- 软参配置：SET SMFSOFTPARA（BIT1202=1）
- 适用于非热备PCRF的场景

### 6. QoS能力开放功能

UNC通过私有Restif接口提供QoS能力开放：
- **功能**：SBC通过HTTP接口向UNC查询用户的PCRF ID
- **接口**：Restif接口（HTTP/BSF方式）
- **协议**：HTTP/1.1
- **交互**：queryPCRFRequest / queryPCRFResponse消息

### 7. N7 Failover（5G）

5G N7接口Failover机制：
- PCF主备配置
- 支持GROUPID或PRIORITY两种负荷分担模式
- Failover仅尝试一次
- 失败后按SET PCCFAILACTION配置处理

### 8. 异常处理

#### 8.1 PENDING_TRANSACTION处理（5G N7）

- PCF返回PENDING_TRANSACTION（400错误码）
- SMF根据SET PCCTIMER的PENDRETRYTIMES和PENDRETRYTIMER参数重试
- 重试次数耗尽后按SET PCCFAILACTION处理

#### 8.2 回退到本地PCC（5G）

- SMF发送DEA SMCTX消息到UPF，携带FAIL_HANDLE_TYPE=PCC_ROLLBACK
- UPF收到后按本地PCC规则处理
- 回退后按SET PCCFAILACTION的在线保持时间配置决定是否允许新用户上线

#### 8.3 Gx接口异常处理（2/3/4G）

7种异常场景通过SET PCCFAILACTION和ADD RESULTCODECTRL配置处理策略：

| 异常场景 | 典型处理策略 |
|----------|------------|
| PCRF无响应 | 回退到本地PCC或拒绝 |
| PCRF返回失败 | 根据Result-Code配置处理 |
| 链路中断 | Failover到备用PCRF |
| 规则安装失败 | 拒绝用户或降级处理 |
| CCR-U发送失败 | 保持当前策略或回退 |
| 规则更新失败 | 保持或回退 |
| 资源不足 | 拒绝或降级 |

**SET FHBYPASS（紧急旁路）**：
- 最高优先级的故障旁路处理
- 必须获得客户书面授权后才能启用
- 启用后所有PCC用户按非PCC方式处理

---

## 配置规则

### 1. PCC使能层级（2/3/4G Gx）

PCC功能使能分三个层级，上层开关控制下层是否生效：

| 层级 | 命令 | 说明 |
|------|------|------|
| 全局 | SET PCCFUNC | 控制Home/Roam/Visit用户的PCC开关 |
| APN | SET APNPCCFUNC | 控制特定APN的PCC开关 |
| 号段 | ADD GLBPCRFGROUP | 控制特定号段使用的PCRF组 |

### 2. PCRF组选择优先级（2/3/4G Gx）

| 优先级 | 来源 | 命令 | 说明 |
|--------|------|------|------|
| 1（最高） | APN绑定 | ADD PCRFGRPBNDAPN | 指定APN使用的PCRF组 |
| 2 | 号段绑定 | ADD GLBPCRFGROUP | 指定号段使用的PCRF组 |
| 3（最低） | 全局缺省 | SET DFTGLBPCRFGRP | 全局缺省PCRF组 |

### 3. 动态PCC配置流程（2/3/4G Gx）

```
步骤1：License配置
  LST LICENSESWITCH → SET LICENSESWITCH（LKV3W9SPCC11）

步骤2：基础数据配置
  ADD IMSIMSISDNSEG（IMSI/MSISDN号段）

步骤3：PCRF对接配置
  ADD PCRF → ADD PCRFGROUP → ADD PCRFBINDGRP → SET DFTGLBPCRFGRP

步骤4：PCC功能使能
  SET PCCFUNC（使能Home/Roam/Visit）

步骤5：APN级配置
  ADD PCRFGRPBNDAPN → SET APNPCCFUNC

步骤6：预定义规则配置（可选）
  ADD RULE → ADD RULEBINDDNAI（规则绑定DNAI）

步骤7：预定义规则组配置（可选）
  ADD USERPROFILE → ADD RULEBINDING → ADD USRPROBINDDNAI（UserProfile绑定DNAI）
```

### 4. 本地PCC配置流程（2/3/4G Gx）

当无PCRF部署时，使用本地静态规则：

```
步骤1：License配置
步骤2：关闭动态PCC
  SET PCCFUNC（DISABLE所有开关）
步骤3：PCC模板配置
  ADD PCCTEMPLATE（INITIALFAILACT=FORBIDDEN）
步骤4：APN级配置
  SET APNPCCFUNC
步骤5：QoS映射
  ADD QOSPROP
步骤6：策略组配置
  ADD PCCPOLICYGRP
步骤7：规则配置
  ADD RULE
步骤8：UserProfile配置
  ADD USERPROFILE → ADD RULEBINDING
步骤9：用户模板组配置
  ADD USRPROFGROUP → ADD UPBINDUPG → ADD APNUSRPROFG
步骤10（可选）：多UserProfile安装
  ADD PCCPBINDUPG
```

### 5. 与PCRF对接数据配置（2/3/4G Gx）

#### 5.1 标准场景（不同PGW-U用户IP）

```
VPN配置 → SET CONCENPOINT → ADD LOGICINF → ADD DIAMLOCINFO
→ ADD PCRF → ADD DIAMPEERADDR → ADD DIAMCONNGRP → ADD DIAMCONNECTION
```

#### 5.2 用户IP重叠场景

当多个PGW-U的用户IP存在重叠时，需要额外配置：
- ADD LOCALHOSTGRP（本端主机组）
- ADD LOCALHOSTBIND（本端主机绑定）
- ADD GXUPFGROUP（Gx UPF组）
- ADD UPFBINDGXUPFGRP（UPF绑定Gx UPF组）
- ADD UPFGLOCGBNDGRP（UPF组绑定本端主机组）
- ADD UPFGBINDLOCG（UPF组绑定本端主机组）

### 6. 5G AMF配置流程

```
步骤1：License配置
  LST LICENSESWITCH → SET LICENSESWITCH（LKV2PCCBF01）

步骤2：PCF选择策略
  ADD PCFSELPLCY

步骤3：AM/UE策略控制
  ADD AMUEPLCYCTRL →（可选）MOD AMUEPLCYCTRL

步骤4：AMF策略功能
  SET AMFPLCYFUNC

步骤5：NGMM用户数据
  ADD NGMMSUBDATA

步骤6：AMF对等选择功能
  SET AMFPEERSELFUNC
```

### 7. 5G SMF配置流程

```
步骤1：License配置
  LST LICENSESWITCH → SET LICENSESWITCH（LKV3W9SPCC11）

步骤2：PCC功能使能
  SET PCCFUNC

步骤3：N7消息属性控制
  SET N7RCVATTRCTRL → SET N7SNDATTRCTRL

步骤4：PCC模板
  ADD PCCTEMPLATE

步骤5：APN级配置
  SET APNPCCFUNC

步骤6（可选）：预定义规则和策略组
  ADD PCCPOLICYGRP → ADD RULE → ADD USERPROFILE

步骤7：用户模板组
  ADD USRPROFGROUP → ADD APNUSRPROFG

步骤8（可选）：接口模式选择
  SET POLICYMODE → ADD APNPOLICYMODE → ADD PCCCHGMODEBYPCFID

步骤9（可选）：PCF Serving Scope
  ADD PCFSSCOPE → ADD USRTAIRANGE → ADD PCFSSCOPEBIND
```

### 8. 异常场景配置（2/3/4G Gx）

```
步骤1：配置异常处理策略
  SET PCCFAILACTION（全局异常处理策略）

步骤2：配置返回码控制
  ADD RESULTCODECTRL（按Result-Code配置处理方式）

步骤3（可选）：配置紧急旁路
  SET FHBYPASS（需客户书面授权）
```

### 9. QoS能力开放配置

```
步骤1：VPN和IP配置
  ADD VPNINST → ADD LOGICIP

步骤2：HTTP链路配置
  ADD HTTPLEGRP → ADD HTTPLE（CLIENT+SERVER）

步骤3：SBI应用配置
  ADD SBIAPLE（NFType=BSF）

步骤4：HTTP协议配置
  SET HTTPCONF（HTTP1.1）

步骤5：功能开关
  SET SMCOMMFUNC（PCRFQRYSW=ENABLE）
```

### 10. Gx Failover配置

```
步骤1：PCRF配置
  ADD PCRF（配置主备PCRF）

步骤2：PCRF组配置
  ADD PCRFGROUP（FAILOVERSW=ENABLE）

步骤3：定时器配置
  SET PCCTIMER（APPRETRYTIMEOUT）

步骤4（可选）：增强Failover
  SET SMFSOFTPARA（BIT1202=1）

步骤5：消息属性配置
  SET PCCMSGATTR
```

---

## 配置案例

### 案例1：2G/3G/4G动态PCC基本配置

**场景**：PGW-C通过Gx接口连接2个PCRF（主备模式），为Home用户启用PCC。

```
// 1. License使能
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 2. 集中点模式
SET CONCENPOINT:MODE=CONCENTRATION;

// 3. 逻辑接口
ADD LOGICINF:NAME="gxif1/0/0",IPV4ADDR1="10.8.10.1",IPV4MASK1="255.255.255.255",VPNNAME="vpn_gxif";

// 4. Diameter本端信息
ADD DIAMLOCINFO:LOCALHOST="pgw_1",LOCALREALM="huawei.com";

// 5. PCRF配置
ADD PCRF:HOSTNAME="pcrf_1",REALM="example.com";
ADD PCRF:HOSTNAME="pcrf_2",REALM="example.com";

// 6. PCRF对端地址
ADD DIAMPEERADDR:PEERHOSTNAME="pcrf_1",PEERADDR="10.11.21.59";
ADD DIAMPEERADDR:PEERHOSTNAME="pcrf_2",PEERADDR="10.11.21.60";

// 7. Diameter链路组和链路
ADD DIAMCONNGRP:GROUPNAME="gx_grp";
ADD DIAMCONNECTION:CONNNAME="gx_conn_1",GROUPNAME="gx_grp",LOCALHOST="pgw_1",PEERHOSTNAME="pcrf_1";
ADD DIAMCONNECTION:CONNNAME="gx_conn_2",GROUPNAME="gx_grp",LOCALHOST="pgw_1",PEERHOSTNAME="pcrf_2";

// 8. PCRF组（主备模式）
ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_1",SHAREMODE=MASTER_SLAVE,FAILOVERSW=ENABLE;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_1",PERCENTAGE=100;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_2",PERCENTAGE=0;
SET MASTERPCRF:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_1";

// 9. 全局缺省PCRF组
SET DFTGLBPCRFGRP:PCRFGRPNAME="pcrf_group_1";

// 10. PCC功能使能
SET PCCFUNC:HOMESWITCH=ENABLE;

// 11. PCC模板
ADD PCCTEMPLATE:TEMPLATENAME="pcc_tpl_1",INITIALFAILACT=FORBIDDEN;
SET APNPCCFUNC:APN="pccnet",PCCSWITCH=ENABLE,TEMPLATENAME="pcc_tpl_1";
```

### 案例2：5G SMF动态PCC基本配置

**场景**：SMF通过N7接口连接PCF，为DNN启用5G PCC。

```
// 1. License使能
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 2. PCC功能使能
SET PCCFUNC:HOMESWITCH=ENABLE;

// 3. N7消息属性控制
SET N7RCVATTRCTRL:...;
SET N7SNDATTRCTRL:...;

// 4. PCC模板
ADD PCCTEMPLATE:TEMPLATENAME="sm_pcc_tpl",INITIALFAILACT=FORBIDDEN;

// 5. DNN级配置
SET APNPCCFUNC:APN="internet",PCCSWITCH=ENABLE,TEMPLATENAME="sm_pcc_tpl";

// 6. 全局接口模式（5G使用N7）
SET POLICYMODE:POLICYMODE=N7;

// 7. 预定义规则（可选）
ADD RULE:RULENAME="rule_video",PRIORITY=10;
ADD PCCPOLICYGRP:POLICYGRPNAME="policy_grp_1";
```

### 案例3：本地PCC配置（无PCRF）

**场景**：未部署PCRF，PGW-C使用本地静态规则。

```
// 1. License使能
SET LICENSESWITCH:LICITEM="LKV3W9SPCC11",SWITCH=ENABLE;

// 2. 关闭动态PCC
SET PCCFUNC:HOMESWITCH=DISABLE,ROAMSWITCH=DISABLE,VISITSWITCH=DISABLE;

// 3. PCC模板
ADD PCCTEMPLATE:TEMPLATENAME="local_tpl",INITIALFAILACT=FORBIDDEN;

// 4. APN配置
SET APNPCCFUNC:APN="internet",PCCSWITCH=DISABLE,TEMPLATENAME="local_tpl";

// 5. QoS映射
ADD QOSPROP:...;

// 6. 策略组
ADD PCCPOLICYGRP:POLICYGRPNAME="local_policy_grp";

// 7. 规则
ADD RULE:RULENAME="local_rule_1",PRIORITY=10;

// 8. UserProfile
ADD USERPROFILE:PROFILENAME="profile_1";
ADD RULEBINDING:PROFILENAME="profile_1",RULENAME="local_rule_1";

// 9. 用户模板组
ADD USRPROFGROUP:GROUPNAME="user_grp_1";
ADD UPBINDUPG:GROUPNAME="user_grp_1",PROFILENAME="profile_1";
ADD APNUSRPROFG:APN="internet",GROUPNAME="user_grp_1";
```

### 案例4：PCRF负荷分担配置

**场景**：2个PCRF按40:60比例负荷分担。

```
ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_1",SHAREMODE=PERCENTAGE;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_1",PERCENTAGE=40;
ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",HOSTNAME="pcrf_2",PERCENTAGE=60;
SET DFTGLBPCRFGRP:PCRFGRPNAME="pcrf_group_1";
```

### 案例5：异常处理配置

```
// 1. 异常处理策略
SET PCCFAILACTION:FAILACTION=ROLLBACK_LOCAL,ONLINEHOLDTIME=3600;

// 2. Failover ALL（指定时间后全部Failover）
SET PCCFAILACTION:FAILACTION=FAILOVER_ALL,DURATIONTIMER=300;

// 3. 返回码控制
ADD RESULTCODECTRL:RESULTCODE=5012,ACTION=ROLLBACK_LOCAL;

// 4. 紧急旁路（需书面授权）
SET FHBYPASS:SWITCH=ENABLE;
```

---

## 验证与调测

### 1. 验证PCRF链路状态（2/3/4G）

```
// 查询PCRF状态
DSP PCRFSTATUS:PCRFNAME="pcrf_1";

// 期望输出：
// PCRF主机名  =  pcrf_1
// POD名称     =  uncpod-0
// 本端地址    =  10.8.10.1:16400
// 对端地址    =  10.11.21.59:3868
// Gx 状态    =  Normal
// 本端主机名  =  pgw_1
```

### 2. 验证PCRF配置

```
// 查询PCRF信息
LST PCRF:HOSTNAME="pcrf_1";

// 查询PCRF组
LST PCRFGROUP:PCRFGRPNAME="pcrf_group_1";

// 查询PCRF绑定
LST PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1";
```

### 3. 验证Gx接口配置

```
// 查询逻辑接口
LST LOGICINF:;

// 查询Diameter本端信息
LST DIAMLOCINFO:;
```

### 4. 验证PCC业务（2/3/4G）

```
// 1. 查询License
LST LICENSESWITCH:LICITEM="LKV3W9SPCC11";

// 2. OM Portal建立用户跟踪
// 3. 激活用户，跟踪消息
// 4. 检查CCR-I/CCA-I消息内容

// 5. 查询PCC会话信息
DSP PCCSESSINFO:IMSI="460000123456789";

// 6. 查询PCRF组状态
DSP PCRFGRPSTATUS:PCRFGRPNAME="pcrf_group_1";

// 7. 查询APN PCC配置
LST APNPCCFUNC:APN="pccnet";

// 8. 查询APN绑定的PCRF组
LST PCRFGRPBNDAPN:APN="pccnet";
```

### 5. 验证PCRF负荷分担

```
// 1. 激活大量PCC用户
// 2. 使用U2020/MAE客户端查看"PCC发送CCR-I消息数(PCRF)"指标
// 3. 验证各PCRF的CCR-I消息比例与配置一致

// 异常排查：
DSP PCRFSTATUS:PCRFNAME="pcrf_1";
DSP PCRFSTATUS:PCRFNAME="pcrf_2";
LST PCRFGROUP:PCRFGRPNAME="pcrf_group_1";
LST PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1";
```

### 6. 验证5G PCC

```
// 1. 添加测试PCF绑定
ADD TSTPCFBINDING:...;

// 2. 删除SM上下文触发重新建立
DEA SMCTX:...;

// 3. 用户激活后查询
DSP PDUSESSION:IMSI="460000123456789";
DSP PCCSESSINFO:IMSI="460000123456789";

// 4. 清理测试绑定
RMV TSTPCFBINDING:...;
```

### 7. 验证QoS能力开放

```
// 1. OM Portal建立用户跟踪
// 2. 激活用户
// 3. 检查queryPCRFRequest/queryPCRFResponse消息
// 4. 验证local_addr和peer_addr与规划一致

// 异常排查：
LST SMCOMMFUNC:;  // 检查PCRFQRYSW是否开启
```

### 8. 规则失败码

| 失败码 | 描述 | 可能原因 |
|--------|------|----------|
| UNKNOWN_RULE_NAME | 未知规则名 | 规则未配置或名称不匹配 |
| RATING_GROUP_ERROR | Rating Group错误 | 计费组配置错误 |
| SERVICE_IDENTIFIER_ERROR | Service ID错误 | 业务标识配置错误 |
| GW/PCEF_MALFUNCTION | 网关/PECF故障 | 设备异常 |
| RESOURCES_LIMITATION | 资源不足 | 承载资源不足 |
| MAX_NR_BEARERS_REACHED | 最大承载数达到 | 承载数超限 |
| UNKNOWN_RULE_BASE_NAME | 未知规则组名 | UserProfile未配置 |
| RAT_GRANULARITY_MISMATCH | RAT粒度不匹配 | RAT配置错误 |
| UNSUPPORTED_RULE_DATA | 不支持的规则数据 | 规则格式不兼容 |
| RULE_EVENT_TRIGGER_ERROR | 事件触发错误 | 事件触发配置错误 |
| RULE_CONDITIONS_ERROR | 规则条件错误 | 流过滤器配置错误 |
| REQUESTED_RULE_NOT_APPLIED | 请求规则未应用 | 规则安装失败 |
| RULE_NOT_ADDED | 规则未添加 | 资源或配置不足 |
| TRIGGER_TYPE_ERROR | 触发类型错误 | 触发类型不支持 |

### 9. 告警处理

| 告警ID | 告警名称 | 处理建议 |
|--------|----------|----------|
| ALM-81024 | PCRF无响应 | 检查PCRF状态、链路连通性、路由配置 |
| ALM-100065 | 资源过载 | 检查系统资源使用情况 |
| ALM-100066 | 资源拥塞 | 检查系统资源使用情况，考虑扩容 |

---

## 参考信息

### 1. 核心MML命令清单（2/3/4G Gx）

| 命令 | 功能 | 配置对象 |
|------|------|----------|
| SET CONCENPOINT | 设置集中点部署模式 | 基础参数 |
| ADD LOGICINF | 增加逻辑接口 | Gx接口 |
| ADD DIAMLOCINFO | 增加Diameter本端信息 | Diameter连接 |
| ADD DIAMPEERADDR | 增加Diameter对端地址 | Diameter连接 |
| ADD DIAMCONNGRP | 增加Diameter链路组 | Diameter连接 |
| ADD DIAMCONNECTION | 增加Diameter链路 | Diameter连接 |
| ADD PCRF | 增加PCRF | PCRF Diameter连接 |
| ADD PCRFGROUP | 增加PCRF组 | PCRF Diameter连接 |
| ADD PCRFBINDGRP | 增加PCRF与PCRF组的关联 | PCRF Diameter连接 |
| SET MASTERPCRF | 设置主用PCRF | PCRF Diameter连接 |
| ADD GLBPCRFGROUP | 增加全局PCRF组绑定 | PCRF Diameter连接 |
| SET DFTGLBPCRFGRP | 设置全局缺省PCRF组 | PCRF Diameter连接 |
| ADD PCRFGRPBNDAPN | 增加APN和PCRF组关联 | PCRF Diameter连接 |
| SET PCCFUNC | 设置PCC功能 | PCC公共参数 |
| SET PCCFAILACTION | 设置PCC故障处理 | PCC公共参数 |
| SET PCCTIMER | 设置PCC定时器 | 信令控制 |
| ADD RESULTCODECTRL | 增加返回码控制 | 信令控制 |
| ADD PCCTEMPLATE | 增加PCC模板 | PCC模板 |
| SET APNPCCFUNC | 设置APN PCC功能 | APN控制 |
| ADD RULE | 增加规则 | 规则 |
| ADD RULEBINDDNAI | 增加预定义规则DNAI绑定 | DNAI绑定 |
| ADD USERPROFILE | 增加用户模板 | 用户模板 |
| ADD RULEBINDING | 增加用户模板和规则绑定 | 规则绑定 |
| ADD USRPROFGROUP | 增加用户模板组 | 用户模板组 |
| ADD UPBINDUPG | 增加用户模板组和用户模板绑定 | 用户模板绑定 |
| ADD APNUSRPROFG | 增加APN用户模板组绑定 | APN用户模板组绑定 |
| ADD USRPROBINDDNAI | 增加用户模板DNAI绑定 | DNAI绑定 |
| ADD IMSIMSISDNSEG | 增加IMSI和MSISDN号段 | 业务公共 |
| ADD PCCPOLICYGRP | 增加PCC策略组 | 业务策略 |
| SET FHBYPASS | 设置失败旁路处理 | 失败旁路处理 |

### 2. 核心MML命令清单（5G AMF）

| 命令 | 功能 |
|------|------|
| ADD GUAMI | 增加GUAMI |
| ADD PCFSELPLCY | 增加PCF选择策略 |
| ADD AMUEPLCYCTRL | 增加AM/UE策略控制 |
| MOD AMUEPLCYCTRL | 修改AM/UE策略控制 |
| SET AMFPLCYFUNC | 设置AMF策略功能 |
| ADD NGMMSUBDATA | 增加NGMM用户数据 |
| SET AMFPEERSELFUNC | 设置AMF对等选择功能 |

### 3. 核心MML命令清单（5G SMF）

| 命令 | 功能 |
|------|------|
| SET PCCFUNC | 设置PCC功能 |
| ADD PCCTEMPLATE | 增加PCC模板 |
| SET APNPCCFUNC | 设置APN PCC功能 |
| SET N7RCVATTRCTRL | 设置N7接收消息属性控制 |
| SET N7SNDATTRCTRL | 设置N7发送消息属性控制 |
| SET POLICYMODE | 设置接口模式 |
| ADD APNPOLICYMODE | 增加APN接口模式 |
| ADD PCCCHGMODEBYPCFID | 增加PCF实例级接口模式 |
| ADD PCFSSCOPE | 增加PCF Serving Scope |
| ADD USRTAIRANGE | 增加用户TAI范围 |
| ADD PCFSSCOPEBIND | 增加PCF Serving Scope绑定 |

### 4. 关键软参（2/3/4G Gx）

| 软参 | 功能 | 说明 |
|------|------|------|
| BYTE68 | 控制号段匹配位数 | UserProfile选择时的号段匹配精度 |
| BYTE589 | 控制Diameter协议故障倒换处理 | Diameter故障倒换增强 |
| BYTE654 | 控制PCC定制功能 | PCC定制功能开关 |
| BIT1790 | 控制MSISDN前缀剥离 | Gx/N7发送MSISDN时是否剥离965/00965前缀 |
| BIT1854 | Private Extension传递ANSI | 通过Private Extension传递Access Network Switch Indication |
| STRING20 | 特殊Charging-Rule-Name | 传递ANSI的特殊规则名 |
| BIT1202 | Gx Failover增强 | 非热备PCRF的Failover增强 |
| BIT1596 | X-HW-Session-Restoration AVP严格检查 | 控制是否严格检查该AVP |

### 5. 关键软参（5G AMF）

| 软参 | 功能 |
|------|------|
| DWORD60 | AMF策略控制相关 |
| DWORD68/71/72 | AM/UE策略控制参数 |
| DWORD74/80 | AMF策略功能参数 |

### 6. 测量指标

| 测量类别 | 说明 |
|----------|------|
| Gx接口测量 | Gx接口消息统计（CCR/CCA/RAR/RAA等） |
| SMF策略控制测量 | 5G SM策略控制统计 |
| N7接口测量 | N7接口消息统计 |
| N15接口测量 | N15接口消息统计 |
| RESTful接口会话绑定测量 | QoS能力开放接口统计 |
| PCC发送CCR-I消息数(PCRF) | 按PCRF统计CCR-I数量（用于负荷分担验证） |

---

## 知识来源

| 序号 | 文档标题 | 范围 | 来源路径 |
|------|----------|------|----------|
| 1 | PCC基本功能（2G/3G/4G）参考信息 | MML命令、告警、软参、测量指标 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md |
| 2 | 实现原理 | 规则类型、IP-CAN会话、专有承载、PCRF冗余、Event Triggers、QoS映射 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/实现原理_29056158.md |
| 3 | 特性概述（2G/3G/4G） | 适用NF、License、规格、标准 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/特性概述_29056157.md |
| 4 | Gx Failover功能 | Failover原理、增强Failover、配置 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/Gx Failover功能_31422950.md |
| 5 | 配置QoS能力开放功能 | Restif接口、HTTP/BSF配置 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置QoS能力开放功能_48518810.md |
| 6 | 配置与PCRF对接数据 | VPN、Diameter链路、IP重叠场景 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置与PCRF对接数据_30805096.md |
| 7 | 配置动态PCC功能 | PCC使能层级、PCRF组选择、预定义规则 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置动态PCC功能_30805098.md |
| 8 | 配置异常场景数据 | 7种异常场景、SET PCCFAILACTION、SET FHBYPASS | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置异常场景数据_31422947.md |
| 9 | 配置本地PCC功能 | 无PCRF场景、本地规则配置流程 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/配置本地PCC功能_30805097.md |
| 10 | 调测PCC业务 | 验证流程、规则失败码 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCC业务_31422956.md |
| 11 | 调测PCRF负荷分担功能 | 负荷分担验证、指标查看 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测PCRF负荷分担功能_31422955.md |
| 12 | 调测QoS能力开放功能 | queryPCRF消息验证 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测QoS能力开放功能_84718093.md |
| 13 | 调测到PCRF的数据 | PCRF链路验证、配置检查 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（2G_3G_4G，基于Gx接口）/调测PCC基本功能/调测到PCRF的数据_31422954.md |
| 14 | PCC基本功能特性概述（5G） | AMF/SMF适用范围、5G策略类型、PCF发现 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能特性概述（适用于5G）_71770359.md |
| 15 | PCC基本功能（5G）参考信息 | AMF/SMF MML命令、告警、软参、测量 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md |
| 16 | 激活PCC基本功能（5G） | AMF/SMF配置流程、接口模式选择、PCF Serving Scope | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/激活PCC基本功能_72467890.md |
| 17 | 调测PCC基本功能（5G） | 5G验证流程、TSTPCFBINDING | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/调测PCC基本功能_45059543.md |
| 18 | 相关概念（5G） | AM/UE/SM策略详解、PCR Triggers | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/相关概念_71770360.md |
| 19 | AM策略偶联建立流程 | AMF→PCF Create流程 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/AM策略偶联建立流程_50510738.md |
| 20 | AM策略偶联修改流程 | 三种修改场景 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/AM策略偶联修改流程_50510739.md |
| 21 | AM策略偶联终止流程 | AM策略终止 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/AM策略偶联终止流程_50510740.md |
| 22 | UE策略偶联建立流程 | AMF→PCF Create→UE Config Update | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/UE策略偶联建立流程_50510744.md |
| 23 | UE策略偶联修改流程 | 三种修改场景 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/UE策略偶联修改流程_50510745.md |
| 24 | UE策略偶联终止流程 | UE策略终止 | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/UE策略偶联终止流程_50510746.md |
| 25 | 异常处理流程（5G） | PENDING_TRANSACTION、回退本地PCC | output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/智能PCC解决方案/WSFD-109101 PCC基本功能/PCC基本功能（5G）/异常处理流程_53323998.md |
