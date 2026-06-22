# Batch-07: URL 过滤与 UNC 接入控制（含双轨动作机制）

> 批次 07 | 主题：URL 过滤的独立 ACTION 机制 + UNC 侧接入控制 + 位置策略触发 | 来源：GWFD-110471、WSFD-211001 feature-knowledge + UNC接入控制专题 | 特性数 2 + 1 专题 | 核心度 ★★★★★（**双轨动作机制厘清的核心批次**）

---

## 1. 概述

本批次厘清访问限制场景中**最关键的架构事实**：访问限制动作存在**两条独立的轨道路径**——

- **轨道 A（PCC 体系）**：通过 `RULE → PCCPOLICYGRP + PCCACTIONPROP` 触发动作，ADC、重定向族、头防欺诈走这条
- **轨道 B（URL 过滤体系）**：通过 `CONTCATEGBIND.ACTION` / `CFTEMPLATE.ACTION` 直接指定 BLOCK/PERMIT/REDIRECT，URL 过滤走这条

这两条轨道在 ConfigObject、MML 命令、动作类型上**完全独立**，但都最终作用于用户业务流。理解双轨机制是设计访问限制场景三层图谱的前提。

同时，本批次还涵盖 **UNC 侧的接入控制**——UDG 侧的访问限制需要 UNC 侧的策略下发与位置触发来驱动。

---

## 2. 核心知识点（KP）

### KP-1 URL 过滤的工作机制（来自 GWFD-110471 §3）

URL 过滤是**唯一引入外部服务器（ICAP Server）**的访问限制特性：

```
用户访问 URL
    ↓
UDG 解析报文提取 URL（HTTP Get/Post 或 HTTPS SNI/证书）
    ↓
UDG 通过 ICAP REQMOD 请求消息上送 URL 到 ICAP Server
    ↓
ICAP Server 查询 URL 分类数据库
    ↓ （两种返回模式）
    ├─ 分类匹配模式：返回 Category ID，UDG 本地匹配套餐策略
    └─ 直接动作模式：直接返回动作策略
    ↓
UDG 执行动作：BLOCK / PERMIT / REDIRECT
```

**关键独立性**：URL 过滤的 BLOCK/PERMIT/REDIRECT 动作**不经过 RULE.POLICYTYPE**，而是在 `CFTEMPLATE` 和 `CONTCATEGBIND` 的 `ACTION` 参数中直接指定。

---

### KP-2 URL 过滤的 ConfigObject 体系（来自 GWFD-110471 §4.1）

URL 过滤的配置对象分为两大块，**完全独立于 PCC 体系**：

#### ICAP Server 互通配置（前置）
| 对象 | 命令 | 用途 |
|------|------|------|
| `VPNINST` | ADD VPNINST | VPN 实例 |
| `LOGICINF` | ADD LOGICINF | UDG 与 ICAP Server 间逻辑接口 |
| `ICAPSERVER` | ADD ICAPSERVER | ICAP 服务器（ICAPSERVERTYPE=URL_FILTERING） |
| `ICAPLOCALINFO` | ADD ICAPLOCALINFO | 本端信息（User Agent） |
| `ICAPSVRGRP` | ADD ICAPSVRGRP | ICAP 服务器组 |
| `ICAPSVRBINDISG` | ADD ICAPSVRBINDISG | 服务器与组绑定 |

#### URL 过滤业务配置（核心，独立动作体系）
| 对象 | 命令 | 用途 | 关键参数 |
|------|------|------|----------|
| `APN` | ADD APN | URL 过滤用户使用的 APN | — |
| `APNCFFUNC` | SET APNCFFUNC | APN 粒度开关 | CFSWITCHVALUE=ENABLE |
| `CFPROFILE` | ADD CFPROFILE | 内容过滤策略 | — |
| `CFTEMPLATE` | ADD CFTEMPLATE | 内容过滤模板（**含 ACTION**） | **ACTION=BLOCK/PERMIT/REDIRECT**（缺省动作） |
| `APNCFTEMPLATE` | SET APNCFTEMPLATE | APN 与模板绑定 | — |
| `CFPROFBINDCFT` | ADD CFPROFBINDCFT | 策略与模板绑定 | — |
| `CONTCATEGROUP` | ADD CONTCATEGROUP | 内容分类组 | CATEGORYTYPE=SPECIFIC, CATEGORYID |
| `CONTCATEGBIND` | ADD CONTCATEGBIND | 策略与分类组绑定（**含 ACTION**） | **ACTION=BLOCK/PERMIT/REDIRECT**（分类级动作） |
| `CFCACHEPARA` | SET CFCACHEPARA | 本地缓存参数 | CACHEIDLETIME, CACHESW |

