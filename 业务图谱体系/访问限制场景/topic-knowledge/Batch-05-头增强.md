# Batch-05: 头增强族（HTTP/HTTPS/RTSP/NSH）

> 批次 05 | 主题：头增强族共性机制与差异 | 来源：GWFD-110261/262/263 feature-knowledge + UDG头增强功能专题 | 特性数 3（+NSH 扩展） | 核心度 ★★★★（DISCARD/HEADEN/REDIRECT 中的 HEADEN 轨道核心）

---

## 1. 概述

头增强（Header Enrichment, HEADEN）是访问限制场景中**信息插入层**的核心机制：在用户业务请求报文头中插入运营商规划的用户属性字段（MSISDN、IMSI、IMEI、APN、位置信息等），传递给业务服务器，支持业务认证、个性化服务、防欺诈校验。

头增强是**带内（in-band）方案**：相对于带外（RADIUS 查询）方式，带内方案简化了业务服务器逻辑、保证了业务实时性，是 UDG 内置 WAP 网关的关键技术。

**族内特性**：
- **GWFD-110261 HTTP 头增强**（License 82209777 LKV3G5HTHE01）
- **GWFD-110263 HTTPS 头增强**（License 82209779 LKV3G5HTSE01）
- **GWFD-110262 RTSP 头增强**（License 82209778 LKV3G5RTHE01）
- **NSH 头增强**（专题中列出，feature-knowledge 未单独提取）

---

## 2. 核心知识点（KP）

### KP-1 头增强族共性：字段格式与配置载体（来自 110261/262/263 §4.1 + 专题概述）

**字段格式**：`<字段前缀名称: 字段值>`

| 组成 | 数据来源 | 配置载体 |
|------|----------|----------|
| 字段前缀名称（如 `X-imsi`） | UDG 本地配置 | `ADD HEADEN:PREFIXNAME=...` |
| 字段值（如 `460001234567890`） | 用户激活时的实时信息 | `ADD HEADEN:DATATYPE=IMSI1` |

**所有头增强特性共用同一配置命令**：`ADD HEADEN`（HEADERENNAME + DATATYPE + PREFIXNAME + ENCRYALGORI + PSWDKEY）。

**头增强动作被 RULE 引用的方式**：
```
ADD HEADEN:HEADERENNAME="header_test",DATATYPE=IMSI1,PREFIXNAME="X-imsi",ENCRYALGORI=AES128,...;
ADD RULE:RULENAME="rule_test",POLICYTYPE=HEADEN,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="...",POLICYNAME="header_test";
```

`POLICYTYPE=HEADEN` 是**头增强族所有协议共用的 RULE 策略类型**；`POLICYNAME` 指向 `HEADEN` 对象名。

---

### KP-2 族内共有 25+ 个可插入字段（来自 110261 §4.2）

头增强族统一支持以下字段类型，加密支持因字段而异：

| 字段类型 | 典型用途 | 加密支持 |
|---------|----------|----------|
| **MSISDN** | 用户手机号，业务认证核心 | 支持 |
| **IMSI / SUPI** | 用户永久标识，防欺诈核心 | 支持 |
| **IMEI / PEI** | 设备标识 | 支持 |
| **APN** | 接入点名称 | 支持 |
| **MS IP** | 用户 IP（IPv4/IPv6） | 支持 |
| **SGSN IP / GGSN IP / UPIPV4 / UPIPV6** | 网元 IP | 支持 |
| **ULI** | 用户接入位置（SAI/CGI/ECGI/TAI/EULF/NRLF） | 支持 |
| **Roaming** | 漫游属性（home/roaming/visiting） | 支持 |
| **RAT / MCC / MNC / SGSN-MCC-MNC** | 接入网络类型、PLMN | 支持/不支持混合 |
| **SUBPROFILE** | PCRF/PCF 开户存储信息（性别、年龄） | 支持 |
| **CHGCHAR / Billing Type** | 计费属性 | 支持/不支持混合 |
| **TIMESTAMP** | 时间戳 | 支持 |
| **USERDEF** | 运营商自定义字段（最多4个） | 不支持 |
| **MULTIPARA** | 多参数拼接（仅 MSISDN/SGSNIP/MSIP） | 支持 |

**关键约束**：MULTIPARA 多参数拼接，每个头增强对象最多 3 个拼接字段，每个拼接字段最多 4 个参数。

---

### KP-3 族内共用的加密与编码机制（来自 110261 §4.3 + 差异表）

**加密算法**（族内统一）：
| 算法 | 安全建议 | 盐值支持 |
|------|----------|----------|
| **AES-128 / AES-256** | 推荐 | 否 |
| **RSA-2048** | 推荐 | 否 |
| **SHA-256** | 推荐 | 支持 |
| MD5 | 有风险，不建议 | 支持 |
| RC4 | 有风险，不建议 | 否 |
| RSA-1024 | 有风险，不建议 | 否 |

