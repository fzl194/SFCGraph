# Batch 05-01: Gy接口协议与5G会话流程计费交互 知识草稿

## 来源文件清单

| # | 文件 | UNC路径 |
|---|------|---------|
| 1 | 接口错误码_30780484 | 快速入门/协议与流程/EPC信令分析/EPC信令与协议分析/接口协议/Gy/ |
| 2 | 接口协议简介_30780312 | 同上 |
| 3 | PDU会话建立_97353800 | 快速入门/协议与流程/5G Core信令分析/业务流程/会话流程/ |
| 4 | PDU会话释放（SMF发起）_97353780 | 同上 |
| 5 | PDU会话修改（PCF发起）_97033372 | 同上 |
| 6 | 会话管理基本概念_76784844 | 同上 |
| 7 | QoS基本概念_76785291 | 同上 |
| 8 | Multiple-Services-Credit-Control_30780406 | 快速入门/协议与流程/EPC信令分析/.../Gy/相关信元解释/ |
| 9 | Granted-Service-Unit_30780397 | 同上 |
| 10 | Final-Unit-Indication_30780393 | 同上 |
| 11 | CC-Request-Type_30780361 | 同上 |
| 12 | Result-Code_30780440 | 同上 |
| 13 | Reporting-Reason_30780435 | 同上 |
| 14 | Trigger-Type_30780466 | 同上 |
| 15 | Validity-Time_30780477 | 同上 |
| 16 | Redirect-Server_30780432 | 同上 |
| 17 | Tariff-Time-Change_30780459 | 同上 |

---

## 一、Gy接口协议层

### K315: Gy接口完整消息列表与方向
> 来源: 接口协议简介_30780312

**协议知识**

Gy接口为GGSN/P-GW和OCS间的信令面接口，基于Diameter协议。完整消息列表如下：

| 消息 | 方向 | 作用 |
|------|------|------|
| CCR (Credit-Control-Request) | P-GW -> OCS | 为用户请求计费控制信息 |
| CCA (Credit-Control-Answer) | OCS -> P-GW | 返回CCR消息的请求结果 |
| RAR (Re-Auth-Request) | OCS -> P-GW | 为用户请求重新认证/授权服务 |
| RAA (Re-Auth-Answer) | P-GW -> OCS | 返回RAR消息的请求结果 |
| ASR (Abort-Session-Request) | OCS -> P-GW | 发送会话终止信息 |
| ASA (Abort-Session-Answer) | P-GW -> OCS | 返回ASR消息的请求结果 |
| DPR (Disconnect-Peer-Request) | P-GW -> OCS | 通知对端将断开链路 |
| DPA (Disconnect-Peer-Answer) | OCS -> P-GW | 返回DPR消息的请求结果 |
| CER (Capabilities-Exchange-Request) | P-GW -> OCS | 链路维护消息 |
| CEA (Capabilities-Exchange-Answer) | OCS -> P-GW | 返回CER消息的请求结果 |
| DWR (Device-Watchdog-Request) | P-GW -> OCS | 心跳检测消息 |
| DWA (Device-Watchdog-Answer) | OCS -> P-GW | 返回DWR消息的请求结果 |

**计费相关**：CCR/CCA是核心计费交互对，对应CC-Request-Type的initial/update/terminate三种类型。RAR/RAA用于OCS发起重授权（对应Reporting-Reason=FORCED_REAUTHORISATION）。ASR/ASA用于OCS强制终止会话。DPR/DPA/CER/CEA/DWR/DWA为Diameter基础链路维护消息。

---

### K316: Gy接口Diameter Result-Code错误码分类体系
> 来源: 接口错误码_30780484, Result-Code_30780440

**协议知识**

Result-Code AVP编码268，Unsigned32类型，由千位数字标识错误分类：

