# Batch-06: 重定向族（HTTP重定向 / DNS纠错 / Portal / WebProxy）

> 批次 06 | 主题：REDIRECT 动作的多种实现机制 | 来源：GWFD-110284/110283/110281/110282 feature-knowledge | 特性数 4 | 核心度 ★★★★★（访问限制三大动作中 REDIRECT 的全部实现）

---

## 1. 概述

重定向（REDIRECT）是访问限制场景中最复杂的动作类别——同一个业务目标（"把用户引导到指定服务器/页面"）有**四种不同的协议层实现**，各适用于不同场景。本批次归纳四种重定向机制的共性接口与差异维度。

**族内特性**：

| 特性 | 中文名 | 重定向层级 | 协议层 | License |
|------|--------|-----------|--------|---------|
| GWFD-110284 | HTTP 智能重定向 | **L7 HTTP 响应改写** | HTTP1.x | 82209783 SHPR01 |
| GWFD-110283 | DNS 纠错 | **DNS 解析层 DNS Overwriting** | DNS（UDP 53） | 82209782 DNSO01 |
| GWFD-110281 | 用户 Portal | **L7 HTTP 重定向到 Portal Server** | HTTP1.x/WAP | 82209780 CPPT01 |
| GWFD-110282 | Web Proxy | **L3 IP NAT 重定向到 Proxy** | TCP/IP（NAT） | 82209781 WEBP01 |

---

## 2. 核心知识点（KP）

### KP-1 重定向族的四种层级实现（归纳各特性原理章节）

```
用户访问 → [各层级介入点]
                  ↓
    ┌─────────────────────────────────────────────────────┐
    │ 1. DNS 解析层（最早介入，用户还未建立 TCP）           │
    │    GWFD-110283 DNS纠错：DNS Overwriting              │
    │    构造新的 DNS 响应，IP 指向第三方 Platform          │
    ├─────────────────────────────────────────────────────┤
    │ 2. L3 IP NAT 层（透明代理，用户无感知）               │
    │    GWFD-110282 WebProxy：替换目的 IP 为 Proxy IP      │
    │    报文走 Proxy Server，由 Proxy 决定访问             │
    ├─────────────────────────────────────────────────────┤
    │ 3. L7 HTTP 响应层（用户已建立 TCP，重写 HTTP 响应）   │
    │    GWFD-110284 HTTP智能重定向：301/302/303 重定向     │
    │    基于错误码/URL/UserAgent/ContentType 触发          │
    ├─────────────────────────────────────────────────────┤
    │ 4. L7 HTTP Portal 层（重定向到特定 Portal 服务器）    │
    │    GWFD-110281 用户Portal：captive/non-captive 交替  │
    │    定时重定向到个人门户，用户可订购/管理业务           │
    └─────────────────────────────────────────────────────┘
                  ↓
            用户访问目标服务器/页面
```

**介入时机对比**：DNS纠错（最早）→ WebProxy（建立TCP时）→ HTTP智能重定向（HTTP响应时）→ 用户Portal（定时主动触发）

---

### KP-2 重定向族共用的"服务器集群"机制——IP Farm（来自 110281/110282 §4.2）

Portal 和 WebProxy 共用 **IP Farm** 机制：

| 维度 | 机制 |
|------|------|
| **IP Farm 定义** | 若干个重定向目标服务器的集合 |
| **负荷分担方式（LBMETHOD）** | ROUND_ROBIN（轮询）/ LEAST_RECENTLY_USED（最久未用）/ LEAST_LOAD（最小负荷，默认） |
| **心跳检测** | UDG 定时发送 ICMP 报文，UP↔DOWN 状态切换由 `HEALTHSUCCLIMIT`/`HEALTHFAILLIMIT` 控制 |
| **心跳接口** | 每个 IP Farm 绑定一个逻辑接口（`LOGICINF`），不同 IP Farm 必须用不同接口 |
| **全部 DOWN 处理** | Portal 默认 BLOCK；WebProxy 不做重定向（业务按原路径走） |
| **告警** | ALM-81034 IPFarm无可用server / ALM-81035 IPFarm服务器无响应 |
| **规格** | 整机 64 个 IP Farm，每个 IP Farm 512 个 IP |