---

### KP-3 UNC 接入控制的四类限制（来自 UNC 接入控制专题概述）

接入控制是 **UNC 侧**的访问限制机制，分为移动接入控制和会话管理控制：

#### 移动接入控制（注册阶段）
| 限制级别 | 限制对象 | 功能 | 相关特性 |
|---------|---------|------|----------|
| 系统级 | RAT | 限制无线接入方式（如4G用户不接入NG-RAN） | WSFD-106003 用户接入控制（AMF） |
| 系统级 | 核心网 | 限制核心网接入方式（如4G不接入5GC） | WSFD-106003 用户接入控制（AMF） |
| 用户级 | 号段/单用户 | 禁止区域接入 | WSFD-105003 区域漫游限制（AMF） |
| 用户级 | 单用户 | ODB 限制（如禁止漫游用户接入本网） | WSFD-106005 支持ODB（AMF） |
| 区域级 | TAI | 区域级黑白名单接入控制 | WSFD-105003 区域漫游限制（AMF） |

#### 会话接入限制（会话阶段）
| 限制级别 | 限制对象 | 功能 | 相关特性 |
|---------|---------|------|----------|
| 用户级 | 单用户 | ODB 限制业务（如欠费禁用数据业务） | WSFD-106005 支持ODB（AMF） |
| 区域级 | TAI | 服务区域限制（如套餐只能在 A 市用） | WSFD-105006 服务区域限制 |

---

### KP-4 WSFD-211001 基于初始接入位置的策略控制（位置触发层）

WSFD-211001 是 **UNC 侧的位置触发特性**，本身不产生动作，而是提供"**用户在哪里接入**"作为策略决策输入：

**核心机制**：
- 用户激活时 SGSN/MME/AMF 上报 ULI（User Location Information）
- UNC（SMF/PGW-C）将 ULI 透传给 PCRF/PCF（动态PCC）或本地决策（本地PCC）
- 匹配 `USRLOCATION` + `USRLOCATIONGRP` → 触发对应的访问限制/带宽控制策略

**ConfigObject**：
| 对象 | 命令 | 用途 |
|------|------|------|
| `USRLOCATION` | ADD USRLOCATION | 用户位置（CGI/ECGI/NCGI） |
| `USRLOCATIONGRP` | ADD USRLOCATIONGRP | 位置组（批量绑定） |
| `UPBINDUPG` | ADD/MOD UPBINDUPG | 用户模板组绑定（含位置组） |
| `APNUSRPROFG` | ADD APNUSRPROFG | APN/DNN 与用户模板组绑定 |

**位置类型**：CGI（2/3G）、ECGI（4G）、NCGI（5G）。

**License**：`82200BNQ LKV2PCIAL01`，依赖 PCC基本功能（WSFD-109101）+ 基于业务感知的带宽控制（WSFD-211005，无PCRF场景）。

---

## 3. 关键发现（跨特性横向归纳）

### ⭐ 发现-1 双轨动作机制对比（本批次核心输出）

访问限制场景中存在**两条完全独立的动作轨道路径**：

#### 轨道 A：PCC 体系（RULE.POLICYTYPE 驱动）

```
用户业务流
    ↓
FILTER + FLOWFILTER + FLTBINDFLOWF（L3/L4匹配）
[+ L7FILTER + PROTBINDFLOWF（L7匹配）]
    ↓
RULE（POLICYTYPE = ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY）
    ↓ POLICYNAME 指向
┌─────────────────────────────────────────────┐
│ ADC：直接在 RULE 上（FLOWFILTER）             │
│ PCC：PCCPOLICYGRP + URRGROUP                 │
│ HEADEN：HEADEN 对象                           │
│ SMARTREDIRECT：SMARTHTTPREDIR / DNSOVERWRITING│
│ WEBPROXY：IPFARM                              │
└─────────────────────────────────────────────┘
    ↓
UDG 执行动作（隐式 BLOCK / 头增强插入 / 重定向报文改写）
```

