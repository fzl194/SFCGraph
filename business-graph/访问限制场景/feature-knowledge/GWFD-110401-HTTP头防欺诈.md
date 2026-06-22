# GWFD-110401 HTTP头防欺诈 知识文档

> 访问限制场景 | 防欺诈协议族（与HTTP头增强强耦合）| UDG | 来源：特性概述+实现原理+约束+激活+调测+防欺诈功能专题 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110401 |
| feature_name | HTTP头防欺诈 |
| feature_group | 防欺诈 |
| parent_feature_id | -（本特性在配置树无独立父节点；业务上归属"智能策略控制功能 → HTTP头防欺诈"分支；防欺诈协议族父概念见 `UDG防欺诈功能专题`） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["模式(插入+防欺诈双开 / 灰名单仅防欺诈不插入)", "ANTIFRAUD开关(ADD HEADEN ANTIFRAUD=ENABLE/DISABLE，内嵌于HTTP头增强命令)", "GRAYLIST开关(ADD HEADEN GRAYLIST=ENABLE 灰名单模式)", "触发方式(基于三四层特征触发 / 基于七层特征触发)", "过滤条件(FILTER三四层 vs L7FILTER URL+METHODTYPE+PROTBINDFLOWF)", "防欺诈字段类型(MSISDN/IMSI/APN/MSIP等，需为非标准HTTP头域名)", "POLICYTYPE=HEADEN（共用HTTP头增强的动作机制，RULE直接引用HEADEN对象）", "执行顺序控制(BIT1030控制防欺诈是否在头增强前执行)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110401-01, EV-FK-AC-110401-02, EV-FK-AC-110401-03, EV-FK-AC-110401-04, EV-FK-AC-110401-05]（P4建evidence-index时确定，先用占位） |
| license_required | `82209786 LKV3G5HHAS01 HTTP头防欺诈` |

---

## 1. 概述

### 1.1 特性定义（是什么）

HTTP头防欺诈是 UDG 在HTTP头增强的过程中进行**检测和修正**，保证HTTP报文头增强的内容正确，防止用户使用欺诈的头增强信息进行业务。

**核心机制（关键）**：在HTTP头增强动作执行**之前**，增加一个"判断插入字段是否正确"的动作。即在插入前，UDG 先检测用户数据报文的HTTP头中**是否已存在**需要插入的字段：

- 若**存在**该字段，进一步检查字段取值是否正确
  - 取值**正确** → 继续业务
  - 取值**不正确** → UDG 将字段修改为正确值，再继续业务（防止欺诈接入）
  - 报文中**存在多个**该字段 → 删除冗余字段，保留一个正确字段
- 若**不存在**该字段 → 执行正常的HTTP头增强动作（插入字段）

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §定义、§原理概述
> SourcePath: `HTTP头防欺诈原理_59318043.md` §HTTP头防欺诈原理

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 对用户HTTP报文头做内容增强处理时，如果报文头中已经含有增强字段，先检查字段是否正确，如果不正确，则修改为正确的值 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §适用NF

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布 |

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §发布历史

### 1.4 License

- **License控制项**：`82209786 LKV3G5HHAS01 HTTP头防欺诈`
- 必须获得 License 许可后才能使用本特性
- License开关命令：`SET LICENSESWITCH:LICITEM="LKV3G5HHAS01",SWITCH=ENABLE;`

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §License支持

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 保证HTTP头中插入的头增强内容正确，避免运营商和业务提供商根据头增强内容进行业务处理时出现错误而发生用户投诉 |
| 用户 | 避免头增强的信息错误而发生计费/业务控制失败或错误，确保用户享有正常的定制服务，用户利益没有受损 |

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §客户价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| MSISDN欺诈防护 | 某些Web服务器可接收HTTP报文头扩展字段MSISDN对用户进行标识，SP/CP基于此对用户进行费用核算及业务增强处理。实际应用中，用户访问Web业务时，**有些浏览器可插入MSISDN号码**，不管用户输入的MSISDN号码是否正确都会插入到HTTP头中。如果用户输入的MSISDN号码不正确，就会导致**计费失败，或错误计费到其他用户上**。HTTP头防欺诈特性可解决该问题 |
| 业务控制保障 | HTTP头增强通过将APN、MS IP、IMSI等用户信息插入到HTTP报文头最后的位置传递给Web Server，满足运营商业务访问认证、个性化管理与查询、广告宣传、业务推广和账户管理需求。HTTP头防欺诈通过**检测增强字段内容是否正确**，保证业务控制可以正常处理 |
| 冗余字段清理 | 未启用HTTP头防欺诈时，由于用户的HTTP报文头本身会携带一个增强字段，UDG的HTTP头增强功能又会在报文头中再插入一次该字段，导致报文头中可能存在**多个该字段**，业务控制可能失败。防欺诈特性解决此问题（删除冗余，保留一个正确字段） |

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §应用场景；`HTTP头防欺诈原理_59318043.md` §HTTP头防欺诈原理

### 1.7 前置条件与依赖（与HTTP头增强强耦合）

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | 开启本功能前，需要先识别和解析HTTP报文；SA-Basic是所有SA(Service Awareness)协议解析的基础 |
| 依赖 | GWFD-110103 SA-Web Browsing | 82209755 LKV3G5SAWB01 SA-Web Browsing | 需要识别和解析HTTP报文 |
| **强耦合依赖** | **GWFD-110261 HTTP头增强** | **82209777 LKV3G5HTHE01 HTTP头增强** | **HTTP头防欺诈特性依赖于HTTP头增强特性，启用HTTP头防欺诈功能必须开启HTTP头增强功能**；防欺诈开关内嵌于 `ADD HEADEN` 的 `ANTIFRAUD` 参数 |

> **强耦合关系核心**：HTTP头防欺诈**不独立配置策略对象**，其开关内嵌于 `ADD HEADEN` 命令的 `ANTIFRAUD` 参数。License层面 LKV3G5HHAS01（防欺诈）+ LKV3G5HTHE01（头增强）双开；配置层面共用 HEADEN 对象、RULE（POLICYTYPE=HEADEN）、FILTER/L7FILTER/FLOWFILTER。

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §与其他特性的交互

### 1.8 对系统的影响

启用HTTP头防欺诈功能**必须开启HTTP头增强功能**，当在UDG上开启HTTP头增强特性后，由于匹配到头增强动作的用户**所有报文**，UDG都需要对其进行报文的解析和HTTP头增强处理，因此：
- 系统处理负荷增加
- 报文转发性能和吞吐量将下降

详细性能影响需要基于流量模型进行评估，请联系华为技术支持获取服务。

> SourcePath: `约束限制和系统影响_13425672.md` §系统影响

### 1.9 应用限制（约束）

| # | 限制项 | 说明 |
|---|--------|------|
| 1 | 报文类型限制 | HTTP头防欺诈特性**只针对HTTP或WAP2.0上传业务（对应Post报文）、下载业务和浏览请求业务（两者对应Get报文）有效**，且根据HTTP头防欺诈的应用场景，该功能对**上行报文**处理有意义 |
| 2 | 头域类型限制 | UDG支持对**非标准HTTP头域**的增强字段进行HTTP头防欺诈。如果头增强字段配置为**HTTP标准头域名**（如 host），可能**无法做到防欺诈**。例如用户数据报文HTTP头扩展字段中使用"host"字符作为APN增强字段前缀，则UDG可能无法进行防欺诈处理 |
| 3 | 协议限制 | 本特性**只支持HTTP1.x协议，不支持HTTP2.0协议** |
| 4 | 加密场景 | 本特性**不支持加密场景下基于host的计费和控制** |

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §应用限制；`约束限制和系统影响_13425672.md` §约束限制

### 1.10 特性规格

**本特性无特殊规格**（产品文档明确声明）。

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF | 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §遵循标准

### 1.12 计费与话单

**本特性不涉及计费与话单**（产品文档明确声明）。

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §计费与话单

---

## 2. 激活（License开启命令）

> 本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关（LKV3G5HHAS01）+ HTTP头增强License（LKV3G5HTHE01）+ ADD HEADEN（ANTIFRAUD=ENABLE）+ ADD RULE(POLICYTYPE=HEADEN) + 绑定UserProfile"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5HHAS01",SWITCH=ENABLE;
```

> **强耦合说明**：同时需确保 HTTP头增强License已开：
> ```
> SET LICENSESWITCH:LICITEM="LKV3G5HTHE01",SWITCH=ENABLE;
> ```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5HHAS01";
```

> SourcePath: `激活HTTP头防欺诈_69815661.md` §任务示例

---

## 3. 原理

### 3.1 动作机制：防欺诈内嵌于 HEADEN（强耦合HTTP头增强）

**核心结论**：HTTP头防欺诈**不独立配置策略对象**，其开关内嵌于 HTTP头增强的 `ADD HEADEN` 命令的 `ANTIFRAUD` 参数。业务流通过 RULE 的 `POLICYTYPE=HEADEN` 触发（共用HTTP头增强的动作机制），在头增强插入动作执行**之前**，先执行防欺诈检测。

**与POLICYTYPE四轨道的关系**：

| POLICYTYPE | 动作对象（POLICYNAME引用） | 业务含义 | 防欺诈位置 |
|------------|--------------------------|---------|---------|
| PCC | PCCPOLICYGRP | 三四层匹配 + 计费/带宽 | — |
| **HEADEN** | HEADEN（ADD HEADEN，含ANTIFRAUD参数） | **报文头增强 + 头防欺诈** | **内嵌于HEADEN对象的ANTIFRAUD参数** |
| SMARTREDIRECT | 重定向对象 | URL/HTTP层重定向 | — |
| （URL过滤） | CFTEMPLATE / CONTCATEGBIND | URL内容过滤 | — |

> **防欺诈是HEADEN动作的增强特性**：不是独立的第5种POLICYTYPE，而是 HEADEN 动作机制的可选安全增强层（由 ANTIFRAUD=ENABLE 激活）。

> SourcePath: `激活HTTP头防欺诈_69815661.md` §表4（ADD HEADEN ANTIFRAUD=ENABLE）；`HTTP头防欺诈原理_59318043.md` §HTTP头防欺诈原理

### 3.2 HTTP头防欺诈类型（两种触发方式）

UDG 支持两种触发方式：

| 类型 | 触发条件 | 配置方式 |
|------|----------|----------|
| **基于三四层特征触发** | 业务流信息匹配 `ADD FILTER` 三四层过滤条件 | 配置 FILTER（不配置 L7FILTER/PROTBINDFLOWF），在 RULE 中配置头增强策略，`ADD HEADEN` 使能防欺诈（ANTIFRAUD=ENABLE） |
| **基于七层特征触发** | 业务流信息匹配 `ADD L7FILTER` + `ADD PROTBINDFLOWF` 七层过滤条件 | 配置 L7FILTER（URL + METHODTYPE=GET/POST）和 PROTBINDFLOWF（绑定http协议+L7FILTER），在 RULE 中配置头增强策略，`ADD HEADEN` 使能防欺诈（ANTIFRAUD=ENABLE） |

> **重要说明**：当配置了三四层或七层特征触发的HTTP头防欺诈功能，对于**非HTTP协议**的业务流，即使匹配到了规则，也**不会**进行HTTP头防欺诈处理。

> SourcePath: `HTTP头防欺诈原理_59318043.md` §HTTP头防欺诈类型

### 3.3 业务流程（防欺诈检测纠正逻辑）

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. 终端建立会话后，向Web服务器发起建立TCP连接请求                 │
│    Web服务器回应响应消息，TCP三次握手完成，成功建立连接           │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. 终端发起HTTP业务访问请求，请求报文到达UDG                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. UDG对HTTP报文进行以下处理（关键）                             │
│    a. 协议识别：识别出HTTP报文后解析出关键字                      │
│       （Method=Get/Post、URL）                                   │
│    b. 规则匹配：根据报文特征信息                                  │
│       （七层关键字 / 三四层五元组）进行规则匹配                   │
│    c. 【防欺诈检测】报文匹配到HTTP头防欺诈动作后，                │
│       获取本地预先配置的增强字段信息（ADD HEADEN），              │
│       判断用户HTTP报文是否已存在该字段：                          │
│       ┌─ 存在该字段：将报文头中的取值与本地保存的取值比较          │
│       │   ├─ 不正确 → 修改为本地保存的用户信息（纠正）            │
│       │   ├─ 正确   → 进行后续业务                               │
│       │   └─ 多个该字段 → 删除冗余，保留一个正确字段              │
│       └─ 不存在该字段：执行HTTP头增强动作（插入字段）             │
│    d. 【灰名单模式】（ADD HEADEN GRAYLIST=ENABLE）：              │
│       UDG只处理防欺诈（检测并纠正），不插入头增强字段              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. UDG将经过防欺诈处理的HTTP GET/POST请求报文发送给Web服务器      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. Web服务器获取增强的用户信息（已纠正/已清理冗余），             │
│    构造个性化响应报文返回UDG                                      │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. UDG将HTTP响应报文转发给用户                                   │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `HTTP头防欺诈原理_59318043.md` §HTTP头防欺诈业务流程

### 3.4 执行顺序与BIT1030软参

防欺诈检测与头增强插入的执行顺序由软参 **BIT1030** 控制：BIT1030 控制HTTP头防欺诈功能是否在头增强业务前执行。默认配置下，防欺诈检测 → 字段纠正/冗余清理 → 头增强插入（灰名单模式下跳过插入）。

> SourcePath: `GWFD-110261 HTTP头增强参考信息_79595496.md` §软参（BIT1030 控制HTTP头防欺诈功能是否在头增强业务前执行）

### 3.5 与HTTP头增强的关系（强耦合详解）

| 维度 | 说明 |
|------|------|
| **License双开** | LKV3G5HHAS01（防欺诈）+ LKV3G5HTHE01（头增强）必须同时开启 |
| **配置载体相同** | 防欺诈开关内嵌于 `ADD HEADEN` 命令的 `ANTIFRAUD` 参数，不独立配置策略对象 |
| **执行顺序** | 防欺诈检测 → 字段纠正/冗余清理 → 头增强插入（灰名单模式下跳过插入） |
| **触发条件共用** | 共用 FILTER/L7FILTER/FLOWFILTER 过滤条件，RULE 的 POLICYTYPE=HEADEN |
| **字段类型限制** | 防欺诈字段需为**非标准HTTP头域名**（如 host 是标准头域名则无法防欺诈） |
| **报文类型限制** | 仅对 HTTP/WAP2.0 的 Post/Get 报文的上行报文处理有意义 |

### 3.6 与其他防欺诈特性的关系（UDG防欺诈协议族）

UDG防欺诈功能专题包含多个防欺诈特性，HTTP头防欺诈是其中之一：

| 防欺诈特性 | 特性ID（推断） | 检测对象 | 业务专题位置 |
|-----------|---------------|---------|------------|
| **HTTP头防欺诈** | **GWFD-110401** | HTTP头增强字段正确性 | `UDG防欺诈功能专题/HTTP头防欺诈` |
| HTTP计费防欺诈 | GWFD-110403 | HTTP计费行为（Server IP） | `UDG防欺诈功能专题/HTTP计费防欺诈` |
| DNS计费防欺诈 | （推断） | DNS tunnel/端口计费 | `UDG防欺诈功能专题/DNS计费防欺诈` |

> 说明：HTTP头防欺诈与HTTP计费防欺诈（GWFD-110403）虽同属防欺诈族，但检测对象不同（头字段 vs 计费行为），配置独立。

> SourcePath: `output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/`（防欺诈协议族目录结构）

---

## 4. 配置

### 4.1 配置对象总览

HTTP头防欺诈**不独立配置策略对象**，所有配置对象与HTTP头增强共用（详见 GWFD-110261 §4.1）。关键对象：

| 对象类型 | 命令 | 用途 |
|----------|------|------|
| FILTER | ADD FILTER | 三四层过滤条件（基于三四层触发时配置） |
| FLOWFILTER | ADD FLOWFILTER / ADD FLTBINDFLOWF | 流过滤器及其过滤器绑定 |
| L7FILTER | ADD L7FILTER | 七层过滤条件（URL + METHODTYPE=GET/POST，基于七层触发时配置） |
| PROTBINDFLOWF | ADD PROTBINDFLOWF | 流过滤器的协议绑定（http协议+L7FILTER） |
| WELLKNOWNPORT | ADD WELLKNOWNPORT | 知名端口（识别HTTP协议端口80/8080等） |
| SIGNATUREDB | LOD SIGNATUREDB | 加载协议特征库（识别HTTP协议） |
| PARSERDB | LOD PARSERDB | 加载协议解析数据库 |
| **HEADEN** | **ADD HEADEN** | **头增强对象（含防欺诈开关ANTIFRAUD和灰名单开关GRAYLIST）—— 防欺诈核心配置载体** |
| RULE | ADD RULE | 业务规则，POLICYTYPE=HEADEN |
| USERPROFILE | ADD USERPROFILE | 用户模板 |
| RULEBINDING | ADD RULEBINDING | 用户模板和规则绑定关系 |

> SourcePath: `激活HTTP头防欺诈_69815661.md` §必备事项-数据 表2~表6

### 4.2 配置流程

```
1. 打开License配置开关（双开：防欺诈 + 头增强）
   SET LICENSESWITCH（LKV3G5HHAS01）
   SET LICENSESWITCH（LKV3G5HTHE01）

2. 配置三四层过滤条件（基于三四层触发时）
   ADD FILTER → ADD FLOWFILTER → ADD FLTBINDFLOWF → SET REFRESHSRV

3. 配置七层过滤条件（基于七层触发时）
   ADD L7FILTER（URL + METHODTYPE=GET/POST）
   ADD PROTBINDFLOWF（绑定http协议+L7FILTER）
   SET REFRESHSRV
   ADD WELLKNOWNPORT（http端口80/8080）
   LOD SIGNATUREDB / LOD PARSERDB

4. 配置头增强对象（使能防欺诈）—— 防欺诈核心步骤
   ADD HEADEN（ANTIFRAUD=ENABLE；GRAYLIST 可选 ENABLE）

5. 配置业务规则（策略类型=头增强）
   ADD RULE（POLICYTYPE=HEADEN，引用FLOWFILTER和HEADEN）

6. 配置用户模板并绑定规则
   ADD USERPROFILE → ADD RULEBINDING
```

> SourcePath: `激活HTTP头防欺诈_69815661.md` §操作流程

### 4.3 ADD HEADEN 关键参数（防欺诈核心）

| 参数 | 名称 | 取值样例 | 说明 |
|------|------|----------|------|
| HEADERENNAME | 头增强名称 | header_test | 头增强字段**不能配置为HTTP标准头域名**（如 accept、host），否则可能导致防欺诈失败 |
| DATATYPE | 数据类型 | IMSI1 | 要插入的用户信息字段类型 |
| PREFIXNAME | 前缀名称 | X-imsi | HTTP头扩展字段前缀，**非标准头域名** |
| ENCRYALGORI | 加密算法标识 | AES128 | 头增强字段加密算法（建议使用安全算法） |
| PSWDKEY / PSWDKEYCONFIRM | 密码/确认密码 | XXXXXX | 加密密钥 |
| **ANTIFRAUD** | **防欺诈标识** | **ENABLE** | **使能HTTP头防欺诈（本特性核心开关）** |
| GRAYLIST | 灰名单标识（可选） | ENABLE/DISABLE | ENABLE=只防欺诈不插入头增强 |

> SourcePath: `激活HTTP头防欺诈_69815661.md` §表4 头增强的防欺诈标识规划数据

### 4.4 典型配置实例

**场景**：对URL是 `www.huawei.com/*` 的HTTP GET、POST报文进行HTTP头增强，将用户的IMSI字段加入用户报文头，并启动HTTP头防欺诈功能。

```
// 1. 打开本特性的License配置开关（防欺诈）
SET LICENSESWITCH:LICITEM="LKV3G5HHAS01",SWITCH=ENABLE;

// （强耦合：确保HTTP头增强License已开）
// SET LICENSESWITCH:LICITEM="LKV3G5HTHE01",SWITCH=ENABLE;

// 2. 配置HTTP头防欺诈使用的三四层过滤规则
ADD FILTER:FILTERNAME="filter_test_0",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRSTARTPORT=0,SVRENDPORT=0;
ADD FILTER:FILTERNAME="filter_test_65535",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRSTARTPORT=65535,SVRENDPORT=65535;
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test_0";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",FILTERNAME="filter_test_65535";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 3. 配置HTTP头防欺诈的七层过滤规则
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="1",URL="www.huawei.com/*",METHODTYPE=GET-1;
ADD L7FILTER:L7FILTERNAME="l7filter_test",SUBL7FLTNAME="2",URL="www.huawei.com/*",METHODTYPE=POST-1;
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test",PROTOCOLNAME="http",L7FILTERNAME="l7filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;
ADD WELLKNOWNPORT:IDENPROTNAME="http0",PROTOCOLNAME="http",PORTOP=EQUAL,STARTPORT=0,PRIORITY=5;
ADD WELLKNOWNPORT:IDENPROTNAME="http65535",PROTOCOLNAME="http",PORTOP=EQUAL,STARTPORT=65535,PRIORITY=10;
LOD SIGNATUREDB:LOADMODE=LATEST;
LOD PARSERDB:LOADMODE=LATEST;

// 4. 配置HTTP头防欺诈的动作属性，使能防欺诈标识（ANTIFRAUD=ENABLE）
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="X-imsi",ENCRYALGORI=AES128,PSWDKEY="XXXXXX",PSWDKEYCONFIRM="XXXXXX",ANTIFRAUD=ENABLE;

// 5. 配置HTTP头防欺诈使用的业务规则（POLICYTYPE=HEADEN）
ADD RULE:RULENAME="rule_test",POLICYTYPE=HEADEN,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_test",POLICYNAME="header_test";

// 6. 配置HTTP头防欺诈使用的业务策略组合
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

> 来源：`激活HTTP头防欺诈_69815661.md` §任务示例（脚本完整保留）

---

## 5. 验证与调测

### 5.1 验证方法

#### 5.1.1 调测前提与目的

当运营商完成部署HTTP头防欺诈功能后，需对本功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF。

#### 5.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 测试终端使用的APN | APN名称（APN） | apn-head-test | 与对端协商（与SMF上的APN名称保持一致） |
| 触发HTTP头防欺诈的URL | URL | www.huawei.com | 已配置数据中获取 |
| 用户IMSI号 | IMSI | 123324423123195 | 测试终端自带 |
| 用户MSISDN | MSISDN | 8615001336713 | 测试终端自带 |

工具：测试终端、第三方抓包工具（UDG接入侧/PDN侧镜像接口）

#### 5.1.3 调测执行步骤

**步骤1**：打开镜像接口侧的抓包工具，准备抓取测试终端的出入报文。

**步骤2**：测试终端使用 `apn-head-test` APN接入网络。
- 成功接入 → 步骤3
- 无法接入 → 调测UDG的接入功能

**步骤3**：测试终端浏览Web业务，访问 `www.huawei.com`，查看镜像接口的抓包信息。
- 部分浏览器（Firefox、Chrome）支持在用户HTTP报文头中插入增强字段，**可利用此功能插入 `X-imsi` 增强字段验证防欺诈**
- 如果测试终端可以正常浏览网页，且PDN侧接口抓包显示HTTP请求报文中插入了**正确的**头增强字段 → 防欺诈功能正常，调测结束
- 如果可以浏览网页但抓包显示**没有插入正确**的头增强字段 → 执行步骤4
- 如果无法浏览网页 → 调测UDG的Web浏览功能

**步骤4**：检查HTTP头防欺诈相关配置是否正确（见5.1.4验证命令）。

**步骤5**：收集信息并寻求技术支持。
- a. 在镜像接口或服务器上开启抓包工具，执行步骤2并保存报文
- b. 执行 `EXP MML` 命令将当前配置数据导出为MML脚本文件并保存
- c. 收集并保存上述所有查询信息
- d. 收集归纳所有信息并联系华为技术支持解决

> SourcePath: `调测HTTP头防欺诈_23347830.md` §操作步骤

#### 5.1.4 配置验证命令与预期输出

| 命令 | 用途 | 验证点 |
|------|------|--------|
| `LST LICENSESWITCH:LICITEM="LKV3G5HHAS01";` | 查询License开关 | LICITEM=LKV3G5HHAS01 是否 ENABLE（同时确认 LKV3G5HTHE01 已开） |
| `LST RULEBINDING:USERPROFILENAME="up_test";` | 查询规则绑定 | 规则名称=rule_test，策略类型=Header Enrichment |
| `LST RULE:RULENAME="rule_test",POLICYTYPE=HEADEN;` | 查询规则 | 流过滤器名称、头增强名称是否与规划一致 |
| `LST PROTBINDFLOWF:FLOWFILTERNAME="flowfilter_test";` | 查询协议绑定 | 协议名称=http，七层过滤器名字=l7filter_test |
| `LST L7FILTER:L7FILTERNAME="l7filter_test";` | 查询七层过滤器 | URL、Method=GET/POST 配置是否正确 |
| `LST HEADEN:HEADERENNAME="header_test";` | 查询头增强 | **防欺诈标识=使能**，数据类型、前缀名称是否一致 |
| `LST FILTER:FILTERNAME="filter_test_80";` | 查询过滤器 | 三四层协议类型、服务器端口是否一致 |
| `LST FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_test";` | 查询过滤器绑定 | FlowFilter 绑定的过滤器名字是否一致 |
| `LST WELLKNOWNPORT:;` | 查询知名端口 | UDG 能否识别HTTP协议类型（端口80/8080） |
| `DSP SIGNATUREDB:;` | 查询特征库加载状态 | Load Finish |
| `EXP MML` | 导出MML配置脚本 | 故障信息收集 |

**LST HEADEN 预期输出（防欺诈关键）**：
```
LST HEADEN:HEADERENNAME="header_test";
```
预期输出（参照 HTTP头增强调测 LST HEADEN 格式）：
```
---------------------------
               头增强名称  =  header_test
                 数据类型  =  IMSI1
                 前缀名称  =  X-imsi
             加密算法标识  =  AES128
                     密码  =  *****
               防欺诈标识  =  使能        ← 关键：ANTIFRAUD=ENABLE时显示"使能"
                    ......
(结果个数 = 1)
--- END
```

> SourcePath: `调测HTTP头防欺诈_23347830.md` §操作步骤 步骤4-5；`调测HTTP头增强_21598754.md` §步骤6.d（LST HEADEN 输出格式参照）

### 5.2 告警参考

产品文档未明确列出HTTP头防欺诈的独立告警。防欺诈异常通常会反映在HTTP头增强的相关日志和镜像抓包中。

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md`（特性概述未列告警章节）

### 5.3 测量指标

产品文档未明确列出HTTP头防欺诈的独立测量指标。防欺诈相关的性能测量可参考业务安全测量维度（OM参考中"用户平面业务防欺诈测量"）。

> SourcePath: `output/UDG_Product_Documentation_CH_20.15.2/OM参考/性能指标/UDG性能指标/用户面指标/业务安全测量/用户平面业务防欺诈测量`（防欺诈测量指标目录位置）

### 5.4 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 无法浏览网页 | 先调测UDG的Web浏览功能（GWFD-110103 SA-Web Browsing License未开） | `LST LICENSESWITCH:LICITEM="LKV3G5SAWB01";` 确认 ENABLE |
| 抓包显示未插入正确头增强字段 | 配置错误 | 按 `LST RULEBINDING → LST RULE → LST PROTBINDFLOWF/L7FILTER → LST HEADEN → LST FILTER → LST FLTBINDFLOWF → LST WELLKNOWNPORT` 顺序逐项核查 |
| 防欺诈标识为"不使能" | ADD HEADEN 未设置 ANTIFRAUD=ENABLE | `LST HEADEN:HEADERENNAME="header_test";` 确认"防欺诈标识=使能"；重新执行 `ADD HEADEN` 含 `ANTIFRAUD=ENABLE` |
| 防欺诈License未生效 | LKV3G5HHAS01 未开 | `LST LICENSESWITCH:LICITEM="LKV3G5HHAS01";` 确认 ENABLE |
| 头增强License未开（强耦合） | LKV3G5HTHE01 未开 | `LST LICENSESWITCH:LICITEM="LKV3G5HTHE01";` 确认 ENABLE |
| 防欺诈未对标准头域字段生效 | 字段前缀配置为HTTP标准头域名（如host） | 重新配置 ADD HEADEN 的 PREFIXNAME 为**非标准头域名**（如 X-imsi、pre-msisdn） |
| 知名端口未配置HTTP | 协议无法识别 | `LST WELLKNOWNPORT:;` 确认HTTP端口80/8080；参考激活文档重新配置 |
| 防欺诈对HTTPS报文未生效 | 本特性仅HTTP/WAP2.0（应用限制） | HTTPS防欺诈需使用 GWFD-110263 HTTPS头增强（ADD TLSHEADEN ANTIFRAUD=ENABLE） |
| 防欺诈对Post/Get外方法未生效 | 仅对Post/Get报文有效（应用限制） | 属预期行为；METHODTYPE需配置 GET-1 / POST-1 |
| 浏览器插入的MSISDN未被纠正 | 字段取值比较失败或字段前缀不匹配 | 确认浏览器插入的字段前缀与 ADD HEADEN PREFIXNAME 一致；确认本地保存的用户信息正确 |
| 冗余字段未被清理 | 多个相同字段场景下防欺诈未生效 | 确认 ANTIFRAUD=ENABLE；检查 BIT1030 软参（控制防欺诈在头增强前执行） |
| 兜底（仍无法解决） | — | 镜像抓包 + `EXP MML` 导出配置 → 联系华为技术支持 |

> SourcePath: `调测HTTP头防欺诈_23347830.md` §操作步骤

---

## 6. 参考信息

### 6.1 与其他特性的关系（防欺诈协议族 + 强耦合）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| **HTTP头增强** | **GWFD-110261（UDG）** | **强耦合依赖**：防欺诈开关内嵌于 ADD HEADEN 的 ANTIFRAUD 参数；启用防欺诈必须开启头增强（License 82209777 + 82209786 双开） |
| SA-Basic | GWFD-110101（UDG） | **依赖**：HTTP报文识别解析基础 |
| SA-Web Browsing | GWFD-110103（UDG） | **依赖**：HTTP/WAP2.0协议解析 |
| 增强的ADC基本功能 | GWFD-020357（UDG） | **配合关系**：ADC检测是HTTP解析的前置能力 |
| HTTPS头增强 | GWFD-110263（UDG） | **HTTPS防欺诈载体**：HTTPS头防欺诈通过 ADD TLSHEADEN ANTIFRAUD=ENABLE 实现（与HTTP头防欺诈对应） |
| HTTP智能重定向 | GWFD-110284（UDG） | **可串联**：防欺诈纠正后的正确头信息支撑后续重定向认证 |
| 用户Portal | GWFD-110281（UDG） | **Portal认证依赖**：Portal认证可依赖防欺诈保证的头增强信息 |
| HTTP计费防欺诈 | GWFD-110403（UDG） | **防欺诈族兄弟**：同属UDG防欺诈功能专题，检测对象不同（头字段 vs 计费行为） |
| DNS计费防欺诈 | （防欺诈族） | **防欺诈族兄弟**：DNS层防欺诈变体 |

> SourcePath: `GWFD-110401 HTTP头防欺诈_67104710.md` §与其他特性的交互

### 6.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110401 HTTP头防欺诈_67104710.md` | 适用NF（PGW-U/UPF，UDG 20.0.0+）、定义、客户价值、应用场景（MSISDN欺诈防护/业务控制保障）、可获得性（License LKV3G5HHAS01）、与其他特性交互（SA-Basic/SA-Web Browsing/HTTP头增强强耦合）、对系统影响、应用限制（4条）、原理概述（防欺诈检测纠正逻辑）、计费与话单（无）、特性规格（无特殊）、遵循标准（3GPP 23.214/29.244、IETF 2616）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/HTTP头防欺诈/原理描述/HTTP头防欺诈原理_59318043.md` | HTTP头防欺诈原理（检测纠正逻辑）、HTTP头防欺诈类型（基于三四层/七层特征触发两种）、业务流程（7步端到端，含防欺诈检测纠正）、灰名单模式（GRAYLIST） |
| 3 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/HTTP头防欺诈/原理描述/约束限制和系统影响_13425672.md` | 约束限制（4条：报文类型/头域类型/协议/加密场景）、系统影响（必须开启HTTP头增强） |
| 4 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/HTTP头防欺诈/激活HTTP头防欺诈_69815661.md` | 操作流程、数据规划表（License/流过滤器/三四层过滤/七层过滤/头增强防欺诈标识 共6张表）、完整MML脚本（License+FILTER+FLOWFILTER+FLTBINDFLOWF+REFRESHSRV+L7FILTER+PROTBINDFLOWF+WELLKNOWNPORT+SIGNATUREDB+PARSERDB+HEADEN+RULE+USERPROFILE+RULEBINDING） |
| 5 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/HTTP头防欺诈/调测HTTP头防欺诈_23347830.md` | 调测流程（抓包验证防欺诈纠正）、步骤4-5配置验证命令清单（LST LICENSESWITCH/RULEBINDING/RULE/PROTBINDFLOWF/L7FILTER/HEADEN/FILTER/FLTBINDFLOWF/WELLKNOWNPORT） |
| 6 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/防欺诈功能概述_11753654.md` | UDG防欺诈协议族概述（HTTP头防欺诈在族中的定位） |
| 7 | `UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG防欺诈功能专题/特性映射_58713491.md` | 防欺诈协议族特性映射 |

### 6.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| ANTIFRAUD | 防欺诈标识 | ADD HEADEN 参数，使能HTTP头防欺诈（本特性核心开关，内嵌于HTTP头增强命令） |
| GRAYLIST | 灰名单标识 | ADD HEADEN 参数，ENABLE=只防欺诈不插入头增强字段 |
| MSISDN欺诈 | MSISDN Fraud | 用户浏览器插入错误MSISDN导致计费失败或错误计费到其他用户的风险 |
| HTTP标准头域名 | Standard HTTP Header | 如 host、accept、user-agent 等；防欺诈字段前缀**不能**使用此类标准头域名 |
| BIT1030 | 软参 | 控制HTTP头防欺诈功能是否在头增强业务前执行 |
| HTTP计费防欺诈 | GWFD-110403 | 防欺诈族兄弟特性（检测HTTP计费行为，非头字段） |

---

## 7. 文档一致性说明（配置树 vs 产品文档）

> 配置树/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | feature_group 归属 | feature-doc-list 归为"防欺诈"组 | 产品文档路径在"智能策略控制功能"下；业务专题归"UDG防欺诈功能专题/HTTP头防欺诈" | 一致（分组语义一致） |
| 2 | 与HTTP头增强关系 | 文档清单将两者列为独立特性 | 产品文档明确 **强耦合**：防欺诈开关内嵌于 ADD HEADEN 的 ANTIFRAUD 参数，不独立配置策略对象；启用防欺诈必须开启头增强 | 补全：强耦合关系（非独立特性） |
| 3 | POLICYTYPE | 文档清单未明确策略类型 | 产品文档明确 共用 **POLICYTYPE=HEADEN**（与HTTP头增强同一RULE），防欺诈是HEADEN动作的安全增强层 | 补全：防欺诈不独立配置POLICYTYPE |
| 4 | License双开 | 文档清单仅列 LKV3G5HHAS01 | 产品文档明确 防欺诈License LKV3G5HHAS01 + 头增强License LKV3G5HTHE01 **必须双开** | 补全：强耦合License双开 |
| 5 | 触发方式 | 文档清单未明确 | 产品文档明确 **两种触发方式**：基于三四层特征触发 / 基于七层特征触发 | 补全 |
| 6 | 灰名单模式 | 文档清单未明确 | 产品文档明确 灰名单模式（GRAYLIST=ENABLE）：UDG只处理防欺诈，不插入头增强字段；适用于"只进行防欺诈而不需要头增强"的场景 | 补全 |
| 7 | 字段前缀限制 | 文档清单未明确 | 产品文档明确 头增强字段**不能配置为HTTP标准头域名**（如host），否则可能导致防欺诈失败 | 补全：关键约束 |
| 8 | 报文类型限制 | 文档清单未明确 | 产品文档明确 仅对 HTTP/WAP2.0 的 **Post/Get报文上行报文**有效 | 补全 |
| 9 | 执行顺序 | 文档清单未明确 | 头增强参考信息列出软参 **BIT1030** 控制HTTP头防欺诈功能是否在头增强业务前执行 | 补全：BIT1030软参控制执行顺序 |
| 10 | HTTPS防欺诈 | 文档清单未明确 | 头增强差异表明确 **HTTPS头增强也支持防欺诈**（ADD TLSHEADEN ANTIFRAUD=ENABLE）；RTSP头增强不支持防欺诈 | 补全：HTTPS防欺诈=支持，RTSP防欺诈=不支持 |
| 11 | 告警与测量指标 | 文档清单未列 | 产品文档特性概述未列独立告警/测量指标章节；防欺诈测量可能在OM参考"用户平面业务防欺诈测量"维度 | 补全：特性概述未列独立告警/测量 |
| 12 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（4份文档MML脚本参数一致） | 无 |

---