| 分类 | 含义 | 关键错误码 |
|------|------|-----------|
| 1xxx | Informational（信息） | - |
| 2xxx | Success（成功） | 2001 DIAMETER_SUCCESS |
| 3xxx | Protocol Errors（协议错误） | 3001 COMMAND_UNSUPPORTED, 3002 UNABLE_TO_DELIVER, 3004 TOO_BUSY, 3007 APPLICATION_UNSUPPORTED |
| 4xxx | Transient Failures（临时失败） | 4001 AUTHENTICATION_REJECTED, 4010 END_USER_SERVICE_DENIED, 4011 CREDIT_CONTROL_NOT_APPLICABLE, **4012 CREDIT_LIMIT_REACHED** |
| 5xxx | Permanent Failure（永久失败） | 5001 AVP_UNSUPPORTED, 5002 UNKNOWN_SESSION_ID, 5003 AUTHORIZATION_REJECTED, 5004 INVALID_AVP_VALUE, 5005 MISSING_AVP, 5006 RESOURCES_EXCEEDED, 5030 USER_UNKNOWN, **5031 RATING_FAILED** |

**计费相关**：
- 4012 CREDIT_LIMIT_REACHED：用户信用额度已用完，是计费控制的核心错误码
- 4010 END_USER_SERVICE_DENIED：OCS拒绝用户业务访问
- 4011 CREDIT_CONTROL_NOT_APPLICABLE：用户不适用在线计费
- 5030 USER_UNKNOWN：OCS不识别该用户
- 5031 RATING_FAILED：OCS对用户进行批价失败
- 非成功Result-Code必须包含Error-Reporting-Host AVP
- 定义之外的结果编码必须处理为永久失败

---

### K317: CC-Request-Type四种取值与P-GW实际支持
> 来源: CC-Request-Type_30780361

**协议知识**

CC-Request-Type AVP编码416，枚举类型，所有CCR消息必须携带：

| 取值 | 枚举值 | 含义 | 使用场景 |
|------|--------|------|---------|
| INITIAL_REQUEST | 1 | 发起CC会话 | 用户首次激活、PDP上下文建立、IP CAN会话建立 |
| UPDATE_REQUEST | 2 | 更新已存在的CC会话 | 配额/有效期到达需重授权、特定业务事件触发 |
| TERMINATION_REQUEST | 3 | 终止CC会话 | PDP上下文释放、IP CAN会话终止 |
| EVENT_REQUEST | 4 | 一次性事件请求 | 不保留CC会话状态时使用，必须同时携带Requested-Action AVP |

**P-GW当前仅支持三种**：initial、update、terminate（不支持EVENT_REQUEST）。

UPDATE_REQUEST触发条件：分配的配额耗尽、Validity-Time到期、特定业务事件（如QoS变化、位置变化等Trigger事件）。

---

### K318: Multiple-Services-Credit-Control (MSCC) AVP完整结构
> 来源: Multiple-Services-Credit-Control_30780406

**协议知识**

MSCC AVP编码456，Grouped类型，是多重业务特性组合时非独立配额的控制标记。完整结构：

```
Multiple-Services-Credit-Control ::= < AVP Header: 456 >
  [ Granted-Service-Unit ]         -- OCS下发的授权配额
  [ Requested-Service-Unit ]       -- P-GW请求的配额
  *[ Used-Service-Unit ]           -- 已使用的配额上报
  [ Tariff-Change-Usage ]          -- 费率变化使用量标识
  *[ Service-Identifier ]          -- 业务标识
  [ Rating-Group ]                 -- 费率组
  *[ G-S-U-Pool-Reference ]       -- 信用池引用
  [ Result-Code ]                  -- 该MSCC的结果码
  [ Final-Unit-Indication ]        -- 最后单元指示
  [ Time-Quota-Threshold ]         -- 时间配额门限
  [ Volume-Quota-Threshold ]       -- 流量配额门限
  [ Unit-Quota-Threshold ]         -- 单元配额门限
  [ Quota-Holding-Time ]           -- 配额保持时间
  [ Quota-Consumption-Time ]       -- 配额消费时间
  *[ Reporting-Reason ]            -- 上报原因
  [ Trigger ]                      -- 重授权触发条件
  *[ Envelope ]                    -- 信封
  [ Envelope-Reporting ]           -- 信封上报
  [ Time-Quota-Mechanism ]         -- 时间配额机制
```

