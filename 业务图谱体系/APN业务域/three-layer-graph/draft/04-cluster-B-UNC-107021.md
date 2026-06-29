# APN 业务域命令图谱 · 簇B UNC 侧：WSFD-107021 静态地址用户路由冗余（UNC/SMF）

> **文件定位**：`three-layer-graph/draft/04-cluster-B-UNC-107021.md`
> **特性范围**：仅 WSFD-107021 静态地址用户路由冗余（UNC 侧，1 个激活子场景：主备 UPF 路由冗余）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow 样板 `04-cluster-B-GWFD-010105.md`（编号 `CMD-UNC-107021-xx`，9 节结构）；UNC 命令体系参考 `04-cluster-B-UNC-010502-010504.md`（ADD ADDRPOOL 系，区分 UDG 的 ADD POOL）
> **数据来源**：4 篇特性文档（激活/参考信息/特性概述/调测）+ MML 命令手册原文（路径见 §抽取核对清单）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。

---

## 0. 命令清单总览（WSFD-107021 用到的全部命令）

### 0.1 按命令类型分布

| 类型 | 命令数 | 命令清单 |
|------|-------|---------|
| 配置类（ADD） | 8 | ADD ADDRPOOL、ADD SECTION、ADD ADDRPOOLGRP、ADD POOLBINDGRP、ADD UPNODE、ADD ADDRUPGROUP、ADD UPFBINDGRP、ADD POOLGRPMAP、ADD POOLBINDAPN（白名单检查可选） |
| 维护类（RMV/MOD/LST） | 6 | RMV ADDRPOOL、LST ADDRPOOL、RMV SECTION、LST SECTION、RMV ADDRPOOLGRP、LST ADDRPOOLGRP、MOD UPNODE、RMV POOLGRPMAP、LST POOLGRPMAP（参考信息列出，维护/查询类，本期略，不抽参数） |
| 查询类（DSP） | 1 | DSP PDUSESSION（调测查询类，本期略，不抽参数） |
| 前置依赖类（非本特性核心，但在激活脚本中出现） | 2 | ADD APN（簇A）、ADD PNFPROFILE（簇F，ADD UPNODE 关联） |

> **说明**：本特性是「辅助特性」，其全部配置类命令均与 WSFD-010502（地址分配方式）的「配置静态IP地址网段与UPF的绑定」激活子场景**命令集完全重合**（ADD ADDRPOOL/SECTION/ADDRPOOLGRP/POOLBINDGRP/UPNODE/ADDRUPGROUP/UPFBINDGRP/POOLGRPMAP/POOLBINDAPN）。本特性独有的语义不在命令本身，而在 **ADD UPFBINDGRP.PRIORITY 的主备取值**（主用 PRIORITY=0 高优先级，备用 PRIORITY=1 低优先级）以及 UPF 故障时的选择倒换逻辑。本文件不重复抽参数（参数已在 `04-cluster-B-UNC-010502-010504.md` 完整抽取），仅在 §1 命令表登记 + §4/§6/§7 标注主备冗余特有的规则与边。
>
> **维护类命令**（RMV/MOD/LST）为本特性参考信息明确列出，用于冗余关系的增删改查；本期不抽参数（与样板「查询类本期略」一致），仅在 §0.1 登记。

### 0.2 ConfigObject 分布（本特性涉及，全部与 010502 共用）

| 功能域 | 对象数 | 关键对象 | 是否本特性独有 |
|-------|-------|---------|--------------|
| UNC 地址池体系 | 5 | ADDRPOOL、SECTION、ADDRPOOLGRP、POOLBINDGRP、POOLGRPMAP | 否（与 010502 共用） |
| UNC 地址-UPF 绑定体系 | 3 | ADDRUPGROUP、UPFBINDGRP、UPNODE | 否（与 010502 共用）；★UPFBINDGRP.PRIORITY 在本特性承载主备语义 |
| UNC 地址池-APN 绑定 | 1 | POOLBINDAPN | 否（白名单检查可选） |
| 前置依赖（引用，非本特性拥有） | 2 | APN、PNFPROFILE | 否 |

> **★关键判断**：本特性**无独有 ConfigObject**，也无独有 MML 命令。其「冗余」能力通过 **UPFBINDGRP.PRIORITY 主备取值 + POOLGRPMAP 一池组对一 UPF 组的多 UPF 绑定** 实现，属于配置语义层而非命令层。本文件据此在 §2 复用 010502 的 ConfigObject 实例，仅在备注中标注主备语义。

### 0.3 全局字段声明（status）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。WSFD-107021 所有正式命令均处于启用状态。
> **依据**：所有命令均在产品文档正式登记（参考信息明确列出 ADD/RMV/LST/MOD 全套），无 `deprecated` 或 `planned` 状态。

