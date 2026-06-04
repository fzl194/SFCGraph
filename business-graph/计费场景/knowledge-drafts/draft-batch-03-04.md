# Batch 03-04: 常见故障案例 + 接入侧功能 + 例行维护 知识草稿

## 来源文件清单

| # | 文件 | UNC路径 |
|---|------|---------|
| 1 | 用户激活时N40未发送Initial消息_80259366 | 计费解决方案概述/常见故障案例/ |
| 2 | 用户激活时预申请配额未携带预期RG_80259367 | 同上 |
| 3 | 用户计费方式和/或RG计费方式不符合预期_80259368 | 同上 |
| 4 | Trigger未上报_80259369 | 同上 |
| 5 | 主备CHF未生效_80259370 | 同上 |
| 6 | 业务被放通未上报CHF_80259371 | 同上 |
| 7 | 缓存消息没有正常回放_80259372 | 同上 |
| 8 | CP和UP URR配置不一致_80259373 | 同上 |
| 9 | N40接口计费流量与用户实际访问流量不一致_80259374 | 同上 |
| 10 | 用户异常去活_80259375 | 同上 |
| 11 | 3GPP PS data off功能_74569639 | 计费原理/接入侧相关计费功能/ |
| 12 | 计费暂停功能_30615504 | 同上 |
| 13 | 检查N40接口链路状态_86867966 | 例行维护/ |

UNC根路径前缀: `网络部署/业务专题/5G Core 计费解决方案/`

---

## 一、计费配置五层模型（故障案例归纳）

### K114: 融合计费配置五层嵌套模型
> 来源: 综合故障案例1-3归纳

**隐性规则**

融合计费配置是五层嵌套结构，任何一层配置错误都导致下游功能异常：

| 层级 | 配置项 | 命令 | 说明 |
|------|--------|------|------|
| L1 计费模式 | CHGMODE | SET CHGMODE | 设为NchfMode才走N40接口 |
| L2 融合计费使能 | CHARGECTRL | SET CHARGECTRL/SET USRPROFCHARGE/SET APNCHARGECTRL | 按用户/APN粒度使能 |
| L3 CHF交互使能 | CHFINIT | SET CHFINIT | 设为SENDREQ才在激活时发Initial |
| L4 RG配置 | URR/URRGROUP | ADD/MOD URR/URRGROUP | 定义RG和计费方式 |
| L5 Rule绑定 | RULE/PCCPOLICYGRP | ADD/MOD RULE/PCCPOLICYGRP | 将RG绑定到业务匹配规则 |

---

## 二、常见故障案例

### K115: 故障1 — N40未发送Initial消息
> 来源: 用户激活时N40接口未发送Charging Data Request [Initial]消息_80259366

**故障案例**

- **现象**：SMF未通过N40接口发送Charging Data Request [Initial]消息
- **根因**：(1) 计费模式未配为N40 (2) 融合计费未使能 (3) CHFINIT未设为SENDREQ (4) 无可用CHF (5) N40链路故障
- **排查**：LST CHGMODE → LST CHARGECTRL → LST CCT → LST GLBDFTCHFGROUP → ALM-100072
- **隐含知识**：三层配置必须全部正确：CHGMODE=NchfMode + CHARGECTRL使能 + CHFINIT=SENDREQ

### K116: 故障2 — 预申请配额未携带预期RG
> 来源: 用户激活时预申请配额未携带预期RG_80259367

**故障案例**

- **现象**：Initial消息中RG缺失或不符合预期
- **根因**：(1) CCRINITRGNUM设置不合理 (2) RGSOURCE设置不合理 (3) RG配置或绑定错误
- **排查**：LST CCT(CCRINITRGNUM/RGSOURCE) → LST URRGROUP → LST URR → LST CTXSTARTRATING
- **隐含知识**：RG来源两种模式：CTXSTARTRATING（显式配置RG）和DEFAULT（按优先级自动获取）。RG绑定链路：URR → URRGROUP → CTXSTARTRATING。

### K117: 故障3 — RG计费方式不符合预期
> 来源: 用户计费方式和_或RG计费方式不符合预期_80259368

**故障案例**

- **现象**：N40接口RG的在线/离线计费方式与规划不一致
- **根因**：(1) 用户计费方式(RGAPPLIED)设置错误 (2) URR的USAGERPTMODE与用户计费方式不一致
- **排查**：LST CHARGECTRL → LST USRPROFCHARGE → LST URR(USAGERPTMODE)
- **隐含知识**：
  - RGAPPLIED三个取值：ONLINERGONLY、OFFLINERGONLY、DEFAULT（同一N40会话可同时支持在线和离线RG）
  - **URR的USAGERPTMODE必须与用户级别的RGAPPLIED一致，否则不生效**
  - 计费方式可基于User Profile或DNN或CC三种粒度配置

### K118: 故障4 — Trigger未上报
> 来源: Trigger未上报_80259369