**关键规则**：
- Service-Identifier与Rating-Group同时下发时，优先采用Service-Identifier
- 仅下发Rating-Group时，MSCC关联的所有业务都采用该费率组
- G-S-U-Pool-Reference中必须携带实际业务标识（如Unit-Type为TIME则必须携带CC-Time）
- MSCC仅在多重业务采用非独立信用池时生效
- 参见: 3GPP TS 32.299 Va.4.0 7.1.9章节

---

### K319: Granted-Service-Unit (GSU) AVP子信元详解
> 来源: Granted-Service-Unit_30780397

**协议知识**

GSU AVP编码431，Grouped类型，指示业务释放或需发送新CCR前可用的资源总量。P-GW只有重新收到CCA消息时才能明确配额类型。

```
Granted-Service-Unit ::= < AVP Header: 431 >
  [ Tariff-Time-Change ]            -- 费率切换时间点
  [ CC-Time ]                       -- 授权时长（秒）
  [ CC-Total-Octets ]               -- 授权总字节数
  [ CC-Input-Octets ]               -- 授权上行字节数
  [ CC-Output-Octets ]              -- 授权下行字节数
  [ CC-Service-Specific-Units ]     -- 业务特定单元
```

**关键行为**：
- 如果CCA中未携带GSU（如OCS判定用户已终止业务访问），OCS在用户账户中预支配额
- 如果GSU不可接受，P-GW可通过Termination-Cause AVP携带DIAMETER_BAD_ANSWER终止业务承载
- CC-Input-Octets + CC-Output-Octets 与 CC-Total-Octets 可以组合使用
- 参见: RFC 4006 8.17章节

---

### K320: Final-Unit-Indication与三种Final-Unit-Action
> 来源: Final-Unit-Indication_30780393, Redirect-Server_30780432

**协议知识**

Final-Unit-Indication AVP编码430，Grouped类型，表示GSU中包含的是最后一个单元。当这些单元截止，P-GW执行Final-Unit-Action指示的动作。

```
Final-Unit-Indication ::= < AVP Header: 430 >
  { Final-Unit-Action }              -- 必选：终止动作
  *[ Restriction-Filter-Rule ]       -- 限制过滤规则
  *[ Filter-Id ]                     -- 过滤器ID
  [ Redirect-Server ]                -- 重定向服务器
```

三种Final-Unit-Action及配套要求：

| 动作 | 含义 | 必须同时携带的AVP |
|------|------|-----------------|
| TERMINATE | 终止业务 | 无（不携带其他AVP） |
| REDIRECT | 重定向到指定服务器 | Redirect-Server（必须）+ Restriction-Filter-Rule/Filter-Id（可选，限制非重定向地址的访问） |
| RESTRICT_ACCESS | 限制访问 | Restriction-Filter-Rule 或 Filter-Id（至少一个） |

**Redirect-Server AVP**（编码434，Grouped）结构：
```
Redirect-Server ::= < AVP Header: 434 >
  { Redirect-Address-Type }          -- 地址类型
  { Redirect-Server-Address }        -- 服务器地址
```

**特殊行为**：
- 首次交互时Final-Unit-Action=REDIRECT或RESTRICT_ACCESS但CCA未携带GSU，P-GW需立即执行指定动作
- OCS需支持暂时中断功能才能执行终止业务的策略动作

---

### K321: Reporting-Reason九种上报原因详解
> 来源: Reporting-Reason_30780435

**协议知识**

