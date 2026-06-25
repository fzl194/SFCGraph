# Phase 3 参考文件：参数收集

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 3。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **用户必须已确认方案**：必须已通过 GATE-1（用户在 Phase 2 明确确认了匹配结果，含动作轨道 A/B 选择）。如果用户未确认方案，**STOP**，回到 Phase 2 等待用户确认。
2. **本阶段完成后必须 STOP**：执行完 §1~§4 后，**必须生成并展示 `xxxLLD.md` 后停止执行**，等待用户在 Phase 4（GATE-2）确认。`LLD` 就是 markdown 形式的规划数据表，不再拆成第二份同义文档。不得自动进入配置生成。
3. **禁止在本阶段生成任何 MML 配置命令**：本阶段只收集和推断参数，不生成配置。

---

> 本文件定义 Phase 3 的 pipeline 要求、输出模板和操作规则（访问限制场景专属）。
> 业务知识（参数语义、双轨道参数体系、推导规则）由 Agent 从图谱和知识库动态加载。
> 域共享参数规则（优先级、REFRESHSRV）见 `../业务感知域规则.md`，本文件不复述。

---

## 1. Pipeline 步骤

### Step 1: 从需求和现网中推断参数

**操作**：尽可能从以下来源自动推断参数值：
- 用户需求描述（动作类型、匹配条件、目标 URL/IP、URL 分类等）
- 现网配置（命名规律、已有参数值）
- 业务图谱中的方案示例（CS-AC-01~09 的 core_mechanism_combo）
- 知识库中的默认值

**必须加载**：
- `../../访问限制场景/three-layer-graph/04-command-graph.md` — 读取 CommandParameter 定义（§5 各命令关键参数集），确认参数枚举值和约束
- `../kb/02-双轨道动作机制与POLICYTYPE路由.md` — POLICYTYPE 路由决策规则
- `../kb/04-头增强族协议差异.md` / `../kb/05-重定向族.md` / `../kb/06-URL过滤与ICAP.md` — 各子轨参数语义（按匹配的 CS 闭包加载对应章节）

**推断规则**（现网命名规律）：
- 如果现网 RULE 命名为 `rule_pcc_xxx` / `rule_headen_xxx` / `rule_redirect_xxx`，则新 RULE 建议用相同前缀 + POLICYTYPE 语义命名
- 如果现网 HEADEN 对象命名为 `headen_http_msisdn`，则新 HEADEN 建议用 `headen_{protocol}_{datatype}` 命名
- 如果现网 IPFarm 命名为 `ipfarm_portal_01` / `ipfarm_proxy_01`，则按用途命名（Portal vs WebProxy）
- 优先级参考现网已有 RULE 的 PRIORITY 分布，保持合理间距（间距取 10 的倍数）
- URL 过滤 CATEGORYID 来自 ICAP Server，必须与 ICAP Server 返回分类一致（CR-AC-09）

### Step 2: 列出参数表（按动作轨道分组）

**操作**：根据 DP-AC-03（动作轨道）选择对应的参数表模板，对每条业务按模板展示参数，标注所有"待提供"和"待确认"项。

**必须加载**：
- `04-command-graph.md` — 读取 ConfigObject 关键参数列表
- `01-business-graph.md` — 读取 SemanticObject 定义，确认各动作类型对象差异

### Step 3: 全局参数

**操作**：列出不属于单条业务的全局参数（UserProfile、License 全集、SA 特征库、URL 过滤全局开关、UNC 侧位置组等）。

**必须加载**：
- `../kb/07-接入控制与UNC侧.md`（当 DP-AC-04 包含 SMF/AMF 时）— UNC 侧参数差异和协同要求
- `../kb/08-规则匹配与SA前置.md` — SA 识别前置与 License 依赖

---

## 2. 输出格式模板

### 2.1 轨道 A — PCC 阻塞方案（CS-AC-01）参数表

