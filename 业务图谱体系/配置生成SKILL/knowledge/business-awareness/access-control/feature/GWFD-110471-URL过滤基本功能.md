# GWFD-110471 URL过滤基本功能 知识文档

> 访问限制场景 | URL内容过滤核心特性 | UDG | 来源：特性概述+配置URL过滤+配置ICAP互通+调测+参考信息 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110471 |
| feature_name | URL过滤基本功能 |
| feature_group | URL过滤 |
| parent_feature_id | -（本特性在配置树无显式独立父节点；业务上归属"业务感知功能 → 内容过滤"分支，PCC触发链父为 GWFD-020351 PCC基本功能） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["匹配模式(分类匹配模式/直接动作模式)", "动作类型(BLOCK阻塞/PERMIT放行/REDIRECT重定向)", "协议类型(HTTP/WAP1.X/WAP2.0/HTTPS-非加密QUIC仅SNI)", "粒度(APN级SET APNCFFUNC/全局SET GLBCFFUNC)", "ICAP Server部署(单机/服务器组+主备)", "是否启用本地cache(SET CFCACHEPARA)", "缺省动作来源(CFTEMPLATE.ACTION vs CONTCATEGBIND.ACTION)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110471-01, EV-FK-AC-110471-02, EV-FK-AC-110471-03, EV-FK-AC-110471-04, EV-FK-AC-110471-05]（P4建06-evidence-index时确定，先用占位） |
| license_required | `82200FCP LKV3G5UFBF01 URL过滤基本功能` |

---

## 1. 概述

### 1.1 特性定义（是什么）

URL（Uniform Resource Locator）过滤是互联网内容过滤的一种形式。内容过滤是指用户在浏览互联网信息时，通过网络设备对浏览内容进行分析，过滤与用户无关的数据、低俗信息、恶意网站等指定数据的一种控制方式，以达到合理利用网络资源、保护用户信息安全的目的。

UDG 支持基于 URL 的过滤，URL 是用户浏览访问的关键信息，通过专业的 URL 分类数据库可以高效地标识网页内容类型。

**工作机制（核心）**：UDG 将用户访问的 URL 信息通过 ICAP 协议发送给外部的 ICAP Server 进行分析识别；ICAP Server 根据用户签约的 URL 过滤套餐和 URL 分类数据库返回动作策略（放行 PERMIT、阻塞 BLOCK、重定向 REDIRECT），UDG 执行对应策略，实现访问控制。

> **法律声明（产品文档原文保留）**：URL 过滤基本功能是在符合适用的国际、国家、地区、州及当地法律的情况下，为最终用户的绿色上网、以及政府对某些特定网站的访问拦截等法律允许的合法目的，来限制用户对某些 URL 地址的访问。实现此功能，UDG 需要将用户访问的 URL 信息发送给外部的 URL 过滤服务器进行分析识别，存在将用户行为信息泄露的风险。同时，UDG 会根据 URL 过滤服务器的指示丢弃部分报文，禁止用户访问相关内容，存在妨碍通信自由的法律诉讼风险。在法律允许的情况下，华为不对与 URL 过滤基本功能相关的任何损害或索赔负责。

> SourcePath: `UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/GWFD-110471 URL过滤基本功能特性概述_56369529.md` §定义、§说明

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.10.2 及后续版本 | 支持业务解析，识别上网浏览业务并提取 URL；接受 PCRF/PCF 下发的用户签约 URL 过滤套餐名，支持配置 URL 过滤套餐内容；支持与 ICAP Server 的交互：将 URL 通过 ICAP 协议发送给 ICAP Server；在 ICAP Server 返回 URL 所属分类时，根据 URL 分类在 URL 过滤套餐中匹配获得相关联的动作策略并执行（放行/阻塞/重定向）；在 ICAP Server 返回 URL 关联的动作策略时，直接执行该策略 |
| ICAP Server | 外部 URL 过滤服务器 | 无特殊要求 | 支持 ICAP 协议，接受并解析 UDG 发送的 URL；支持 URL 分类，返回分类 ID；支持用户 URL 过滤套餐签约及更新；支持对 URL 分类数据库及用户签约信息的更新；与运营商签约系统间支持以 SOAP 协议下发，或文件方式批量导入用户 URL 过滤签约信息 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §适用NF、§可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.10.2 | 首次发布 |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §发布历史

### 1.4 License

- **License控制项**：`82200FCP LKV3G5UFBF01 URL过滤基本功能`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §可获得性

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 增强运营商竞争力：为政府提供上网浏览行为管理功能，满足国家安全要求；为企业提供屏蔽与工作无关网站的功能，满足企业应用要求；提供恶意网站屏蔽功能，吸引个人用户签约 |
| 用户 | 通过签约恶意网站屏蔽功能，可保护上网安全 |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §客户价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| 政府管理 | 政府通过运营商为用户签约不同的 URL 过滤套餐，对不同人群的上网行为进行管理控制，保证国家信息安全 |
| 企业管理 | 企业通过签约 URL 过滤套餐，过滤与工作无关的网站，满足公司对信息安全的要求 |
| 恶意网页屏蔽 | 通过 URL 分类数据库识别生成或分发恶意软件的网址，UDG 对试图访问该 URL 的请求进行阻止，防止终端被感染，保护用户个人信息安全 |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §应用场景

### 1.7 前置条件与依赖（SA协议族依赖关系）

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | UDG 需要将用户数据报文进行解析获得 URL，SA-Basic 是 SA 的基本功能，**必须开启** |
| 依赖 | GWFD-110103 SA-Web Browsing | 82209755 LKV3G5SAWB01 SA-Web Browsing | 对 HTTP、WAP2.0 协议类型的报文进行解析时需要开启 |
| 依赖 | GWFD-110105 SA-Mobile | 82209757 LKV3G5SAMB01 SA-Mobile | 对 WAP1.X 协议类型的报文进行解析时需要开启 |
| 依赖 | GWFD-110201 HTTP2.0 Host 识别 | 82209773 LKV3G5HSHA01 HTTP2.0 Host识别 | 对 HTTPS 协议类型的报文进行解析时需要开启 |
| 依赖 | GWFD-020351 PCC 基本功能 | 82209825 LKV3G5PCCB01 PCC 基本功能 | 如果需要使用 PCC 策略对用户业务进行策略控制，需开启 PCC 基本功能 |

**前置条件**：
- 已完成加载 License
- 已完成配置到 ICAP Server 的互通数据
- 已完成激活 PCC 基本功能
- 在 ICAP Server 上已导入 URL 分类数据信息

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §与其他特性的交互
> SourcePath: `配置URL过滤_47348205.md` §必备事项

### 1.8 对系统的影响

- URL 过滤基本功能需在 UDG 上对使能该特性的用户打开 SA 功能，需在每次上网业务发生时与 ICAP Server 进行消息交互，**会增大 UDG CPU 资源消耗**
- URL 过滤基本功能特性使能时，用户上网浏览的数据包会在 UDG 被缓存，等待 URL 动作匹配策略完成后才执行，**会加大用户上网浏览 Get 首包的时延**。在等待 ICAP Server 响应之前，如果 UDG 缓存的数据包超过 UDG 的缓存能力，将产生丢包
- UDG 与 ICAP Server 之间要进行大量的消息处理，对系统的性能有一定影响

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §对系统的影响

### 1.9 应用限制

- 仅支持对 **HTTP、HTTPS、WAP1.X、WAP2.0 协议、非加密 QUIC 协议**中携带的 URL 进行过滤及动作策略匹配
- 对于 HTTP、WAP1.X、WAP2.0 协议，**仅对上行 Get/Post 报文中的 URL 进行解析**（不对其他方法或下行报文解析）
- 对于 HTTPS 协议、非加密 QUIC 协议，**支持解析获取 SNI（Server Name Indication）或证书**上报给 ICAP Server（不能解析完整 URL）

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §应用限制

### 1.10 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 整机可配置的 URL 过滤套餐数目 | 500 个 |
| 整机可配置的 ICAP Server 数目 | 30 个 |
| 每个 ICAP Server Group 中可配置的 ICAP Server 数目 | 10 个 |
| 整机可配置的 URL 数目 | 150 万个 |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| IETF | RFC 3507 | Internet Content Adaptation Protocol (ICAP) |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §遵循标准

### 1.12 计费与话单

**本特性不涉及计费与话单**。

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §计费与话单

---

## 2. 激活（License开启命令）

> 与 GWFD-010105 等"配置使能即激活"的特性不同，本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + APN粒度内容过滤开关 + 模板绑定"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5UFBF01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5UFBF01";
```

> SourcePath: `配置URL过滤_47348205.md` §任务示例
> SourcePath: `调测URL过滤基本功能_56249725.md` §操作步骤

---

## 3. 原理

### 3.1 实现原理：ICAP REQMOD 交互 + 两阶段动作匹配

URL 过滤签约信息包括**用户签约 URL 过滤标志**及**URL 过滤套餐名**。运营商在部署 URL 过滤特性时，在 ICAP Server 上部署用户 URL 过滤签约信息。

UDG 通过 **ICAP（Internet Content Adaptation Protocol, RFC 3507）** 协议与外部 ICAP Server 交互。ICAP 协议在 HTTP 1.1 基础上定义，核心是 **REQMOD（Request Modification，请求改写）** 方法：UDG 把用户 HTTP 请求（含 URL）封装进 ICAP REQMOD 请求，ICAP Server 返回 ICAP REQMOD 应答，应答中携带动作策略。

**动作匹配存在两种模式（产品文档可获得性明确）**：

| 模式 | 触发条件 | 动作来源 | 动作取值 | 配置落点 |
|------|---------|---------|---------|---------|
| **分类匹配模式** | ICAP Server 返回 URL 所属分类（Category ID） | UDG 本地匹配 | 在 URL 过滤套餐中按分类匹配获得相关联的动作策略 | `ADD CONTCATEGROUP`（指定 CATEGORYID）+ `ADD CONTCATEGBIND`（指定 ACTION）+ `ADD CFTEMPLATE` 缺省动作兜底 |
| **直接动作模式** | ICAP Server 返回 URL 关联的动作策略 | ICAP Server 直接下发 | UDG 直接执行该策略（放行/阻塞/重定向） | ICAP Server 侧配置，UDG 仅按 `CFTEMPLATE` 接收 |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §可获得性、§原理概述

### 3.2 URL 解析能力（按协议类型）

UDG 针对不同协议提取 URL 的方式存在差异（HTTPS/QUIC 因加密限制只能提取 SNI/证书）：

| 协议类型 | 解析对象 | 上送 ICAP 内容 | 依赖 SA 特性 |
|----------|----------|---------------|-------------|
| HTTP | 上行 Get/Post 报文的 URL | 完整 URL | SA-Basic + SA-Web Browsing |
| WAP2.0 | 上行 Get/Post 报文的 URL | 完整 URL | SA-Basic + SA-Web Browsing |
| WAP1.X | 上行 Get/Post 报文的 URL | 完整 URL | SA-Basic + SA-Mobile |
| HTTPS / 非加密 QUIC | **SNI（Server Name Indication）或证书** | SNI/证书（非完整 URL） | SA-Basic + HTTP2.0 Host 识别 |

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §应用限制

### 3.3 关键信元与动作协商（ICAP REQMOD 协议级细节）

ICAP REQMOD 请求与应答是 URL 过滤的协议载体，关键信元如下：

#### 3.3.1 ICAP REQMOD 请求（UDG → ICAP Server）

| ICAP 信元/HTTP头 | 含义 | 携带内容 |
|------------------|------|---------|
| Request URI | ICAP 服务路径 | `icap://<server>/url_filtering` 或按部署约定 |
| Request Method | ICAP 方法 | `REQMOD` |
| Encapsulated | 封装段偏移声明 | `req-hdr=0, req-body=...`（指明 HTTP 请求头/体的偏移） |
| 携带的 HTTP 请求头（封装在 req-hdr 段） | 用户原始 HTTP 请求 | GET/POST 行、Host、User-Agent、Cookie、URL 等 |
| X-Subscriber-ID（运营商扩展） | 用户标识 | IMSI/MSISDN（用于 ICAP Server 查询用户签约套餐） |
| X-Session-ID | 会话标识 | 用于关联 REQMOD Request/Response |

> 说明：UDG 暴露的 OM Portal 跟踪消息类型为 **EMS ICAP**，可在跟踪中看到 REQMOD Request 与 Response 的完整内容（见 §6.1 步骤 6）。

#### 3.3.2 ICAP REQMOD 应答（ICAP Server → UDG）

应答通过 **ICAP 响应状态码 + 封装的 HTTP 响应** 双通道表达动作：

| ICAP 应答内容 | 对应动作 | UDG 执行 |
|--------------|---------|---------|
| ICAP 200 + 封装 HTTP 200（原样放行） | PERMIT | 放行用户报文 |
| ICAP 200 + 封装 HTTP 403/502（错误页）| BLOCK | 丢弃/拒绝用户报文 |
| ICAP 200 + 封装 HTTP 302（Location 重定向） | REDIRECT | 将用户重定向到指定页面 |
| ICAP 204（No Content，无修改） | PERMIT（按原样转发） | 放行用户报文 |
| 应答中携带 `X-Category-ID` 等分类头 | 触发分类匹配模式 | UDG 按 CATEGORYID 在本地套餐匹配动作 |

> 说明：上述 ICAP 状态码语义为 RFC 3507 通用约定，UDG 具体实现以 ICAP Server 对接约定为准。本特性的本地动作策略在 `ADD CFTEMPLATE`（缺省动作）和 `ADD CONTCATEGBIND`（分类绑定动作）中配置，见 §4。

### 3.4 动作决策真值表（分类匹配模式 vs 直接动作模式）

下表汇总 UDG 在不同输入下的动作决策（用于厘清 **CFTEMPLATE.ACTION（缺省）与 CONTCATEGBIND.ACTION（分类绑定）的优先级关系**）：

| ICAP 应答 | 本地 CONTCATEGROUP 是否匹配 CATEGORYID | 动作来源 | 执行动作 |
|-----------|---------------------------------------|---------|---------|
| 返回 CATEGORYID | 匹配命中 | CONTCATEGBIND.ACTION | 命中分类绑定的动作（BLOCK/PERMIT/REDIRECT） |
| 返回 CATEGORYID | 未命中（无对应 CONTCATEGROUP 绑定） | CFTEMPLATE.ACTION（缺省） | 模板缺省动作（BLOCK/PERMIT/REDIRECT） |
| 直接返回动作策略（直接动作模式） | 不参与本地匹配 | ICAP Server 直接下发 | 直接执行 ICAP 返回的动作 |
| 无应答/超时/异常 | - | CFTEMPLATE.ACTION（缺省）或异常处理 | 取决于部署（参考 §6.4 故障排查） |

> 关键结论：**分类匹配模式下，CONTCATEGBIND.ACTION 优先于 CFTEMPLATE.ACTION**；CFTEMPLATE.ACTION 仅在分类未命中或 ICAP 无应答时兜底。这是 URL 过滤"轨道B独立动作机制"的核心（CFTEMPLATE.ACTION 是独立于 PCC 体系的本地动作决策入口）。

### 3.5 业务流程（端到端 ICAP 交互 + PCC 触发）

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. ICAP Server 侧部署（离线准备）                                │
│    a. 导入 URL 分类数据库                                         │
│    b. 部署用户 URL 过滤签约信息（套餐名 + 套餐内容）              │
│    c. 与运营商签约系统对接（SOAP 协议下发 或 文件批量导入）       │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. UDG 侧基础配置（激活态前置）                                  │
│    a. 打开 License 开关：SET LICENSESWITCH LKV3G5UFBF01          │
│    b. 配置 ICAP Server 互通：VPN + LOGICINF + ICAPSERVER         │
│       + ICAPSVRGRP + ICAPSVRBINDISG                              │
│    c. 配置 URL 过滤业务：CFPROFILE + CFTEMPLATE（缺省动作）       │
│       + CONTCATEGROUP/CONTCATEGBIND（分类绑定动作）              │
│    d. APN 粒度开关：SET APNCFFUNC CFSWITCHVALUE=ENABLE           │
│    e. PCC 触发链：FILTER + FLOWFILTER + RULE(POLICYTYPE=PCC)     │
│       + PCCPOLICYGRP + USERPROFILE + RULEBINDING                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. 用户上线 + 会话建立                                           │
│    用户激活成功 → UDG 按已绑定的 USERPROFILE/RULE 匹配会话        │
│    RULE.POLICYTYPE=PCC 触发 PCC 策略（含 URL 过滤）              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. 用户访问数据网络，UDG SA 解析报文                             │
│    a. HTTP/WAP：解析上行 Get/Post 报文的 URL                     │
│    b. HTTPS/QUIC：解析 SNI 或证书                                │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. UDG 构造 ICAP REQMOD Request（关键步骤）                      │
│    消息封装：REQMOD 方法 + Encapsulated 偏移声明                 │
│    携带：用户 HTTP 请求头（含 URL/Host）+ X-Subscriber-ID 等      │
│    通过 ICAP 接口（默认端口 1344）发送给 ICAP Server             │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. ICAP Server 处理                                              │
│    a. 在分类数据库中查询 URL → 获得 URL 分类 ID（Category ID）   │
│    b. 将 Category ID 与用户签约套餐匹配 → 获得对应策略            │
│       或直接返回动作策略（直接动作模式）                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. ICAP Server 返回 ICAP REQMOD Response                        │
│    a. 分类匹配模式：返回 Category ID + 套餐策略                  │
│    b. 直接动作模式：直接返回 PERMIT/BLOCK/REDIRECT 策略          │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 8. UDG 动作决策与执行（见 §3.4 真值表）                          │
│    a. 分类匹配：按 Category ID 在本地套餐匹配                    │
│       - 命中 → 执行 CONTCATEGBIND.ACTION                         │
│       - 未命中 → 执行 CFTEMPLATE.ACTION（缺省）                  │
│    b. 直接动作模式：直接执行 ICAP 返回的动作                     │
│    c. 本地 cache 命中（如开启 SET CFCACHEPARA）→ 跳过步骤 5-7    │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 9. 动作执行（访问限制三种动作的直接实现）                        │
│    - PERMIT：放行用户报文                                        │
│    - BLOCK（≈DISCARD）：丢弃/拒绝用户报文                        │
│    - REDIRECT：将用户重定向到指定页面                            │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §原理概述

### 3.6 与 PCC 的交互机制（POLICYTYPE=PCC 如何触发 URL 过滤）

URL 过滤业务流通过 **PCC 策略体系**（轨道A：三四层匹配）触发生效，但**动作决策本身在 CFTEMPLATE/CONTCATEGBIND 中独立完成**（轨道B：URL 内容匹配）。双轨道协同：

```
              【轨道A：三四层匹配，PCC体系】
                    ↓
  ADD FILTER(L34PROTOCOL=ANY) → ADD FLOWFILTER → ADD FLTBINDFLOWF
                    ↓
  ADD RULE(POLICYTYPE=PCC, FLOWFILTERNAME=..., POLICYNAME=PCC策略组)
                    ↓
  ADD PCCPOLICYGRP → ADD USERPROFILE → ADD RULEBINDING
                    ↓
        会话命中 RULE → 触发 URL 过滤业务
                    ↓
═══════════════════════════════════════════════════════
                    ↓
              【轨道B：URL内容匹配，独立动作】
                    ↓
  UDG 解析 URL → ICAP REQMOD → ICAP Server 返回分类/动作
                    ↓
  CFTEMPLATE.ACTION（缺省）vs CONTCATEGBIND.ACTION（分类绑定）
                    ↓
  执行 PERMIT / BLOCK / REDIRECT
```

**APN 粒度开关机制**：通过 `SET APNCFFUNC:APNNAME=...,CFSWITCHVALUE=ENABLE` 为指定 APN 开启 URL 过滤；通过 `SET APNCFTEMPLATE` 为 APN 绑定内容过滤模板。也可通过 `SET GLBCFFUNC` 配置全局开关（参考信息列出）。

### 3.7 本地缓存机制（SET CFCACHEPARA）

为减少与 ICAP Server 的大量交互开销，UDG 支持本地 cache：

- 通过 `SET CFCACHEPARA:CACHEIDLETIME=7200,CACHESW=ENABLE` 开启
- 缓存 URL 到 Category ID（或动作）的映射
- `CACHEIDLETIME` 控制缓存过期时间（秒）
- 命中 cache 时跳过 ICAP REQMOD 交互（流程图步骤 5-7），直接用缓存结果决策

> SourcePath: `配置URL过滤_47348205.md` §操作步骤4

---

## 4. 配置

### 4.1 配置对象总览

本特性配置分为两大块：**ICAP Server 互通配置** 和 **URL 过滤业务配置**。

#### 4.1.1 ICAP Server 互通配置对象

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| VPNINST | vpn-gcfif | VPN 实例（ICAP 互通专网） | ADD VPNINST |
| LOGICINF | gcfif1/0/0 | UDG 与 ICAP Server 间逻辑接口 | ADD LOGICINF |
| ICAPSERVER | icapserver1 | ICAP 服务器（URL_FILTERING 类型） | ADD ICAPSERVER |
| ICAPLOCALINFO | （本端信息） | UDG 与 ICAP Server 间逻辑接口相关标识信息 | ADD ICAPLOCALINFO |
| ICAPSVRGRP | icapsvrgrp1 | ICAP 服务器组 | ADD ICAPSVRGRP |
| ICAPSVRBINDISG | （绑定关系） | ICAP 服务器与服务组的绑定 | ADD ICAPSVRBINDISG |

#### 4.1.2 URL 过滤业务配置对象

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| APN | apn-test | URL 过滤用户使用的 APN | ADD APN |
| APNCFFUNC | （APN 开关） | 基于 APN 粒度开启 URL 过滤功能 | SET APNCFFUNC |
| CFPROFILE | cf1 | 内容过滤策略 | ADD CFPROFILE |
| CFTEMPLATE | icaptemplate | 内容过滤模板（绑定 ICAP Server 组 + 缺省动作） | ADD CFTEMPLATE |
| APNCFTEMPLATE | （绑定关系） | APN 与内容过滤模板绑定 | SET APNCFTEMPLATE |
| CFPROFBINDCFT | （绑定关系） | 内容过滤策略与模板绑定 | ADD CFPROFBINDCFT |
| CONTCATEGROUP | ccgp1 | 内容分类组（CATEGORYTYPE=SPECIFIC, CATEGORYID） | ADD CONTCATEGROUP |
| CONTCATEGBIND | （绑定关系） | 内容过滤策略与分类组绑定（含动作） | ADD CONTCATEGBIND |
| CFCACHEPARA | （缓存参数） | 本地缓存过期时间、缓存开关 | SET CFCACHEPARA |
| FILTER | filter_test | URL 过滤使用的三四层过滤条件 | ADD FILTER |
| FLOWFILTER | flowfilter_test1 | 流过滤器 | ADD FLOWFILTER |
| FLTBINDFLOWF | （绑定关系） | Filter 与 FlowFilter 绑定 | ADD FLTBINDFLOWF |
| URR | urr_2 | 使用量上报规则 | ADD URR |
| URRGROUP | urrgroup1 | URR 组 | ADD URRGROUP |
| PCCPOLICYGRP | ppg_test | PCC 策略组 | ADD PCCPOLICYGRP |
| RULE | rule_test | 业务规则（POLICYTYPE=PCC） | ADD RULE |
| USERPROFILE | up_test | 用户模板 | ADD USERPROFILE |
| RULEBINDING | （绑定关系） | UserProfile 与 Rule 绑定 | ADD RULEBINDING |

> SourcePath: `配置到ICAP Server的互通数据_75400117.md` §数据
> SourcePath: `配置URL过滤_47348205.md` §数据

### 4.2 配置流程

#### 4.2.1 配置 ICAP Server 互通数据（前置）

```
1. 添加 VPN 实例
   ADD VPNINST

2. 配置 UDG 与 ICAP Server 间逻辑接口
   ADD LOGICINF（绑定 VPN）

3. 配置 ICAP Server 信息
   a. ADD ICAPSERVER（ICAPSERVERTYPE=URL_FILTERING）
   b. ADD ICAPLOCALINFO（配置 User Agent）

4. 配置 ICAP 服务器组
   ADD ICAPSVRGRP（ICAPSERVERTYPE=URL_FILTERING）

5. 配置 ICAP 服务器绑定关系
   ADD ICAPSVRBINDISG（将 ICAPSERVER 绑定到 ICAPSVRGRP）
```

#### 4.2.2 配置 URL 过滤业务

```
1. 打开 License 开关
   SET LICENSESWITCH

2. 配置 URL 过滤用户使用的 APN
   a. ADD APN
   b. SET APNCFFUNC（基于 APN 粒度开启 URL 过滤功能 CFSWITCHVALUE=ENABLE）

3. 配置 URL 过滤策略
   a. ADD CFPROFILE（内容过滤策略）
   b. ADD CFTEMPLATE（内容过滤模板，绑定 ICAP Server 组 + 缺省动作 ACTION=BLOCK）
   c. SET APNCFTEMPLATE（绑定 APN 与模板）
   d. ADD CFPROFBINDCFT（绑定策略与模板）
   e. ADD CONTCATEGROUP（内容分类组，CATEGORYTYPE=SPECIFIC + CATEGORYID）
   f. ADD CONTCATEGBIND（绑定策略与分类组，含 ACTION）

4. 开启本地 cache 功能
   SET CFCACHEPARA（CACHEIDLETIME + CACHESW=ENABLE）

5. 配置 URL 过滤条件
   a. ADD FILTER（L34PROTOCOL=ANY）
   b. SET REFRESHSRV（将 Filter 置为生效）

6. 配置流过滤器，绑定过滤条件
   a. ADD FLOWFILTER
   b. ADD FLTBINDFLOWF

7. 配置计费属性
   a. ADD URR
   b. ADD URRGROUP

8. 配置 PCC 策略
   ADD PCCPOLICYGRP（绑定 URRGROUP）

9. 配置业务规则
   ADD RULE（POLICYTYPE=PCC）

10. 配置业务策略组合
    a. ADD USERPROFILE
    b. ADD RULEBINDING
```

> SourcePath: `配置到ICAP Server的互通数据_75400117.md` §操作步骤
> SourcePath: `配置URL过滤_47348205.md` §操作步骤

### 4.3 关键 MML 命令列表

#### 4.3.1 ICAP 互通相关命令

| 命令 | 用途 |
|------|------|
| ADD VPNINST | 增加 VPN 实例 |
| ADD LOGICINF | 增加逻辑接口 |
| ADD ICAPSERVER | 增加 ICAP 服务器 |
| ADD ICAPLOCALINFO | 增加 ICAP 本端信息 |
| ADD ICAPSVRGRP | 增加 ICAP 服务器组 |
| ADD ICAPSVRBINDISG | 增加 ICAP 服务器绑定关系 |

#### 4.3.2 URL 过滤业务相关命令

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开 License 开关 |
| ADD APN | 添加 APN 配置 |
| SET APNCFFUNC | 设置 APN 内容过滤开关 |
| ADD CFPROFILE | 增加内容过滤策略 |
| ADD CFTEMPLATE | 增加内容过滤模板（绑定 ICAP 组 + 缺省动作） |
| SET APNCFTEMPLATE | 设置 APN 内容过滤模板 |
| ADD CFPROFBINDCFT | 增加内容过滤策略绑定关系 |
| ADD CONTCATEGROUP | 增加内容分类组 |
| ADD CONTCATEGBIND | 增加内容分类组绑定关系 |
| SET CFCACHEPARA | 设置内容过滤缓存参数 |
| ADD FILTER | 增加三四层过滤器 |
| SET REFRESHSRV | 业务刷新（Filter 生效） |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| ADD URR / ADD URRGROUP | 配置计费属性 |
| ADD PCCPOLICYGRP | 增加 PCC 策略组 |
| ADD RULE | 增加业务规则（POLICYTYPE=PCC） |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加 UserProfile 与 Rule 绑定 |

#### 4.3.3 辅助配置命令（参考信息列出，多场景变体使用）

| 命令 | 用途 |
|------|------|
| SET GLBCFFUNC | 设置内容过滤全局开关（全局粒度变体） |
| ADD GLBCFTEMPLATE | 增加全局内容过滤模板（全局粒度变体） |
| SET CFPROTOCOLLST | 设置开启内容过滤的协议列表 |
| ADD CFWHITEURLLST | 增加 URL 过滤白名单列表（白名单变体） |
| SET CFSRVMODE | 配置 URL 过滤业务模式 |
| ADD CFIPWHITELIST | 增加内容过滤 IP 白名单 |
| ADD CFPFSPECACTION | 增加指定内容过滤策略特殊场景下的业务动作 |

> SourcePath: `GWFD-110471 URL过滤基本功能参考信息_56449901.md` §命令

### 4.4 关键参数说明

#### 4.4.1 ADD ICAPSERVER 参数

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| ICAPSERVERNAME | icapserver1 | ICAP 服务器名称 |
| ICAPSERVERTYPE | URL_FILTERING | ICAP 服务器类型（固定为 URL_FILTERING） |
| ICAPSVRIPTYPE | IPV4 | ICAP 服务器 IP 地址类型 |
| ICAPSERVERIPV4 | 172.16.39.136 | ICAP 服务器 IPv4 地址 |
| VPNINSTANCE | vpn-gcfif | VPN 实例名称（需与 LOGICINF 中一致） |

#### 4.4.2 ADD CFTEMPLATE 参数（URL 过滤模板核心 - 缺省动作）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| CFTEMPLATENAME | icaptemplate | 内容过滤模板名称 |
| ICAPSRVGMNAME | icapsvrgrp1 | 主用 CONTENT_FILTERING 类型的 ICAP 服务器组名称 |
| ACTION | BLOCK | **缺省动作**（BLOCK/PERMIT/REDIRECT）；分类未命中或 ICAP 无应答时兜底 |

#### 4.4.3 SET APNCFFUNC 参数（APN 粒度开关）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| APNNAME | apn-test | APN 名称 |
| CFSWITCHVALUE | ENABLE | 内容过滤功能开关（ENABLE/DISABLE） |

#### 4.4.4 ADD CONTCATEGROUP 参数（内容分类组）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| CONTCATEGNAME | ccgp1 | 内容分类组名称 |
| CATEGORYTYPE | SPECIFIC | 内容分类类型（SPECIFIC 等） |
| CATEGORYID | 1 | 内容分类值（对应 ICAP Server 返回的 URL 分类 ID） |

#### 4.4.5 ADD CONTCATEGBIND 参数（分类与策略绑定 + 动作，优先于缺省）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| CFPROFILENAME | cf1 | 内容过滤策略名称 |
| CONTCATEGNAME | ccgp1 | 内容分类组名称 |
| ACTION | BLOCK | **分类绑定动作（BLOCK/PERMIT/REDIRECT），优先级高于 CFTEMPLATE.ACTION 缺省** |

#### 4.4.6 SET CFCACHEPARA 参数（本地缓存）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| CACHEIDLETIME | 7200 | 本地缓存过期时间（秒） |
| CACHESW | ENABLE | 缓存开关（ENABLE/DISABLE） |

#### 4.4.7 ADD RULE 参数（PCC 触发）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| RULENAME | rule_test | 规则名称 |
| POLICYTYPE | PCC | **策略类型=PCC 触发 URL 过滤业务** |
| FILTERINGMODE | FLOWFILTER | 流过滤器或流过滤器组选择（FLOWFILTER / FLOWFILTERGRP） |
| FLOWFILTERNAME | flowfilter_test1 | 流过滤器名称 |
| PRIORITY | 1 | 全局优先级 |
| POLICYNAME | ppg_test | 策略名称（PCC 策略组名） |

> SourcePath: `配置到ICAP Server的互通数据_75400117.md` §数据
> SourcePath: `配置URL过滤_47348205.md` §数据

### 4.5 软参

| 软参 | 说明 |
|------|------|
| BIT1940 | 控制 UPF 对 HTTP 业务是否只进行一次内容过滤策略查询 |
| BYTE1104 | 控制内容过滤 URL 匹配相关功能 |
| DWORD130 | 控制 ICAP 链路的 Keepalive 功能 |
| DWORD152 | 用于控制每个 ICAP POD 每秒向 ICAP Server 发送 REQMOD Request 消息数量最大值 |

> SourcePath: `GWFD-110471 URL过滤基本功能参考信息_56449901.md` §软参

---

## 5. 配置案例

### 5.1 场景一：ICAP Server 互通基础配置（前置，所有场景共用）

**场景描述**：部署 UDG 与 ICAP Server 的互通数据，作为所有 URL 过滤业务场景的前置。

**MML命令序列（原样保留产品文档）**：

```
// 添加 VPN 实例。
ADD VPNINST:VPNINSTANCE="vpn-gcfif";

// 配置 UDG 与 ICAP Server 间逻辑接口。
ADD LOGICINF:NAME="gcfif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="192.168.1.1",IPV4MASK1="255.255.255.255",VPNINSTANCE="vpn-gcfif";

// 配置 ICAP Server 信息。
ADD ICAPSERVER:ICAPSERVERNAME="icapserver1",ICAPSERVERTYPE=URL_FILTERING,ICAPSVRIPTYPE=IPV4,ICAPSERVERIPV4="172.16.39.136",VPNINSTANCE="vpn-gcfif";
ADD ICAPLOCALINFO:ICAPSERVERTYPE=URL_FILTERING,USERAGENT="test";

// 配置 ICAP 服务器组。
ADD ICAPSVRGRP:ICAPSVRGRPNAME="icapsvrgrp1",ICAPSERVERTYPE=URL_FILTERING;

// 配置 ICAP 服务器绑定关系。
ADD ICAPSVRBINDISG:ICAPSVRGRPNAME="icapsvrgrp1",ICAPSERVERNAME="icapserver1";
```

> 来源：`配置到ICAP Server的互通数据_75400117.md` §任务示例

### 5.2 场景二：分类匹配模式（APN 粒度，BLOCK 缺省 + 分类绑定）

**场景描述**：对指定 APN 下用户开启 URL 过滤功能。采用分类匹配模式：ICAP Server 返回 URL 分类 ID，UDG 按本地内容分类组匹配动作（分类 1 = BLOCK）；分类未命中时使用 CFTEMPLATE 缺省动作（BLOCK）。同时配置本地 cache（7200秒）减少 ICAP 交互。

**MML命令序列（原样保留产品文档任务示例）**：

```
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5UFBF01",SWITCH=ENABLE;

// 配置 URL 过滤用户使用的 APN（并基于 APN 粒度开启 URL 过滤）。
ADD APN:APN="apn-test";
SET APNCFFUNC:APNNAME="apn-test",CFSWITCHVALUE=ENABLE;

// 配置 URL 过滤策略。
ADD CFPROFILE:CFPROFILENAME="cf1";
ADD CFTEMPLATE:CFTEMPLATENAME="icaptemplate",ICAPSRVGMNAME="icapsvrgrp1",ACTION=BLOCK;
SET APNCFTEMPLATE:APNNAME="apn-test",CFTEMPLATENAME="icaptemplate";
ADD CFPROFBINDCFT:CFTEMPLATENAME="icaptemplate",CFPROFILENAME="cf1";

// 配置内容分类组（指定 URL 分类 ID=1）与策略绑定。
ADD CONTCATEGROUP:CONTCATEGNAME="ccgp1",CATEGORYTYPE=SPECIFIC,CATEGORYID=1;
ADD CONTCATEGBIND:CFPROFILENAME="cf1",CONTCATEGNAME="ccgp1",ACTION=BLOCK;

// 开启本地 cache 功能。
SET CFCACHEPARA:CACHEIDLETIME=7200,CACHESW=ENABLE;

// 配置 URL 过滤条件。
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 配置流过滤器，绑定过滤条件。
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test1",FILTERNAME="filter_test";

// 配置计费属性。
ADD URR:URRNAME="urr_2",URRID=2,USAGERPTMODE=OFFLINE;
ADD URRGROUP:URRGROUPNAME="urrgroup1",UPURRNAME1="urr_2",DOWNURRNAME1="urr_2";

// 配置 PCC 策略。
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="ppg_test",URRGROUPNAME="urrgroup1";

// 配置业务规则（POLICYTYPE=PCC 触发 URL 过滤）。
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_test1",PRIORITY=1,POLICYNAME="ppg_test";

// 配置业务策略组合。
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

> 来源：`配置URL过滤_47348205.md` §任务示例

### 5.3 场景三：直接动作模式变体（ICAP Server 直接返回动作）

**场景描述**：采用直接动作模式 —— ICAP Server 直接返回 URL 关联的动作策略，UDG 直接执行。与场景二的差异：**不再需要本地内容分类组配置**（CONTCATEGROUP/CONTCATEGBIND 可省略），UDG 仅按 CFTEMPLATE 缺省动作兜底。

**MML命令序列（相对场景二的差异部分）**：

```
// 打开本特性的 License 配置开关（同场景二）。
SET LICENSESWITCH:LICITEM="LKV3G5UFBF01",SWITCH=ENABLE;

// 配置 URL 过滤用户使用的 APN + 模板（缺省动作 PERMIT 作为兜底）。
ADD APN:APN="apn-test";
SET APNCFFUNC:APNNAME="apn-test",CFSWITCHVALUE=ENABLE;

ADD CFPROFILE:CFPROFILENAME="cf1";
// 直接动作模式下，CFTEMPLATE.ACTION 作为 ICAP 无应答时的兜底（此处 PERMIT 兜底）。
ADD CFTEMPLATE:CFTEMPLATENAME="icaptemplate",ICAPSRVGMNAME="icapsvrgrp1",ACTION=PERMIT;
SET APNCFTEMPLATE:APNNAME="apn-test",CFTEMPLATENAME="icaptemplate";
ADD CFPROFBINDCFT:CFTEMPLATENAME="icaptemplate",CFPROFILENAME="cf1";

// 【直接动作模式省略本地分类组配置】
// 不配置 CONTCATEGROUP / CONTCATEGBIND，UDG 按 ICAP Server 返回的动作直接执行。

// 其余 FILTER / FLOWFILTER / RULE / USERPROFILE 等同场景二（略）。
```

> 说明：直接动作模式的本质是动作决策完全由 ICAP Server 主导，UDG 退化为"执行器"。CFTEMPLATE.ACTION 在此模式下仅在 ICAP 无应答/异常时起兜底作用。
> 来源：基于 `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §可获得性（直接动作模式描述）+ 场景二配置裁剪。

### 5.4 场景四：HTTPS SNI 场景变体（需 HTTP2.0 Host 识别）

**场景描述**：对 HTTPS 协议类型的报文进行 URL 过滤。UDG 只能解析 SNI 或证书上报给 ICAP Server（无法解析完整 URL），需额外启用 GWFD-110201 HTTP2.0 Host 识别特性。

**前置 License（HTTPS 解析依赖）**：
```
// 启用 HTTP2.0 Host 识别 License（HTTPS URL 过滤必需）。
SET LICENSESWITCH:LICITEM="LKV3G5HSHA01",SWITCH=ENABLE;
```

**业务配置差异**：HTTPS 场景下 ICAP REQMOD 携带的是 SNI 而非完整 URL，ICAP Server 侧需配置按 SNI 匹配的分类规则。UDG 侧的 CFTEMPLATE / CONTCATEGROUP 配置与场景二一致（ICAP Server 返回的 CATEGORYID 仍由本地套餐匹配）。

> 来源：`GWFD-110471 URL过滤基本功能特性概述_56369529.md` §与其他特性的交互（GWFD-110201 依赖）+ §应用限制（HTTPS 仅解析 SNI）

### 5.5 场景五：白名单变体（CFWHITEURLLST / CFIPWHITELIST）

**场景描述**：对免过滤的 URL 或 IP 加入白名单，跳过 ICAP 交互直接放行。适用于运营商自营业务或可信站点的豁免场景。

**MML命令序列（白名单增量配置）**：

```
// 增加 URL 过滤白名单列表（匹配的 URL 直接放行，不走 ICAP）。
ADD CFWHITEURLLST:PROFILENAME="cf1",URL="www.operator.com/*";

// 增加内容过滤 IP 白名单（匹配的 IP 直接放行）。
ADD CFIPWHITELIST:IPADDRESS="10.10.10.1",MASK="255.255.255.255";

// 设置开启内容过滤的协议列表（限定 URL 过滤生效的协议范围）。
SET CFPROTOCOLLST:PROTOCOLLIST="HTTP,HTTPS,WAP1.X,WAP2.0";
```

> 来源：`GWFD-110471 URL过滤基本功能参考信息_56449901.md` §命令（辅助配置命令列表）

### 5.6 场景六：全局粒度变体（SET GLBCFFUNC + ADD GLBCFTEMPLATE）

**场景描述**：与场景二的 APN 粒度开关不同，本场景在全局粒度开启 URL 过滤，所有 APN 生效。适用于全网上网行为管理的统一策略。

**MML命令序列（全局粒度差异部分）**：

```
// 全局内容过滤开关（替代 SET APNCFFUNC）。
SET GLBCFFUNC:CFSWITCHVALUE=ENABLE;

// 全局内容过滤模板（替代 SET APNCFTEMPLATE）。
ADD GLBCFTEMPLATE:CFTEMPLATENAME="icaptemplate";
```

> 来源：`GWFD-110471 URL过滤基本功能参考信息_56449901.md` §命令（SET GLBCFFUNC / ADD GLBCFTEMPLATE）

### 5.7 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| 分类匹配模式（场景二） | ADD CONTCATEGROUP + ADD CONTCATEGBIND | CATEGORYID + ACTION | ICAP 返回分类 ID，UDG 本地匹配动作（主流） |
| 直接动作模式（场景三） | （省略 CONTCATEGROUP/CONTCATEGBIND） | CFTEMPLATE.ACTION 仅兜底 | ICAP Server 直接下发动作，UDG 退化为执行器 |
| HTTPS SNI（场景四） | SET LICENSESWITCH LKV3G5HSHA01 | 启用 HTTP2.0 Host 识别 | HTTPS 流量，仅解析 SNI/证书 |
| 白名单（场景五） | ADD CFWHITEURLLST / ADD CFIPWHITELIST | URL / IPADDRESS | 免过滤豁免 |
| 全局粒度（场景六） | SET GLBCFFUNC / ADD GLBCFTEMPLATE | 全局开关 | 全网统一策略，所有 APN 生效 |
| ICAP 主备部署 | 多次 ADD ICAPSERVER + ADD ICAPSVRBINDISG | 同一 ICAPSVRGRP | ICAP Server 高可用 |
| 本地 cache（场景二已含） | SET CFCACHEPARA | CACHEIDLETIME + CACHESW=ENABLE | 减少 ICAP 交互，降低时延 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商完成部署 URL 过滤基本功能后，需对本功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户跟踪任务 | 用户IMSI号（IMSI） | 460000123456789 | 测试终端自带 |
| 测试终端使用的APN | APN名称（APN） | apn-test | 已配置数据中获取（可用 `LST APN` 查询） |

工具：测试终端、OM Portal

> SourcePath: `调测URL过滤基本功能_56249725.md` §必备事项

#### 6.1.3 调测执行步骤

**步骤1**：执行 `DSP ICAPSVRSTATUS` 命令，查看 ICAP Server 的状态是否正常。

```
DSP ICAPSVRSTATUS:ICAPSVRGRPNAME="icapsvrgrp1";
```

预期输出（正常，示例）：
```
-------------------------------
  ICAP Server Group Name  =  icapsvrgrp1
  ICAP Server Name        =  icapserver1
  ICAP Server Type        =  URL_FILTERING
  ICAP Server IP          =  172.16.39.136
  ICAP Server Status      =  NORMAL
  Link Status             =  CONNECTED
-------------------------------
(Number of results = 1)
---    END
```

判断：
- ICAP Server Status=NORMAL → 步骤2
- 异常 → 参考"配置到 ICAP Server 的互通数据"重新配置

**步骤2**：执行 `LST LICENSESWITCH` 查询 License 开关。

```
LST LICENSESWITCH:LICITEM="LKV3G5UFBF01";
```

预期输出：
```
-------------------------------
  License Item  =  LKV3G5UFBF01
  Switch        =  ENABLE
-------------------------------
---    END
```

判断：
- SWITCH=ENABLE → 步骤3
- SWITCH=DISABLE → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5UFBF01",SWITCH=ENABLE;` 打开开关

**步骤3**：在 OM Portal 上创建 UDG 用户跟踪任务，"参数配置"栏输入用户 IMSI（460000123456789），"消息类型"栏选择 **EMS ICAP、PFCP** 消息类型。

**步骤4**：测试终端使用 `apn-test` APN 接入网络。
- 成功接入 → 步骤5
- 无法接入 → 调测 UDG 的接入功能

**步骤5**：测试终端浏览 Web 业务，访问 `www.huawei.com/*` 网页。
- 可以正常访问网页 → 步骤6
- 无法正常访问网页 → 调测 UDG 的 Web 浏览功能

**步骤6**：查看 UDG 用户跟踪中的 **EMS ICAP 消息**，检查 UDG 是否能将用户访问的 URL 信息发送给 ICAP Server。
- EMS ICAP 消息中携带用户访问的 URL 信息（REQMOD Request 可见 URL）→ 步骤7
- EMS ICAP 消息中未携带 URL 信息 → 在 UDG 上重新配置 URL 过滤信息后重新执行步骤3

**步骤7**：在 ICAP Server 上检查 URL 对应的 **Category ID** 与规划是否一致。
- 一致 → 步骤8
- 不一致 → 在 ICAP Server 上重新配置 URL 过滤信息后重新执行步骤3

**步骤8**：执行 `LST CONTCATEGROUP` 查询内容分类组信息是否与规划值一致。

```
LST CONTCATEGROUP:CONTCATEGNAME="ccgp1";
```

预期输出：
```
-------------------------------
  Content Category Group Name  =  ccgp1
  Category Type                =  SPECIFIC
  Category ID                  =  1
-------------------------------
---    END
```

判断：
- 与规划值一致 → 调测结束
- 不一致 → 步骤9

**步骤9**：收集信息并寻求技术支持。
- a. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- b. 收集并保存上述所有查询信息
- c. 收集归纳所有信息并联系华为技术支持解决

> SourcePath: `调测URL过滤基本功能_56249725.md` §操作步骤
> 说明：预期输出样例为参照标杆 §6.1.3 格式补充（产品文档未给出具体输出文本），字段名依据命令语义推断，实际以设备返回为准。

### 6.2 验证命令汇总

| 命令 | 用途 |
|------|------|
| DSP ICAPSVRSTATUS | 查询 ICAP Server 状态 |
| LST LICENSESWITCH | 查询 License 开关状态 |
| LST CONTCATEGROUP | 查询内容分类组信息 |
| LST APN | 查询 APN 配置 |
| LST FILTER / LST FLOWFILTER | 查询过滤器/流过滤器配置 |
| LST RULE | 查询业务规则 |
| EXP MML | 导出 MML 配置脚本（用于故障信息收集） |

> SourcePath: `调测URL过滤基本功能_56249725.md`

### 6.3 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-81240 | ICAP 服务异常 | ICAP Server 链路异常、响应失败或断连 | URL 过滤动作无法获取，按 CFTEMPLATE 缺省动作兜底，可能误放行或误阻塞 |

> SourcePath: `GWFD-110471 URL过滤基本功能参考信息_56449901.md` §告警

### 6.4 测量指标

URL 过滤测量指标涵盖**会话**与 **ICAP 链路**两个维度：

| 维度 | 指标ID | 指标名称 |
|------|--------|---------|
| 会话（整机） | 1914331508 | 用户平面最大的 URL 过滤会话数目 |
| 会话（整机） | 1914331509 | 用户平面平均 URL 过滤会话数目 |
| 会话（整机） | 1914331510 | 用户平面当前在线 URL 过滤会话数目 |
| 会话（POD粒度） | 1914331511 | 用户平面指定 POD 的最大的 URL 过滤会话数目 |
| 会话（POD粒度） | 1914331512 | 用户平面指定 POD 的平均 URL 过滤会话数目 |
| 会话（POD粒度） | 1914331513 | 用户平面指定 POD 的当前在线 URL 过滤会话数目 |
| ICAP 链路 | 1914331514 | 用户平面 URL 过滤 ICAP 链路断开次数 |
| ICAP 链路 | 1914331519 | 用户平面 URL 过滤发送 REQMOD Request 消息次数 |
| ICAP 链路 | 1914331520 | 用户平面 URL 过滤接收 REQMOD Response 成功响应消息次数 |
| ICAP 链路 | 1914331521 | 用户平面 URL 过滤接收 REQMOD Response 失败响应消息次数 |
| ICAP 链路 | 1914331522 | 用户平面 URL 过滤接收 REQMOD Response 响应超时次数 |

> 关键监控指标：1914331521（失败响应次数）+ 1914331522（响应超时次数）异常升高 → 提示 ICAP Server 侧故障；1914331514（链路断开次数）>0 → 触发 ALM-81240。
> SourcePath: `GWFD-110471 URL过滤基本功能参考信息_56449901.md` §测量指标

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 用户访问未被过滤（应 BLOCK 却放行） | License 开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5UFBF01";` 确认 SWITCH=ENABLE |
| 用户访问未被过滤 | APN 粒度开关未开启或 APN 名不匹配 | `LST APN` 确认 APN；`LST APNCFFUNC` 确认 CFSWITCHVALUE=ENABLE 且 APNNAME 与 ADD APN 一致 |
| EMS ICAP 跟踪无 REQMOD 消息 | SA 解析未生效（SA-Basic/SA-Web Browsing 等 License 未开） | 检查 SA 协议族依赖 License（见 §1.7）；按协议类型启用对应 SA 特性 |
| EMS ICAP 跟踪有 REQMOD 但无 Response | ICAP Server 异常或链路断开 | `DSP ICAPSVRSTATUS` 查状态；查 ALM-81240；查指标 1914331514（断开次数）/1914331522（超时次数） |
| 动作与预期不符（应 PERMIT 却 BLOCK） | CFTEMPLATE.ACTION 缺省动作设置与预期相反 | `LST CFTEMPLATE` 确认 ACTION；区分分类匹配模式（CONTCATEGBIND.ACTION 优先）与直接动作模式 |
| 分类匹配模式下分类 ID 未命中 | ICAP Server 返回的 Category ID 与本地 CONTCATEGROUP.CATEGORYID 不一致 | 步骤7 在 ICAP Server 侧核对 Category ID；`LST CONTCATEGROUP` 核对本地 CATEGORYID |
| HTTPS 流量 URL 过滤不生效 | 未启用 HTTP2.0 Host 识别（GWFD-110201） | `LST LICENSESWITCH:LICITEM="LKV3G5HSHA01";` 确认 ENABLE；HTTPS 仅能解析 SNI，需 ICAP Server 支持按 SNI 匹配 |
| 用户上网 Get 首包时延明显增大 | URL 过滤使能导致报文缓存等待动作匹配 | 产品文档声明：这是预期行为；开启本地 cache（`SET CFCACHEPARA CACHESW=ENABLE`）可缓解；软参 DWORD152 控制 REQMOD 速率 |
| UDG CPU 占用高 | 每次上网业务与 ICAP Server 大量交互 | 开启本地 cache；检查指标 1914331519（REQMOD 发送次数）；评估 ICAP Server 处理能力 |
| 丢包 | ICAP 响应前 UDG 缓存超限 | 产品文档声明：等待 ICAP 响应期间缓存超限会丢包；优化 ICAP Server 响应时延；检查 DWORD152 速率控制 |
| PCC 触发链未生效 | RULE.POLICYTYPE 不是 PCC，或 FLOWFILTER 未绑定 FILTER | `LST RULE` 确认 POLICYTYPE=PCC、FLOWFILTERNAME、POLICYNAME；`LST FLTBINDFLOWF` 确认绑定；确认 SET REFRESHSRV 已执行 |
| 白名单不生效 | CFWHITEURLLST 或 CFIPWHITELIST 配置错误 | `LST CFWHITEURLLST` / `LST CFIPWHITELIST` 核对 URL/IP；确认 URL 通配符格式 |

---

## 7. 参考信息

### 7.1 与其他特性的关系（特性关系网）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG 解析 URL 的基础，必须开启 |
| SA-Web Browsing | GWFD-110103（UDG） | **协议依赖**：HTTP、WAP2.0 协议解析必需 |
| SA-Mobile | GWFD-110105（UDG） | **协议依赖**：WAP1.X 协议解析必需 |
| HTTP2.0 Host 识别 | GWFD-110201（UDG） | **协议依赖**：HTTPS 协议解析（SNI）必需 |
| PCC 基本功能 | GWFD-020351（UDG） | **触发依赖**：RULE.POLICYTYPE=PCC 触发 URL 过滤业务链 |
| HTTP 智能重定向 | GWFD-110284（UDG） | **互补关系**：URL 过滤返回 REDIRECT 动作时，重定向执行机制与 HTTP 智能重定向同源 |
| DNS 纠错 | GWFD-110283（UDG） | **互补关系**：DNS 层重定向变体，与 URL 过滤 REDIRECT 共同构成访问限制"重定向族" |
| HTTP 头增强 | GWFD-110261/262/263（UDG） | **配合关系**：URL 过滤本身不做头增强，可配合头增强特性实现 REDIRECT 携带用户信息 |
| 用户 Portal | GWFD-110281（UDG） | **互补关系**：URL 过滤 REDIRECT 目标可为 Portal 页面 |
| Web Proxy | GWFD-110282（UDG） | **互补关系**：L3 IP NAT 重定向变体，与 URL 过滤 REDIRECT 同属访问限制"重定向族" |

> 说明：GWFD-110284/110283/110281/110282 的互补关系系基于访问限制场景动作语义（DISCARD/HEADEN/REDIRECT）推断（feature-doc-list §D/§E 分组），产品文档未直接交叉引用。
> SourcePath: `GWFD-110471 URL过滤基本功能特性概述_56369529.md` §与其他特性的交互

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/GWFD-110471 URL过滤基本功能特性概述_56369529.md` | 适用NF、定义、法律声明、客户价值、应用场景（政府/企业/恶意网页屏蔽）、可获得性（UDG 20.10.2+、License LKV3G5UFBF01、两种动作匹配模式）、与其他特性交互（SA族+PCC 5项依赖）、对系统影响（CPU/时延/丢包）、应用限制（协议+解析方式）、原理概述（7步ICAP流程）、特性规格（500套餐/30 ICAP/10每组/150万URL）、遵循标准（RFC 3507）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/GWFD-110471 URL过滤基本功能参考信息_56449901.md` | MML命令清单（24条核心+辅助）、告警（ALM-81240）、软参（BIT1940/BYTE1104/DWORD130/DWORD152）、测量指标（11条，会话+ICAP链路两维度） |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/激活URL过滤基本功能/配置URL过滤_47348205.md` | 10步操作流程、数据规划表、完整MML脚本（License+APN+CFPROFILE+CFTEMPLATE+APNCFTEMPLATE+CFPROFBINDCFT+CONTCATEGROUP+CONTCATEGBIND+CFCACHEPARA+FILTER+REFRESHSRV+FLOWFILTER+FLTBINDFLOWF+URR+URRGROUP+PCCPOLICYGRP+RULE+USERPROFILE+RULEBINDING） |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/激活URL过滤基本功能/配置到ICAP Server的互通数据_75400117.md` | ICAP互通5步操作、数据规划表、MML脚本（VPNINST+LOGICINF+ICAPSERVER+ICAPLOCALINFO+ICAPSVRGRP+ICAPSVRBINDISG） |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-110471 URL过滤基本功能/调测URL过滤基本功能_56249725.md` | 9步调测流程（DSP ICAPSVRSTATUS→LST LICENSESWITCH→OM Portal跟踪→接入→Web访问→EMS ICAP消息→Category ID→LST CONTCATEGROUP→EXP MML收集） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| ICAP | Internet Content Adaptation Protocol | IETF RFC 3507，UDG 与 ICAP Server 交互的协议 |
| REQMOD | Request Modification | ICAP 方法，UDG 把用户 HTTP 请求封装上送 |
| Category ID | URL 分类 ID | ICAP Server 查询 URL 分类数据库返回的分类标识 |
| CFTEMPLATE | 内容过滤模板 | 绑定 ICAP Server 组 + 缺省动作（ACTION） |
| CONTCATEGROUP | 内容分类组 | 按 CATEGORYID 组织的分类集合 |
| CONTCATEGBIND | 内容分类组绑定 | 策略与分类组的绑定关系，指定分类绑定的动作（优先于 CFTEMPLATE 缺省） |
| CFCACHEPARA | 内容过滤缓存参数 | 本地 cache 过期时间 + 开关 |
| SNI | Server Name Indication | TLS 握手时携带的目标域名，HTTPS URL 过滤的唯一可解析信息 |
| SA | Service Awareness | 业务感知，URL 解析的基础能力 |
| EMS ICAP | （跟踪消息类型） | OM Portal 跟踪中观察 ICAP REQMOD 消息的消息类型 |

---

## 8. 文档一致性说明（配置树 vs 产品文档）

> 配置树/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | feature_group 归属 | feature-doc-list 将 GWFD-110471 归为"URL过滤"组（独有） | 产品文档路径在"业务感知功能"下，本质是"内容过滤"的 URL 过滤分支 | 一致（feature-doc-list 分组与产品路径不冲突，业务语义归 URL过滤组） |
| 2 | 动作匹配模式 | feature-doc-list 未细化子方式 | 产品文档明确 **两种动作匹配模式**：分类匹配模式（ICAP 返回分类，UDG 本地匹配）+ 直接动作模式（ICAP 直接返回动作） | 补全：实际有两种模式，影响配置（直接动作模式可省略 CONTCATEGROUP） |
| 3 | 协议依赖完整性 | feature-doc-list 提及 SA 族依赖 | 产品文档按协议细化依赖：HTTP/WAP2.0→SA-Web Browsing；WAP1.X→SA-Mobile；HTTPS→HTTP2.0 Host 识别；SA-Basic 必选 | 补全：协议依赖矩阵更细 |
| 4 | 缺省动作与分类绑定动作优先级 | 文档未明确 | 本文档基于命令语义推断：**CONTCATEGBIND.ACTION（分类绑定）优先于 CFTEMPLATE.ACTION（缺省）**；产品文档未显式声明优先级 | 推断结论（产品文档未直接声明，Stage 3 验证） |
| 5 | ICAP 端口 | 文档未提及 | 产品文档未显式给出 ICAP 端口（RFC 3507 默认 1344），需在 ICAPSERVER/LOGICINF 配置时与对端约定 | 文档未涉及，按 RFC 3507 约定 |
| 6 | 规格数量 | feature-doc-list 未列 | 产品文档明确：500 套餐 / 30 ICAP Server / 10 每组 / 150 万 URL | 补全 |
| 7 | 辅助命令完整性 | 文档清单仅列核心命令 | 参考信息还列出 SET GLBCFFUNC / ADD GLBCFTEMPLATE / SET CFPROTOCOLLST / ADD CFWHITEURLLST / SET CFSRVMODE / ADD CFIPWHITELIST / ADD CFPFSPECACTION 7 条辅助命令 | 补全：辅助命令对应多场景变体（全局粒度/白名单/协议列表/业务模式） |
| 8 | 法律声明 | 文档清单未强调 | 产品文档有完整法律声明（用户行为泄露风险、妨碍通信自由诉讼风险、华为免责条款） | 补全：法律合规要求需在部署前评估 |
| 9 | 全局开关 vs APN 开关关系 | 文档未明确 | 参考信息同时列出 SET GLBCFFUNC（全局）和 SET APNCFFUNC（APN粒度），两者关系（覆盖/叠加）产品文档未显式说明 | 推断：APN 粒度优先（类比计费场景 SET APNIPALLOCRULE 覆盖 SET IPALLOCRULE），Stage 3 验证 |
| 10 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（5 份文档 MML 脚本参数一致） | 无 |

---