### 0.4 ★ UDG vs UNC 冗余命令区分核对（铁律：不混）

| 核对项 | UDG 侧（GWFD-010107 静态地址用户路由冗余，UDG/UPF 侧） | UNC 侧（本文件 WSFD-107021） | 区分结论 |
|--------|------------------------------------------------------|------------------------------|---------|
| 冗余承载命令 | **ADD POOL.REDUNDFUNC + MASTERFLAG**（地址池级冗余开关 + 主用标识，GRE 冗余容灾） | **ADD UPFBINDGRP.PRIORITY**（UPF 级主备优先级，0=主用，1=备用） | ✅已区分：UDG 在地址池参数（REDUNDFUNC/MASTERFLAG）；UNC 在 UPF 绑定参数（PRIORITY），冗余粒度不同（UDG=地址池/UPF 对，UNC=UPF 组内主备） |
| 地址池命令 | ADD POOL（POOLTYPE=LOCAL/EXTERNAL/MULTICAST） | ADD ADDRPOOL（POOLTYPE=Local/UDM/Radius/DHCP） | ✅已区分（与 010502 样板一致，ADD POOL vs ADD ADDRPOOL） |
| UPF 节点命令 | UDG 无 ADD UPNODE（用 CPNODEID 表 SMF） | ADD UPNODE（ADDRALLOCMODE=INHERIT） | ✅已区分（UNC 独有 UPF 节点体系） |
| 主备倒换触发 | UDG：MASTERFlag + GRE 冗余 | UNC：UPF 故障（LOCK/故障）触发选择倒换至低优先级 UPF | ✅已区分（倒换机制不同） |

> **铁律核对**：本文件**不引用** UDG 的 ADD POOL.REDUNDFUNC/MASTERFLAG 参数，所有冗余语义均落在 UNC 的 ADD UPFBINDGRP.PRIORITY。

---

## 1. MMLCommand 实例化（WSFD-107021，8 个配置类命令 + 6 个维护/查询类）

> **★参数抽取策略**：本特性 8 个配置类命令的**全量参数表已在 `04-cluster-B-UNC-010502-010504.md` §5.1~5.9 完整抽取**（ADD ADDRPOOL 13 参数 / ADD SECTION 8 / ADD ADDRPOOLGRP 4 / ADD POOLBINDGRP 3 / ADD UPNODE 29 / ADD ADDRUPGROUP 2 / ADD UPFBINDGRP 3 / ADD POOLBINDAPN 3 / ADD POOLGRPMAP 6）。本文件 §1 仅登记命令实例（`command_id` 用 107021 编号空间），**不重复抽参数**，关键参数列指向 010502 样板对应小节，并在「主备语义」列标注本特性独有约束。

### 1.1 UNC 地址池体系（5个，与 010502 共用）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数（详见 010502 样板） | 主备冗余语义 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------------|------------|----------------------|
| `CMD-UNC-107021-01` | `ADD ADDRPOOL` | ADD | ADDRPOOL | UNC 地址池（POOLTYPE=UDM 静态分配；本特性激活脚本固定 UDM；HASVPN=Enable + VPNINSTANCE 与 UPF 侧一致） | POOLNAME, IPVERSION, POOLTYPE(UDM), CHECKIPVALID(Enable), HASVPN, VPNINSTANCE（详见 010502 §5.1，13 参数） | 地址池网段为静态 IP 网段，承载主备 UPF 共享的地址空间 | EV-UNC-107021 |
| `CMD-UNC-107021-02` | `ADD SECTION` | ADD | SECTION | UNC 地址段（V4STARTIP/V4ENDIP；主备 UPF 共享同一网段，如 10.0.0.0~10.1.2.3） | POOLNAME, SECTIONNUM, IPVERSION, V4STARTIP, V4ENDIP（详见 010502 §5.2，8 参数） | 网段须同时包含在主备 UPF 的地址池规划内 | EV-UNC-107021 |
| `CMD-UNC-107021-03` | `ADD ADDRPOOLGRP` | ADD | ADDRPOOLGRP | UNC 地址池组（POOLGRPTYPE=UDM） | POOLGRPNAME, POOLGRPTYPE(UDM)（详见 010502 §5.3，4 参数） | — | EV-UNC-107021 |
| `CMD-UNC-107021-04` | `ADD POOLBINDGRP` | ADD | POOLBINDGRP | UNC 地址池绑定到池组 | POOLGRPNAME, POOLNAME（详见 010502 §5.4，3 参数） | — | EV-UNC-107021 |
| `CMD-UNC-107021-05` | `ADD POOLGRPMAP` | ADD | POOLGRPMAP | UNC 池组映射（POOLGRPNAME↔UPFGRPNAME；★一个地址池组映射到一个 UPF 组，该 UPF 组内含主备两个 UPF） | MAPPINGNAME, POOLGRPNAME, UPFGRPNAME（详见 010502 §5.5，6 参数） | ★POOLGRPMAP 是主备冗余的「挂载点」：地址池组经映射绑定到含主备 UPF 的 UPF 组 | EV-UNC-107021 |