Reporting-Reason AVP编码872，Enumerated类型，指出特定类别配额的使用量上报原因。仅在CCR消息上报使用量时携带。

| 取值 | 枚举值 | 携带位置 | 适用范围 | 含义 |
|------|--------|---------|---------|------|
| 0 | THRESHOLD | Used-Service-Units | 特定配额类型 | 配额门限达到 |
| 1 | QHT | MSCC | 所有配额类型 | 配额保持时长达到 |
| 2 | FINAL | MSCC | 所有配额类型 | 业务终止（PDP/IP CAN会话终止） |
| 3 | QUOTA_EXHAUSTED | Used-Service-Units | 特定配额类型 | 配额耗尽 |
| 4 | VALIDITY_TIME | MSCC | 所有配额类型 | Validity-Time到期 |
| 5 | OTHER_QUOTA_TYPE | Used-Service-Units | 特定配额类型 | 多重配额中一个达到触发条件 |
| 6 | RATING_CONDITION_CHANGE | MSCC | 所有配额类型 | Trigger预定义的费率条件变化 |
| 7 | FORCED_REAUTHORISATION | MSCC | 所有配额类型 | OCS发起重授权 |
| 8 | POOL_EXHAUSTED | Used-Service-Units / MSCC | 信用池级 | 信用池保障单元足够但费率组不够 |

**关键规则**：
- MSCC中可携带：QHT、FINAL、VALIDITY_TIME、FORCED_REAUTHORISATION、RATING_CONDITION_CHANGE（适用所有配额类型）
- Used-Service-Units中可携带：THRESHOLD、QUOTA_EXHAUSTED、OTHER_QUOTA_TYPE（仅指示特定配额类型）
- POOL_EXHAUSTED：在Used-Service-Units中指示该信用池所有类型配额；所有配额类型使用同一信用池时可在MSCC中携带
- Reporting-Reason=RATING_CONDITION_CHANGE时，必须同时在Trigger AVP中指出引发重授权的具体触发事件

参见: 3GPP TS 32.299 Va.4.0 7.2.175章节

---

### K322: Trigger-Type完整取值与重授权触发条件
> 来源: Trigger-Type_30780466

**协议知识**

Trigger-Type AVP编码870，Enumerated类型。CCA中指示P-GW在何种事件下重新申请配额；CCR中指示触发重授权的是RATING_CONDITION_CHANGE事件。

| 取值 | 枚举值 | 触发条件 |
|------|--------|---------|
| 1 | CHANGE_IN_SGSN_IP_ADDRESS | SGSN IP地址变化 |
| 2 | CHANGE_IN_QOS | 用户协商QoS变化 |
| 3 | CHANGE_IN_LOCATION | 用户位置变化 |
| 4 | CHANGE_IN_RAT | 接入技术变化（Rate） |
| 5 | CHANGE_IN_UE_TIMEZONE | 终端时区变化 |
| 30 | CHANGEINLOCATION_MCC | 服务网络MCC改变 |
| 31 | CHANGEINLOCATION_MNC | 服务网络MNC改变 |
| 33 | CHANGEINLOCATION_LAC | 终端LAC改变 |
| 35 | CHANGEINLOCATION_TAC | 终端TAC改变 |
| 36 | CHANGEINLOCATION_ECGI | 终端ECGI改变 |
| 74 | CHANGE_IN_SERVING_PLMN_RATE_CONTROL | 服务PLMN速率控制改变 |
| 75 | CHANGE_IN_APN_RATE_CONTROL | APN速率改变 |

**计费关联**：只有由Trigger AVP给出的事件才能触发重新申请配额。OCS在CCA中下发Trigger-Type，P-GW监测对应条件变化，变化后发送CCR(UPDATE)并携带Reporting-Reason=RATING_CONDITION_CHANGE和Trigger-Type。

参见: 3GPP TS 32.299 Va.4.0 7.2.236章节

---

### K323: Validity-Time与配额有效期机制
> 来源: Validity-Time_30780477