**故障案例**

- **现象**：SMF未向CHF发送Charging Data Request [update]上报Trigger
- **根因**：(1) CHF未下发对应Trigger (2) SMF本地未配置 (3) Session级与RG级冲突
- **排查**：用户跟踪查看CHF Response的triggers → LST PDUTRIGGER → LST RGTRIGGER
- **隐含知识**：
  - Trigger分两级：Session级(PDUTRIGGER)和RG级(RGTRIGGER)
  - **优先级规则**：Session级和RG级同一Trigger冲突时，Session级优先。Session级"不上报"时才按RG级生效
  - Trigger来源：CHF下发（Response的triggers信元）+ SMF本地配置

### K119: 故障5 — 主备CHF未生效
> 来源: 主备CHF未生效_80259370

**故障案例**

- **现象**：主CHF故障时SMF未切换到备用CHF
- **根因**：(1) 未配置备用CHF (2) CHF下发FAILOVER_NOT_SUPPORTED (3) SMF本地FAILOVERSUP未使能 (4) 备用CHF链路故障
- **排查**：LST SELECTCHFGBYCC → LST TNFBINDGRP → LST TNFGRP → LST FAILHANDLING
- **隐含知识**：
  - **Failover三要素**：备用CHF已配置 + CHF未指示FAILOVER_NOT_SUPPORTED + SMF本地FAILOVERSUP=ENABLE
  - CHF侧sessionFailover信元具有决定权
  - CHF选择基于CC绑定：SELECTCHFGBYCC → TNFBINDGRP → TNFGRP → TNFINSIP

### K120: 故障6 — 业务被放通未上报CHF
> 来源: 业务被放通未上报CHF_80259371

**故障案例**

- **现象**：用户数据业务被放通但计费信息被缓存或丢弃
- **根因**：(1) CHF无响应 (2) CHF链路故障 (3) CHF返回异常结果码
- **排查**：用户跟踪消息 → ALM-100072告警
- **隐含知识**："放通"是容错机制，保证业务连续性但牺牲计费准确性。计费消息可能被缓存（等CHF恢复后回放）或丢弃。

### K121: 故障7 — 缓存消息未正常回放
> 来源: 缓存消息没有正常回放_80259372

**故障案例**

- **现象**：CHF恢复后SMF缓存消息未回放
- **根因**：(1) 无缓存文件 (2) N40链路不正常 (3) 缓存文件超期 (4) 未达到回放间隔
- **排查**：DSP CDRSTRGINFO → ALM-100072 → ALM-81059(超期告警) → LST N40MSGSTG(回放间隔)
- **隐含知识**：**回放四条件**全部满足才回放：有缓存文件 + 链路正常 + 文件未超期(CDRSTORAGECTRL) + 达到回放间隔(N40MSGSTG)。

### K122: 故障8 — CP和UP URR配置不一致
> 来源: CP和UP URR配置不一致_80259373

**故障案例**

- **现象**：ALM-81026(接口信元不一致) + ALM-81054(CP/UP关键配置不一致)
- **根因**：SMF和UPF的URR配置不一致
- **隐含知识**：SMF产生ALM-81026，UPF产生ALM-81054，是配对告警。URR变更必须同步CP和UP。

### K123: 故障9 — 计费流量与实际访问流量不一致
> 来源: N40接口计费流量与用户实际访问流量不一致_80259374

**故障案例**

- **现象**：N40上报的计费流量与用户实际访问流量不一致
- **根因**：(1) 存在免费业务(METERINGTYPE=FREE) (2) PCF动态Rule未指定RG (3) 预定义Rule不绑定RG (4) 欠费场景信令流量丢弃
- **排查**：LST URR(METERINGTYPE) → LST USERPROFILE(FREESER) → LST RULE → LST PCCPOLICYGRP → LST SPECTRAFURRGRP
- **隐含知识**：
  - 免费业务和欠费丢弃是"正常现象"，Rule未绑定RG是"配置错误"
  - Rule→PCCPOLICYGRP→URRGROUP→URR绑定链路任何一环断裂都导致流量不一致
  - 欠费场景信令流量由SPECTRAFURRGRP控制

### K124: 故障10 — 用户异常去活诊断体系
> 来源: 用户异常去活_80259375

**故障案例**

- **现象**：用户异常去活，Termination消息携带ABNORMAL_RELEASE
- **根因**：周边网元故障，通过diagnostics原因值定位
- **排查**：用户跟踪查看diagnostics字段 → LST N40DIAGTRIGGER

**关键运维知识 — 去活原因值映射表**：

| 原因值 | 指向网元 | 场景 |
|--------|---------|------|
| 12 | GTPC链路 | GTPC链路中断 |
| 21 | UPF | UPF收到Error indication |
| 22 | 对端网元 | 对端重启(recovery IE不匹配) |
| 258 | **CHF** | CHF返回信元不合法 |
| 262 | **CHF** | CHF响应超时 |
| 263 | **CHF** | 主备CHF重发均超时 |
| 302 | **PCF** | PCF无响应 |
| 351 | **UPF** | UPF请求去活 |
| 352 | **UPF** | UPF无响应 |