### 1.2 UNC 地址-UPF 绑定体系（3个，★主备语义核心）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数（详见 010502 样板） | 主备冗余语义 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------------|------------|----------------------|
| `CMD-UNC-107021-06` | `ADD UPNODE` | ADD | UPNODE | UNC UPF 节点（★主备两个 UPF 实例，分别 ADD UPNODE 创建；ADDRALLOCMODE=INHERIT 继承全局） | NFINSTANCENAME(UPF_Instance_1/2), ADDRALLOCMODE(INHERIT)（详见 010502 §5.6，29 参数） | ★主用 UPF（UPF_Instance_1）与备用 UPF（UPF_Instance_2）各自独立创建节点 | EV-UNC-107021 |
| `CMD-UNC-107021-07` | `ADD ADDRUPGROUP` | ADD | ADDRUPGROUP | UNC UPF 组（UPFGRPTYPE=UDM；★一组含主备两 UPF） | UPFGRPNAME, UPFGRPTYPE(UDM)（详见 010502 §5.7，2 参数） | ★主备 UPF 绑定到同一 UPF 组，组内按 PRIORITY 区分主备 | EV-UNC-107021 |
| `CMD-UNC-107021-08` | `ADD UPFBINDGRP` | ADD | UPFBINDGRP | UNC UPF 绑定到 UPF 组（★PRIORITY 0~255；★主用 PRIORITY=0 高优先级，备用 PRIORITY=1 低优先级） | UPFGRPNAME, UPFID, PRIORITY(0~255)（详见 010502 §5.8，3 参数） | ★★★本特性核心命令：主备语义由此命令的 PRIORITY 取值承载（手册：仅 UPFGRPTYPE=UDM/Radius 时 PRIORITY 生效，越小优先级越高） | EV-UNC-107021 |

### 1.3 UNC 地址池-APN 绑定（白名单检查可选，1个）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数（详见 010502 样板） | 主备冗余语义 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------------------------|------------|----------------------|
| `CMD-UNC-107021-09` | `ADD POOLBINDAPN` | ADD | POOLBINDAPN | UNC 地址池绑 APN（白名单检查场景；ADDRPOOL.CHECKIPVALID=Enable 配套；静态用户激活时按地址查池再查 UPF） | POOLNAME, APN, PRIORITY（详见 010502 §5.9，3 参数） | 白名单检查开启时，主备倒换后仍按地址反查 UPF 组，自然落到备用 UPF | EV-UNC-107021 |

### 1.4 维护/查询类（参考信息列出，本期略，不抽参数）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 说明 |
|--------------|----------------|--------|------------------|-------------------|------|
| `CMD-UNC-107021-M1` | `RMV ADDRPOOL` | RMV | ADDRPOOL | 删除地址池 | 维护类，本期略（参考信息列出） |
| `CMD-UNC-107021-M2` | `LST ADDRPOOL` | LST | ADDRPOOL | 查询地址池 | 维护类，本期略 |
| `CMD-UNC-107021-M3` | `RMV SECTION` | RMV | SECTION | 删除地址段 | 维护类，本期略 |
| `CMD-UNC-107021-M4` | `LST SECTION` | LST | SECTION | 查询地址段 | 维护类，本期略 |
| `CMD-UNC-107021-M5` | `RMV ADDRPOOLGRP` | RMV | ADDRPOOLGRP | 删除地址池组 | 维护类，本期略 |
| `CMD-UNC-107021-M6` | `LST ADDRPOOLGRP` | LST | ADDRPOOLGRP | 查询地址池组 | 维护类，本期略 |
| `CMD-UNC-107021-M7` | `MOD UPNODE` | MOD | UPNODE | 修改 UPF 节点（如改 LOCK/ADDRALLOCMODE） | 维护类，本期略；★可用于手动锁定主用 UPF 触发倒换测试 |
| `CMD-UNC-107021-M8` | `RMV POOLGRPMAP` | RMV | POOLGRPMAP | 删除池组映射 | 维护类，本期略 |
| `CMD-UNC-107021-M9` | `LST POOLGRPMAP` | LST | POOLGRPMAP | 查询池组映射 | 维护类，本期略 |
| `CMD-UNC-107021-Q1` | `DSP PDUSESSION` | DSP | PDUSESSION | PDU 会话查询（调测主备倒换：查用户 IP 与 PFCP IPv4 是否落在主/备 UPF） | 调测查询类，本期略（调测文档引用） |