**协议知识**

Validity-Time AVP编码448，Unsigned32类型，OCS下发给P-GW，以秒为单位。

**核心行为**：
- 有效时间以P-GW收到CCA消息的时刻为起点计时
- 有效时间内业务资源耗尽 → P-GW发送CCR重新申请配额
- 有效时间到达 → 所有MSCC都需要上报配额（不管单个MSCC是否耗尽）
- 单一MSCC上报配额时计时不停止（只有全部MSCC都上报才重置）

**特殊用途**：
- 可用于控制REDIRECT或RESTRICT_ACCESS动作后的网络资源使用时长
- 到达后需OCS重新发送交互消息

参见: RFC 4006 8.33章节

---

### K324: Tariff-Time-Change费率切换时间机制
> 来源: Tariff-Time-Change_30780459, Granted-Service-Unit_30780397

**协议知识**

Tariff-Time-Change AVP编码451，Time类型。以January 1, 1900, 00:00 UTC为起点，以秒为单位。

**机制**：
- OCS在GSU中下发Tariff-Time-Change，指示费率切换的时间点
- 当MSCC和GSU同时绑定同一个业务标识或费率组时，Tariff-Time-Change和Tariff-Change-Usage会同时下发
- 两个配额值可能绑定同一个信用池，也可能是不同的两个信用池
- 应答消息中使用Used-Service-Unit AVP来表示时长费率的变化

**限制**：
- 费率改变机制是可选的，不能应用在基于时长的业务中
- 如果OCS不支持费率随时间改变的机制，该AVP值无效，OCS终止CC承载并在Termination-Cause中携带DIAMETER_BAD_ANSWER

参见: RFC 4006 8.20章节

---

## 二、5G会话管理中的计费交互

### K325: PDU会话建立流程中的计费交互点
> 来源: PDU会话建立_97353800

**协议知识**

PDU会话建立流程共29步，其中计费相关的关键交互点：

**步骤12-14: PCF策略交互（N7接口）**
- 步骤12: SMF选择PCF（如果部署动态PCC）
- 步骤13: SMF -> PCF: Npcf_SMPolicyControl_Create Request
  - 携带: supi, pduSessionId, notificationUri, pduSessionType, sliceInfo
- 步骤14: PCF -> SMF: Npcf_SMPolicyControl_Create Response
  - **计费关键信元**: chargingInfo（包含PDU会话的CHF地址）
  - 其他: sessRules(会话级QoS), authSessAmbr(授权Session-AMBR), authDefQos(默认QoS), pccRules(业务级PCC规则), flowInfos(流过滤信息), policyCtrlReqTriggers(策略触发器)

**步骤15-17: UPF选择与PFCP会话建立（N4接口）**
- 步骤16: SMF -> UPF: PFCP Session Establishment Request
  - **计费关键信元**: Create URR（定义统计类上报动作，如流量耗尽上报、离线计费上报等）
  - 其他: Create PDR, Create FAR, Create QER, Create BAR

**步骤18-19: IP地址分配后PCF更新**
- 步骤18: SMF -> PCF: Npcf_SMPolicyControl_Update（携带UE IP地址）
  - 触发器: UE_IP_CH（IP地址变更）
- 步骤19: PCF -> SMF: 更新SM策略关联

**要点**：PDU会话建立时chargingInfo由PCF下发给SMF，SMF根据其中的CHF地址创建融合计费会话。Create URR在PFCP Session Establishment中同步下发。

---

### K326: PDU会话释放（SMF发起）流程中的计费交互
> 来源: PDU会话释放（SMF发起）_97353780

**协议知识**

SMF发起的PDU会话释放共17步，触发条件为SMF识别本地配置策略刷新。

**步骤1-2: PFCP会话删除（N4接口）**
- 步骤1: SMF -> UPF: PFCP Session Deletion Request
- 步骤2: UPF -> SMF: PFCP Session Deletion Response
  - **计费关键信元**: Usage Report（如果UPF已开通URR且存在流量使用测量，必须返回使用量报告）