**原因值258子场景**：请求体类型与返回码不匹配、UPF独享配额模式下CHF未携带uPFID、CHF未携带ResultCode、SMF申请配额但CHF未授权也未指示重定向。

**关键参数**：SET CNVRGDCHGPARA的BADRSPACT=CONTINUE时允许CHF异常时业务继续而非去活。

---

## 三、接入侧功能

### K125: 3GPP PS Data Off功能
> 来源: 3GPP PS data off功能_74569639

**原理知识**

PS Data Off解决UE关闭移动数据开关后网络仍转发下行数据并产生计费的问题。生效需**同时满足三条件**：
1. UE携带3GPP PS Data Off UE Status为activated
2. SMF/PGW-C/GGSN-C配置PSDATAOFFSWITCH=ENABLE
3. 当前业务为**非豁免业务**

核心机制：网络侧通过下发Gate Status=closed的Create QER绑定到PDR上，阻止UPF向UE转发下行数据。

### K126: PS Data Off豁免业务与各制式差异
> 来源: 3GPP PS data off功能_74569639

**方案设计知识**

**豁免业务**：IMS默认豁免（SET APNIMSATTR/SET GLOBALIMS配置），其他通过ADD EXEMPTSERVICE配置。

**各制式差异**：

| 维度 | 2/3G | 4G | 5G |
|------|------|----|-----|
| UE携带方式 | PCO | PCO | **ePCO** |
| 能力协商 | 需协商 | 需协商 | **不需协商（5G必须支持）** |
| Non-3GPP互操作 | 不涉及 | 切到Non-3GPP时清除status并删QER | 不涉及 |

### K127: PS Data Off ULCL场景处理
> 来源: 3GPP PS data off功能_74569639

**方案设计知识**

- **I-UPF**：仅通知锚点UPF，不通知I-UPF
- **ULCL**：需同时通知主锚点+辅锚点UPF停止下行转发
- 新辅锚点插入时若data off已activated → 在PFCP Session Establishment Request中直接包含Gate Status=closed的Create QER

### K128: 计费暂停功能
> 来源: 计费暂停功能_30615504

**原理知识**

计费暂停用于移出网络覆盖区的用户，提高计费准确性。**仅4G支持，5G不支持**。

三个触发场景：
1. **S1 Release（ARRL）**：Release Access Bearers Request中ARRL=1，无线链路异常释放
2. **DDN寻呼失败**：DDN Acknowledge携带失败原因值（排除"Context not found"和"Unable to page UE due to Suspension"）
3. **下行丢包阈值**：SGW-U检测下行丢包达设定阈值后上报

### K129: 计费暂停能力协商与配置
> 来源: 计费暂停功能_30615504

**方案设计知识**

**协商流程**：SGW-C检查SET SGWCHGPAUSE → Create Session Request中PDN Pause Support Indication=1 → PGW-C检查ADD APNPGWCHGPAUSE(APN级优先)或SET GLBPGWCHGPAUSE(全局) → Response中PDN Pause Enable Indication=1

**PFCP机制**：触发计费暂停时PGW-C向PGW-U下发优先级最高的Create PDR（**不携带URR ID**，表示不计费），停止时下发Remove PDR。

**隐含规则**：计费暂停**只在空闲态生效**，Handover只在连接态，因此不可能同时存在。

### K130: 计费暂停互操作场景
> 来源: 计费暂停功能_30615504

**方案设计知识**

| 场景 | 处理 |
|------|------|
| PGW-C→GGSN-C | GGSN不支持，需停止计费暂停(Remove PDR) |
| GGSN-C→PGW-C | 重新协商；满足条件时下发丢包检测URR |
| PGW-C→SMF | 5G不支持，需停止计费暂停 |
| SMF→PGW-C | 重新协商；满足条件时下发丢包检测URR |

---

## 四、例行维护

### K131: N40接口链路状态检查
> 来源: 检查N40接口链路状态_86867966

**运维知识**

SMF和CHF之间N40接口链路状态检查步骤：
1. 执行`DSP SBILINKSTATUS`命令，选择对端NF类型为NFTypeCHF，检查链路状态是否为"正常"
2. 查看是否存在ALM-100072（目的NF服务不可达，对端网元类型为CHF）告警
3. 不符合预期时收集告警、日志、配置信息联系技术支持

---

## 知识统计

| 类别 | 数量 |
|------|------|
| 故障案例 | 10 (K115-K124) |
| 原理知识 | 3 (K125, K128) |
| 方案设计知识 | 4 (K126, K127, K129, K130) |
| 隐性规则 | 1 (K114) |
| 运维知识 | 1 (K131) |
| **合计** | **18条 (K114-K131)** |