---

## 2. ConfigObject 实例化（复用 010502，9 个，无独有对象）

> **★复用声明**：本特性无独有 ConfigObject。下列 9 个对象实例定义与 `04-cluster-B-UNC-010502-010504.md` §2 完全一致，本文件仅引用其 `object_id`，不重复定义属性。仅在「本特性主备语义」列标注差异。

| `object_id`（复用 010502） | `object_name` | `product_side` | `object_kind` | 本特性主备语义 |
|----------------------------|---------------|----------------|---------------|--------------|
| `OBJ-ADDRPOOL` | ADDRPOOL | UNC | entity | POOLTYPE=UDM；地址池网段为主备 UPF 共享的静态 IP 网段 |
| `OBJ-SECTION-UNC` | SECTION | 共用 | entity | 地址段同时落在主备 UPF 的地址池规划内（特性概述：网段须包含在 UDG 地址池内，且主备 UPF 均配置该网段） |
| `OBJ-ADDRPOOLGRP` | ADDRPOOLGRP | UNC | composite | POOLGRPTYPE=UDM |
| `OBJ-POOLBINDGRP` | POOLBINDGRP | UNC | binding | — |
| `OBJ-POOLGRPMAP-UNC` | POOLGRPMAP | UNC | binding | ★POOLGRPNAME↔UPFGRPNAME 映射，UPF 组内含主备两 UPF |
| `OBJ-ADDRUPGROUP` | ADDRUPGROUP | UNC | composite | UPFGRPTYPE=UDM；★一组含主备两 UPF |
| `OBJ-UPFBINDGRP` | UPFBINDGRP | UNC | binding | ★★★PRIORITY 主备取值：主用=0，备用=1（本特性核心语义承载对象） |
| `OBJ-UPNODE` | UPNODE | UNC | entity | ★主备两个 UPNODE 实例（UPF_Instance_1 主、UPF_Instance_2 备），ADDRALLOCMODE=INHERIT |
| `OBJ-POOLBINDAPN` | POOLBINDAPN | UNC | binding | 白名单检查可选 |

---

## 3. ConfigObject 间关系边（§11.7，复用 010502，仅标注主备路径）

> 本特性无新增关系边，下列边与 `04-cluster-B-UNC-010502-010504.md` §3 一致，本文件仅用「主备冗余路径」视角重述。

### 3.1 主备冗余数据路径（依赖 010502 已建关系边）

| 路径节点 | 关系 | 下一节点 | 说明 |
|----------|------|----------|------|
| ADDRPOOL（静态网段） | `belongs_to`（via POOLBINDGRP） | ADDRPOOLGRP | 静态地址池挂入池组 |
| ADDRPOOLGRP | `mapped_to`（via POOLGRPMAP） | ADDRUPGROUP | ★池组映射到含主备 UPF 的 UPF 组 |
| ADDRUPGROUP | `contains`（via UPFBINDGRP） | UPNODE（主 + 备） | ★UPF 组内含两个 UPNODE，按 PRIORITY 区分主备 |

### 3.2 depends_on 边（复用 010502，3条关键）

| 起点 | 关系 | 终点 | 主备冗余说明 |
|------|------|------|--------------|
| ADDRUPGROUP | `depends_on` | UPNODE | ★主备两 UPNODE 必须先各自 ADD UPNODE 创建，才能 ADD UPFBINDGRP 绑定到同一 UPF 组 |
| POOLGRPMAP | `depends_on` | ADDRPOOLGRP + ADDRUPGROUP | 池组映射依赖池组+UPF组存在；UDM 类型 UPFGRPNAME 不能为空 |
| SECTION | `depends_on` | ADDRPOOL | 地址段依赖地址池存在 |

---