**轨道 A 的特点**：
- 以 `RULE.POLICYTYPE` 为核心区分
- 动作类型由 POLICYTYPE 隐式决定（ADC 兜底阻塞、HEADEN 插入、SMARTREDIRECT 改写）
- 配置链路长（FILTER → FLOWFILTER → RULE → POLICYNAME 指向的具体对象）
- 走 PCC 体系时需要 PCRF/PCF 下发规则或本地预定义

**走轨道 A 的特性**：GWFD-020357 ADC、GWFD-110261/262/263 头增强、GWFD-110401 头防欺诈、GWFD-110284 HTTP智能重定向、GWFD-110283 DNS纠错、GWFD-110281 用户Portal、GWFD-110282 WebProxy

#### 轨道 B：URL 过滤体系（CFTEMPLATE/CONTCATEGBIND.ACTION 驱动）

```
用户访问 URL
    ↓
UDG 解析提取 URL（HTTP Get/Post / HTTPS SNI）
    ↓
ICAP REQMOD 上送 URL 到 ICAP Server
    ↓
ICAP Server 返回 Category ID 或直接动作
    ↓
UDG 匹配本地套餐策略：
┌─────────────────────────────────────────────┐
│ ADD CFTEMPLATE:ACTION=BLOCK/PERMIT/REDIRECT  │ ← 模板级缺省动作
│ ADD CONTCATEGBIND:ACTION=BLOCK/PERMIT/REDIRECT│ ← 分类级精确动作
└─────────────────────────────────────────────┘
    ↓
UDG 直接执行 BLOCK/PERMIT/REDIRECT
```

**轨道 B 的特点**：
- 以 `CFTEMPLATE.ACTION` 和 `CONTCATEGBIND.ACTION` 为核心（**显式指定 BLOCK/PERMIT/REDIRECT**）
- 动作类型直接在配置参数中声明，不通过 POLICYTYPE 间接表达
- 依赖外部 ICAP Server（引入 ICAP Server/Group/VPN 配置体系）
- 触发维度单一（仅基于 URL 分类），不涉及复杂的多条件组合

**走轨道 B 的特性**：GWFD-110471 URL 过滤基本功能

#### 双轨对比矩阵

| 维度 | 轨道 A（PCC 体系） | 轨道 B（URL 过滤体系） |
|------|-------------------|----------------------|
| **核心 ConfigObject** | RULE（POLICYTYPE差异化） | CFTEMPLATE + CONTCATEGBIND |
| **动作指定方式** | 隐式（POLICYTYPE 决定） | 显式（ACTION=BLOCK/PERMIT/REDIRECT） |
| **匹配维度** | 多维度（L3/L4/L7/错误码/URL/UserAgent...） | 单维度（URL 分类） |
| **外部依赖** | 可选 PCRF/PCF | **必需 ICAP Server** |
| **动作类型** | 隐式阻塞、头增强、重定向改写 | 直接 BLOCK/PERMIT/REDIRECT |
| **典型 MML 命令** | ADD RULE, ADD PCCPOLICYGRP, ADD HEADEN, ADD SMARTHTTPREDIR | ADD CFTEMPLATE, ADD CONTCATEGBIND, ADD ICAPSERVER |
| **独立配置体系** | 共用 FILTER/FLOWFILTER/USERPROFILE | 独有 APNCFFUNC/CFPROFILE/CFTEMPLATE/CONTCATEGROUP/ICAP* |
| **License 共用** | 各特性独立 License | URL 过滤独立 License（82200FCP UFBF01） |

#### 双轨协同（重要）

**两条轨道可以并存于同一用户**：
- 轨道 A 处理 ADC/头增强/重定向类需求（基于应用、URL、用户属性）
- 轨道 B 处理 URL 分类过滤（基于外部 URL 分类数据库）
- 用户业务流可能先后被两条轨道检查，最终动作取决于配置优先级和规则匹配顺序