**步骤16-17: PCF策略删除（N7接口）**
- 步骤16: SMF -> PCF: Npcf_SMPolicyControl_Delete
  - 携带: userLocationInfo, nrLocation, pduSessRelCause
- 步骤17: PCF -> SMF: 204 No Content

**计费流程要点**：
1. 释放时先删PFCP会话，UPF返回最终Usage Report
2. SMF收到Usage Report后，需向CHF发送Charging Data Request[Termination]上报最终使用量
3. 最后删除PCF策略关联

---

### K327: PDU会话修改（PCF发起）流程中的计费交互
> 来源: PDU会话修改（PCF发起）_97033372

**协议知识**

PCF发起的PDU会话修改共19步，触发条件为PCF识别配置策略有修改。

**步骤1-2: PCF通知SMF策略更新**
- 步骤1: PCF -> SMF: Npcf_SMPolicyControl_UpdateNotify
  - 携带: smPolicyDecision, sessRules, pduSessionId, supi
- 步骤2: SMF -> PCF: 204 No Content 或 200 OK
  - 200 OK表示PCC规则和/或会话规则部分未安装/激活成功

**步骤11-12/16-17: PFCP会话修改（N4接口）- 两次**
- 步骤11: SMF -> UPF: PFCP Session Modification Request（QoS参数修改涉及UPF侧时触发）
- 步骤16: SMF -> UPF: PFCP Session Modification Request
  - 携带: Remove PDR/FAR/QER, Create PDR/FAR/QER, Update PDR, QoS Flow Identifier
  - **计费关联**：PCC规则变更可能导致URR的增删改

**步骤18-19: SMF向PCF上报事件**
- 步骤18: SMF -> PCF: Npcf_SMPolicyControl_Update
  - 携带: repPolicyCtrlReqTriggers（如SUCC_RES_ALLO表示资源分配成功）
- 步骤19: PCF -> SMF: 响应

**计费流程要点**：PCF发起策略修改 → SMF可能需要更新UPF的URR规则 → SMF向CHF发送Charging Data Update上报策略变更

---

### K328: 5G会话管理与4G的关键差异（计费视角）
> 来源: 会话管理基本概念_76784844

**协议知识**

4G vs 5G会话管理对比（计费相关）：

| 对比项 | 4G | 5G |
|--------|-----|-----|
| 数据通道 | PDN连接 | PDU会话 |
| QoS控制粒度 | EPS承载 | QoS Flow |
| 计费承载 | 每个EPS承载独立URR | 每个QoS Flow独立URR |
| 默认承载 | 注册后强制建立默认承载 | 不强制建立，按需建立PDU会话 |
| 会话释放 | PDN去连接=释放所有承载 | PDU会话释放=释放所有QoS Flow |
| 控制面 | MME + S-GW/P-GW控制面 | SMF集中完成 |
| 业务连续性 | 仅IP连续性 | SSC Mode 1/2/3三种模式 |

**SSC Mode对计费的影响**：
- SSC Mode1: IP地址和UPF不变，计费会话连续
- SSC Mode2: 先断后连，旧PDU会话释放（上报最终Usage Report），新建PDU会话（新建计费会话）
- SSC Mode3: 先连后断，存在新旧两个PDU会话重叠期，两套计费会话并存

**5G新增流程（计费关联）**：
- 已有PDU会话用户面的选择性激活/去激活：去激活仅删除用户面连接、信令面保持不变，不影响计费会话状态

---

### K329: 5G QoS模型与计费QoS Flow的映射关系
> 来源: QoS基本概念_76785291

**协议知识**

5G QoS模型中与计费直接相关的概念：