**关键差异**：
- Portal 的 IP Farm 服务器类型 = `REDIRECT`（仅做重定向）
- WebProxy 的 IP Farm 服务器类型 = `REDIRECT`，但会做目的 IP NAT

---

### KP-3 重定向族的 RULE POLICYTYPE 差异化（来自各特性 §4 配置章节）

每个重定向特性用不同的 `POLICYTYPE` 触发：

| 特性 | RULE POLICYTYPE | POLICYNAME 指向的对象 | 独有配置对象 |
|------|----------------|---------------------|-------------|
| HTTP 智能重定向（110284） | `SMARTREDIRECT` | `SMARTHTTPREDIR` | `SMARTHTTPREDIR` + `REDIRAPPENDINFO` + `EXTENDEDFILTER` + `ERRORCODE` |
| DNS 纠错（110283） | `SMARTREDIRECT`（与 HTTP 重定向共用！） | `DNSOVERWRITING` | `DNSOVERWRITING` + `EXTENDEDFILTER` + `ERRORCODE` |
| 用户 Portal（110281） | `PCC`（含 captive 配置在 USERPROFILE） | `PCCPOLICYGRP` | `IPFARM` + `IPFARMSERVER` + `IPFARMGLOBAL` + `LOGICINF` |
| Web Proxy（110282） | `WEBPROXY` | `IPFARM`（IP Farm 名） | 同 Portal + WEBPROXY 独有的 NAT 行为 |

**关键发现**：HTTP 智能重定向和 DNS 纠错**共用 POLICYTYPE=SMARTREDIRECT**，区分点在 `POLICYNAME` 指向的对象类型（SMARTHTTPREDIR vs DNSOVERWRITING）。

---

### KP-4 重定向族共用的扩展过滤器 EXTENDEDFILTER（来自 110284/110283 §4.2）

HTTP 智能重定向和 DNS 纠错都使用 `EXTENDEDFILTER` 做七层匹配：

| 特性 | EXTENDEDFILTER 匹配维度 |
|------|------------------------|
| HTTP 智能重定向 | URL / USERAGENT / ERRORCODE / CONTENTTYPE / URLPOSTFIX |
| DNS 纠错 | URL（域名）+ ERRORCODE |

EXTENDEDFILTER 通过 `EXTFLTTYPE1=AND/OR, EXTFLTNAME1=...` 实现多条件逻辑组合。

**ERRORCODE 命令**（`ADD ERRORCODE`）也是两者共用：
- HTTP 智能重定向：错误码范围（如 `GT 400`）
- DNS 纠错：DNS 错误码（如 `EQUAL 3` NXDOMAIN）

---

### KP-5 HTTP 智能重定向的"多条件触发"维度（来自 110284 §3）

HTTP 智能重定向是**触发条件最丰富**的重定向特性，支持 6 种应用场景：

| 场景 | 触发条件 |
|------|----------|
| URL 错误重定向 | URL 不存在/不正确 |
| URL 过滤重定向 | 匹配 URL 过滤条件 |
| 内容类型过滤重定向 | HTTP content-type 匹配 |
| URL 后缀过滤重定向 | url-postfix 扩展名匹配 |
| 终端类型过滤重定向 | user-agent 浏览器类型匹配 |
| 错误码自动重定向 | HTTP 响应码 400-1000 范围 |

**携带信息**：重定向报文可携带 `REQURLFLAG`（初始请求URL）、`IMSIFLAG`、`IMEIFLAG`、用户IP等（通过 `ADD REDIRAPPENDINFO` 配置）——与头增强的插入字段语义相近但实现不同。

---

### KP-6 用户 Portal 的 captive/non-captive 交替机制（来自 110281 §4.1）

Portal 是唯一具有**周期性触发**特征的重定向特性：

```
用户首次访问 HTTP
    ↓ captive 模式
UDG 构造 301/302/303 重定向到 Portal Server
    ↓ 启动 CAPMODETHRES 定时器
进入 non-captive 模式（定时器超时前不重定向）
    ↓ 用户正常访问业务
定时器超时
    ↓
再次进入 captive 模式（下一次 HTTP 请求被重定向）
```

`CAPMODETHRES` 配置在 `USERPROFILE` 上（分钟级），是 Portal 区别于其他重定向特性的核心参数。

---

## 3. 关键发现（跨特性横向归纳）

