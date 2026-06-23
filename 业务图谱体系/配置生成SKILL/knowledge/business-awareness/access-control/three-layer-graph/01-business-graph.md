# 访问限制场景三层图谱 · 第1层：业务图谱

> **文件定位**：`three-layer-graph/01-business-graph.md`
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §8 业务图谱（§8.3~§8.12）
> **本体参考**：`三层图谱本体标准定义.md`、`三层图谱对象与关系设计.md`
> **作用**：实例化访问限制场景业务层对象（BD/NS/CS/DP/BR/SO）及其关系边
> **与现有横向分析的关系**：本文件为 `cross-topic-analysis.md` §6（9个CS闭包+8个DP）的业务层落地，字段严格按 Schema §8.7~§8.12 实例化，不修改原横向分析文件。

---

## 0. 适用定义与来源

### 0.1 根定义
- `三层图谱本体标准定义.md`
- `三层图谱Schema-最终版-v0.1.md`

### 0.2 访问限制场景知识来源
- `cross-topic-analysis.md`（1558行，8批次约117份源文档综合分析）
- `feature-knowledge/cross-feature-analysis.md`（11特性横向分析）
- `feature-knowledge/*.md`（11个特性知识文档，UDG 10 + UNC 1）
- `topic-knowledge/Batch-*.md`（8个主题知识批次）

