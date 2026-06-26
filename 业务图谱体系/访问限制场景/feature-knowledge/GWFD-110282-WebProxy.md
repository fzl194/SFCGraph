# GWFD-110282 Web Proxy 知识文档

> 访问限制场景 | 代理重定向特性（轨道B：WEBPROXY独立体系，L3 IP NAT） | UDG | 来源：特性概述+实现原理+配置+调测+参考信息+参数调整 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110282 |
| feature_name | Web Proxy |
| feature_group | Portal |
| parent_feature_id | -（配置树无显式独立父节点；业务上归属"业务感知功能 → 智能策略控制功能 → 重定向族"分支；PCC触发链父为 GWFD-020351 PCC基本功能） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["重定向动作触发(POLICYTYPE=WEBPROXY 与 PCC 联动)", "IP Farm负荷分担方式(ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD)", "NAT地址转换方向(上行目的IP→ProxyIP / 下行源IP→WebIP)", "代理服务器检测(ICMP心跳 UP/DOWN)", "无法重定向时缺省动作(报文丢弃/重新选server)", "在线用户server切换(软参 BIT596 控制)", "多WebProxy策略支持(软参 BIT1541 控制)", "动作优先级(系统固定优先级 vs Rule PRIORITY)", "IP版本(IPv4/IPv6)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110282-01, EV-FK-AC-110282-02, EV-FK-AC-110282-03, EV-FK-AC-110282-04, EV-FK-AC-110282-05]（P4建06-evidence-index时确定，先用占位） |
| license_required | `82209781 LKV3G5WEBP01 Web Proxy` |

> **动作轨道归类结论（轮1三轨体系的补充确认）**：WebProxy 属于 **轨道B（WEBPROXY独立体系，L3 IP NAT方式）**，与 GWFD-110471 URL过滤（CFTEMPLATE/CONTCATEGBIND.ACTION）同属轨道B（独立动作机制，非PCC/SMARTREDIRECT），但实现层级不同。关键证据：`ADD RULE:POLICYTYPE=WEBPROXY`（配置Web Proxy文档任务示例明确），`POLICYNAME` 指向 IP Farm（`farm_test`）；动作机制为 **L3 IP NAT** —— UDG 将报文**目的 IP 地址替换为代理服务器 IP**（上行），将**源 IP 地址还原回 Web 服务器 IP**（下行），对用户透明。与用户Portal（POLICYTYPE=SMARTREDIRECT，L7 URL 重写）属不同轨道。**关键区别**：IP重定向不转换目的 IP 直接转发，WebProxy 转换目的 IP（NAT方式）。

---

## 1. 概述

### 1.1 特性定义（是什么）

UDG 可以把用户的浏览页面请求进行 **IP 重定向到指定代理服务器（Proxy Server）**，通过代理服务器实现**网络访问加速或病毒防护**。

**工作机制（核心）**：当用户业务流触发匹配的 Rule（POLICYTYPE=WEBPROXY）后，UDG 将报文**目的 IP 地址替换为代理服务器的 IP 地址**（上行 NAT），并将响应报文**源 IP 地址还原回原始 Web 服务器 IP 地址**（下行反向 NAT），对用户透明。代理服务器收到报文后执行加速或病毒防护处理，再将响应返回 UDG。

**WebProxy 与 IP 重定向的主要区别（产品文档原文）**：IP 重定向业务流程中 UDG **不会**将目的 IP 地址转换为代理服务器的 IP 地址，而是直接转发报文，所以 IP 重定向更适用于直连网络的应用场景；WebProxy 会转换目的 IP（NAT方式），更适用于需要代理服务器介入处理的场景。

> SourcePath: `UDG特性指南/智能策略控制功能/GWFD-110282 Web Proxy/GWFD-110282 Web Proxy特性概述_66666840.md` §定义、§原理概述
> SourcePath: `实现原理_74004639.md` §末尾说明

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 对用户业务流进行三四层匹配和规则匹配，将匹配 WEBPROXY 规则的报文目的 IP 替换为代理服务器 IP，实现重定向到 Proxy Server |
| Proxy Server | 代理服务器（第三方） | 无特殊要求 | 接收 UDG 重定向的业务流，实现网络访问加速和病毒防护 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §适用NF、§可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布 |

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §发布历史

### 1.4 License

- **License控制项**：`82209781 LKV3G5WEBP01 Web Proxy`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §可获得性

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 实现网络访问加速，提高收入；实现病毒防护，提高网络安全 |
| 用户 | 网络访问速度加快，提高用户体验 |

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §客户价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| 网络访问加速 | 通过 Proxy Server 缓存和优化，提高用户访问网页速度 |
| 病毒防护 | Proxy Server 对业务流进行病毒检测和过滤，提高网络安全 |

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §应用场景

### 1.7 前置条件与依赖

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|----------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | UDG 需要对用户的 Web Proxy 业务进行解析以获得 Web Proxy 动作和重定向地址，启用本特性前需先启用 SA 特性 |
| 触发依赖 | GWFD-020351 PCC 基本功能 | 82209825 LKV3G5PCCB01 PCC 基本功能 | RULE.POLICYTYPE=WEBPROXY 与 PCC 规则协同（rule_test2 POLICYTYPE=PCC 负责计费），PCC 触发链为访问限制通用骨架 |

**前置条件**：
- 已完成加载 License（LKV3G5WEBP01）
- UDG 与周边网元的互通配置已完成
- 已完成 SA-Basic 特性激活

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §与其他特性的交互
> SourcePath: `配置Web Proxy_66987339.md` §必备事项

### 1.8 对系统的影响

需要替换大量报文的 IP 地址时，**系统吞吐量将下降**。

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §对系统的影响

### 1.9 应用限制

- 在配置多个 Server IP 的场景下，如果出现链路、Server 或者网关设备故障导致心跳中断，UDG 会为业务流**重新选择 server IP**，这样可能会引起**老的业务流访问受影响**
- IPv4/IPv6 一致性约束：IPv4 规则下 IP Farm、Virtual IP、VPN、Server IP、心跳检测接口 IP、Filter 都必须使用 IPv4 形式；IPv6 同理

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §应用限制
> SourcePath: `配置Web Proxy_66987339.md` §数据 说明

### 1.10 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 支持的 IP Farm 个数（整机） | 64 |
| 每个 IP Farm 中支持的 IP 地址个数（整机） | 512 |

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| 3GPP | 23.214 | Architecture enhancements for control and user plane separation of EPC nodes |
| 3GPP | 29.244 | Interface between the Control Plane and the User Plane of EPC Nodes |
| IETF RFC | 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |
| IETF RFC | 3022 | Traditional IP Network Address Translator (Traditional NAT) |

> 说明：**RFC 3022（Traditional NAT）** 是 WebProxy L3 IP NAT 机制的核心标准依据，区别于用户Portal 的 HTTP 重定向标准。
> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §遵循标准

### 1.12 计费与话单

**本特性不涉及计费与话单**（NAT 动作本身不计费；如需对 WebProxy 业务计费，通过 rule_test2 POLICYTYPE=PCC + URR/URRGROUP 实现）。

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §计费与话单

---

## 2. 激活（License开启命令）

> 本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + IP Farm + WEBPROXY规则 + 用户模板"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5WEBP01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5WEBP01";
```

> SourcePath: `配置Web Proxy_66987339.md` §任务示例
> SourcePath: `调测Web Proxy_66987340.md` §操作步骤1

---

## 3. 原理

### 3.1 实现原理：L3 IP NAT 双向地址转换

WebProxy 的核心机制是 **L3 IP NAT（Network Address Translation，RFC 3022）**：

| 方向 | UDG 转换动作 | 原地址 | 转换后地址 |
|------|-------------|--------|-----------|
| **上行（MS/UE → Proxy）** | 目的 IP 替换 | Web Server IP（用户原始请求目的IP） | Proxy Server IP（IP Farm 选定的代理服务器IP） |
| **下行（Proxy → MS/UE）** | 源 IP 还原 | Proxy Server IP（代理服务器响应源IP） | Web Server IP（还原为用户期望的Web服务器IP） |

**对用户透明**：MS/UE 始终认为在与 Web Server 通信，感知不到 Proxy Server 的存在。

**与 IP 重定向的本质区别**：
- **IP 重定向**：UDG **不转换**目的 IP，直接转发报文到代理服务器（适用于直连网络）
- **WebProxy**：UDG **转换**目的 IP 为代理服务器 IP（NAT 方式，适用于需要代理介入的场景）

> SourcePath: `实现原理_74004639.md` §末尾说明
> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §定义

### 3.2 代理服务器选择机制（IP Farm 负荷分担）

若干个代理服务器的集合称为 **IP Farm**。UDG 的重定向功能会将用户报文重定向到 IP Farm 中指定服务器上，对于不同的用户报文，可以选择不同的服务器作为重定向的目的地。为平衡代理服务器负荷，需要在一个 IP Farm 内对服务器进行负荷分担：

| 负荷分担方式（LBMETHOD） | 说明 |
|--------------------------|------|
| ROUND_ROBIN | 轮询方式 |
| LEAST_RECENTLY_USED | 选择最久未被使用的 server |
| LEAST_LOAD | 选择最小负荷 server |

具体模式通过 `SET IPFARMGLOBAL` 命令配置。

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §原理概述

### 3.3 代理服务器检测机制（ICMP 心跳检测）

UDG 定时向 IP Farm 中的服务器发送 ICMP 报文，服务器收到报文后会对 UDG 做出应答：

- **UP 判定**：UDG 在设置时间内收到服务器应答
- **DOWN 判定**：UDG 在设置时间内连续收不到响应
- **UP→DOWN**：处于 UP 状态的服务器心跳检测连续失败次数达到 `HEALTHFAILLIMIT` 门限 → 状态转化为 DOWN；**如果 IP Farm 内所有服务器状态都为 DOWN，则不会对报文做重定向动作**
- **DOWN→UP**：处于 DOWN 状态的服务器心跳检测连续成功次数达到 `HEALTHSUCCLIMIT` 门限 → 状态转化为 UP
- **服务器 DOWN 时报文处理**：在报文需要被重定向时，负荷分担功能只会选择状态为 UP 的服务器作为重定向地址；如果有用户选定某个服务器为重定向地址，而该服务器的状态变为 DOWN，**此业务的报文将会被丢弃**，后续的新业务将会重新选择状态为 UP 的服务器作为重定向地址

不论服务器的状态是 UP 还是 DOWN，UDG 都会持续不断地向其发送 ICMP 报文，更新服务器的状态。

**心跳检测接口要求**：
- 在做心跳检测时，需要为不同 IP Farm 下的服务器配置不同的心跳检测接口
- 接口与 IP Farm 绑定，作为发送心跳检测消息的源地址
- **建议**：心跳检测的源地址采用 UDG 上配置的 Loopback 接口地址，该地址取自 UDG 地址池中的一个地址，地址池配置时需要预留一个地址用于 IP Farm 心跳检测

> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §原理概述

### 3.4 关键信元与协议交互（L3 IP NAT 报文级）

#### 3.4.1 TCP SYN 阶段（连接建立的 NAT 触发点）

WebProxy 的 NAT 在 **TCP SYN 报文**阶段即触发：
1. MS/UE 发送 TCP SYN 到 PGW-U/UPF（目的 IP = Web Server IP）
2. TCP SYN 触发 PGW-U/UPF 匹配 RULE 成功（POLICYTYPE=WEBPROXY）
3. PGW-U/UPF 执行 WebProxy 重定向动作：**将目的 IP 地址转换为代理服务器 IP 地址**
4. PGW-U/UPF 将 TCP SYN 发送给代理服务器（目的 IP = Proxy IP）

#### 3.4.2 TCP ACK 阶段（下行源 IP 还原）

1. 代理服务器收到 TCP SYN，接受请求，向 PGW-U/UPF 回应 TCP ACK（源 IP = Proxy IP）
2. PGW-U/UPF **将源 IP 地址转换为 Web 服务器的 IP 地址**，向 MS/UE 回应 TCP ACK（源 IP = Web Server IP）

#### 3.4.3 HTTP 请求/响应阶段（持续 NAT）

- **上行 HTTP 请求**：MS/UE 发起 HTTP 请求（目的 IP = Web Server IP）→ PGW-U/UPF 将目的 IP 转换为代理服务器 IP，发送给代理服务器
- **可选**：代理服务器与 Web 服务器进行交互，执行 HTTP 代理处理功能（加速/病毒防护）
- **下行 HTTP 响应**：代理服务器回复 HTTP 响应（源 IP = Proxy IP）→ PGW-U/UPF 将源 IP 转换回 Web 服务器 IP，发送给 MS/UE

#### 3.4.4 动作优先级（系统固定，非 Rule PRIORITY）

**重要约束**：如果针对同一个业务流配置不同的动作策略，系统根据**固定的动作优先级**执行策略，**不会根据 Rule 中配置的 PRIORITY 进行策略执行**。这意味着 Rule 的 PRIORITY 参数在 WebProxy 场景下不决定执行顺序。

> SourcePath: `配置Web Proxy_66987339.md` §数据 说明（PRIORITY 字段）
> SourcePath: `实现原理_74004639.md` §9步业务流程

### 3.5 业务流程（端到端 L3 IP NAT 交互）

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. TCP 连接建立触发（关键：NAT 在 SYN 阶段即触发）                │
│    MS/UE → PGW-U/UPF：TCP SYN（目的IP=Web Server IP）            │
│    TCP SYN 触发 PGW-U/UPF 匹配 rule_test1 成功                   │
│    rule_test1: POLICYTYPE=WEBPROXY, POLICYNAME=farm_test         │
│    PGW-U/UPF 执行 WebProxy 重定向：目的IP → Proxy IP              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. PGW-U/UPF 将 TCP SYN 发送给代理服务器（目的IP=Proxy IP）       │
│    从 IP Farm（farm_test）按 LEAST_LOAD 选 Proxy Server           │
│    （如 192.168.253.253）                                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. 代理服务器收到报文，接受请求                                   │
│    代理服务器 → PGW-U/UPF：TCP ACK（源IP=Proxy IP）              │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. PGW-U/UPF 将源 IP 转换为 Web 服务器 IP（下行反向 NAT）         │
│    PGW-U/UPF → MS/UE：TCP ACK（源IP=Web Server IP）              │
│    对 MS/UE 透明（MS/UE 认为在与 Web Server 通信）               │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. MS/UE 发起 HTTP 请求（目的IP=Web Server IP）                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. PGW-U/UPF 将目的 IP 转换为代理服务器 IP（上行 NAT）            │
│    将 HTTP 请求发送到代理服务器（目的IP=Proxy IP）                │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. 【可选】代理服务器与 Web 服务器进行交互                        │
│    执行 HTTP 代理处理功能（网络加速 / 病毒防护）                  │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 8. 代理服务器 → PGW-U/UPF：HTTP 响应（源IP=Proxy IP）            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 9. PGW-U/UPF 将源 IP 转换回 Web 服务器 IP（下行反向 NAT）         │
│    PGW-U/UPF → MS/UE：HTTP 响应（源IP=Web Server IP）            │
│    对 MS/UE 透明，用户看到正常的 Web Server 响应                 │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `实现原理_74004639.md` §9步业务流程

### 3.6 访问限制场景中的角色（三轨体系下的定位）

在访问限制场景（NS-03）中，WebProxy 作为**网络加速与代理重定向特性**，提供：

- **代理重定向动作**：基于三四层过滤条件将匹配的业务流透明代理到 Proxy Server，由 Proxy Server 执行加速或内容过滤（如病毒防护）
- **与 Portal/重定向的关系**：WebProxy 是 **L3/L4 重定向（IP NAT 方式，轨道B独立）**，与用户Portal（L7 URL 重写，轨道C SMARTREDIRECT）属不同层级。可作为 Portal 的代理前置节点，或作为透明代理实现访问控制（由 Proxy Server 决定放行/阻塞）
- **访问控制三种动作对应**：
  - **DISCARD（阻塞）**：当 IP Farm 全部服务器 DOWN，UDG 不做重定向（业务按原路径走）；也可结合 Proxy Server 实现阻塞
  - **HEADEN（头增强）**：WebProxy 不直接做头增强，但可与 GWFD-110261/262/263 头增强特性联动
  - **REDIRECT（重定向）**：本特性的核心动作，通过 `ADD RULE:POLICYTYPE=WEBPROXY` 实现 L3 IP 重定向（NAT方式，区别于 SMARTREDIRECT 的 URL 重写）

```
              【轨道A：三四层匹配，PCC体系（访问限制通用骨架）】
                    ↓
  ADD FILTER(L34PROTOCOL=TCP, SVRIP=192.168.10.123) → ADD FLOWFILTER → ADD FLTBINDFLOWF
                    ↓
  ADD USERPROFILE → ADD RULEBINDING
                    ↓
        会话命中 rule_test1 → 触发 WEBPROXY 动作
                    ↓
═══════════════════════════════════════════════════════
                    ↓
        【轨道B：WEBPROXY独立体系，L3 IP NAT 动作】
                    ↓
  TCP SYN 触发 → 上行目的IP 替换为 Proxy IP
                    ↓
  IP Farm 负荷分担选 Proxy Server → ICMP 心跳检测保活
                    ↓
  下行源IP 还原为 Web Server IP → 对用户透明
                    ↓
  执行 L3 IP NAT 重定向（访问限制"重定向族"成员，NAT级别）
```

> 说明：rule_test2 POLICYTYPE=PCC 与 rule_test1 POLICYTYPE=WEBPROXY 并列绑定到同一 USERPROFILE，PCC 规则负责计费属性，WEBPROXY 规则负责 NAT 重定向，两者协同。

---

## 4. 配置

### 4.1 配置对象总览

本特性配置分为三大块：**IP Farm 代理基础设施**、**三四层过滤条件（含 SVRIP）**、**WEBPROXY 规则与业务策略组合**。

#### 4.1.1 IP Farm 代理基础设施对象

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| IPFARMGLOBAL | （全局） | 整机 IP Farm 全局参数（服务器类型、心跳阈值、负荷分担方式） | SET IPFARMGLOBAL |
| LOGICINF | phif1/0/0 | IP Farm 心跳检测使用的逻辑接口（建议 Loopback） | ADD LOGICINF |
| IPFARM | farm_test | 重定向 IP Farm（代理服务器集合） | ADD IPFARM |
| IPFARMSERVER | （绑定到 farm_test） | IP Farm 下的代理服务器 IP | ADD IPFARMSERVER |

#### 4.1.2 三四层过滤条件对象（WebProxy 不需要 L7FILTER）

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| FILTER | filter_test | 三四层过滤条件（含 **SVRIP** 服务器 IP 匹配，关键差异） | ADD FILTER |
| FLOWFILTER | flow-l34 | 流过滤器 | ADD FLOWFILTER |
| FLTBINDFLOWF | （绑定关系） | Filter 与 FlowFilter 绑定 | ADD FLTBINDFLOWF |
| REFRESHSRV | （刷新） | 新配置的 Filter 置为生效 | SET REFRESHSRV |

> 说明：与用户Portal 不同，WebProxy **不需要** L7FILTER/PROTBINDFLOWF/SIGNATUREDB（仅三四层匹配 SVRIP 即可触发）。

#### 4.1.3 WEBPROXY 规则与业务策略组合对象

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| URR | cbb_test | 使用量上报规则（计费，rule_test2 用） | ADD URR |
| URRGROUP | cp_test | URR 组 | ADD URRGROUP |
| PCCPOLICYGRP | pcc-pg_test | PCC 策略组（绑定 URRGROUP，rule_test2 用） | ADD PCCPOLICYGRP |
| RULE（WEBPROXY） | rule_test1 | **WebProxy 重定向规则（POLICYTYPE=WEBPROXY）** | ADD RULE |
| RULE（PCC） | rule_test2 | 计费规则（POLICYTYPE=PCC） | ADD RULE |
| USERPROFILE | up_test | 用户模板（含 CAPMODETHRES） | ADD USERPROFILE |
| RULEBINDING | （绑定关系） | UserProfile 与 rule_test1/rule_test2 绑定 | ADD RULEBINDING |
| APN | apn-test | APN 配置 | ADD APN |

> SourcePath: `配置Web Proxy_66987339.md` §数据

### 4.2 配置流程

```
1. 打开 License 开关
   SET LICENSESWITCH:LICITEM="LKV3G5WEBP01",SWITCH=ENABLE

2. 配置整机 IP Farm 全局参数
   SET IPFARMGLOBAL（SERVERTYPE=REDIRECT、心跳阈值、LBMETHOD）

3. 配置 IP Farm 心跳检测接口（建议 Loopback）
   ADD LOGICINF

4. 配置 IP Farm
   a. ADD IPFARM（创建 IP Farm，绑定心跳检测接口）
   b. ADD IPFARMSERVER（添加代理服务器 IP）

5. 配置三四层过滤条件（关键：含 SVRIP 匹配）
   a. ADD FILTER（L34PROTOCOL=TCP, SVRIP=192.168.10.123）
   b. ADD FLOWFILTER
   c. ADD FLTBINDFLOWF
   d. SET REFRESHSRV:REFRESHTYPE=ALL

6. 配置计费属性（rule_test2 用）
   a. ADD URR
   b. ADD URRGROUP

7. 配置 PCC 策略组（rule_test2 用）
   ADD PCCPOLICYGRP

8. 配置业务规则
   a. ADD RULE rule_test1（POLICYTYPE=WEBPROXY, POLICYNAME=farm_test）
   b. ADD RULE rule_test2（POLICYTYPE=PCC, POLICYNAME=pcc-pg_test）

9. 配置业务策略组合
   a. ADD USERPROFILE
   b. ADD RULEBINDING（绑定 rule_test1 + rule_test2）
   c. ADD APN
```

> SourcePath: `配置Web Proxy_66987339.md` §操作步骤

### 4.3 任务实例（保留原始 MML）

**场景**：
- UDG 使用最小负荷 server 方式（LEAST_LOAD）实现 Web Proxy 功能
- UDG 将用户发往 `192.168.10.123` 服务器的 IPv4 报文重定向到 `192.168.253.251` 或 `192.168.253.253` 代理服务器
- UDG 与重定向服务器之间进行心跳检测

```mml
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5WEBP01",SWITCH=ENABLE;

// 配置整机的 Web Proxy 参数。
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=LEAST_LOAD;

// 配置 IP Farm 使用的心跳检测接口。
ADD LOGICINF:NAME="phif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.10.10.10",IPV4MASK1="255.255.255.255";

// 配置 IP Farm。
ADD IPFARM:HEALTHCHECKFLAG=ENABLE,IPFARMNAME="farm_test",IPVERSION=IPV4,INTERFACENAME="phif1/0/0";
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="192.168.253.251";
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="192.168.253.253";

// 配置 Web Proxy 业务使用的三四层过滤条件。
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IP,SVRIP="192.168.10.123",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0";
ADD FLOWFILTER:FLOWFILTERNAME="flow-l34";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flow-l34",FILTERNAME="filter_test";
SET REFRESHSRV:REFRESHTYPE=ALL;

// 配置 Web Proxy 业务使用的计费属性。
ADD URR:URRNAME="cbb_test",URRID=1000,USAGERPTMODE=ONLINE;
ADD URRGROUP:URRGROUPNAME="cp_test",UPURRNAME1="cbb_test",DOWNURRNAME1="cbb_test";

// 配置 Web Proxy 业务使用的 PCC 策略组。
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pcc-pg_test",URRGROUPNAME="cp_test";

// 配置 Web Proxy 业务使用的规则。
// rule_test1: POLICYTYPE=WEBPROXY（WebProxy L3 IP NAT 重定向，关键）
ADD RULE:RULENAME="rule_test1",POLICYTYPE=WEBPROXY,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flow-l34",PRIORITY=10,POLICYNAME="farm_test";

// rule_test2: POLICYTYPE=PCC（计费）
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,
FILTERINGMODE=FLOWFILTER,
FLOWFILTERNAME="flow-l34",PRIORITY=20,POLICYNAME="pcc-pg_test";

// 配置 Web Proxy 业务使用的业务策略组合。
ADD USERPROFILE:USERPROFILENAME="up_test",CAPMODETHRES=6;
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
ADD APN:APN="apn-test";
```

> SourcePath: `配置Web Proxy_66987339.md` §任务示例

### 4.4 关键 MML 命令列表

#### 4.4.1 IP Farm 相关命令

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开/关闭 License 开关 |
| SET IPFARMGLOBAL | 设置 IP Farm 全局参数（类型、心跳阈值、负荷分担方式） |
| ADD LOGICINF | 增加逻辑接口（心跳检测接口） |
| ADD IPFARM | 增加 IP Farm |
| ADD IPFARMSERVER | 增加 IP Farm 服务器 |
| ADD BLACKLISTRULE | 增加黑名单规则 |

#### 4.4.2 过滤条件相关命令

| 命令 | 用途 |
|------|------|
| ADD FILTER | 增加三四层过滤器（含 SVRIP 匹配） |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| SET REFRESHSRV | 业务刷新（Filter 生效） |

#### 4.4.3 规则与业务策略组合命令

| 命令 | 用途 |
|------|------|
| ADD URR | 增加使用量上报规则 |
| ADD URRGROUP | 增加 URR 组 |
| ADD PCCPOLICYGRP | 增加 PCC 策略组 |
| ADD RULE | 增加业务规则（POLICYTYPE=WEBPROXY 触发 WebProxy） |
| ADD USERPROFILE | 增加用户模板 |
| ADD RULEBINDING | 增加 UserProfile 与 Rule 绑定 |
| ADD APN | 添加 APN 配置 |

> SourcePath: `GWFD-110282 Web Proxy参考信息_77079754.md` §命令

### 4.5 关键参数说明

#### 4.5.1 SET IPFARMGLOBAL 参数

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| SERVERTYPE（服务器类型） | REDIRECT | 指定 IP Farm 全局配置的类型 |
| TIMETHRESHOLD（时间阈值秒） | 10 | 两次心跳检测间的时间阈值，单位秒 |
| HEALTHSUCCLIMIT（健康检查成功次数） | 2 | down 状态连续成功次数达此值 → 置为 up |
| HEALTHFAILLIMIT（健康检查失败次数） | 4 | up 状态连续失败次数达此值 → 置为 down |
| LBMETHOD（负载均衡模式） | LEAST_LOAD | 支持 ROUND_ROBIN / LEAST_RECENTLY_USED / LEAST_LOAD |

#### 4.5.2 ADD IPFARM 参数

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| HEALTHCHECKFLAG | ENABLE | 健康检查标记 |
| IPFARMNAME | farm_test | IP Farm 名称 |
| IPVERSION | IPV4 | IP 协议版本（IPV4/IPV6） |
| INTERFACENAME | phif1/0/0 | 心跳检测接口名称 |

#### 4.5.3 ADD FILTER 参数（WebProxy 关键：含 SVRIP 匹配）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| FILTERNAME | filter_test | 过滤器名称 |
| L34PROTTYPE | STRING | 三四层 IPv4 协议输入类型 |
| L34PROTOCOL | TCP | 三四层协议类型 |
| **SVRIPMODE** | **IP** | **服务器 IP 地址配置模式（WebProxy 关键，匹配目的服务器）** |
| **SVRIP** | **192.168.10.123** | **服务器 IP 地址（触发 WebProxy 的目的服务器 IP）** |
| **SVRIPMASKTYPE** | **IPTYPE** | **服务器 IP 地址掩码类型** |
| **SVRIPMASK** | **0.0.0.0** | **服务器 IP 地址反掩码（0.0.0.0 表示精确匹配）** |

> 说明：SVRIP 参数是 WebProxy 与用户Portal 过滤条件的核心差异 —— WebProxy 通过 SVRIP 精确匹配目的服务器，用户Portal 通过 L7FILTER URL 匹配。

#### 4.5.4 ADD RULE 参数（WEBPROXY 关键）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| RULENAME | rule_test1 | 规则名称 |
| POLICYTYPE | **WEBPROXY** | **策略类型=WEBPROXY 触发 WebProxy L3 IP NAT 重定向动作（轨道B）** |
| FILTERINGMODE | FLOWFILTER | 流过滤器或流过滤器组选择（FLOWFILTER / FLOWFILTERGRP） |
| FLOWFILTERNAME | flow-l34 | 流过滤器名称 |
| PRIORITY | 10 | 全局优先级（**注意：系统按固定动作优先级执行，不按此 PRIORITY**） |
| POLICYNAME | farm_test | 策略名称（WEBPROXY 下为 IP Farm 名称） |

#### 4.5.5 ADD USERPROFILE 参数

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| USERPROFILENAME | up_test | 用户模板名称 |
| CAPMODETHRES（Captive模式时间阈值，分） | 6 | 用户模板级 captive 定时器（WebProxy 场景下保留参数） |

> SourcePath: `配置Web Proxy_66987339.md` §数据

### 4.6 软参

| 软参 | 说明 |
|------|------|
| BIT596 | 控制是否支持根据业务配置切换在线用户 web proxy 的 server ip |
| BIT1541 | 控制一个用户是否支持多个 web proxy 策略 |

> SourcePath: `GWFD-110282 Web Proxy参考信息_77079754.md` §软参

### 4.7 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| IP 版本一致性 | IPv4 WebProxy 规则：IP Farm、Virtual IP、VPN、Server IP、心跳检测接口 IP、Filter 都必须使用 IPv4 形式；IPv6 同理。可通过 `DSP RULECHECK` 检查 |
| 心跳检测接口独立 | 不同 IP Farm 下的服务器必须配置不同的心跳检测接口 |
| 心跳检测地址预留 | 心跳检测源地址建议采用 UDG 上配置的 Loopback 接口地址，地址池配置时需预留一个地址用于 IP Farm 心跳检测 |
| 服务器状态门槛 | IP Farm 配置完成后，需保证至少有一个 server 状态为 up（`LST IPFARMSERVER` 验证） |
| 全部 DOWN 时不重定向 | 如果 IP Farm 内所有服务器状态都为 DOWN，则不会对报文做重定向动作（业务按原路径走） |
| 服务器 DOWN 时报文丢弃 | 用户选定的服务器状态变为 DOWN 后，此业务报文将被丢弃；后续新业务重新选 UP 服务器 |
| 多 Server 场景老业务影响 | 配置多个 Server IP 时，链路/Server/网关故障导致心跳中断，UDG 重新选 server IP，可能引起老业务流访问受影响 |
| 动作优先级（非 Rule PRIORITY） | 同一业务流配置不同动作策略时，系统按固定动作优先级执行，不按 Rule PRIORITY 执行 |
| SA-Basic 依赖 | 必须先启用 SA-Basic 特性（UDG 解析报文获得 WebProxy 动作和重定向地址的前提） |

---

## 5. 配置案例

### 5.1 场景一：基础 WebProxy 重定向（LEAST_LOAD，L3 IP NAT）

**场景描述**：UDG 使用最小负荷 server 方式实现 Web Proxy 功能。用户发往 `192.168.10.123` 服务器的 IPv4 报文被重定向到 `192.168.253.251` 或 `192.168.253.253` 代理服务器。UDG 与重定向服务器之间进行心跳检测。

**MML 命令序列**：见 §4.3 任务实例（原样保留产品文档）。

> SourcePath: `配置Web Proxy_66987339.md` §任务示例

### 5.2 场景二：负荷分担方式变体（ROUND_ROBIN 轮询）

**场景描述**：与场景一差异 —— 采用轮询方式选择代理服务器，适用于代理服务器性能均等场景。

**MML 命令序列（差异部分）**：

```
// 负载均衡模式改为 ROUND_ROBIN（轮询）
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=ROUND_ROBIN;
```

> 来源：基于 `GWFD-110282 Web Proxy特性概述_66666840.md` §原理概述（LBMETHOD 三选一）

### 5.3 场景三：负荷分担方式变体（LEAST_RECENTLY_USED 最近最少使用）

**场景描述**：与场景一差异 —— 选择最久未被使用的代理服务器。

**MML 命令序列（差异部分）**：

```
// 负载均衡模式改为 LEAST_RECENTLY_USED
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=LEAST_RECENTLY_USED;
```

> 来源：基于 §原理概述 LBMETHOD 选项

### 5.4 场景四：在线用户 Server 切换变体（软参 BIT596）

**场景描述**：控制是否支持根据业务配置切换在线用户 web proxy 的 server IP。启用后，业务配置变更可动态切换在线用户的代理服务器；禁用则保持原 server 不变（避免老业务流受影响）。

**软参配置（差异部分）**：

```
// 启用在线用户 server ip 切换（软参 BIT596）
// 具体设置命令以软参管理命令参考为准
// SET SOFTPARA:...BIT596=ENABLE;
```

> 说明：具体设置命令以 `BIT596` 软参管理命令参考为准。多 Server 场景下，启用切换可能影响老业务流（见 §1.9 应用限制）。
> SourcePath: `GWFD-110282 Web Proxy参考信息_77079754.md` §软参

### 5.5 场景五：多 WebProxy 策略变体（软参 BIT1541）

**场景描述**：控制一个用户是否支持多个 web proxy 策略。启用后，同一用户可绑定多个 WEBPROXY 规则（不同 SVRIP 触发不同代理服务器）；禁用则仅生效第一个策略。

**软参配置（差异部分）**：

```
// 启用多 web proxy 策略（软参 BIT1541）
// 具体设置命令以软参管理命令参考为准
// SET SOFTPARA:...BIT1541=ENABLE;
```

> SourcePath: `GWFD-110282 Web Proxy参考信息_77079754.md` §软参

### 5.6 场景六：IPv6 变体（IPv6 WebProxy 规则）

**场景描述**：配置 IPv6 WebProxy 规则，所有 IP 地址必须使用 IPv6 形式。

**MML 命令序列（差异部分）**：

```
// IPv6 心跳检测接口
ADD LOGICINF:NAME="phif1/0/0",IPVERSION=IPV6,IPV6ADDRESS1="FC00::10",IPV6MASK1=128;

// IPv6 IP Farm 与 Server
ADD IPFARM:HEALTHCHECKFLAG=ENABLE,IPFARMNAME="farm_test",IPVERSION=IPV6,INTERFACENAME="phif1/0/0";
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV6,SERVERIPV6="FC00:253::251";

// IPv6 Filter（SVRIP 为 IPv6）
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IP,SVRIP="FC00:10::123",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="::";

// 通过 DSP RULECHECK 检查 IPv6 一致性
DSP RULECHECK:RULENAME="rule_test1",POLICYTYPE=WEBPROXY;
```

> SourcePath: `配置Web Proxy_66987339.md` §数据 说明（IPv4/IPv6 一致性约束）

### 5.7 场景七：全部 DOWN 时不重定向变体（业务按原路径走）

**场景描述**：当 IP Farm 内所有代理服务器状态都为 DOWN 时，UDG **不对报文做重定向动作**（业务按原路径直接走）。这是产品文档明确的内置行为，无需额外配置。

**验证（无额外配置）**：

```
// 查询 IP Farm 内所有 server 状态
LST IPFARMSERVER:IPFARMNAME="farm_test";
// 若所有 server 状态为 down，UDG 不做 NAT 重定向，报文按原路径走
```

> 说明：此为产品文档明确的内置行为（§3.3）。区别于用户Portal 的 DEFAULTACT=BLOCK（阻塞），WebProxy 全部 DOWN 时是"不重定向"而非"阻塞"。
> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §原理概述

### 5.8 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| LEAST_LOAD（场景一） | SET IPFARMGLOBAL LBMETHOD | LBMETHOD=LEAST_LOAD | 代理服务器性能不均（默认/推荐） |
| ROUND_ROBIN（场景二） | SET IPFARMGLOBAL LBMETHOD | LBMETHOD=ROUND_ROBIN | 代理服务器性能均等 |
| LEAST_RECENTLY_USED（场景三） | SET IPFARMGLOBAL LBMETHOD | LBMETHOD=LEAST_RECENTLY_USED | 避免单台 server 空闲 |
| 在线用户切换（场景四） | 软参 BIT596 | BIT596=ENABLE | 动态切换在线用户 server ip |
| 多策略（场景五） | 软参 BIT1541 | BIT1541=ENABLE | 一个用户多个 web proxy 策略 |
| IPv6（场景六） | IPv6 命令 + DSP RULECHECK | IPVERSION=IPV6 | IPv6 用户面 |
| 全部 DOWN 不重定向（场景七） | （内置行为，无配置） | IP Farm 全 DOWN | 代理服务器全故障时业务保持 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商需要部署 Web Proxy 功能以达到网络加速效果时，需对 UDG 的 Web Proxy 功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 用户信息查询 | IMSI | 460000123456789 | 测试终端自带 |
| 测试终端使用的 APN | APN | apn-test | 已配置数据中获取 |
| WebProxy 触发地址 | 服务器 IP 地址（SVRIP） | 192.168.10.123 | 已配置数据中获取（FILTER） |
| WebProxy 目的地址 | 服务器 IPv4 地址（SERVERIPV4） | 192.168.253.251 / 192.168.253.253 | 已配置数据中获取（IPFARMSERVER） |

工具：测试终端、OM Portal、第三方抓包工具

> SourcePath: `调测Web Proxy_66987340.md` §必备事项

#### 6.1.3 调测执行步骤

**步骤1**：执行 `LST LICENSESWITCH` 查询 License 开关。

```
LST LICENSESWITCH:LICITEM="LKV3G5WEBP01";
```

预期输出（正常）：
```
-------------------------------
  License Item  =  LKV3G5WEBP01
  Switch        =  ENABLE
-------------------------------
---    END
```

判断：
- SWITCH=ENABLE → 步骤2
- SWITCH=DISABLE → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5WEBP01",SWITCH=ENABLE;` 打开开关

**步骤2**：打开接入侧/PDN 侧镜像接口上的抓包工具，准备抓取测试终端出入报文。

**步骤3**：测试终端使用 `apn-test` APN 接入网络。
- 成功接入 → 步骤4
- 无法接入 → 调测 UDG 的接入功能

**步骤4**：测试终端进行 Web 浏览业务，访问 `192.168.10.123` 网页，查看镜像接口抓包信息。

预期抓包行为（L3 IP NAT 验证关键）：
- **上行报文**：接入侧抓包目的 IP 应为 `192.168.10.123`（触发地址），**PDN 侧抓包目的 IP 应为 `192.168.253.253`**（重定向 server 地址，NAT 转换后）
- **下行报文**：PDN 侧抓包源 IP 应为 `192.168.253.253`，**接入侧抓包源 IP 应为 `192.168.10.123`**（源 IP 还原后）

判断：
- 接入侧/PDN 侧抓包结果与预期一致 → WebProxy 业务正常，调测结束
- 接入侧/PDN 侧抓包的目的 IP 与源 IP 一样 → 步骤5（NAT 未生效）
- 测试终端未看到任何页面 → 步骤7

**步骤5**：执行 `DSP SESSIONINFO` 查询用户上下文，确认 APN。

```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
```

预期输出：
```
-------------------------------
                           IMSI  =  460000123456789
                    APN name  =  apn-test
---    END
```

判断：
- APN 与规划值一致 → 步骤6
- APN 不一致 → 返回步骤3 使用规划 APN 重新接入

**步骤6**：检查 APN 下 WebProxy 业务相关配置。
- a. `LST RULEBINDING:USERPROFILENAME="up_test";`

预期输出：
```
-------------------------------
用户模板名称    规则名称       优先级       策略类型
 up_test       rule_test1    10          Web Proxy
 up_test       rule_test2    20          PCC
(结果个数 = 2)
---    END
```

- b. `LST RULE:RULENAME="rule_test1",POLICYTYPE=WEBPROXY;`

预期输出：
```
-------------------------------
                  规则名称  =  rule_test1
                  策略类型  =  Web Proxy
             流过滤器名称  =  flow-l34
                全局优先级  =  10
   Web Proxy IP-Farm名称  =  farm_test
---    END
```

- c. `LST PCCPOLICYGRP:PCCPOLICYGRPNM="pcc-pg_test";`

预期输出：
```
-------------------------------
       PCC策略组名称  =  pcc-pg_test
        计费属性名称  =  cp_test
---    END
```

- d. `LST FLOWFILTER` / `LST FLTBINDFLOWF` / `LST FILTER` 查询过滤器链

预期输出（节选）：
```
LST FILTER:FILTERNAME="filter_test";
                   过滤器名字  =  filter_test
       三四层IPv4协议输入类型  =  字符串类型
                三四层协议类型  =  TCP
                     服务器IP  =  192.168.10.123
                     生效标记  =  是
```

**步骤7**：执行 `LST IPFARM` / `LST IPFARMSERVER` 检查 IP Farm 中 server 状态。

```
LST IPFARM:IPFARMNAME="farm_test";
```

预期输出：
```
-------------------------------
       IP-Farm名称  =  farm_test
         服务器类型  =  重定向
       健康检查标记  =  使能
        IP协议版本  =  IPV4
   心跳检测接口名称  =  phif1/0/0
       接口IP地址  =  10.10.10.10
---    END
```

```
LST IPFARMSERVER:IPFARMNAME="farm_test";
```

预期输出：
```
----------------------------
   IP-Farm名称  =  farm_test
       地址信息  =  192.168.253.251
   请求URL携带标识  =  不使能
       服务器状态  =  up
   重定向缺省动作  =  block
(结果个数 = 1)
---    END
```

判断：需保证至少一个 server 状态为 up。

**步骤8**：执行 `LST LOGICINF:NAME="phif1/0/0";` 检查心跳检测接口配置。

预期输出：
```
-------------------------------
        逻辑接口名称  =  phif1/0/0
 逻辑接口的IPv4地址1  =  10.10.10.10
 逻辑接口的IPv4掩码1  =  255.255.255.255
---    END
```

**步骤9**：收集信息并寻求技术支持。
- a. 在镜像接口或服务器上开启抓包工具，执行步骤4 并保存报文
- b. 执行 `EXP MML` 命令将当前配置数据导出为 MML 脚本文件并保存
- c. 收集并保存上述所有查询信息
- d. 查看并收集对端设备配置及接口状态信息
- e. 收集归纳所有信息并联系华为技术支持解决

> SourcePath: `调测Web Proxy_66987340.md` §操作步骤

### 6.2 验证命令汇总

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询 License 开关状态 |
| DSP SESSIONINFO | 显示用户上下文，确认 APN |
| LST RULEBINDING | 查询 UserProfile 绑定的 Rule |
| LST RULE | 查询规则配置（含 Web Proxy IP-Farm 名称） |
| LST PCCPOLICYGRP | 查询 PCC 策略组 |
| LST URRGROUP | 查询 URR 组 |
| LST FLOWFILTER / LST FLTBINDFLOWF / LST FILTER | 查询过滤器链配置 |
| LST IPFARM / LST IPFARMSERVER | 查询 IP Farm 及 server 状态（含 up/down） |
| LST LOGICINF | 查询心跳检测接口配置 |
| DSP RULECHECK | 检查规则 IP 版本一致性 |
| EXP MML | 导出 MML 配置脚本（故障信息收集） |

> SourcePath: `调测Web Proxy_66987340.md`

### 6.3 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-81034 | IPFarm 无可用 server | IP Farm 内全部 server 状态为 down | WebProxy 不做重定向，业务按原路径走（不阻塞，区别于 Portal 的 BLOCK） |
| ALM-81035 | IPFarm 服务器无响应 | 服务器心跳检测失败（连续失败达 HEALTHFAILLIMIT） | 该 server 被排除出负荷分担候选 |

> SourcePath: `GWFD-110282 Web Proxy参考信息_77079754.md` §告警

### 6.4 测量指标

WebProxy 测量指标涵盖**上下行包数、千字节数、平均/峰值千字节速率**共 8 项：

| 指标ID | 指标名称 |
|--------|---------|
| 1914314604 | 用户平面 Web Proxy/负载均衡上行包数 |
| 1914314605 | 用户平面 Web Proxy/负载均衡下行包数 |
| 1914314606 | 用户平面 Web Proxy/负载均衡上行千字节数 |
| 1914314607 | 用户平面 Web Proxy/负载均衡下行千字节数 |
| 1914314608 | 用户平面 Web Proxy/负载均衡上行平均千字节速率 |
| 1914314609 | 用户平面 Web Proxy/负载均衡下行平均千字节速率 |
| 1914314610 | 用户平面 Web Proxy/负载均衡上行峰值千字节速率 |
| 1914314611 | 用户平面 Web Proxy/负载均衡下行峰值千字节速率 |

> 关键监控：上行/下行千字节速率（1914314608/4609）异常下降 → 提示代理服务器故障或 NAT 转换异常。
> SourcePath: `GWFD-110282 Web Proxy参考信息_77079754.md` §测量指标

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| WebProxy 未生效（报文按原路径走） | License 开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5WEBP01";` 确认 SWITCH=ENABLE |
| WebProxy 未生效 | IP Farm 内所有 server 状态为 down | `LST IPFARMSERVER` 查 server 状态；查 ALM-81034；产品文档明确：全 DOWN 时不重定向（业务按原路径走） |
| WebProxy 未生效 | SA-Basic 未激活（UDG 无法解析获得 WebProxy 动作） | 检查 SA-Basic License（82209749）；SA-Basic 是 WebProxy 的强依赖 |
| NAT 未转换（接入侧/PDN 侧 IP 一样） | rule_test1 POLICYTYPE 不是 WEBPROXY | `LST RULE:RULENAME="rule_test1",POLICYTYPE=WEBPROXY;` 确认 |
| NAT 未转换 | FILTER SVRIP 不匹配用户实际访问的目的 IP | `LST FILTER` 核对 SVRIP=192.168.10.123 与用户访问的目的 IP 一致；SVRIPMASK=0.0.0.0 精确匹配 |
| NAT 未转换 | FLOWFILTER 未绑定 FILTER | `LST FLTBINDFLOWF:FLOWFILTERNAME="flow-l34";` 确认绑定 |
| 用户选定 server DOWN 后报文被丢弃 | 服务器状态变为 DOWN，此业务报文丢弃（产品文档明确） | `LST IPFARMSERVER` 查 server 状态；属预期行为；后续新业务会重新选 UP server |
| 老业务流访问受影响 | 多 Server 场景下链路/Server/网关故障导致心跳中断，UDG 重新选 server IP | 产品文档应用限制；评估软参 BIT596（在线切换）是否启用 |
| IPv6 规则不生效 | IP 版本不一致 | `DSP RULECHECK:RULENAME="rule_test1",POLICYTYPE=WEBPROXY;` 检查一致性 |
| 动作优先级与预期不符 | 系统按固定动作优先级执行，非 Rule PRIORITY | 产品文档明确：Rule PRIORITY 不决定执行顺序；需调整动作策略配置而非 PRIORITY |
| 用户多策略不生效 | 一个用户不支持多个 web proxy 策略（软参 BIT1541 默认禁用） | 启用软参 BIT1541；`LST SOFTPARA` 确认 |
| PCC 触发链未生效 | rule_test2 POLICYTYPE 不是 PCC | `LST RULE:RULENAME="rule_test2",POLICYTYPE=PCC;` 确认 |
| 代理服务器收不到报文 | 心跳检测接口配置错误或 Loopback 地址不可达 | `LST LOGICINF` 确认接口；检查 Loopback 地址路由可达性 |
| 系统吞吐量下降 | 大量报文 IP 地址替换（NAT）消耗资源 | 产品文档声明：替换大量报文 IP 时吞吐量下降；评估硬件容量 |

---

## 7. 参考信息

### 7.1 与其他特性的关系（特性关系网）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG 解析报文获得 WebProxy 动作和重定向地址的基础 |
| PCC 基本功能 | GWFD-020351（UDG） | **触发依赖**：rule_test2 POLICYTYPE=PCC 负责计费属性，PCC 触发链为骨架 |
| 用户 Portal | GWFD-110281（UDG） | **互补（不同轨道）**：用户Portal 为 L7 URL 重写（轨道C SMARTREDIRECT），WebProxy 为 L3 IP NAT（轨道B）；可串联部署 |
| HTTP 智能重定向 | GWFD-110284（UDG） | **互补（不同轨道）**：HTTP智能重定向为轨道C SMARTREDIRECT，WebProxy 为轨道B |
| DNS 纠错 | GWFD-110283（UDG） | **互补（不同轨道）**：DNS纠错为轨道C，WebProxy 为轨道B |
| URL 过滤基本功能 | GWFD-110471（UDG） | **同轨道（B）**：URL过滤动作机制独立（CFTEMPLATE/CONTCATEGBIND.ACTION），与 WebProxy（WEBPROXY）同属轨道B，但实现层级不同 |
| HTTP 头增强 | GWFD-110261/262/263（UDG） | **配合关系**：WebProxy 不直接做头增强，可与头增强特性联动 |
| 增强的 ADC 基本功能 | GWFD-020357（UDG） | **互补关系**：ADC 提供应用级识别 |

> 说明：GWFD-110281/110284/110283/110261-263/020357/110471 的关系系基于访问限制场景动作语义（轨道A/B/C 三轨体系）+ 产品文档交互表推断。
> SourcePath: `GWFD-110282 Web Proxy特性概述_66666840.md` §与其他特性的交互

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110282 Web Proxy/GWFD-110282 Web Proxy特性概述_66666840.md` | 适用NF（PGW-U/UPF）、定义、客户价值、应用场景、可获得性（UDG 20.0.0+、License LKV3G5WEBP01）、与其他特性交互（SA-Basic依赖）、对系统影响（吞吐量下降）、应用限制（多Server场景老业务影响）、原理概述（IP Farm负荷分担+ICMP心跳检测+全DOWN不重定向）、计费与话单（不涉及）、特性规格（64 IP Farm/512 IP每组）、遵循标准（3GPP 23.214/29.244+RFC 2616/3022 NAT）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110282 Web Proxy/实现原理_74004639.md` | 9步完整业务流程（TCP SYN触发NAT→目的IP转Proxy IP→代理服务器回应→源IP还原Web IP→HTTP请求/响应持续NAT）、WebProxy与IP重定向区别（NAT vs 直接转发） |
| 3 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110282 Web Proxy/配置Web Proxy_66987339.md` | 9步操作流程、数据规划表（含SVRIP完整字段）、完整MML脚本（License+IPFARMGLOBAL+LOGICINF+IPFARM+IPFARMSERVER+FILTER(SVRIP)+FLOWFILTER+FLTBINDFLOWF+REFRESHSRV+URR+URRGROUP+PCCPOLICYGRP+RULE(WEBPROXY+PCC)+USERPROFILE+RULEBINDING+APN）、IPv4/IPv6一致性约束、动作优先级说明（系统固定，非Rule PRIORITY） |
| 4 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110282 Web Proxy/调测Web Proxy_66987340.md` | 9步调测流程（LST LICENSESWITCH→抓包→接入→访问192.168.10.123→抓包验证NAT上行目的IP=192.168.253.253/下行源IP还原→DSP SESSIONINFO→LST RULEBINDING/RULE/PCCPOLICYGRP/FLOWFILTER/IPFARM/IPFARMSERVER/LOGICINF→EXP MML）、各步骤预期输出样例（中文） |
| 5 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110282 Web Proxy/GWFD-110282 Web Proxy参考信息_77079754.md` | MML命令清单（15条核心）、告警（ALM-81034/ALM-81035）、软参（BIT596/BIT1541）、测量指标（8项，1914314604~4611） |
| 6 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110282 Web Proxy/调整Web Proxy参数/` 目录（5个子文档） | 修改IPFarm ServerIP/VIRTUALIP/心跳检测参数/心跳检测接口/负荷分担方式（参数调整操作） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| Proxy Server | 代理服务器 | 第三方系统，接收 UDG 重定向的业务流，实现网络访问加速和病毒防护 |
| IP Farm | IP 服务器集合 | Proxy Server 的负荷分担集合，支持 ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD |
| WEBPROXY | Web Proxy 策略类型 | RULE.POLICYTYPE=WEBPROXY，访问限制轨道B的动作类型（L3 IP NAT 级别） |
| NAT | Network Address Translator | RFC 3022，WebProxy 的核心机制（目的IP/源IP双向转换） |
| SVRIP | 服务器 IP | FILTER 中的服务器 IP 匹配字段，触发 WebProxy 的目的服务器 IP |
| Loopback 接口 | 环回接口 | 建议作为 IP Farm 心跳检测源地址（取自地址池预留地址） |

---

## 8. 文档一致性说明（feature-doc-list vs 产品文档）

> feature-doc-list/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | feature-doc-list/旧文档描述 | 产品文档实际内容 | 差异类型 |
|---|------|------------------------------|-----------------|---------|
| 1 | **动作机制归类（重大）** | 旧文档（轮1）归类为"L3 IP NAT方式的代理重定向（独立体系，非PCC/SMARTREDIRECT）"，但未明确归入轨道B | 产品文档明确：WebProxy 使用 `POLICYTYPE=WEBPROXY`（配置Web Proxy文档任务示例 line 203）、`POLICYNAME=farm_test` 指向 IP Farm，属于 **轨道B（WEBPROXY独立体系，L3 IP NAT）**；遵循标准含 RFC 3022（Traditional NAT）证实 NAT 机制 | **补全（强化）**：旧文档归类基本正确，本文档进一步明确归入轨道B，与 URL过滤（CFTEMPLATE动作）同属轨道B独立动作机制，与 SMARTREDIRECT（轨道C）区分 |
| 2 | NAT 双向转换机制 | 旧文档已描述 | 产品文档明确：上行目的IP→ProxyIP，下行源IP→WebIP，对用户透明 | 一致（已强化） |
| 3 | WebProxy vs IP重定向区别 | 旧文档已描述 | 产品文档（实现原理 §末尾）明确：IP重定向不转换目的IP直接转发，WebProxy 转换目的IP（NAT方式） | 一致 |
| 4 | 动作优先级（非 Rule PRIORITY） | 旧文档未明确强调 | 产品文档（配置Web Proxy §数据）明确：系统按固定动作优先级执行，不按 Rule PRIORITY | 补全：重要约束，影响多规则场景 |
| 5 | 全部 DOWN 时不重定向 | 旧文档未明确 | 产品文档（特性概述 §原理概述）明确：IP Farm 内所有服务器 DOWN 时，不对报文做重定向动作（业务按原路径走，不阻塞） | 补全：区别于 Portal 的 DEFAULTACT=BLOCK |
| 6 | 服务器 DOWN 时报文丢弃 | 旧文档已提及 | 产品文档一致：用户选定 server DOWN 后此业务报文丢弃，后续新业务重选 UP server | 一致 |
| 7 | 心跳检测源地址建议 | 旧文档提及 Loopback | 产品文档明确：建议采用 UDG 上配置的 Loopback 接口地址，地址池预留一个地址 | 一致（已强化） |
| 8 | FILTER SVRIP 字段 | 旧文档已列 | 产品文档明确：SVRIPMODE/SVRIP/SVRIPMASKTYPE/SVRIPMASK 四参数，SVRIP=192.168.10.123 触发 WebProxy | 一致（已细化） |
| 9 | 软参完整性 | 旧文档已列 BIT596/BIT1541 | 产品文档一致：BIT596（在线切换）、BIT1541（多策略） | 一致 |
| 10 | 遵循标准（RFC 3022） | 旧文档已列 | 产品文档明确：3GPP 23.214/29.244 + RFC 2616（HTTP/1.1）+ RFC 3022（NAT）；**RFC 3022 是 NAT 机制的标准依据** | 补全：RFC 3022 证实轨道B NAT 归类 |
| 11 | 测量指标数量 | 旧文档已列 8 项 | 产品文档一致：1914314604~4611 共 8 项 | 一致 |
| 12 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（5 份核心文档 + 5 份调整参数文档 MML 脚本参数一致） | 无 |
| 13 | feature_group 归属 | feature-doc-list 标注 feature_group=Portal | 产品文档路径在"智能策略控制功能"下，业务上归属重定向族；feature_group=Portal 与产品路径不冲突（与用户Portal同组） | 一致（业务语义归 Portal 组，归属重定向族） |

---