```markdown
### 业务 {N}: PCC 阻塞 {业务描述}

| 参数项 | UPF(UDG)侧 | SMF(UNC)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| **识别条件** | | | | |
| 匹配层次 (DP-AC-05) | L3/L4 / L7 / ADC | — | 需求 | 已知/待确认 |
| FILTER / L7FILTER | {五元组 / URL} | — | 需求 | 已知/待确认 |
| **阻塞参数** | | | | |
| POLICYTYPE | **PCC**（固定，CS-AC-01） | — | DP-AC-01 | 已知 |
| POLICYNAME 指向 | PCCPOLICYGRP | — | 自动 | 已知 |
| 兜底机制 | 是否启用 ADC 兜底阻塞 | — | 需求 | 待确认 |
| **计费属性（可选）** | | | | |
| URR / URRGROUP | { ONLINE/OFFLINE，仅 ADC/Portal/WebProxy/URL 过滤共用} | — | 需求 | 待确认 |
| **命名** | | | | |
| FILTER / FLOWFILTER / RULE 名 | {建议值} | {RULE 名必须一致} | 推断 | 已知/待确认 |
| **其他** | | | | |
| 优先级 PRIORITY | {数值} | {数值} | 见 §3 优先级分析 | 待确认 |
| 三网元一致性 (BR-AC-01) | RULE/FLOWFILTER 一致 | 同 UPF | 规则类型=预定义时 | 已知 |
```

### 2.2 轨道 A — 头增强方案（CS-AC-02）参数表

```markdown
### 业务 {N}: 头增强 {协议/字段}

| 参数项 | UPF(UDG)侧 | 来源 | 状态 |
|--------|-----------|------|------|
| **协议 (DP-AC-07)** | HTTP1.x / HTTPS(TLS) / RTSP | 需求 | 已知/待确认 |
| **HEADEN 对象参数** | | | |
| HEADERENNAME | {建议值} | 推断 | 已知/待确认 |
| DATATYPE | IMSI1 / MSISDN1 / IMEI1 / APN / ULI / MULTIPARA 等 25 类 | 需求 | 待提供 |
| PREFIXNAME | {如 X-msisdn，非 HTTP 标准头避免防欺诈失败} | 需求 | 待确认 |
| ENCRYALGORI | NONE / MD5 / RC4 / AES128 / AES256 / RSA1024 / RSA2048 / SHA256 | 需求 | 待确认 |
| PSWDKEY / PSWDKEYCONFIRM | {密钥，两字段必须一致} | 需求 | 待提供 |
| **★ HTTPS 协议差异 (BR-AC-08)** | | | |
| ENCRYALGORI 限制 | **无 RSA**，字段按 TLS TLV 格式插入 SSL Extension | 规则 | 已知 |
| 触发方式 | **仅基于 SNI** | 规则 | 已知 |
| **★ 防欺诈子模式 (BR-AC-06, CR-AC-04)** | | | |
| ANTIFRAUD | ENABLE / DISABLE（ENABLE 需 License 双开：HHAS+HTHE） | DP-AC-02 | 待确认 |
| GRAYLIST | ENABLE / DISABLE（ENABLE=只防欺诈不插入） | 需求 | 待确认 |
| **RTSP 限制 (CR-AC-11)** | RTSP 不支持防欺诈（族内唯一例外） | 规则 | 已知 |
| **RULE 参数** | | | |
| POLICYTYPE | **HEADEN**（固定，CS-AC-02） | — | 已知 |
| POLICYNAME | 指向 HEADEN 对象名 | 自动 | 已知 |
```

### 2.3 轨道 A — SMARTREDIRECT 重定向方案（CS-AC-03/04）参数表