**QoS Flow（数据通路）= 计费最小粒度**
- QFI（QoS Flow ID）在PDU Session中唯一
- QFI可动态分配，也可等于5QI
- 一个PDU会话共用一个NG-U隧道，通过QFI区分QoS Flow

**QoS参数与计费配置的关联**：

| QoS参数 | 计费关联 |
|---------|---------|
| ARP | QoS Flow建立/修改优先级，影响URR的创建时机 |
| 5QI | 业务质量索引，可用于区分不同费率组(Rating-Group) |
| Session-AMBR | PDU会话级聚合速率限制，影响流量计量 |
| GFBR/MFBR | GBR QoS Flow的保证/最大带宽 |

**QoS控制机制与计费触发**：
- 信令控制: SMF在PDU会话建立/修改时向UPF/RAN/UE发送QoS Flow信息（含URR）
- Reflective QoS: 仅用于Non-GBR，UE自行推演上行QoS Rule，SMF不发送信令
- Notification Control: RAN不满足GFBR时通知SMF，可能触发QoS变更进而触发计费更新

**两级映射机制**：
1. 数据包 -> QoS Flow（通过PDR/QoS Rule匹配）
2. QoS Flow -> Radio Bearer（RAN自主决定）

计费关注第一级映射：PDR匹配到QoS Flow后，关联对应的URR进行计量。

---

### K330: MSCC中Service-Identifier与Rating-Group的优先级规则
> 来源: Multiple-Services-Credit-Control_30780406

**协议知识**

MSCC中业务标识与费率组的优先级关系：
- Service-Identifier与Rating-Group同时下发时：**采用Service-Identifier的值**
- 仅下发Rating-Group：MSCC关联的所有业务都采用该费率组
- Service-Identifier标识具体业务（如某个应用）
- Rating-Group标识一组业务的费率

**与PCC规则的关系**：PCF下发的PCC规则中包含Rating-Group AVP，SMF将其映射到PFCP的URR中。在5GC融合计费中，Rating-Group通过Charging Data Request传递给CHF。

---

### K331: Reporting-Reason与Trigger-Type的对应关系
> 来源: Reporting-Reason_30780435, Trigger-Type_30780466

**协议知识**

Reporting-Reason与Trigger-Type的关联使用场景：

| 场景 | CCA中OCS下发 | CCR中P-GW上报 |
|------|-------------|--------------|
| 配额门限 | Time-Quota-Threshold / Volume-Quota-Threshold | Reporting-Reason=THRESHOLD |
| 配额保持时间 | Quota-Holding-Time | Reporting-Reason=QHT |
| 有效期到期 | Validity-Time | Reporting-Reason=VALIDITY_TIME |
| 配额耗尽 | Granted-Service-Unit中的配额量 | Reporting-Reason=QUOTA_EXHAUSTED |
| 费率条件变化 | Trigger AVP（含Trigger-Type列表） | Reporting-Reason=RATING_CONDITION_CHANGE + Trigger-Type |
| OCS强制重授权 | RAR消息 | Reporting-Reason=FORCED_REAUTHORISATION |
| 信用池耗尽 | G-S-U-Pool-Reference | Reporting-Reason=POOL_EXHAUSTED |
| 业务终止 | - | Reporting-Reason=FINAL |

**RATING_CONDITION_CHANGE的特殊规则**：CCA中下发Trigger AVP（包含多个Trigger-Type），当对应条件满足时，P-GW发送CCR(UPDATE)，同时携带Reporting-Reason=RATING_CONDITION_CHANGE和具体的Trigger-Type值。

---

### K332: PDU会话建立中PFCP Session Establishment的计费相关信元
> 来源: PDU会话建立_97353800

**协议知识**

PDU会话建立步骤16（SMF -> UPF: PFCP Session Establishment Request）中的计费相关信元：