**对图谱建模的关键启示**：
1. RULE 对象需要**两个 variant_dimension**：`policy_track`（A/B）和 `policy_type`（POLICYTYPE/ACTION）
2. 轨道 B 的 CFTEMPLATE/CONTCATEGBIND 是**独立于 RULE 体系**的配置对象，需要单独建模
3. ICAP Server 互通配置是 URL 过滤**独有的资源类对象**，类似 Portal/WebProxy 的 IPFarm

---

### 发现-2 UNC 侧接入控制与 UDG 侧访问限制的分工

访问限制场景中，**UNC 侧和 UDG 侧承担不同角色**：

```
UNC 侧（SMF/PGW-C/AMF）：
├─ 移动接入控制：RAT/核心网/区域/ODB 限制（注册阶段，WSFD-106003/105003/106005）
├─ 会话接入控制：ODB/服务区域限制（会话阶段，WSFD-106005/105006）
├─ 位置触发：基于 ULI 的策略决策（WSFD-211001）
└─ 策略下发：通过 Gx/N7 向 PCRF/PCF，通过 N4/PFCP 向 UDG
        ↓
UDG 侧（PGW-U/UPF）：
├─ 应用检测：ADC（GWFD-020357）
├─ 头增强：HTTP/HTTPS/RTSP 头增强（GWFD-110261/262/263）
├─ 头防欺诈：GWFD-110401
├─ 重定向：HTTP重定向/DNS纠错/Portal/WebProxy（GWFD-110284/283/281/282）
└─ URL 过滤：GWFD-110471（与 ICAP Server 协同）
```

**关键观察**：
- UNC 侧的接入控制是**注册/会话阶段**的"是否允许接入"决策（粗粒度）
- UDG 侧的访问限制是**业务流阶段**的"允许做什么"决策（细粒度）
- 两层共同构成完整的访问限制链路：先 UNC 决定能否接入，再 UDG 决定能访问什么

**WSFD-211001 是连接两层的关键桥梁**：在 UNC 侧用 ULI 匹配位置，下发策略到 UDG 侧执行（带宽控制、重定向、阻塞）。

---

### 发现-3 URL 过滤的 URL 解析能力差异（来自 GWFD-110471 §3.2）

URL 过滤对不同协议的 URL 提取能力不同：

| 协议 | URL 解析能力 | 依赖 SA |
|------|-------------|---------|
| HTTP/WAP1.X/WAP2.0 | **完整 URL**（仅上行 Get/Post） | SA-Basic + SA-Web Browsing + SA-Mobile |
| HTTPS | **仅 SNI 或证书**（不能解析完整 URL） | SA-Basic + SA-Web Browsing + HTTP2.0 Host识别 |
| 非加密 QUIC | SNI 或证书 | 同 HTTPS |

**关键限制**：HTTPS 场景下，URL 过滤**不能基于完整 URL**，只能基于 SNI——这是 HTTPS 加密带来的固有限制。

---

### 发现-4 URL 过滤的本地缓存加速机制（来自 GWFD-110471 §4.2）

为减少与 ICAP Server 的交互，URL 过滤支持本地缓存：
- `SET CFCACHEPARA:CACHEIDLETIME=7200,CACHESW=ENABLE`
- 缓存 URL 分类查询结果，默认过期时间 7200 秒
- 缓存开启时显著降低 ICAP 链路负荷和用户 Get 首包时延

**性能权衡**（来自 §6.4）：
- 开启 URL 过滤会增大 UDG CPU 消耗（每次业务都需 ICAP 交互）
- 用户 Get 首包时延增加（等待 URL 动作匹配完成）
- 缓存超限会丢包

---

### 发现-5 URL 过滤与接入控制映射到访问限制三种动作

| 访问限制动作 | URL 过滤如何实现 | UNC 接入控制如何实现 |
|-------------|----------------|---------------------|
| **DISCARD（阻塞）** | `CFTEMPLATE.ACTION=BLOCK` 或 `CONTCATEGBIND.ACTION=BLOCK` | 区域漫游限制拒绝接入、ODB 禁用数据业务、服务区域限制 |
| **HEADEN（头增强）** | 不直接做头增强（与 GWFD-110261/262/263 配合） | 不做头增强 |
| **REDIRECT（重定向）** | `CFTEMPLATE.ACTION=REDIRECT` 或 `CONTCATEGBIND.ACTION=REDIRECT` | 不直接做重定向（但可下发重定向策略到 UDG 执行） |
| **PERMIT（放行）** | `CFTEMPLATE.ACTION=PERMIT` 或 `CONTCATEGBIND.ACTION=PERMIT` | 默认行为（允许接入） |