**编码方式**（族内基本统一）：
- **base64** 编码：通过 `SET BASE64` 开启
- **ASCII** 编码：通过软参开启（HTTP/RTSP）/ HTTPS 还支持十六进制编码（Byte837 软参）

**关键规则**：配置加密时，UDG **仅加密字段取值**，**不加密字段名称**。

---

### KP-4 族内差异：协议、插入位置、依赖（来自头增强差异专题表1）

| 差异点 | HTTP 头增强 | HTTPS 头增强 | RTSP 头增强 |
|-------|-------------|-------------|-------------|
| **触发条件** | 特定IP / 特定URL / HTTP协议 | 特定IP / 特定**SNI** / HTTPS协议 | 特定IP / 特定URL / RTSP协议 |
| **支持协议** | HTTP1.x（不支持 HTTP2.0） | TLS 1.0/1.1/**1.2/1.3** | RTSP（不支持 RTSP over HTTP） |
| **字段插入位置** | HTTP 扩展字段 | **SSL 报文头 Extension 字段，TLV 格式组织** | RTSP 扩展字段 |
| **业务** | Web 浏览 | Web 浏览 | 视频流媒体 |
| **业务服务器** | Web Server | Web Server | Streaming Server |
| **依赖 SA 特性** | SA-Basic + SA-Web Browsing + SA-Mobile（MMS场景） | SA-Basic + SA-Web Browsing + SA-Mobile + **HTTP2.0 Host识别** | SA-Basic + **SA-Streaming** |
| **加密算法** | MD5/RC4/AES-128/256/RSA-1024/2048/SHA-256 | MD5/RC4/AES-128/256/SHA-256（无 RSA） | 同 HTTP |
| **编码能力** | base64 + ASCII | base64 + ASCII + **十六进制** | base64 + ASCII |
| **头防欺诈支持** | **支持** | **支持** | **不支持** |
| **License** | 82209777 HTHE01 | 82209779 HTSE01 | 82209778 RTHE01 |
| **多参数拼接** | 支持（v02 起） | 不支持 | 支持（v02 起） |

**最关键的差异**：
1. **HTTPS 头增强的 TLV 格式**：字段必须按 TLS 协议 TLV 格式组织插入到 SSL Extension 内（RFC 5246），技术复杂度最高
2. **HTTPS 头增强的 SNI 触发**：因 HTTPS 报文加密，只能基于 SNI（Server Name Indication）触发
3. **头防欺诈仅支持 HTTP/HTTPS**：RTSP 协议不支持头防欺诈（Batch-08 详述）

---

### KP-5 头增强族共用的应用限制（来自 110261/262/263 §6）

1. **IPv6 分片限制**：所有协议统一要求 `TCP MSS ≤ PMTU - 60字节`
2. **MTU 限制**：网络设备 MTU 过小时，UDG 不对分片报文做头增强
3. **头域分片**：报文头域分片时不支持头增强
4. **外置 PCEF 场景**：外置 PCEF 计费时，内置 PCEF 上不建议部署头增强
5. **加密场景基于 host 的计费**：不支持
6. **整机规格**：所有协议统一，整机支持 100 个 Header Enrichment 动作

---

## 3. 关键发现（跨特性横向归纳）

### 发现-1 头增强是"带内信息插入"的统一机制——族内特性共用 HEADEN 配置对象

族内三个（四个含 NSH）协议的头增强**共用同一套配置对象和命令**，差异仅在"**解析 SA 特性依赖**"和"**字段插入位置**"两个维度：

```
统一配置载体（所有协议共用）：
  ADD HEADEN（含 HEADERENNAME/DATATYPE/PREFIXNAME/ENCRYALGORI/PSWDKEY/ANTIFRAUD/GRAYLIST）
  ADD RULE:POLICYTYPE=HEADEN,POLICYNAME=<HEADEN 对象名>

差异点：
  ├─ HTTP：依赖 SA-Web Browsing，插入 HTTP 扩展字段
  ├─ HTTPS：依赖 SA-Web Browsing + HTTP2.0 Host识别，插入 SSL Extension（TLV 格式）
  ├─ RTSP：依赖 SA-Streaming，插入 RTSP 扩展字段
  └─ NSH：依赖 NSH 相关 SA
```

**对图谱第 4 层（ConfigObject）的启示**：`HEADEN` 是一个跨协议复用的 ConfigObject，其 `variant_dimensions` 应包含 `protocol_type`（HTTP/HTTPS/RTSP/NSH）。

---

### 发现-2 头增强动作如何被访问限制规则引用——POLICYTYPE=HEADEN 的统一接口

所有头增强族特性通过**同一个 RULE POLICYTYPE**（`HEADEN`）被引用，这是头增强与其他动作（ADC、SMARTREDIRECT、WEBPROXY、PCC）并列的关键接口：

| 动作类型 | RULE POLICYTYPE | POLICYNAME 指向 |
|---------|-----------------|----------------|
| 头增强（族内统一） | `HEADEN` | HEADEN 对象名 |
| ADC 检测 | `ADC` 或 `PCC` | FLOWFILTER 本地 / PCCPOLICYGRP |
| HTTP 智能重定向 / DNS 纠错 | `SMARTREDIRECT` | SMARTHTTPREDIR / DNSOVERWRITING 对象 |
| Web Proxy | `WEBPROXY` | IPFARM 对象名 |
| 用户 Portal | （captive 配置在 USERPROFILE） | PCCPOLICYGRP |
| URL 过滤 | `PCC`（仅匹配触发） | PCCPOLICYGRP（实际动作在 CFTEMPLATE/CONTCATEGBIND） |

**关键观察**：**访问限制动作的差异化主要通过 `RULE.POLICYTYPE` 区分**，这是图谱建模 RULE 对象时的核心 variant_dimension。

---

### 发现-3 头增强族共用的配置流程模板

```
1. SET LICENSESWITCH:LICITEM="LKV3G5{HTHE|HTSE|RTHE}01",SWITCH=ENABLE;
2. [可选] 配置三四层过滤（基于IP触发）：ADD FILTER → FLOWFILTER → FLTBINDFLOWF
3. [可选] 配置七层过滤（基于URL/SNI触发）：ADD L7FILTER → PROTBINDFLOWF → SET REFRESHSRV
4. ADD HEADEN（统一命令，含加密、防欺诈、灰名单参数）
5. ADD RULE:POLICYTYPE=HEADEN, FLOWFILTERNAME=..., POLICYNAME=<HEADEN名>
6. ADD USERPROFILE → ADD RULEBINDING
```

**对图谱第 3 层（Task）的启示**：头增强族共用一个 Task 模板（"配置头增强规则"），差异仅在步骤 1（License）和步骤 3 的 SA 依赖。可提取为 `T-HEADEN-CONFIG` 通用任务。

---

### 发现-4 头增强与防欺诈的强耦合（详见 Batch-08）

- `ADD HEADEN` 命令自带 `ANTIFRAUD=ENABLE/DISABLE` 和 `GRAYLIST=ENABLE/DISABLE` 参数
- 防欺诈（GWFD-110401）不是独立动作，而是**内嵌于 HEADEN 对象的检测前置**
- 执行顺序：**防欺诈检测 → 字段纠正/冗余清理 → 头增强插入**（灰名单模式下跳过插入）
- RTSP 头增强不支持防欺诈（族内唯一例外）

---

### 发现-5 头增强映射到访问限制三种动作

| 访问限制动作 | 头增强族如何贡献 | 说明 |
|-------------|----------------|------|
| **HEADEN（头增强）** | **直接核心动作**：族内所有特性本身就是 HEADEN 动作 | 直接映射 |
| **DISCARD（阻塞）** | 不直接产生阻塞；但灰名单模式（GRAYLIST=ENABLE）下若检测到欺诈字段会纠正而非阻塞 | 间接贡献 |
| **REDIRECT（重定向）** | 不直接产生重定向；但插入的 MSISDN/IMSI 等字段会被 HTTP 智能重定向、Portal 等下游动作使用（如 REDIRAPPENDINFO 携带 MSISDN/IMEI） | 下游联动 |

---

## 4. 配置对象/命令复用清单

### 头增强族独有配置对象
- `HEADEN`：跨协议复用，含 DATATYPE/PREFIXNAME/ENCRYALGORI/PSWDKEY/**ANTIFRAUD**/**GRAYLIST** 参数