## 4. CommandRule 实例化（本特性相关，3条，★聚焦主备冗余）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。
> 本特性独有规则聚焦「主备优先级」「故障倒换」「网段一致性」三个语义点；其余通用规则（POOLTYPE 四类型对应、白名单配套、ADDRALLOCMODE 切换、位域一致）已在 010502 样板 CR-010502-01~05 建立，本文件不重复。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-107021-01` | ADD UPFBINDGRP.PRIORITY 主备优先级取值（UDM/Radius 类型生效） | `semantic_rule` | explicit | config | parameter | CMD-UNC-107021-08.PRIORITY (ADD UPFBINDGRP) | ADD UPFBINDGRP 的 PRIORITY 取值 0~255，越小优先级越高；★本特性约定：主用 UPF PRIORITY=0，备用 UPF PRIORITY=1（任意主<备即可）；手册原文：仅 UPFGRPTYPE=UDM/Radius 时 PRIORITY 生效（Local/DHCP 类型一 UPF 绑一组，无主备语义）；同一 UPF 组内主备 PRIORITY 不可相同 | 主备优先级配置错误导致倒换次序错误或无法倒换 | critical | EV-UNC-107021 + 手册（ADD UPFBINDGRP） |
| `CR-107021-02` | 主备 UPF 故障倒换（LOCK/故障触发） | `runtime_check_rule` | explicit | restriction | relation | OBJ-UPNODE.LOCK + OBJ-UPFBINDGRP.PRIORITY | 特性概述原理：主用 UPF（高优先级 PRIORITY=0）正常时，静态地址用户/Radius 分配用户基于网段绑定关系选择主用 UPF；主用 UPF 故障（或 MOD UPNODE 设 LOCK=TRUE）时，为用户选择备用 UPF（低优先级 PRIORITY=1）；主用恢复后因优先级较高，备用 UPF 上的用户数据转发回主用 UPF；★UPF 故障期间用户经备用 UPF 的 Gi/N6 接口访问外部网络 | 主用 UPF 故障但未配备用 UPF 导致网段内用户业务异常 | critical | EV-UNC-107021（特性概述原理概述 §1.3.9） |
| `CR-107021-03` | 静态网段须同时包含在主备 UPF 与 UDG 地址池规划内 | `semantic_rule` | explicit | config | relation | OBJ-SECTION-UNC ↔ OBJ-UPNODE（主+备） | 激活文档必备事项原文：「UNC 上配置的用户静态地址网段信息必须包含在 UDG 上配置的地址池内」（参考 GWFD-010104）；特性概述任务示例：UPF_Instance_1 和 UPF_Instance_2 上均需配置包含网段 10.0.0.0~10.1.2.3 的地址池信息；★主备两 UPF 的地址池网段必须一致，否则倒换后备用 UPF 无法为该网段用户分配地址 | 网段不一致导致主用故障倒换后备用 UPF 无法承载用户 | critical | EV-UNC-107021（激活文档必备事项 + 任务示例） |

---

## 5. MMLCommand 关键参数集（核心命令全参数）

> **★参数抽取策略**：本特性 9 个配置类命令的**全量参数表已在 `04-cluster-B-UNC-010502-010504.md` §5 完整抽取**（共 71 参数行：ADD ADDRPOOL 13 / ADD SECTION 8 / ADD ADDRPOOLGRP 4 / ADD POOLBINDGRP 3 / ADD UPNODE 29 / ADD ADDRUPGROUP 2 / ADD UPFBINDGRP 3 / ADD POOLBINDAPN 3 / ADD POOLGRPMAP 6）。
>
> **本文件不重复抽参数**，仅在本节列出「参数表跳转索引」+ 标注本特性主备冗余相关的关键参数。如需查看某命令的全量参数表，跳转至 010502 样板对应小节。

### 5.1 参数表跳转索引（9 命令 → 010502 样板小节）

| `command_id`（本文件） | `command_name` | 全参数表位置（010502 样板） | 参数行数 | 本特性主备冗余关键参数 |
|------------------------|----------------|----------------------------|---------|----------------------|
| `CMD-UNC-107021-01` | ADD ADDRPOOL | `04-cluster-B-UNC-010502-010504.md` §5.1 | 13 | POOLTYPE=UDM（静态分配）、CHECKIPVALID=Enable（白名单）、HASVPN+VPNINSTANCE（与 UPF 侧一致） |
| `CMD-UNC-107021-02` | ADD SECTION | 同上 §5.2 | 8 | V4STARTIP/V4ENDIP（主备 UPF 共享网段） |
| `CMD-UNC-107021-03` | ADD ADDRPOOLGRP | 同上 §5.3 | 4 | POOLGRPTYPE=UDM |
| `CMD-UNC-107021-04` | ADD POOLBINDGRP | 同上 §5.4 | 3 | — |
| `CMD-UNC-107021-05` | ADD POOLGRPMAP | 同上 §5.5 | 6 | UPFGRPNAME（指向含主备 UPF 的 UPF 组） |
| `CMD-UNC-107021-06` | ADD UPNODE | 同上 §5.6 | 29 | NFINSTANCENAME（主备两实例）、ADDRALLOCMODE=INHERIT、LOCK（故障/锁定触发倒换） |
| `CMD-UNC-107021-07` | ADD ADDRUPGROUP | 同上 §5.7 | 2 | UPFGRPTYPE=UDM（PRIORITY 生效前提） |
| `CMD-UNC-107021-08` | ADD UPFBINDGRP | 同上 §5.8 | 3 | ★★★PRIORITY（主=0，备=1；仅 UDM/Radius 生效） |
| `CMD-UNC-107021-09` | ADD POOLBINDAPN | 同上 §5.9 | 3 | 白名单检查可选 |
| **合计** | — | — | **71 参数行** | — |

### 5.2 ★本特性核心参数：ADD UPFBINDGRP.PRIORITY（主备语义唯一承载参数）

> 以下为本特性唯一需要重点标注的参数（全参数表见 010502 §5.8）。

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 本特性说明 |
|------|------|---------|-----------------|--------|-----------|
| PRIORITY | int | 0~255 | `optional` | 255 | ★主备优先级：越小优先级越高；本特性约定主用 UPF=0，备用 UPF=1；**仅 UPFGRPTYPE=UDM/Radius 时生效**（手册原文：Local/DHCP 类型一 UPF 绑一组，PRIORITY 不生效）；同一 UPF 组内主备取值不可相同 |

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

> **Schema 参考**：§11.7 `MMLCommand operates_on ConfigObject`。
> 本特性 9 个配置类命令的 operates_on 边与 010502 样板完全一致（指向同一组 ConfigObject），本文件用 107021 编号空间重新登记，便于特性级溯源。

### 6.1 WSFD-107021 核心命令（9条，全部复用 010502 的 ConfigObject）

| MMLCommand（本文件编号） | operates_on -> ConfigObject | 说明（主备冗余视角） |
|--------------------------|---------------------------|----------------------|
| ADD ADDRPOOL (CMD-UNC-107021-01) | ADDRPOOL | 静态地址池（POOLTYPE=UDM） |
| ADD SECTION (CMD-UNC-107021-02) | SECTION | 主备 UPF 共享网段 |
| ADD ADDRPOOLGRP (CMD-UNC-107021-03) | ADDRPOOLGRP | 地址池组（UDM） |
| ADD POOLBINDGRP (CMD-UNC-107021-04) | POOLBINDGRP | 地址池绑定池组 |
| ADD POOLGRPMAP (CMD-UNC-107021-05) | POOLGRPMAP | ★池组映射到含主备 UPF 的 UPF 组 |
| ADD UPNODE (CMD-UNC-107021-06) | UPNODE | ★主备两个 UPF 节点实例 |
| ADD ADDRUPGROUP (CMD-UNC-107021-07) | ADDRUPGROUP | ★UPF 组（含主备两 UPF） |
| ADD UPFBINDGRP (CMD-UNC-107021-08) | UPFBINDGRP | ★★★主备 PRIORITY 承载对象 |
| ADD POOLBINDAPN (CMD-UNC-107021-09) | POOLBINDAPN | 白名单检查可选 |

### 6.2 前置依赖命令（引用，非本特性拥有，2条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD APN（簇A） | APN | APN/DNN 实例（POOLBINDAPN 引用） |
| ADD PNFPROFILE（簇F） | PNFPROFILE | 对端 NF 实例概述（ADD UPNODE 的 NFINSTANCENAME 关联，主备两 UPF 均需先在 PNFPROFILE 登记） |

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand / CommandParameter / ConfigObject`（反向：规则治理命令，非命令 has_rule）。

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-107021-01 | CMD-UNC-107021-08.PRIORITY (ADD UPFBINDGRP) | 主备优先级取值（主=0，备=1），仅 UDM/Radius 类型生效，同组主备不可相同 |
| CR-107021-02 | OBJ-UPNODE.LOCK + OBJ-UPFBINDGRP.PRIORITY | 主用 UPF 故障/锁定时倒换至备用 UPF，主用恢复后回切 |
| CR-107021-03 | OBJ-SECTION-UNC ↔ OBJ-UPNODE（主+备） | 静态网段须同时包含在主备 UPF 与 UDG 地址池规划内 |