### 发现-1 REDIRECT 动作的四种实现矩阵

| 维度 | HTTP智能重定向 | DNS纠错 | 用户Portal | WebProxy |
|------|---------------|---------|-----------|----------|
| **协议层** | L7 HTTP 响应 | DNS 解析层 | L7 HTTP 请求 | L3 IP NAT |
| **改写对象** | HTTP 响应报文 | DNS 响应报文 | HTTP 响应（301/302/303） | IP 报文目的IP |
| **触发时机** | HTTP 错误码 / 多条件匹配 | DNS 查询失败 | 用户 HTTP 请求（captive周期） | TCP SYN 匹配规则 |
| **用户感知** | 跳转到新页面 | 跳转到新页面 | 跳转到 Portal | **透明（用户无感知）** |
| **目标服务器** | 第三方服务器 | 第三方 Platform | Portal Server（业务订购/管理） | Proxy Server（加速/病毒防护） |
| **典型用途** | URL纠错、内容过滤 | 错误域名引导 | 业务订购、广告推送 | 网络加速、内容过滤 |
| **POLICYTYPE** | SMARTREDIRECT | SMARTREDIRECT | PCC（USERPROFILE captive） | WEBPROXY |
| **IP Farm** | 不用 | 不用 | 用 | 用 |
| **EXTENDEDFILTER** | 用（多维度） | 用（URL） | 不用 | 不用 |
| **依赖 SA** | SA-Basic + SA-Web Browsing | SA-Basic + SA-Network Administration | SA-Basic + SA-Web Browsing + SA-Mobile | SA-Basic |
| **协议限制** | HTTP1.x（不支持 HTTPS/HTTP2.0） | UDP DNS（不支持 TCP DNS） | HTTP1.x/WAP（不支持 HTTPS） | TCP（无协议限制，纯IP层） |

---

### 发现-2 重定向族 ConfigObject 复用矩阵

| ConfigObject | HTTP智能重定向 | DNS纠错 | 用户Portal | WebProxy | 复用情况 |
|--------------|---------------|---------|-----------|----------|---------|
| `FILTER`/`FLOWFILTER`/`FLTBINDFLOWF` | ✓ | ✓ | ✓ | ✓ | **场景级共用** |
| `L7FILTER`/`PROTBINDFLOWF` | 可选 | ✗ | ✓ | ✗ | ADC/头增强也用 |
| `EXTENDEDFILTER` | ✓（多维度） | ✓（URL） | ✗ | ✗ | **重定向族独有共用** |
| `ERRORCODE` | ✓（HTTP错误码） | ✓（DNS错误码） | ✗ | ✗ | **重定向族独有共用** |
| `IPFARM`/`IPFARMSERVER`/`IPFARMGLOBAL`/`LOGICINF` | ✗ | ✗ | ✓ | ✓ | **Portal/WebProxy 独有共用** |
| `SMARTHTTPREDIR` | ✓ | ✗ | ✗ | ✗ | HTTP重定向独有 |
| `DNSOVERWRITING` | ✗ | ✓ | ✗ | ✗ | DNS纠错独有 |
| `REDIRAPPENDINFO` | ✓ | ✗ | ✗ | ✗ | HTTP重定向独有 |
| `URR`/`URRGROUP`/`PCCPOLICYGRP` | 可选 | 可选 | ✓ | ✓ | 场景级共用 |
| `RULE`（SMARTREDIRECT/PCC/WEBPROXY） | SMARTREDIRECT | SMARTREDIRECT | PCC | WEBPROXY | **RULE.POLICYTYPE 是关键差异** |
| `USERPROFILE`/`RULEBINDING`/`APN` | ✓ | ✓ | ✓（含CAPMODETHRES） | ✓（含CAPMODETHRES） | 场景级共用 |

---

### 发现-3 重定向族独有 MML 命令清单（区分场景级共用）

**重定向族独有命令**：
| 命令 | 所属特性 |
|------|----------|
| `ADD SMARTHTTPREDIR` | HTTP 智能重定向 |
| `ADD REDIRAPPENDINFO` | HTTP 智能重定向 |
| `ADD DNSOVERWRITING` | DNS 纠错 |
| `SET IPFARMGLOBAL` | Portal / WebProxy |
| `ADD IPFARM` / `ADD IPFARMSERVER` | Portal / WebProxy |
| `ADD LOGICINF` | Portal / WebProxy（心跳检测接口） |
| `ADD BLACKLISTRULE` | WebProxy（黑名单规则） |