### 头增强族独有 MML 命令
- `ADD HEADEN`（统一）
- `SET BASE64`（编码开关）

### 与场景内其他特性共用的配置对象（场景级通用链）
- 三四层：`FILTER` → `FLOWFILTER` → `FLTBINDFLOWF`
- 七层：`L7FILTER` → `PROTBINDFLOWF`
- 规则绑定：`RULE`（POLICYTYPE=**HEADEN**） → `USERPROFILE` → `RULEBINDING`

### 头增强族不使用的关键对象（与其他动作对比）
- 不用 `PCCPOLICYGRP`（头增强不走 PCC 体系）
- 不用 `URR/URRGROUP`（除非与计费组合）
- 不用 `IPFARM`（那是重定向用的）

### License
- HTTP：`82209777 LKV3G5HTHE01`
- HTTPS：`82209779 LKV3G5HTSE01`
- RTSP：`82209778 LKV3G5RTHE01`

---

## 5. 来源

- 主：
  - `feature-knowledge/GWFD-110261-HTTP头增强.md`
  - `feature-knowledge/GWFD-110262-RTSP头增强.md`
  - `feature-knowledge/GWFD-110263-HTTPS头增强.md`
- 业务专题：
  - `UDG头增强功能专题/头增强功能概述_04211022.md`
  - `UDG头增强功能专题/头增强功能之间的差异_10706790.md`
  - `UDG头增强功能专题/特性映射_57402091.md`