---

## 8. 使用实例脚本（保留激活文档原文，1 个主备冗余场景）

### 8.1 激活静态地址用户路由冗余（来源：激活静态地址用户路由冗余_76652607.md，★主备 UPF 完整脚本）

```
//创建本地地址池（UDM 类型，白名单检查开启，绑定 VPN）。
ADD ADDRPOOL: POOLNAME="pool01", IPVERSION=IPv4, POOLTYPE=UDM, CHECKIPVALID=Enable, HASVPN=Enable, VPNINSTANCE="VRF-A";

//配置地址池与APN的绑定关系（白名单检查）。
ADD POOLBINDAPN:APN="huawei.com",POOLNAME="pool01";

//配置本地地址池里的IPv4地址段（主备 UPF 共享网段）。
ADD SECTION: POOLNAME="pool01", SECTIONNUM=1, IPVERSION=IPv4, V4STARTIP="10.0.0.0", V4ENDIP="10.1.2.3";

//配置地址池组名称（UDM 类型）。
ADD ADDRPOOLGRP: POOLGRPNAME="poolgroup1", POOLGRPTYPE=UDM;

//配置地址池与地址池组绑定。
ADD POOLBINDGRP: POOLGRPNAME="poolgroup1", POOLNAME="pool01";

//配置静态地址用户使用的主、备UPF（各自独立 ADD UPNODE，ADDRALLOCMODE=INHERIT）。
ADD UPNODE: NFINSTANCENAME="UPF_Instance_1", ADDRALLOCMODE=INHERIT;
ADD UPNODE: NFINSTANCENAME="UPF_Instance_2", ADDRALLOCMODE=INHERIT;

//配置静态地址用户使用的UPF组（UDM 类型，一组含主备两 UPF）。
ADD ADDRUPGROUP: UPFGRPNAME="upfgroup1", UPFGRPTYPE=UDM;

//配置主、备UPF与UPF组绑定（★★★PRIORITY 区分主备：主用=0，备用=1）。
ADD UPFBINDGRP: UPFGRPNAME="upfgroup1", UPFID="UPF_Instance_1", PRIORITY=0;
ADD UPFBINDGRP: UPFGRPNAME="upfgroup1", UPFID="UPF_Instance_2", PRIORITY=1;

//配置地址池组与UPF组绑定。
ADD POOLGRPMAP: MAPPINGNAME="mapping01", POOLGRPNAME="poolgroup1", UPFGRPNAME="upfgroup1";
```