| 信元 | 含义 | 计费作用 |
|------|------|---------|
| Create URR | Usage Reporting Rule | 定义统计类上报动作，如流量耗尽上报、离线计费上报 |
| Create PDR | Packet Detection Rule | 流检测规则，匹配数据包后关联URR计量 |
| Create FAR | Forwarding Action Rule | 转发规则 |
| Create QER | QoS Enforcement Rule | QoS流控规则，SMF通常下发3类QER：Session级、QoSFlow级、QFI级 |
| UE IP Address | SMF分配的UE IP | 计费话单中记录 |
| SDF Filter | 业务数据流过滤器 | 内容计费规则匹配 |

**URR与PDR的关联**：PDR匹配数据包后，同时触发关联的URR进行流量/时长计量。PDR区分上下行（Source interface: access=上行N3, core=下行N6）。

---

### K333: PDU会话释放中UPF Usage Report的计费作用
> 来源: PDU会话释放（SMF发起）_97353780

**协议知识**

PDU会话释放步骤2（UPF -> SMF: PFCP Session Deletion Response）中：

**Usage Report信元出现条件**：
- UPF已开通URR（Create URR时已下发）
- PFCP会话被删除
- URR的流量使用测量数据可用

**Usage Report在计费流程中的作用**：
1. UPF在PFCP Session Deletion Response中返回最终Usage Report
2. SMF收到Usage Report后，提取其中的流量/时长使用量
3. SMF构造Charging Data Request[Termination]，携带最终使用量发送给CHF
4. CHF生成最终话单，关闭计费会话

**释放原因分类（SMF维度）**：
- #36 regular deactivation（常规去激活）
- #39 reactivation requested（重激活请求）
- #46 out of LADN service area（离开LADN服务区）
- #38 network failure（网络故障）
- #26 Insufficient resources（资源不足）
- PCF触发的释放

---

### K334: Validity-Time与Quota-Holding-Time的区别
> 来源: Validity-Time_30780477

**协议知识**

Validity-Time（Gy接口RFC 4006）与Quota-Holding-Time（N4接口）的区别：

| 对比项 | Validity-Time (Gy) | Quota-Holding-Time (N4) |
|--------|--------------------|------------------------|
| 协议层 | Diameter/Gy接口 | PFCP/N4接口 |
| 下发方 | OCS | SMF |
| 接收方 | P-GW/SMF | UPF |
| 单位 | 秒 | 秒 |
| 起算点 | P-GW收到CCA消息的时刻 | UPF收到配额的时刻 |
| 触发动作 | 所有MSCC上报配额 | URR上报使用量 |
| 单个MSCC上报时 | 计时不停止 | 取决于配置 |
| Reporting-Reason | VALIDITY_TIME | QHT（配额保持时间） |

**融合计费中的映射**：SMF收到OCS/CHF下发的Validity-Time后，可能将其映射为N4接口的Quota-Holding-Time下发给UPF。

---

### K335: 5G QoS Flow与Gy MSCC的映射模型
> 来源: QoS基本概念_76785291, Multiple-Services-Credit-Control_30780406

**协议知识**

5G融合计费场景下，QoS Flow与MSCC的映射关系：

**EPC场景（Gy接口直连OCS）**：
- 每个EPS承载 = 一个MSCC实例
- 默认承载对应初始CCR(INITIAL)
- 专有承载对应CCR(UPDATE)中新增MSCC

**5GC场景（融合计费Nchf）**：
- 每个QoS Flow = 一个计费单元（通过Rating-Group区分）
- 默认QoS Flow对应Charging Data Request[Initial]
- 专有QoS Flow对应Charging Data Request[Update]中新增的multipleUnitUsage
- PCC规则中通过Rating-Group AVP将QoS Flow关联到费率组
- SMF通过PFCP的URR将QFI与Rating-Group关联，UPF按URR计量

**5G二级映射中的计费位置**：
- UPF执行PDR匹配 -> 关联URR计量（第一级：数据包到QoS Flow）
- 计费发生在UPF用户面，SMF控制面负责将使用量上报给CHF