```markdown
### 业务 {N}: {HTTP 重定向 / DNS 纠错}

| 参数项 | UPF(UDG)侧 | 来源 | 状态 |
|--------|-----------|------|------|
| **重定向类型 (CS-AC-03 vs 04)** | SMARTHTTPREDIR / DNSOVERWRITING | 需求 | 已知 |
| POLICYTYPE | **SMARTREDIRECT**（两特性共用，CR-AC-03） | — | 已知 |
| POLICYNAME 指向 | SMARTHTTPREDIR 对象 / DNSOVERWRITING 对象（区分点） | 自动 | 已知 |
| **HTTP 重定向参数 (CS-AC-03)** | | | |
| SMTHTTPREDINAME | {建议值} | 推断 | 已知/待确认 |
| SERVERURL | {重定向目标 URL} | 需求 | **待提供** |
| EXTFLTTYPE1/2 + EXTFLTNAME1/2 | AND/OR + EXTENDEDFILTER（URL/UA/ContentType 多维） | 需求 | 待确认 |
| BINDErrCODENAME | ERRORCODE（HTTP 错误码 GT 400 触发） | 需求 | 待确认 |
| APPENDINFONAME | REDIRAPPENDINFO（可选，携带 MSISDN/IMSI/IMEI） | 需求 | 待确认 |
| **DNS 纠错参数 (CS-AC-04)** | | | |
| DNSOVERWRTNAME | {建议值} | 推断 | 已知/待确认 |
| SERVERIP1 | {第三方 Platform IP} | 需求 | **待提供** |
| EXTFLTNAME1 | EXTENDEDFILTER（错误域名匹配） | 需求 | 待确认 |
| BINDERRCODENAME | ERRORCODE（DNS NXDOMAIN=3 触发） | 需求 | 待确认 |
| **★ 协议限制 (BR-AC-09)** | | | |
| HTTP 重定向 | 仅 HTTP1.x，不支持 HTTPS/HTTP2.0（加密盲区） | 规则 | 已知 |
| DNS 纠错 | 仅 UDP DNS，不支持 TCP DNS | 规则 | 已知 |
```

### 2.4 轨道 A — Portal/WebProxy 方案（CS-AC-05）参数表

```markdown
### 业务 {N}: {Portal captive / WebProxy}

| 参数项 | UPF(UDG)侧 | 来源 | 状态 |
|--------|-----------|------|------|
| **类型 (Portal vs WebProxy)** | Portal（PCC+captive）/ WebProxy（WEBPROXY+IP NAT） | 需求 | 已知 |
| **IPFarm 集群参数** | | | |
| IPFARMGLOBAL.LBMETHOD | ROUND_ROBIN / LEAST_RECENTLY_USED / LEAST_LOAD | 需求 | 待确认（默认 LEAST_LOAD） |
| HEALTHSUCCLIMIT / HEALTHFAILLIMIT | {心跳阈值} | 需求 | 待提供 |
| IPFARMNAME / IPVERSION / INTERFACENAME | {不同 IPFarm 必须用不同 LOGICINF 接口} | 需求 | 待提供 |
| IPFARMSERVER.SERVERIPV4/V6 | {Portal Server / Proxy Server IP 列表，每 Farm 最多 512 IP} | 需求 | **待提供** |
| **Portal 特有 (CS-AC-05 Portal)** | | | |
| POLICYTYPE | **PCC**（captive 配置在 USERPROFILE） | — | 已知 |
| USERPROFILE.CAPMODETHRES | {captive 周期分钟数，如 6} | 需求 | **待提供** |
| IPFARM.DEFAULTACT | Portal 全 DOWN 时 = **BLOCK**（兜底阻塞） | 规则 | 已知 |
| **WebProxy 特有 (CS-AC-05 WebProxy, CR-AC-10)** | | | |
| POLICYTYPE | **WEBPROXY**（POLICYNAME=IPFarm） | — | 已知 |
| BLACKLISTRULE | {黑名单规则} | 需求 | 待确认 |
| 双规则约束 (TR-AC-06) | 必须同时配 POLICYTYPE=PCC + POLICYTYPE=WEBPROXY 两条 RULE | 规则 | 已知 |
| ★ 协议支持 | **唯一支持 HTTPS/HTTP2.0 的重定向族**（L3 IP NAT） | 规则 | 已知 |
```

### 2.5 轨道 B — URL 过滤方案（CS-AC-06）参数表