> **★与 010502「配置静态IP网段绑定UPF」脚本的关键差异**：
> - 010502 脚本仅绑 1 个 UPF（`ADD UPFBINDGRP: UPFID="UPF_Instance_1";` 无 PRIORITY，单 UPF）；
> - 本特性脚本绑 **2 个 UPF**（主备），且**显式设置 PRIORITY=0/1** 区分主备——这是本特性在命令层的唯一脚本差异。

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径（全部复用 010502 样板）

| 命令 | 参数行数 | 来源手册路径（相对 `output/UNC 20.15.2 产品文档(裸机容器) 05/`） | 本特性是否独立抽参 |
|------|---------|----------------------------------------------------------------|------------------|
| ADD ADDRPOOL | 13 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池管理/增加地址池（ADD ADDRPOOL）_09653289.md` | 否（复用 010502 §5.1） |
| ADD SECTION | 8 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址段管理/增加地址段（ADD SECTION）_09651691.md` | 否（复用 010502 §5.2） |
| ADD ADDRPOOLGRP | 4 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池组管理/增加地址池组（ADD ADDRPOOLGRP）_32232812.md` | 否（复用 010502 §5.3） |
| ADD POOLBINDGRP | 3 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池组管理/增加地址池和地址池组的绑定关系（ADD POOLBINDGRP）_32232813.md` | 否（复用 010502 §5.4） |
| ADD POOLGRPMAP | 6 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池组映射配置/增加地址池组映射关系（ADD POOLGRPMAP）_32232814.md` | 否（复用 010502 §5.5） |
| ADD UPNODE | 29 | `OM参考/命令/UNC MML命令/业务服务管理/接口管理/PFCP接口管理/UP管理/UP节点管理/增加UPF节点（ADD UPNODE）_09652571.md` | 否（复用 010502 §5.6） |
| ADD ADDRUPGROUP | 2 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址分配UPF组管理/增加UPF组（ADD ADDRUPGROUP）_49644911.md` | 否（复用 010502 §5.7） |
| ADD UPFBINDGRP | 3 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址分配UPF组管理/增加UPF和UPF组的绑定关系（ADD UPFBINDGRP）_32232815.md` | 否（复用 010502 §5.8）；★本特性仅重点标注 PRIORITY |
| ADD POOLBINDAPN | 3 | `OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/UE地址管理/UE地址池管理/地址池绑定APN/增加APN实例与地址池绑定关系（ADD POOLBINDAPN）_09653789.md` | 否（复用 010502 §5.9） |
| **合计** | **71 参数行** | 9 命令手册全部已在 010502 样板定位成功 | — |

### 9.2 ⚠️手册未定位列表

| 命令 | 状态 | 原因 |
|------|------|------|
| 无 | — | 本特性参考信息列出的全部命令（ADD/RMV/LST/MOD 系列）+ 激活文档引用的命令手册均已定位（手册路径与 010502 样板一致）。 |

> **说明**：本特性无独有命令，全部命令手册已在 010502 样板完成定位与参数抽取。维护类命令（RMV ADDRPOOL/SECTION/ADDRPOOLGRP/POOLGRPMAP、LST 系列、MOD UPNODE）参考信息已列出，其手册存在但本期按「维护/查询类本期略」不抽参数。

### 9.3 与原 04-command-graph.md 的关键差异（★重点核对项）

| 差异项 | 原 04（若存在） | 本文件（draft） | 影响 |
|--------|----------------|----------------|------|
| **冗余承载参数** | 原 04 未针对 WSFD-107021 建立特性级 CR | §4 建立 CR-107021-01~03，明确主备语义落在 **ADD UPFBINDGRP.PRIORITY**（非 UDG 的 REDUNDFUNC/MASTERFLAG） | 特性级规则治理细化，纠正「冗余=地址池级开关」的误解（UNC 侧实为 UPF 组内 PRIORITY） |
| **主备倒换触发** | 原 04 未建模 | CR-107021-02 建模 UPF 故障/LOCK 触发倒换 + 主用恢复回切（特性概述原理） | 倒换机制可溯源至特性概述 §1.3.9 |
| **网段一致性约束** | 原 04 未建模 | CR-107021-03 建模主备 UPF 网段一致 + UDG 地址池包含（激活文档必备事项） | 跨特性约束（依赖 GWFD-010104）可溯源 |
| **参数抽取策略** | — | 本文件不重复抽参数，全部复用 010502 样板（71 参数行），仅在 §5.2 重点标注 PRIORITY | 避免重复劳动，保持单一参数源（010502） |

### 9.4 与 010502 样板的命令集差异核对

| 核对项 | 010502（配置静态IP网段绑定UPF） | 107021（本特性） | 差异结论 |
|--------|-------------------------------|------------------|---------|
| 配置类命令集 | 9 命令（ADDRPOOL/SECTION/ADDRPOOLGRP/POOLBINDGRP/UPNODE/ADDRUPGROUP/UPFBINDGRP/POOLGRPMAP/POOLBINDAPN） | **完全相同 9 命令** | ✅命令集零差异（本特性为辅助特性，复用 010502 命令族） |
| ADD UPFBINDGRP 调用次数 | 1 次（单 UPF） | **2 次**（主 + 备 UPF） | ★脚本差异：本特性绑 2 个 UPF |
| ADD UPFBINDGRP.PRIORITY | 不显式设置（默认 255，单 UPF 无主备语义） | **显式设置 0/1**（主备） | ★★本特性在命令层的唯一独有语义 |
| ADD UPNODE 调用次数 | 1 次（单 UPF） | **2 次**（主 + 备） | ★脚本差异 |
| 维护类命令 | 010502 参考信息未列 RMV/LST/MOD | 本特性参考信息列出 RMV ADDRPOOL/SECTION/ADDRPOOLGRP/POOLGRPMAP + LST 系列 + MOD UPNODE | ★本特性参考信息更完整（含维护命令），用于冗余关系增删改查 |
| 激活脚本 POOLTYPE | UDM | UDM（一致） | ✅ |
| 独有 ConfigObject | 16 个 | **0 个独有**（全部复用 010502） | ✅无独有对象 |
| 独有 CommandRule | 6 条（CR-010502-01~05 + CR-010504-01） | **3 条独有**（CR-107021-01~03，聚焦主备） | ★本特性规则聚焦主备语义 |

### 9.5 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（手册定位成功，全部复用 010502） | 9 |
| 配置类命令参数总行数（全部复用 010502） | 71 |
| 维护/查询类命令（本期略） | 10（RMV 4 + LST 4 + MOD 1 + DSP 1） |
| ⚠️手册未定位命令 | 0 |
| ConfigObject（全部复用 010502，无独有） | 9 |
| CommandRule（本特性独有，聚焦主备） | 3 |
| ConfigObject 关系边（复用 010502，主备路径视角重述） | 3 depends_on + 主备数据路径 3 跳 |
| operates_on 边 | 9（核心，全部复用 010502 ConfigObject）+ 2（前置依赖引用） |
| 激活子场景脚本 | 1（主备 UPF 路由冗余） |

---

> 本文件为 WSFD-107021 静态地址用户路由冗余（UNC/SMF）命令层抽取，作为簇B UNC 侧的辅助特性补充。
> **★关键贡献**：①明确本特性为「辅助特性」，命令集与 010502 完全重合，无独有命令/ConfigObject；②定位本特性独有语义的承载点为 **ADD UPFBINDGRP.PRIORITY**（主=0，备=1），纠正「冗余=地址池级开关」的误解（区别于 UDG 侧 ADD POOL.REDUNDFUNC/MASTERFLAG）；③建立 3 条特性级 CommandRule（主备优先级取值/故障倒换/网段一致性）；④完整登记参考信息列出的维护类命令（RMV/LST/MOD），为冗余关系增删改查提供溯源；⑤区分 UDG（ADD POOL.REDUNDFUNC/MASTERFLAG）vs UNC（ADD UPFBINDGRP.PRIORITY）冗余机制，零混淆。