**关键观察**：**URL 过滤是访问限制场景中唯一显式支持 PERMIT 动作的特性**（轨道 A 的特性主要是"不做动作"或"做阻塞/重定向"）。

---

## 4. 配置对象/命令复用清单

### URL 过滤独有配置对象（轨道 B 核心）
- 业务：`APNCFFUNC` + `CFPROFILE` + `CFTEMPLATE`（含ACTION） + `APNCFTEMPLATE` + `CFPROFBINDCFT` + `CONTCATEGROUP` + `CONTCATEGBIND`（含ACTION） + `CFCACHEPARA`
- 互通：`VPNINST` + `LOGICINF` + `ICAPSERVER` + `ICAPLOCALINFO` + `ICAPSVRGRP` + `ICAPSVRBINDISG`

### URL 过滤独有 MML 命令
- `ADD CFPROFILE` / `ADD CFTEMPLATE` / `SET APNCFTEMPLATE` / `ADD CFPROFBINDCFT`
- `ADD CONTCATEGROUP` / `ADD CONTCATEGBIND` / `SET CFCACHEPARA` / `SET APNCFFUNC`
- `ADD VPNINST` / `ADD ICAPSERVER` / `ADD ICAPLOCALINFO` / `ADD ICAPSVRGRP` / `ADD ICAPSVRBINDISG`
- 辅助：`SET GLBCFFUNC` / `ADD GLBCFTEMPLATE` / `SET CFPROTOCOLLST` / `ADD CFWHITEURLLST` / `SET CFSRVMODE` / `ADD CFIPWHITELIST` / `ADD CFPFSPECACTION`

### UNC 接入控制独有配置对象
- WSFD-211001：`USRLOCATION` + `USRLOCATIONGRP` + `UPBINDUPG` + `APNUSRPROFG`

### UNC 接入控制独有 MML 命令
- `ADD USRLOCATION` / `ADD USRLOCATIONGRP` / `ADD/MOD UPBINDUPG` / `ADD APNUSRPROFG`

### URL 过滤与场景级共用的配置对象（部分跨轨道）
- 三四层：`FILTER` → `FLOWFILTER` → `FLTBINDFLOWF`（URL 过滤的 RULE 仍走轨道 A 用于匹配触发）
- 策略载体：`URR` → `URRGROUP` → `PCCPOLICYGRP`（URL 过滤的 RULE 用 POLICYTYPE=PCC）
- 规则绑定：`RULE`（URL 过滤仍需 RULE 匹配触发） → `USERPROFILE` → `RULEBINDING`

### License
- URL 过滤：`82200FCP LKV3G5UFBF01`
- 初始接入位置策略：`82200BNQ LKV2PCIAL01`

---

## 5. 来源

- 主：
  - `feature-knowledge/GWFD-110471-URL过滤基本功能.md`
  - `feature-knowledge/WSFD-211001-基于初始接入位置的策略控制.md`
- 业务专题：
  - `UNC接入控制专题/接入控制概述_12835910.md`
- 横向归纳：基于 Batch-04/05/06 的轨道 A 体系与本批次轨道 B 体系的对比

---

## 6. 后续待办（供 P3 横向分析综合）

1. **双轨优先级**：当 RULE（轨道A）和 CFTEMPLATE/CONTCATEGBIND（轨道B）对同一业务流给出不同动作时，实际执行哪个？需查参考信息或现网验证
2. **ICAP 故障降级**：ICAP Server 不可用时，URL 过滤的缺省动作（BLOCK 还是 PERMIT）需查 `ADD CFTEMPLATE` 的 `ACTION` 默认值
3. **双轨与 PCCPOLICYGRP 的交互**：URL 过滤的 RULE 也用 POLICYTYPE=PCC，但其动作不走 PCCPOLICYGRP，这是潜在建模难点