### 0.3 证据ID约定（占位，06-evidence-index建时对齐）
- `EV-CA-AC-01`：cross-topic-analysis.md（横向综合分析）
- `EV-CA-AC-02`：feature-knowledge/cross-feature-analysis.md（特性横向分析）
- `EV-FK-AC-NN`：feature-knowledge/*.md（特性知识，NN为特性序号占位）
- `EV-TK-AC-NN`：topic-knowledge/Batch-NN.md（主题知识批次）

---

## 1. BusinessDomain + NetworkScenario

### 1.1 BusinessDomain

| 字段 | 值 |
|------|---|
| `domain_id` | `BD-AC-01` |
| `domain_name` | `业务感知` |
| `domain_summary` | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制。访问限制是 SA 的"安全防护"领域实现，通过过滤、管理 UPF 承载的数据面流量，对用户访问请求执行阻塞/头增强/重定向/URL 过滤的差异化控制 |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-CA-AC-02`, `EV-FK-AC-01` |

> **★ 三场景共享说明 ★**：`BD-AC-01 = BD-CH-01 = BD-BW-01`，三者是同一根对象 `业务感知`。计费（套餐1）、带宽控制（套餐2）、访问限制（套餐3）三场景均挂在此域下，共享 SA 基础设施（规则匹配引擎、业务识别框架、PCC 策略体系）。

### 1.2 NetworkScenario

| 字段 | 值 |
|------|---|
| `scenario_id` | `NS-AC-01` |
| `scenario_name` | `访问限制场景` |
| `scenario_summary` | 对用户访问网络/业务/内容的请求，根据用户身份、位置、套餐配额、应用类型、URL 分类、接入网元等维度，执行阻塞（DISCARD）、头增强（HEADEN）、重定向（REDIRECT）、URL 过滤（BLOCK/PERMIT/REDIRECT）的差异化访问控制 |
| `judgment_basis` | 需阻塞非法内容/IP 访问；或需在请求报文头插入运营商字段（MSISDN/IMSI）；或需将用户访问引导到指定页面/服务器（充值页/Portal/纠错页）；或需基于 URL 分类执行 BLOCK/PERMIT/REDIRECT；或需在注册/会话阶段执行 SAR/区域/ODB 粗粒度接入控制 |
| `typical_outcome` | 实现 PCC 阻塞/头增强族/重定向族（轨道 A 五子轨）/URL 过滤（轨道 B 独立）/UNC 接入控制的差异化访问控制；双轨道可并存；与计费、带宽控制可叠加执行（类型独立原则） |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-CA-AC-02`, `EV-FK-AC-01`, `EV-TK-AC-01` |

#### 场景边界

**覆盖范围**：
- 产品：UDG（用户面，10特性）+ UNC（控制面，1特性 + 接入控制辅助特性）
- 网元：UPF/PGW-U（UDG，执行体）、SMF/PGW-C/AMF（UNC，决策体+接入控制）、PCF（策略决策源）、ICAP Server（URL 过滤外部依赖）
- 接口：Gx（2/3/4G）、N7（5G）、N4（PFCP）、ICAP（URL 过滤外部协议）
- 动作维度：DISCARD / HEADEN / REDIRECT / PERMIT（URL 过滤独有）/ BLOCK（URL 过滤）
- 控制维度：用户身份、位置（CGI/ECGI/NCGI/PRA/PLMN）、套餐配额、应用类型（ADC）、URL 分类、接入网元（SAR/区域/ODB）

**不覆盖范围**（相邻场景）：
- 计费场景（套餐1）：差异化计费、免费业务、配额计费动作（URR/CG/Ga/Gy/N40 链路，由计费场景图谱承载）
- 带宽控制场景（套餐2）：BWM 限速、Shaping 整形、FUP 降速、GBR 保证（由带宽控制场景图谱承载）
- 访问限制场景不涉及独立协议层 SemanticObject（无 Ga/Gy/N40），这是与计费场景的关键差异

---

## 2. ConfigurationSolution（9个方案闭包）

> **拆分依据**：`cross-topic-analysis.md` §6.3（9个方案闭包）+ §4.1（双轨动作机制）+ §5（依赖关系）。
> 9个方案闭包按"动作类型×动作轨道×触发维度"三正交维度归纳：
> - DISCARD 类（1个）：CS-AC-01 PCC 阻塞
> - HEADEN 类（1个）：CS-AC-02 头增强
> - REDIRECT 类（6个）：CS-AC-03 HTTP 重定向 / CS-AC-04 DNS 重定向 / CS-AC-05 Portal-WebProxy 重定向 / CS-AC-08 配额耗尽重定向 / CS-AC-09 区域引导重定向
> - BLOCK/PERMIT/REDIRECT 类（1个）：CS-AC-06 URL 过滤（轨道 B）
> - 接入控制类（1个）：CS-AC-07 UNC 接入控制（粗粒度，独立于 UDG 侧 PCC）

### 2.1 CS-AC-01 PCC 阻塞方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-01` |
| `solution_name` | `PCC 阻塞方案` |
| `solution_summary` | 通过 PCC 策略类型（POLICYTYPE=PCC）的兜底阻塞或显式阻塞动作丢弃用户报文，实现非法内容/IP 的访问禁止 |
| `design_intent` | 解决"禁止访问非法内容/IP"问题：阻塞不安全数据中心、非法网站、ADC 兜底阻塞 |
| `core_mechanism_combo` | `FILTER/FLOWFILTER（L3/L4 匹配）[+L7FILTER（L7 匹配）] → RULE（POLICYTYPE=PCC） → PCCPOLICYGRP → USERPROFILE → UDG 执行 DISCARD` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-02`, `EV-TK-AC-01`, `EV-TK-AC-02`, `EV-TK-AC-04` |

**scopes**: subscriber（单用户阻塞）、service_selection（按业务类型阻塞，如特定 APP）

**participants**:
- UPF（执行 DISCARD 丢弃报文，user_plane）
- SMF（规则下发与翻译，control_plane）
- PCF（动态阻塞策略决策，external_system）

**uses_feature**: GWFD-020351, WSFD-109101, GWFD-020357
**uses_semantic_object**: SO-AC-01（动作类型-DISCARD）, SO-AC-02（过滤条件）, SO-AC-06（规则语义）
**constrained_by**: BR-AC-01, BR-AC-03, BR-AC-04, BR-AC-05, BR-AC-07

### 2.2 CS-AC-02 头增强方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-02` |
| `solution_name` | `头增强方案` |
| `solution_summary` | 在 HTTP/HTTPS/RTSP 请求报文头插入运营商规划字段（MSISDN/IMSI/IMEI/APN/位置等），支持业务认证、个性化服务、防欺诈校验；可选启用头防欺诈作为前置安全检测 |
| `design_intent` | 解决"业务服务器需获取用户真实身份"问题：WAP 网关、业务认证、防欺诈校验、个性化服务 |
| `core_mechanism_combo` | `FILTER/L7FILTER → FLOWFILTER → HEADEN 对象（含可选 ANTIFRAUD/GRAYLIST） → RULE（POLICYTYPE=HEADEN） → USERPROFILE → UDG 插入字段` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-CA-AC-02`, `EV-FK-AC-03`, `EV-FK-AC-04`, `EV-TK-AC-05`, `EV-TK-AC-08` |

**scopes**: subscriber（单用户头增强）、service_selection（按业务类型/URL/SNI 触发）

**participants**:
- UPF（L7 解析与字段插入，user_plane）
- ADC/SA 引擎（L7 解析前置，提供 URL/SNI/Method）

**uses_feature**: GWFD-110261, GWFD-110262, GWFD-110263, GWFD-110401, GWFD-020357
**uses_semantic_object**: SO-AC-01（动作类型-HEADEN）, SO-AC-04（头增强字段）, SO-AC-06（规则语义）
**constrained_by**: BR-AC-01, BR-AC-04, BR-AC-05, BR-AC-06, BR-AC-08

### 2.3 CS-AC-03 HTTP 重定向方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-03` |
| `solution_name` | `HTTP 重定向方案` |
| `solution_summary` | 基于 HTTP 错误码/URL/UserAgent/ContentType 等多条件触发，改写 HTTP 响应为 301/302/303 重定向，引导用户跳转到第三方服务器/内容过滤页 |
| `design_intent` | 解决"URL 纠错、内容过滤、错误码自动重定向"问题：将错误访问引导到正确页面 |
| `core_mechanism_combo` | `EXTENDEDFILTER（多维度） → ERRORCODE → SMARTHTTPREDIR → RULE（POLICYTYPE=SMARTREDIRECT） → USERPROFILE → UDG 改写 HTTP 响应` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-05`, `EV-TK-AC-06` |

**scopes**: service_selection（按 URL/UserAgent/ContentType 匹配）

**participants**:
- UPF（L7 HTTP 响应改写，user_plane）
- ADC/SA 引擎（L7 解析前置）

**uses_feature**: GWFD-110284, GWFD-020357, GWFD-110261
**uses_semantic_object**: SO-AC-01（动作类型-REDIRECT）, SO-AC-03（重定向目标-SMARTHTTPREDIR）, SO-AC-07（动作轨道-SMARTREDIRECT）
**constrained_by**: BR-AC-04, BR-AC-05, BR-AC-07, BR-AC-09

### 2.4 CS-AC-04 DNS 重定向方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-04` |
| `solution_name` | `DNS 重定向方案` |
| `solution_summary` | 构造新的 DNS 响应（DNS Overwriting），将解析失败域名的响应 IP 指向第三方 Platform，在用户建立 TCP 之前介入，实现错误域名引导 |
| `design_intent` | 解决"域名解析失败引导"问题：用户输错域名时跳转到纠错页 |
| `core_mechanism_combo` | `EXTENDEDFILTER（URL） → ERRORCODE（DNS 错误码如 NXDOMAIN=3） → DNSOVERWRITING → RULE（POLICYTYPE=SMARTREDIRECT） → USERPROFILE → UDG 改写 DNS 响应` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-06`, `EV-TK-AC-06` |

**scopes**: service_selection（按 DNS 查询域名匹配）

**participants**:
- UPF（DNS 解析层重写，user_plane）
- ADC/SA 引擎（DNS 解析前置）

**uses_feature**: GWFD-110283, GWFD-020357
**uses_semantic_object**: SO-AC-01（动作类型-REDIRECT）, SO-AC-03（重定向目标-DNSOVERWRITING）, SO-AC-07（动作轨道-SMARTREDIRECT）
**constrained_by**: BR-AC-04, BR-AC-05, BR-AC-09

### 2.5 CS-AC-05 Portal/WebProxy 重定向方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-05` |
| `solution_name` | `Portal/WebProxy 重定向方案` |
| `solution_summary` | 通过 IP Farm 服务器集群实现重定向：用户 Portal 为周期性 captive/non-captive 交替（业务订购/广告推送），WebProxy 为透明 IP NAT（网络加速/病毒防护/内容过滤，唯一能处理加密协议） |
| `design_intent` | 解决"业务订购推送、透明网络加速、加密协议重定向"问题；Portal 用于感知型重定向，WebProxy 用于无感知代理（HTTPS/HTTP2.0 场景唯一选择） |
| `core_mechanism_combo` | `Portal：IPFARM+IPFARMSERVER+LOGICINF → PCCPOLICYGRP（含 captive） → USERPROFILE（CAPMODETHRES）；WebProxy：IPFARM+IPFARMSERVER+LOGICINF+BLACKLISTRULE → RULE（POLICYTYPE=WEBPROXY） → USERPROFILE` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-07`, `EV-FK-AC-08`, `EV-TK-AC-06` |

**scopes**: subscriber（单用户 Portal captive）、service_selection（WebProxy 按 TCP SYN 匹配）

**participants**:
- UPF（Portal HTTP 响应改写 / WebProxy L3 IP NAT，user_plane）
- IP Farm 服务器集群（Portal Server / Proxy Server，service_endpoint）
- ADC/SA 引擎（Portal 依赖 L7 解析）

**uses_feature**: GWFD-110281, GWFD-110282, GWFD-020357
**uses_semantic_object**: SO-AC-01（动作类型-REDIRECT）, SO-AC-03（重定向目标-IPFarm/WebProxy）, SO-AC-07（动作轨道-PCC/WEBPROXY）
**constrained_by**: BR-AC-04, BR-AC-05, BR-AC-07, BR-AC-09

### 2.6 CS-AC-06 URL 过滤方案（轨道 B）

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-06` |
| `solution_name` | `URL 过滤方案` |
| `solution_summary` | 通过 ICAP 协议将用户访问的 URL 上送给外部 ICAP Server 分类，根据返回的分类匹配本地套餐策略执行 BLOCK/PERMIT/REDIRECT；**访问限制场景唯一显式支持 PERMIT 的方案**，独立于 PCC 体系（轨道 B） |
| `design_intent` | 解决"基于 URL 分类的内容过滤"问题：家长控制、企业内容过滤、合规要求；需要外部 URL 分类数据库支持 |
| `core_mechanism_combo` | `VPNINST+LOGICINF+ICAPSERVER+ICAPSVRGRP（互通） → APN+APNCFFUNC+CFPROFILE+CFTEMPLATE（含 ACTION）+APNCFTEMPLATE+CFPROFBINDCFT+CONTCATEGROUP+CONTCATEGBIND（含 ACTION） → UDG 直接执行 BLOCK/PERMIT/REDIRECT` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-09`, `EV-TK-AC-07` |

**scopes**: subscriber（单用户 URL 分类过滤）、service_selection（按 URL 分类匹配）

**participants**:
- UPF（URL 提取与动作执行，user_plane）
- ICAP Server（外部 URL 分类数据库，external_system）
- ADC/SA 引擎（URL/SNI 解析前置）

**uses_feature**: GWFD-110471, GWFD-020357
**uses_semantic_object**: SO-AC-01（动作类型-BLOCK/PERMIT/REDIRECT）, SO-AC-02（过滤条件-URL 分类）, SO-AC-07（动作轨道-URL 过滤体系）
**constrained_by**: BR-AC-01, BR-AC-03, BR-AC-04, BR-AC-05, BR-AC-10

### 2.7 CS-AC-07 接入控制方案（UNC 侧）

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-07` |
| `solution_name` | `接入控制方案` |
| `solution_summary` | 在注册/会话阶段基于 SAR（服务区域限制）/区域漫游/ODB（所有权闭锁）/位置触发等执行粗粒度接入控制，决策"是否允许接入"；与 UDG 侧业务流细粒度控制构成完整访问限制链路 |
| `design_intent` | 解决"区域套餐、漫游限制、ODB 欠费禁用、拥塞小区流控"问题：在用户接入网络前完成粗粒度准入决策 |
| `core_mechanism_combo` | `移动接入控制：AMF 的 SAR/区域漫游/ODB；会话接入控制：SMF 的服务区域限制；位置触发：USRLOCATION+USRLOCATIONGRP+UPBINDUPG+APNUSRPROFG → 策略下发` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-10`, `EV-FK-AC-11`, `EV-TK-AC-03`, `EV-TK-AC-07` |

**scopes**: access（按接入点/DNN 粒度）、location（按 CGI/ECGI/NCGI/PRA/PLMN 位置触发）

**participants**:
- AMF（注册阶段移动接入控制，SAR/区域/ODB，control_plane）
- SMF（会话阶段服务区域限制，control_plane）
- PCF（基于位置的策略决策，external_system）

**uses_feature**: WSFD-211001, WSFD-106003, WSFD-105003, WSFD-106005, WSFD-105006
**uses_semantic_object**: SO-AC-05（位置条件-USRLOCATION）, SO-AC-06（规则语义-接入控制）
**constrained_by**: BR-AC-01, BR-AC-04, BR-AC-05

### 2.8 CS-AC-08 配额耗尽重定向方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-08` |
| `solution_name` | `配额耗尽重定向方案` |
| `solution_summary` | FUP 配额耗尽触发 US_RE/NO_CREDIT 事件，PCF 决策下发携带 RedirectInformation 的 PCC 规则，重定向用户到充值页面；走轨道 A（PCC 体系）+ PCF 决策垄断 |
| `design_intent` | 解决"套餐耗尽后引导充值"问题：流量/时长配额耗尽或信用失效时禁止上网并跳转充值页 |
| `core_mechanism_combo` | `UPCF 配额+触发器（US_RE/NO_CREDIT）+条件组+动作组（含重定向） → PCF 通过 N7 下发 → SMF 映射 N4 → UPF 执行重定向` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-02`, `EV-TK-AC-03` |

**scopes**: subscriber（单用户配额状态）、subscription（会话级配额累计）

**participants**:
- PCF（配额管理与重定向决策，external_system）
- SMF（N7→N4 策略翻译，control_plane）
- UPF（重定向执行，user_plane）

**uses_feature**: GWFD-020351, WSFD-109101, GWFD-110284
**uses_semantic_object**: SO-AC-01（动作类型-REDIRECT）, SO-AC-03（重定向目标-RedirectInformation URL）, SO-AC-07（动作轨道-PCC）
**constrained_by**: BR-AC-01, BR-AC-04, BR-AC-05, BR-AC-07, BR-AC-09

### 2.9 CS-AC-09 区域引导重定向方案

| 字段 | 值 |
|------|---|
| `solution_id` | `CS-AC-09` |
| `solution_name` | `区域引导重定向方案` |
| `solution_summary` | 用户进入特定位置区域（PRA）或漫游（PLMN 变更）时，PCF 决策下发重定向策略到套餐订购页或免费接入验证页；走轨道 A（PCC 体系）+ PCF 决策 + 位置触发 |
| `design_intent` | 解决"出国引导签约优惠套餐、热点接入区域引导订购"问题：基于用户位置变化主动推送业务 |
| `core_mechanism_combo` | `WSFD-211001（USRLOCATION）+ UPCF 触发器（PRA_CH/PLMN_CH/SAREA_CH）+条件组+动作组（重定向） → PCF → SMF → UPF` |
| `status` | `active` |
| `source_evidence_ids` | `EV-CA-AC-01`, `EV-FK-AC-11`, `EV-TK-AC-03`, `EV-TK-AC-07` |

**scopes**: location（按 PRA/PLMN/服务区域触发）、subscriber（单用户位置策略）

**participants**:
- PCF（基于位置的重定向决策，external_system）
- SMF（位置触发上报与策略翻译，control_plane）
- UPF（重定向执行，user_plane）

**uses_feature**: WSFD-211001, GWFD-110284, GWFD-110281
**uses_semantic_object**: SO-AC-01（动作类型-REDIRECT）, SO-AC-03（重定向目标-套餐订购/验证页）, SO-AC-05（位置条件）, SO-AC-07（动作轨道-PCC）
**constrained_by**: BR-AC-01, BR-AC-04, BR-AC-05, BR-AC-09

---

## 3. DecisionPoint（8个）

> Schema §8.8 共 11 个必选字段（decision_id / owner_layer / owner_ref_type / owner_ref / decision_name / decision_question / option_set / trigger_condition / impact_summary / status / source_evidence_ids）。本节按 13 列宽表展示（含触发条件、影响摘要、状态、证据）。

| `decision_id` | `owner_layer` | `owner_ref_type` | `owner_ref` | `decision_name` | `decision_question` | `option_set` | `trigger_condition` | `impact_summary` | `status` | `source_evidence_ids` |
|---------------|---------------|-------------------|-------------|-----------------|---------------------|--------------|---------------------|------------------|----------|----------------------|
| `DP-AC-01` | `business` | `network_scenario` | `NS-AC-01` | 动作类型选择 | 访问限制应执行哪种动作 | `["DISCARD-阻塞","HEADEN-头增强","REDIRECT-重定向","PERMIT-放行(仅URL过滤)"]` | 进入访问限制配置时 | 决定 CS 闭包（CS-AC-01/02/03~05/06）和动作对象；决定 RULE.POLICYTYPE 或 CFTEMPLATE.ACTION 路径 | `active` | `EV-CA-AC-01`, `EV-TK-AC-01`, `EV-TK-AC-02` |
| `DP-AC-02` | `business` | `network_scenario` | `NS-AC-01` | 规则类型选择 | 访问限制规则应使用动态、预定义还是本地 | `["动态规则(PCF实时,无L7)","预定义规则(UPF本地,支持L7)","本地规则(SMF兜底)"]` | 确定动作类型后 | 决定规则生命周期、三网元一致性要求、是否支持 L7；URL 过滤/定向业务必须用预定义（PCF 无 L7 能力） | `active` | `EV-CA-AC-01`, `EV-TK-AC-01`, `EV-TK-AC-02`, `EV-TK-AC-03` |
| `DP-AC-03` | `business` | `network_scenario` | `NS-AC-01` | 动作轨道选择 | 访问限制走轨道 A（PCC 体系）还是轨道 B（URL 过滤体系） | `["轨道A-PCC体系(RULE.POLICYTYPE驱动)","轨道B-URL过滤体系(CFTEMPLATE.ACTION驱动)"]` | 方案设计阶段 | 决定 ConfigObject 体系（RULE vs CFTEMPLATE）、动作指定方式（隐式 vs 显式）、外部依赖（可选 PCRF vs 必需 ICAP）、是否支持 PERMIT | `active` | `EV-CA-AC-01`, `EV-TK-AC-07` |
| `DP-AC-04` | `business` | `network_scenario` | `NS-AC-01` | 网元范围选择 | 访问限制规则应下发到哪些网元/UPF | `["UPF执行(业务流细粒度)","SMF决策翻译","AMF接入控制(注册阶段)","主+辅锚点ALL","仅主锚点CENTRAL","仅辅锚点LOCAL","DNAI指定辅锚点"]` | SMF 策略下发阶段 | 决定规则生效范围、配置一致性要求；UNC 侧粗粒度接入控制 vs UDG 侧细粒度业务控制 | `active` | `EV-CA-AC-01`, `EV-TK-AC-02`, `EV-TK-AC-03` |
| `DP-AC-05` | `business` | `network_scenario` | `NS-AC-01` | 匹配层次选择 | 访问限制应基于哪个协议层匹配 | `["L3/L4-三四层(IP/端口)","L7-七层(URL/SNI/Method/UserAgent)","DNS层-DNS查询","应用层-ADC应用标识"]` | UPF 规则配置阶段 | 决定 Filter 类型（FILTER/L7FILTER/EXTENDEDFILTER）、SA 依赖、协议限制；HTTPS 场景 L7 只能基于 SNI | `active` | `EV-CA-AC-01`, `EV-TK-AC-01`, `EV-TK-AC-04` |
| `DP-AC-06` | `business` | `network_scenario` | `NS-AC-01` | 重定向目标选择 | REDIRECT 动作应重定向到哪种目标 | `["充值页(CS-AC-08)","套餐订购页(CS-AC-09/Portal)","Portal服务器(CS-AC-05)","Proxy服务器(CS-AC-05 WebProxy)","第三方服务器(CS-AC-03)","第三方Platform(CS-AC-04 DNS)"]` | 选择 REDIRECT 动作后 | 决定重定向特性选择（HTTP 重定向/DNS/Portal/WebProxy）、IP Farm 需求、EXTENDEDFILTER 需求 | `active` | `EV-CA-AC-01`, `EV-TK-AC-06` |
| `DP-AC-07` | `business` | `network_scenario` | `NS-AC-01` | 协议支持选择 | 访问限制方案需支持哪些协议 | `["仅HTTP1.x","HTTP1.x+HTTPS(TLS1.2/1.3)","HTTP1.x+RTSP","任意TCP含HTTPS/HTTP2.0(仅WebProxy)","DNS(UDP)"]` | 方案设计阶段 | 决定特性选择、SA 依赖、加密算法需求；仅 WebProxy 能处理加密协议（L3 不依赖 L7 解析） | `active` | `EV-CA-AC-01`, `EV-TK-AC-05`, `EV-TK-AC-06` |
| `DP-AC-08` | `business` | `network_scenario` | `NS-AC-01` | PCF 容灾决策 | PCF 故障时访问限制策略如何保证连续性 | `["回落本地PCC(SET PCCFAILACTION)","会话失败(严格模式)","DNN粒度混合(动态+本地)"]` | SMF 容灾配置阶段 | 决定访问限制策略的可靠性、容灾能力；本地 PCC 精细化程度低于 PCF 策略 | `active` | `EV-CA-AC-01`, `EV-TK-AC-03` |

---

## 4. BusinessRule（10条）

> Schema §8.9 共 9 列。`rule_type` 严格使用合法枚举：`selection_rule / scope_rule / design_rule / acceptance_rule / diagnosis_rule`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `rule_logic` | `violation_effect` | `status` | `source_evidence_ids` |
|-----------|-------------|-------------|------------------------|--------------------|--------------|---------------------|----------|----------------------|
| `BR-AC-01` | 预定义规则三网元一致性 | `design_rule` | `explicit` | `design` | 凡涉及预定义 PCC 规则（PCF 下发规则名激活）的特性，SMF/UPF/PCF 三网元的规则名、URR ID、流量过滤器 FlowFilter、动作定义必须完全一致 | 规则激活失败，访问限制不生效 | `active` | `EV-CA-AC-01`, `EV-TK-AC-02`, `EV-TK-AC-03` |
| `BR-AC-02` | 规则匹配类型独立原则 | `design_rule` | `explicit` | `principle` | 不同类型规则（PCC/BWM/HEADEN）匹配独立进行，每种类型至多一条生效，不同类型可叠加执行（如阻塞+限速+插头同时命中一条报文） | 误以为冲突而删除其一，导致某段访问限制失控 | `active` | `EV-CA-AC-01`, `EV-TK-AC-01` |
| `BR-AC-03` | 一条规则绑定一条策略 | `design_rule` | `explicit` | `design` | 规则与策略是 1:1 关系，策略与动作类型是 1:1 关系；若要同一流量同时执行阻塞和重定向，必须通过两条不同优先级的规则分别承载 | 复合动作无法用单条规则实现，配置混乱 | `active` | `EV-CA-AC-01`, `EV-TK-AC-01` |
| `BR-AC-04` | License 前置门控 | `scope_rule` | `explicit` | `config` | 各访问限制子能力独立 License；强依赖关系必须双开：头防欺诈(82209786) → HTTP 头增强(82209777)；ADC → SA-Basic(82209749) + PCC(82209825)；WSFD-211001 → PCC + BWM（无 PCRF 场景） | 配置命令成功但功能不生效，难以排查 | `active` | `EV-CA-AC-01`, `EV-FK-AC-04` |
| `BR-AC-05` | REFRESHSRV 必须最后执行 | `acceptance_rule` | `explicit` | `ops` | UDG 侧策略变更（Filter/FlowFilter/RULE 等）后必须执行 `SET REFRESHSRV:REFRESHTYPE=ALL;`，且执行后约 60 秒（PROTBINDFLOWF 定时器）策略才完全下发 | 策略配置完成但未生效，验证失败 | `active` | `EV-CA-AC-01`, `EV-TK-AC-02` |
| `BR-AC-06` | 头防欺诈依赖头增强 | `design_rule` | `explicit` | `design` | 头防欺诈（GWFD-110401）完全寄生头增强配置链路，无独立 MML；启用 ANTIFRAUD 必须同时开启头增强；执行顺序：防欺诈检测 → 字段纠正/冗余清理 → 头增强插入；RTSP 不支持防欺诈 | 防欺诈无法独立生效；RTSP 协议存在安全盲区 | `active` | `EV-CA-AC-01`, `EV-FK-AC-04`, `EV-TK-AC-08` |
| `BR-AC-07` | RULE.POLICYTYPE 决定动作轨道（双轨道+五子轨） | `selection_rule` | `explicit` | `design` | 轨道 A（PCC 体系）动作类型由 RULE.POLICYTYPE 隐式决定（轨道 A 内含五子轨：PCC→DISCARD/REDIRECT 配额、ADC→兜底阻塞、HEADEN→字段插入、SMARTREDIRECT→HTTP/DNS 重定向、WEBPROXY→L3 IP NAT）；轨道 B（URL 过滤体系）由 CFTEMPLATE/CONTCATEGBIND.ACTION 显式决定 BLOCK/PERMIT/REDIRECT（独立于 RULE 体系） | POLICYTYPE 选错导致动作类型错误，访问限制行为不符合预期 | `active` | `EV-CA-AC-01`, `EV-TK-AC-01`, `EV-TK-AC-07` |
| `BR-AC-08` | 头增强字段加密与编码约束 | `design_rule` | `explicit` | `config` | HTTP 头增强支持 MD5/RC4/AES-128/256/RSA-1024/2048/SHA-256；HTTPS 头增强无 RSA，字段须按 TLS TLV 格式插入 SSL Extension；编码支持 base64+ASCII（HTTPS 额外支持十六进制）；HTTPS 触发仅基于 SNI | 加密算法/编码不匹配导致业务服务器无法解析字段 | `active` | `EV-CA-AC-01`, `EV-FK-AC-03`, `EV-TK-AC-05` |
| `BR-AC-09` | 加密协议仅 WebProxy 可处理 | `scope_rule` | `explicit` | `restriction` | HTTPS/HTTP2.0 场景的重定向必须用 WebProxy（L3 IP NAT 不依赖 L7 解析）；HTTP 智能重定向仅 HTTP1.x，DNS 纠错仅 UDP DNS，Portal 仅 HTTP1.x/WAP | 选错重定向方式导致加密协议场景重定向失效 | `active` | `EV-CA-AC-01`, `EV-FK-AC-08`, `EV-TK-AC-06` |
| `BR-AC-10` | PERMIT 唯一性（URL 过滤独有） | `selection_rule` | `explicit` | `design` | URL 过滤是访问限制场景中唯一显式支持 PERMIT 动作的方案（轨道 B）；轨道 A 特性只能"不做动作（隐式放行）"或"做阻塞/重定向"，无显式 PERMIT；家长控制/企业白名单场景必须用 URL 过滤 | 白名单场景误用轨道 A 导致无法显式放行 | `active` | `EV-CA-AC-01`, `EV-FK-AC-09`, `EV-TK-AC-07` |

---

## 5. SemanticObject（7个）

> Schema §8.10 字段：semantic_object_id / semantic_object_name / semantic_summary / semantic_layer_hint / status / source_evidence_ids。
> 访问限制场景无独立协议层 SemanticObject（无 Ga/Gy/N40），这是与计费场景的关键差异（与带宽控制场景一致）。

| `semantic_object_id` | `semantic_object_name` | `semantic_summary` | `semantic_layer_hint` | `status` | `source_evidence_ids` |
|----------------------|------------------------|--------------------|---------------------|----------|-----------------------|
| `SO-AC-01` | 动作类型 | DISCARD / HEADEN / REDIRECT / PERMIT / BLOCK 五种动作类型；前四种跨轨道通用，PERMIT 为 URL 过滤独有 | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-TK-AC-01`, `EV-TK-AC-02` |
| `SO-AC-02` | 过滤条件 | 三四层过滤（FILTER）/ 七层过滤（L7FILTER-URL/SNI/Method）/ 流过滤器（FLOWFILTER）/ URL 分类（CONTCATEGBIND） | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-TK-AC-01`, `EV-TK-AC-07` |
| `SO-AC-03` | 重定向目标 | SMARTHTTPREDIR（HTTP 重定向）/ DNSOVERWRITING（DNS 重写）/ IPFarm（Portal/WebProxy 服务器集群）/ RedirectInformation（PCF 下发 URL） | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-TK-AC-06` |
| `SO-AC-04` | 头增强字段 | MSISDN/IMSI/IMEI/APN/位置等插入字段；含字段前缀、加密算法、编码方式；可选 ANTIFRAUD/GRAYLIST 防欺诈属性 | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-FK-AC-03`, `EV-TK-AC-05` |
| `SO-AC-05` | 位置条件 | CGI（2/3G）/ ECGI（4G）/ NCGI（5G）+ PLMN/TAI + PRA + 漫游区；通过 USRLOCATION+USRLOCATIONGRP 批量绑定 | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-FK-AC-11`, `EV-TK-AC-07` |
| `SO-AC-06` | 规则语义 | RULE.POLICYTYPE 决定动作类型（PCC/BWM/HEADEN/WEBPROXY/SMARTREDIRECT/ADC）；规则与策略 1:1，策略与动作 1:1 | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-TK-AC-01` |
| `SO-AC-07` | 动作轨道 | **双轨道+五子轨**：轨道 A（PCC 体系，RULE.POLICYTYPE 隐式驱动）内含五子轨（PCC 计费/阻塞、SMARTREDIRECT HTTP/DNS 重定向、HEADEN 头增强、WEBPROXY L3 IP NAT、ADC 兜底阻塞）；轨道 B（URL 过滤体系，CFTEMPLATE/CONTCATEGBIND.ACTION 显式驱动，独立于 RULE 体系，唯一支持 PERMIT） | `cross_layer` | `active` | `EV-CA-AC-01`, `EV-TK-AC-07` |

---

## 6. Scope（子对象）

> Schema §8.7：scope_name / scope_type / scope_summary。`scope_type` 枚举：`subscriber / subscription / access / location / slice / service_selection / user_profile / other`。

| `scope_name` | `scope_type` | `scope_summary` | 关联方案 |
|--------------|--------------|-----------------|----------|
| 用户级范围 | `subscriber` | 单用户访问限制（阻塞/头增强/Portal captive/URL 分类过滤/配额重定向） | CS-AC-01, CS-AC-02, CS-AC-05, CS-AC-06, CS-AC-08, CS-AC-09 |
| 会话承载范围 | `subscription` | PDU 会话级配额累计触发重定向（FUP 配额耗尽） | CS-AC-08 |
| 接入点范围 | `access` | 按 APN/DNN 粒度或注册阶段 SAR/区域/ODB 粗粒度接入控制 | CS-AC-07 |
| 业务选择范围 | `service_selection` | 按业务类型/URL/SNI/Method/应用标识/URL 分类差异化控制 | CS-AC-01, CS-AC-02, CS-AC-03, CS-AC-04, CS-AC-05, CS-AC-06 |
| 位置区域范围 | `location` | 按 CGI/ECGI/NCGI/PRA/PLMN/服务区域激活差异化访问限制策略 | CS-AC-07, CS-AC-09 |

---

## 7. Participant（子对象）

> Schema §8.7：participant_name / participant_type / plane_or_side / responsibility_summary。`participant_type` 枚举：`endpoint / network_function / external_system / service_endpoint / access_side / other`。

| `participant_name` | `participant_type` | `plane_or_side` | `responsibility_summary` | 关联方案 |
|--------------------|--------------------|-----------------|--------------------------|----------|
| UPF | `network_function` | `user_plane` | L7 解析、规则匹配、DISCARD/HEADEN/REDIRECT/BLOCK/PERMIT 动作执行、URL 提取、ICAP 互通 | CS-AC-01~06, CS-AC-08, CS-AC-09 |
| SMF | `network_function` | `control_plane` | N7→N4 策略翻译、规则下发（RULERANGE 主辅锚点）、URR 管理、位置触发上报、服务区域限制 | CS-AC-01, CS-AC-07, CS-AC-08, CS-AC-09 |
| AMF | `network_function` | `control_plane` | 注册阶段移动接入控制（SAR/区域漫游限制/ODB）、ULI 上报 | CS-AC-07 |
| PCF | `external_system` | `external` | 策略决策垄断（无协商）、动态规则下发、配额管理、ADC 策略、位置策略、重定向 URL（RedirectInformation） | CS-AC-01, CS-AC-08, CS-AC-09 |
| ICAP Server | `external_system` | `external` | URL 过滤外部分类数据库，通过 ICAP REQMOD 协议返回 Category ID 或直接动作 | CS-AC-06 |
| IP Farm 服务器集群 | `service_endpoint` | `service_side` | Portal Server（业务订购/管理）/ Proxy Server（网络加速/病毒防护），IPFarm 负载均衡+健康检查 | CS-AC-05 |
| ADC/SA 引擎 | `network_function` | `user_plane` | L7 应用识别（应用标识/URL/SNI/Method/Content-Type），所有 L7 动作的前置依赖；ADC 兜底阻塞机制 | CS-AC-01~06 |
| RAN/UE | `access_side` | `access_side` | 上报 ULI（用户位置信息）、发起会话与业务访问产生待控制流量 | CS-AC-07, CS-AC-09 |

---

## 8. 与计费/带宽控制场景业务图谱的对比

| 维度 | 计费场景 | 带宽控制场景 | 访问限制场景 |
|------|---------|------------|------------|
| BusinessDomain | 共享 `业务感知`（BD-CH-01） | 共享 `业务感知`（BD-BW-01） | 共享 `业务感知`（BD-AC-01 = BD-CH-01 = BD-BW-01） |
| NetworkScenario | `NS-CH-01 计费场景` | `NS-BW-01 带宽控制场景` | `NS-AC-01 访问限制场景` |
| ConfigurationSolution | 7个（按计费方式/计量/兜底分） | 7个（按控制机制分） | 9个（按动作类型×轨道×触发维度分，最多） |
| 核心机制 | SA识别→Rule→PCC/URR计费链→Ga/Gy/N40上报→配额闭环 | SA识别→BWM限速→CAR/Shaping/FUP/GBR | SA识别→双轨动作（PCC 隐式/URL 过滤显式）→DISCARD/HEADEN/REDIRECT/PERMIT |
| 独有对象族 | 计费三件套(URR/URRGROUP/PCCPOLICYGRP)、SMF融合计费(CCT/CHFINIT/CHARGECTRL) | BWM(BWMSERVICE/BWMCONTROLLER/BWMUSERGROUP/BWMRULE) | 重定向族(SMARTHTTPREDIR/DNSOVERWRITING/IPFarm)、头增强族(HEADEN)、URL过滤(CFTEMPLATE/CONTCATEGBIND/ICAP*)、接入控制(USRLOCATION/SAR/ODB) |
| 独有协议知识 | Ga/Gy/DCC/N40/PFCP/Gx（6个协议接口） | 无独立协议层 SemanticObject | 无独立协议层 SemanticObject（与带宽一致），但有 ICAP 外部协议 |
| DecisionPoint | 8个 | 8个 | 8个（含★双轨核心 DP-AC-03） |
| BusinessRule | 16条 | 6条 | 10条（含★双轨道+五子轨动作轨道 BR-AC-07、PERMIT 唯一性 BR-AC-10） |
| SemanticObject | 12个（含协议栈2个） | 8个（无协议栈） | 7个（无协议栈，含动作轨道 SO-AC-07） |
| 与其他场景叠加 | 通过类型独立原则可与带宽/访问限制并存 | 通过类型独立原则可与计费/访问限制并存 | 通过类型独立原则可与计费/带宽并存（一条报文可同时命中 PCC阻塞+BWM限速+HEADEN插头） |

> **★ 三场景共享说明 ★**：三场景图谱独立构建，不互相依赖；共享部分限于：
> 1. `业务感知` 根对象（BD-AC-01 = BD-CH-01 = BD-BW-01）
> 2. SA 七步流程通用引擎（规则下发→到达→解析→匹配→执行→转发→上报）
> 3. 通用 ConfigObject（RULE, USERPROFILE, PCCPOLICYGRP, FLOWFILTER, FILTER）
> 4. 规则匹配类型独立原则（PCC/BWM/HEADEN 互不干扰，可叠加）
> 5. ADC（GWFD-020357）作为 L7 解析前置，横切依赖

---

## 9. 业务图谱关系边

### 9.1 层级包含（contains / instantiated_as）

| 起点 | 关系 | 终点 |
|------|------|------|
| `BD-AC-01` | `contains` | `NS-AC-01` |
| `NS-AC-01` | `instantiated_as` | `CS-AC-01` ~ `CS-AC-09` |

### 9.2 方案使用特性（uses_feature，共26条特性引用边）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-AC-01` | `uses_feature` | `GWFD-020351`, `WSFD-109101`, `GWFD-020357` |
| `CS-AC-02` | `uses_feature` | `GWFD-110261`, `GWFD-110262`, `GWFD-110263`, `GWFD-110401`, `GWFD-020357` |
| `CS-AC-03` | `uses_feature` | `GWFD-110284`, `GWFD-020357`, `GWFD-110261` |
| `CS-AC-04` | `uses_feature` | `GWFD-110283`, `GWFD-020357` |
| `CS-AC-05` | `uses_feature` | `GWFD-110281`, `GWFD-110282`, `GWFD-020357` |
| `CS-AC-06` | `uses_feature` | `GWFD-110471`, `GWFD-020357` |
| `CS-AC-07` | `uses_feature` | `WSFD-211001`, `WSFD-106003`, `WSFD-105003`, `WSFD-106005`, `WSFD-105006` |
| `CS-AC-08` | `uses_feature` | `GWFD-020351`, `WSFD-109101`, `GWFD-110284` |
| `CS-AC-09` | `uses_feature` | `WSFD-211001`, `GWFD-110284`, `GWFD-110281` |

> **ADC（GWFD-020357）横切依赖**：CS-AC-01~06 共 6 个方案均依赖 ADC 作为 L7 解析前置（CS-AC-07 接入控制在 UNC 侧不依赖 ADC，CS-AC-08/09 重定向由 PCF 决策+UPF 执行，ADC 为可选）。

### 9.3 决策点归属（has_decision）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-AC-01` | `has_decision` | `DP-AC-01`, `DP-AC-03`, `DP-AC-04`, `DP-AC-08` |
| `CS-AC-01` | `has_decision` | `DP-AC-02`, `DP-AC-05` |
| `CS-AC-02` | `has_decision` | `DP-AC-05`, `DP-AC-07` |
| `CS-AC-03`, `CS-AC-04`, `CS-AC-05`, `CS-AC-08`, `CS-AC-09` | `has_decision` | `DP-AC-06`, `DP-AC-07` |
| `CS-AC-06` | `has_decision` | `DP-AC-03`, `DP-AC-05` |
| `CS-AC-07` | `has_decision` | `DP-AC-04` |

### 9.4 业务规则约束（constrained_by）

| 起点 | 关系 | 终点 |
|------|------|------|
| `CS-AC-01` ~ `CS-AC-09` | `constrained_by` | `BR-AC-04`（License 前置门控，全部方案） |
| `CS-AC-01` ~ `CS-AC-09` | `constrained_by` | `BR-AC-05`（REFRESHSRV 最后执行，全部 UDG 侧方案） |
| `CS-AC-01`, `CS-AC-02`, `CS-AC-06`, `CS-AC-07`, `CS-AC-08`, `CS-AC-09` | `constrained_by` | `BR-AC-01`（预定义规则三网元一致性） |
| `CS-AC-01`, `CS-AC-06` | `constrained_by` | `BR-AC-03`（一条规则绑定一条策略） |
| `CS-AC-01`, `CS-AC-03`, `CS-AC-05`, `CS-AC-08`, `CS-AC-09` | `constrained_by` | `BR-AC-07`（RULE.POLICYTYPE 决定动作轨道，双轨道+五子轨） |
| `CS-AC-02` | `constrained_by` | `BR-AC-06`（头防欺诈依赖头增强）, `BR-AC-08`（字段加密与编码） |
| `CS-AC-03`, `CS-AC-04`, `CS-AC-05`, `CS-AC-08`, `CS-AC-09` | `constrained_by` | `BR-AC-09`（加密协议仅 WebProxy 可处理） |
| `CS-AC-06` | `constrained_by` | `BR-AC-10`（PERMIT 唯一性，URL 过滤独有） |
| `NS-AC-01` | `constrained_by` | `BR-AC-02`（规则匹配类型独立原则，场景级通用） |

### 9.5 语义对象使用（uses_semantic_object）

| 起点 | 关系 | 终点 |
|------|------|------|
| `NS-AC-01` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-06`, `SO-AC-07`（场景级通用动作类型/规则语义/动作轨道） |
| `CS-AC-01` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-02`, `SO-AC-06` |
| `CS-AC-02` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-04`, `SO-AC-06` |
| `CS-AC-03` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-03`, `SO-AC-07` |
| `CS-AC-04` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-03`, `SO-AC-07` |
| `CS-AC-05` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-03`, `SO-AC-07` |
| `CS-AC-06` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-02`, `SO-AC-07` |
| `CS-AC-07` | `uses_semantic_object` | `SO-AC-05`, `SO-AC-06` |
| `CS-AC-08` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-03`, `SO-AC-07` |
| `CS-AC-09` | `uses_semantic_object` | `SO-AC-01`, `SO-AC-03`, `SO-AC-05`, `SO-AC-07` |

### 9.6 决策点影响（selects / sets_value_pattern）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| `DP-AC-01` | `selects` | `CS-AC-01`/`CS-AC-02`/`CS-AC-03`~`05`/`CS-AC-06`/`CS-AC-08`/`CS-AC-09` | 动作类型选择决定方案闭包（DISCARD→01, HEADEN→02, REDIRECT→03~05/08/09, PERMIT→06） |
| `DP-AC-03` | `selects` | `CS-AC-01`~`05`/`CS-AC-08`/`CS-AC-09`（轨道 A）vs `CS-AC-06`（轨道 B） | 动作轨道选择决定走 PCC 体系还是 URL 过滤体系 |
| `DP-AC-02` | `sets_value_pattern` | `RULE.RULETYPE` | 动态/预定义/本地三选一；URL 过滤必选预定义 |
| `DP-AC-05` | `sets_value_pattern` | `FILTER/L7FILTER/EXTENDEDFILTER` 选择 | L3/L4→FILTER；L7→L7FILTER；DNS/多维度→EXTENDEDFILTER |
| `DP-AC-06` | `sets_value_pattern` | 重定向目标对象（SMARTHTTPREDIR/DNSOVERWRITING/IPFarm/RedirectInformation） | 决定重定向特性选择 |
| `DP-AC-07` | `sets_value_pattern` | 协议支持范围（HTTP1.x/HTTPS/RTSP/任意TCP/DNS） | 决定特性选择；加密协议仅 WebProxy |

---

## 10. 端到端方案链路（跨层映射依据）

### 10.1 CS-AC-01 PCC 阻塞端到端
```
PCF 决策（动态）/ UPF 预定义（静态） → N7 下发 → SMF 翻译
→ FILTER+FLOWFILTER（L3/L4 [+L7FILTER L7] 匹配）
→ RULE（POLICYTYPE=PCC, PRIORITY 裁决） → PCCPOLICYGRP
→ USERPROFILE（via RULEBINDING）
→ UDG 执行 DISCARD（丢弃报文）
→ SET REFRESHSRV（60秒生效）
```

### 10.2 CS-AC-02 头增强端到端
```
ADC/SA 解析（GWFD-020357）→ 识别 HTTP/HTTPS/RTSP 报文、提取 Method/URL/SNI
→ FILTER/L7FILTER → FLOWFILTER 匹配
→ 【可选】头防欺诈检测（GWFD-110401）：检查已有字段是否伪造
    ├─ 不存在字段：继续头增强
    ├─ 字段正确：跳过头增强
    ├─ 字段错误：纠正后继续（或灰名单模式停止）
    └─ 多个字段：清理冗余后继续
→ HEADEN 对象（POLICYTYPE=HEADEN）：插入 MSISDN/IMSI/IMEI/APN/位置
    ├─ HTTP：扩展字段（MD5/RC4/AES/RSA/SHA-256）
    ├─ HTTPS：SSL Extension TLV 格式（无 RSA，基于 SNI 触发）
    └─ RTSP：扩展字段（不支持防欺诈）
→ 业务服务器获取增强字段 → 后续访问控制（Portal 认证/重定向携带 MSISDN/URL 过滤）
```

### 10.3 CS-AC-03 HTTP 重定向端到端
```
ADC/SA 解析（GWFD-020357）→ L7 HTTP 报文识别
→ EXTENDEDFILTER（URL/UserAgent/ContentType 多维度）+ ERRORCODE 匹配
→ SMARTHTTPREDIR 对象（含 REDIRAPPENDINFO 可选携带 MSISDN/IMSI/IMEI）
→ RULE（POLICYTYPE=SMARTREDIRECT） → USERPROFILE
→ UDG 改写 HTTP 响应为 301/302/303 重定向
→ 用户浏览器跳转到新页面
（注：仅 HTTP1.x，不支持 HTTPS/HTTP2.0）
```

### 10.4 CS-AC-04 DNS 重定向端到端
```
ADC/SA 解析 → DNS 查询识别（UDP DNS，不支持 TCP DNS）
→ EXTENDEDFILTER（URL 域名）+ ERRORCODE（如 NXDOMAIN=3）匹配
→ DNSOVERWRITING 对象（构造新 DNS 响应）
→ RULE（POLICYTYPE=SMARTREDIRECT） → USERPROFILE
→ UDG 改写 DNS 响应 IP 指向第三方 Platform
→ 用户解析到新 IP，建立 TCP 前介入（最早时机）
```

### 10.5 CS-AC-05 Portal/WebProxy 重定向端到端
```
Portal 链路：
  用户首次 HTTP 请求 → ADC/SA 解析（GWFD-020357）
  → IPFARM+IPFARMSERVER+LOGICINF（Portal Server 集群，负载均衡+健康检查）
  → PCCPOLICYGRP（含 captive） → USERPROFILE（CAPMODETHRES 定时器）
  → UDG 改写 HTTP 响应为 301/302/303 → 跳转 Portal
  → 周期性 captive/non-captive 交替（业务订购/广告推送）
  → Portal 全 DOWN 时 DEFAULTACT=BLOCK

WebProxy 链路（唯一处理加密协议）：
  TCP SYN 匹配规则（L3，不依赖 L7 解析）
  → IPFARM+IPFARMSERVER+LOGICINF+BLACKLISTRULE（Proxy Server 集群）
  → RULE（POLICYTYPE=WEBPROXY） → USERPROFILE
  → UDG 执行 L3 IP NAT（透明代理，用户无感知）
  → 支持 HTTPS/HTTP2.0/任意 TCP（网络加速/病毒防护/内容过滤）
```

### 10.6 CS-AC-06 URL 过滤端到端（轨道 B）
```
ADC/SA 解析（GWFD-020357）→ 提取 URL（HTTP 完整 URL / HTTPS 仅 SNI）
→ VPNINST+LOGICINF+ICAPSERVER+ICAPSVRGRP（互通配置）
→ ICAP REQMOD 上送 URL 到 ICAP Server
→ ICAP Server 返回 Category ID 或直接动作
→ UDG 匹配本地套餐策略：
    ├─ CFTEMPLATE.ACTION（模板级缺省动作）
    └─ CONTCATEGBIND.ACTION（分类级精确动作）
→ 执行 BLOCK（阻塞）/ PERMIT（显式放行，URL 过滤独有）/ REDIRECT（重定向）
→ CFCACHEPARA 本地缓存加速
（注：独立于 RULE 体系，必需 ICAP Server，唯一显式支持 PERMIT）
```

### 10.7 CS-AC-07 接入控制端到端（UNC 侧）
```
用户激活/注册 → SGSN/MME/AMF 上报 ULI（User Location Information）
移动接入控制（注册阶段，AMF）：
  ├─ SAR（服务区域限制，TAI 允许/禁止列表）
  ├─ 区域漫游限制（RAT/核心网/区域）
  └─ ODB（所有权闭锁，欠费禁用）
会话接入控制（会话阶段，SMF）：
  └─ 服务区域限制（WSFD-105006）
位置触发（SMF/PCF）：
  → UNC（SMF/PGW-C）将 ULI 透传 PCRF/PCF（动态 PCC）或本地决策（本地 PCC）
  → USRLOCATION（CGI/ECGI/NCGI）+USRLOCATIONGRP+UPBINDUPG+APNUSRPROFG
  → 匹配位置组 → 触发访问限制/带宽控制策略
→ 决策"是否允许接入"（粗粒度，注册/会话阶段）
→ 通过的流量进入 UDG 侧细粒度访问限制（CS-AC-01~06）
```

### 10.8 CS-AC-08 配额耗尽重定向端到端
```
URR 累计用户流量（与计费场景共享 URR 机制）
→ 配额耗尽触发 US_RE/NO_CREDIT 事件（PCR Trigger）
→ SMF 上报 PCF
→ PCF 决策垄断（无协商）：生成携带 RedirectInformation 的 PCC 规则
→ PCF 通过 N7 下发（Npcf_SMPolicyControl_UpdateNotify）
→ SMF 映射为 N4 PDR/FAR 下发 UPF
→ UPF 执行重定向到充值页 URL
→ 用户浏览器跳转运营商充值首页
（注：走轨道 A PCC 体系 + PCF 决策，规则类型为动态规则）
```

### 10.9 CS-AC-09 区域引导重定向端到端
```
WSFD-211001 感知用户位置变化（ULI 上报）
→ UPCF 触发器：PRA_CH（PRA 变化）/ PLMN_CH（漫游）/ SAREA_CH（服务区域）
→ USRLOCATION 匹配预定义位置组
→ PCF 决策：生成重定向策略（RedirectInformation.URL = 套餐订购页/验证页）
→ PCF 通过 N7 下发 → SMF 翻译 N4 → UPF 执行
→ 用户进入特定区域/漫游时跳转套餐订购页（出国引导签约）
→ 或跳转免费接入验证页（热点区域引导）
```

---

## 11. 对象计数汇总

| 对象类型 | 数量 | 编号范围 |
|---------|------|---------|
| BusinessDomain | 1 | BD-AC-01（=BD-CH-01=BD-BW-01，三场景共享） |
| NetworkScenario | 1 | NS-AC-01 |
| ConfigurationSolution | 9 | CS-AC-01~09 |
| DecisionPoint | 8 | DP-AC-01~08 |
| BusinessRule | 10 | BR-AC-01~10 |
| SemanticObject | 7 | SO-AC-01~07 |
| Scope（子对象） | 5 | subscriber/subscription/access/service_selection/location |
| Participant（子对象） | 8 | UPF/SMF/AMF/PCF/ICAP Server/IP Farm/ADC-SA/RAN-UE |
| **业务层对象总计** | **49** | - |

### 关系边计数

| 关系类型 | 边数 | 说明 |
|---------|------|------|
| `contains` | 1 | BD-AC-01 → NS-AC-01 |
| `instantiated_as` | 9 | NS-AC-01 → CS-AC-01~09 |
| `uses_feature` | 26 | 9个方案引用特性（含 ADC 横切依赖 6 条） |
| `has_decision` | 14 | NS + 6个CS 归属 8个DP |
| `constrained_by` | 27 | NS + 9个CS 受 10个BR 约束 |
| `uses_semantic_object` | 31 | NS + 9个CS 使用 7个SO |
| `selects` / `sets_value_pattern` | 6 | 6个DP 影响下层对象/参数 |
| **关系边总计** | **114** | - |

---

> 本文件为访问限制场景三层图谱第 1 层。第 2 层特性图谱、第 3 层任务原子层、第 4 层命令图谱、第 5 层跨层映射、第 6 层证据索引见同目录其他文件。