```markdown
### 业务 {N}: URL 过滤 {BLOCK/PERMIT/REDIRECT}

| 参数项 | UPF(UDG)侧 | 来源 | 状态 |
|--------|-----------|------|------|
| **★ 动作轨道 (DP-AC-03)** | **轨道 B**（独立于 RULE 体系） | — | 已知 |
| **ICAP 互通前置 (CR-AC-05, TR-AC-05)** | | | |
| VPNINST.VPNINSTANCE | {ICAP 互通专网实例名} | 需求 | **待提供** |
| LOGICINF.NAME / IPVERSION / IP | {ICAP 互通接口（可与 Portal/WebProxy 共用 LOGICINF 类）} | 需求 | **待提供** |
| ICAPSERVER | ICAPSERVERNAME + ICAPSERVERTYPE=URL_FILTERING + ICAPSVRIPTYPE + IP + VPNINSTANCE | 需求 | **待提供** |
| ICAPLOCALINFO | ICAPSERVERTYPE + USERAGENT | 需求 | 待确认 |
| ICAPSVRGRP / ICAPSVRBINDISG | {服务器组与绑定} | 自动 | 已知 |
| **CF 业务层（轨道 B 核心，CR-AC-06）** | | | |
| CFPROFILENAME | {策略载体名} | 推断 | 已知/待确认 |
| CFTEMPLATE.ACTION | **BLOCK / PERMIT / REDIRECT**（模板级缺省动作；PERMIT 仅轨道 B） | DP-AC-01 | **待确认** |
| CONTCATEGBIND.ACTION | **BLOCK / PERMIT / REDIRECT**（分类级精确动作，覆盖模板级缺省） | 需求 | 待确认 |
| CONTCATEGROUP.CATEGORYID | {URL 分类 ID，来自 ICAP Server} | 需求 | **待提供** |
| APNCFTEMPLATE / CFPROFBINDCFT | {APN-模板绑定 / 策略-模板绑定} | 自动 | 已知 |
| CFCACHEPARA / CFWHITEURLLST / CFIPWHITELIST | {缓存参数 / 白名单（可选）} | 需求 | 待确认 |
| **★ RULE 触发层 (TR-AC-03)** | | | |
| RULE.POLICYTYPE | **PCC（仅触发匹配，动作不走 PCCPOLICYGRP）** | — | 已知 |
| RULE.POLICYNAME | 指向 PCCPOLICYGRP（仅匹配，实际动作走 CFTEMPLATE/CONTCATEGBIND） | 自动 | 已知 |
| ★ PERMIT 唯一性 (BR-AC-10) | 显式 PERMIT 仅本方案支持；轨道 A 无法显式 PERMIT | 规则 | 已知 |
| ★ HTTPS 限制 (CR-AC-10) | HTTPS 场景仅能基于 SNI 做分类（不能解析完整 URL） | 规则 | 已知 |
```

### 2.6 接入控制方案（CS-AC-07/09，UNC 侧）参数表

```markdown
### 业务 {N}: 接入控制 {SAR/区域漫游/ODB/位置触发}

| 参数项 | UNC(SMF/AMF)侧 | 来源 | 状态 |
|--------|---------------|------|------|
| **★ 接口模式 (DP-AC-03 任务层, TR-AC-08)** | 动态 PCC（PCRF/PCF 决策，跳过 USRLOCATION）/ 本地 PCC（无 PCRF，完整配置） | 需求 | **待确认** |
| **位置对象（仅本地 PCC）** | | | |
| USRLOCATION.LOCATIONTYPE | CGI（2/3G）/ ECGI（4G）/ NCGI（5G） | 需求 | 待确认 |
| USRLOCATION.MCC/MNC/LAC/ECI/NCI | {位置标识} | 需求 | **待提供** |
| USRLOCATIONGRP.LOCGROUPNAME | {位置组名} | 推断 | 已知/待确认 |
| UPBINDUPG.LOCGROUPNAME | {引用位置组} + UPBINDTYPE=SPECIFIC | 自动 | 已知 |
| APNUSRPROFG | {APN/DNN 绑定用户模板组} | 自动 | 已知 |
| **三网元位置一致性 (CR-AC-09)** | CGI/ECGI/NCGI 需 UNC+RAN+PCRF/PCF 三处一致 | 规则 | 已知 |
| **PCF 容灾 (DP-AC-08)** | SET PCCFAILACTION = CONTINUE / REDIRECT | 需求 | 待确认 |
```

### 2.7 全局参数表