**重定向族共用命令**：
- `ADD EXTENDEDFILTER`（HTTP重定向 + DNS纠错）
- `ADD ERRORCODE`（HTTP重定向 + DNS纠错）

**场景级共用命令**（与其他动作共用）：
- `SET LICENSESWITCH` / `SET REFRESHSRV`
- `ADD FILTER` / `ADD FLOWFILTER` / `ADD FLTBINDFLOWF`
- `ADD URR` / `ADD URRGROUP` / `ADD PCCPOLICYGRP`
- `ADD RULE` / `ADD USERPROFILE` / `ADD RULEBINDING` / `ADD APN`

---

### 发现-4 重定向族的协议层互斥关系

族内特性对加密协议（HTTPS/HTTP2.0）的支持普遍受限：

| 特性 | HTTPS 支持 | HTTP2.0 支持 | 互斥特性 |
|------|-----------|-------------|----------|
| HTTP 智能重定向 | **不支持** | **不支持** | HTTP2.0 Host识别、HTTPS业务地址识别 |
| DNS 纠错 | N/A（DNS独立） | N/A | 仅支持 UDP DNS（不支持 TCP DNS） |
| 用户 Portal | **不支持** | **不支持** | HTTP2.0 Host识别、HTTPS业务地址识别 |
| Web Proxy | 支持（IP NAT 不依赖L7解析） | 支持 | 无（纯L3，不涉及L7解析） |

**关键启示**：**仅 WebProxy 能处理加密协议**（因其在 L3 工作，不解析 L7 内容）。其他三个重定向特性均依赖 L7 解析，受加密协议限制。这是访问限制场景设计时选择重定向方式的关键考量。

---

### 发现-5 重定向映射到访问限制三种动作

| 访问限制动作 | 重定向族如何贡献 |
|-------------|----------------|
| **REDIRECT（重定向）** | **直接核心动作**：族内所有特性本身就是 REDIRECT 的不同实现 |
| **DISCARD（阻塞）** | 间接贡献：Portal 全部 DOWN 时 `DEFAULTACT=BLOCK`；WebProxy 全部 DOWN 时业务报文可能被丢弃 |
| **HEADEN（头增强）** | 间接贡献：HTTP 智能重定向可通过 `REDIRAPPENDINFO` 携带 MSISDN/IMSI/IMEI 等字段（语义类似头增强但实现不同） |

---

## 4. 配置对象/命令复用清单（汇总）

### 重定向族独有配置对象（按特性）
- HTTP 智能重定向：`SMARTHTTPREDIR` + `REDIRAPPENDINFO`
- DNS 纠错：`DNSOVERWRITING`
- Portal：`IPFARMGLOBAL` + `IPFARM` + `IPFARMSERVER` + `LOGICINF`
- WebProxy：同 Portal + `BLACKLISTRULE`

### 重定向族共用配置对象
- `EXTENDEDFILTER`（HTTP重定向 + DNS纠错）
- `ERRORCODE`（HTTP重定向 + DNS纠错）

### 场景级共用配置对象
- 三四层：`FILTER` → `FLOWFILTER` → `FLTBINDFLOWF`
- 策略载体：`URR` → `URRGROUP` → `PCCPOLICYGRP`
- 规则绑定：`RULE`（POLICYTYPE 差异化） → `USERPROFILE` → `RULEBINDING` → `APN`

### License
- HTTP 智能重定向：`82209783 LKV3G5SHPR01`
- DNS 纠错：`82209782 LKV3G5DNSO01`
- 用户 Portal：`82209780 LKV3G5CPPT01`
- Web Proxy：`82209781 LKV3G5WEBP01`

---

## 5. 来源

- 主：
  - `feature-knowledge/GWFD-110284-HTTP智能重定向.md`
  - `feature-knowledge/GWFD-110283-DNS纠错.md`
  - `feature-knowledge/GWFD-110281-用户Portal.md`
  - `feature-knowledge/GWFD-110282-WebProxy.md`
- 横向对比：各特性 §10 "访问限制场景中的角色"