```markdown
### 全局参数

| 参数项 | UPF(UDG)侧 | UNC(SMF)侧 | 来源 | 状态 |
|--------|-----------|-----------|------|------|
| License 全集 | SET LICENSESWITCH（按动作类型开：HTHE/SHPR/DNSO/CPPT/WEBP/HHAS/ADCF/UFBF） | SET LICENSESWITCH（PCIAL/PCC 等） | BR-AC-04 | 待确认 |
| SA 特征库 | LOD SIGNATUREDB + LOD PARSERDB（所有 L7 动作前置） | — | T-008 | 已知 |
| UserProfile 名 | {值} | {必须一致} | 现网/需求 | 已知/待确认 |
| PCCPOLICYGRP（轨道 A 计费属性） | {值}（ADC/Portal/WebProxy/URL 过滤共用） | — | 现网 | 已知/待确认 |
| URL 过滤全局开关 | SET GLBCFFUNC + SET CFSRVMODE | — | T-AC-108 | 待确认 |
| REFRESHSRV | **必须最后执行**（仅 UPF 侧） | 无 | BR-AC-05 | 已知 |
```

---

## 3. 优先级分析流程（必须独立执行，必须用户确认）

> **核心规则**：**数字越小，优先级越高**。不可更改。同 `../业务感知域规则.md` §3。

### 步骤

1. 从现网配置中提取**所有 RULE 的 PRIORITY 值**（不只是访问限制 RULE，要提取全部 RULE，含计费/带宽 RULE），用 Bash grep 搜索 `PRIORITY` 参数
2. 分析现网优先级分布规律（现网数据是最权威判断依据）
3. 根据用户描述的业务优先级关系，计算新规则 PRIORITY（间距取 10 的倍数）
4. 输出分析表（包含现网所有 RULE 的优先级 + 新 RULE 的拟插入位置）
5. **STOP。将分析表展示给用户，等待用户确认优先级值。**

### ★ 访问限制特有：双轨道并存时的优先级考量（CR-AC-14）

- 轨道 A（PCC 体系）与轨道 B（URL 过滤体系）可并存于同一用户业务流
- 双轨 RULE 独立匹配：PCC 类型 RULE 与 URL 过滤 RULE 用 POLICYTYPE=PCC 区分（但动作体系不同）
- WebProxy 必须配两条 RULE（POLICYTYPE=WEBPROXY + POLICYTYPE=PCC），RULENAME 不能同名（CR-AC-01）
- 优先级冲突时执行结果取决于配置优先级和规则匹配顺序（CR-AC-14），需现网验证

### STOP 条件

**完成分析表后必须 STOP，输出分析表并明确要求用户确认优先级。在用户确认之前：**

- **禁止**生成带 PRIORITY 的 RULE 命令
- **禁止**进入 Phase 5 配置生成
- 用户要求调整优先级 → 重新计算，再次等待确认

### 禁止事项

- **禁止**自行假设优先级顺序，必须先从现网提取全部 RULE 的 PRIORITY 数据
- **禁止**只提取访问限制 RULE 的优先级，必须提取现网所有 RULE 的优先级分布
- **禁止**在用户未确认优先级前生成任何带 PRIORITY 的 RULE 命令

---

## 4. 注意事项

- 参数表中每个字段都应标注"来源"（需求/现网/推断/图谱/知识库）和"状态"（已知/待确认/待提供）
- **双轨道参数体系严格区分**：轨道 A 参数（POLICYTYPE/POLICYNAME/HEADEN/IPFARM/SMARTREDIR）与轨道 B 参数（CFTEMPLATE.ACTION/CONTCATEGBIND.ACTION/ICAP 系列）不可混用
- 两侧共用参数（RULENAME、USERPROFILENAME、URRID 等）必须标注"必须与 UPF 一致"（仅当 UNC 侧涉及）
- 头增强族协议差异（HTTP/HTTPS/RTSP）参数必须从 `kb/04-头增强族协议差异.md` 确认，特别是 HTTPS 无 RSA、RTSP 不支持防欺诈
- URL 过滤 CATEGORYID 必须与 ICAP Server 返回分类一致，不可自行编造（CR-AC-09）
- 配置对象引用完整性（CR-AC-08）：RULE.POLICYNAME / FLOWFILTERNAME 必须引用已存在对象，参数表中标注依赖
