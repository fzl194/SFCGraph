# GWFD-110281 用户Portal 知识文档

> 访问限制场景 | Portal重定向核心特性（轨道C：SMARTREDIRECT体系） | UDG | 来源：特性概述+实现原理+配置+调测+参考信息+参数调整 | 2026-06-22

---

## 0. 元数据（三层图谱Schema字段，对齐 §9.3）

| 字段 | 取值 |
|------|------|
| feature_id | GWFD-110281 |
| feature_name | 用户Portal |
| feature_group | Portal |
| parent_feature_id | -（配置树无显式独立父节点；业务上归属"业务感知功能 → 智能策略控制功能 → 重定向族"分支；PCC触发链父为 GWFD-020351 PCC基本功能） |
| applicable_nf_map | `{"UDG": ["PGW-U", "UPF"]}` |
| variant_dimensions | ["工作模式(captive模式/non-captive模式交替)", "重定向动作触发(POLICYTYPE=SMARTREDIRECT 与 PCC 联动)", "IP Farm负荷分担方式(ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD)", "HTTP重定向响应码(301/302/303，通过 SET SRVCOMMONPARA 配置)", "TCP RST拆链行为(软参 BIT1473/BIT412 控制)", "无法重定向时缺省动作(DEFAULTACT=BLOCK/PASS)", "协议类型(HTTP/WAP1.X/WAP2.0)", "IP版本(IPv4/IPv6)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-AC-110281-01, EV-FK-AC-110281-02, EV-FK-AC-110281-03, EV-FK-AC-110281-04, EV-FK-AC-110281-05]（P4建06-evidence-index时确定，先用占位） |
| license_required | `82209780 LKV3G5CPPT01 用户Portal` |

> **动作轨道归类结论（轮1三轨体系的补充确认）**：用户Portal 属于 **轨道C（SMARTREDIRECT体系）**。关键证据：`ADD RULE:POLICYTYPE=SMARTREDIRECT`（配置用户Portal文档任务示例明确），`POLICYNAME` 指向 IP Farm（`farm_test`）；动作机制为 UDG 解析 HTTP/WAP Get/Post 报文 → 构造 301/302/303 重定向报文携带 Portal Server URL → 用户跳转到 Portal Server。与 GWFD-110284 HTTP智能重定向、GWFD-110283 DNS纠错同属 SMARTREDIRECT 体系（URL 重写级别），与 GWFD-110282 WebProxy（POLICYTYPE=WEBPROXY，L3 IP NAT级别）属不同轨道。

---

## 1. 概述

### 1.1 特性定义（是什么）

用户Portal即个人门户网站，其功能是对用户的信息进行管理，包括业务的订购管理、账户管理、费用管理。**UDG 支持在终端上线后被自动重定向到个人门户网站**，然后通过个人门户网站访问各种业务。

**工作机制（核心）**：UDG 对用户 HTTP/WAP Get/Post 报文进行 SA 解析，匹配规则后执行 `PCCACTIONPROP` 中的用户Portal处理 —— 构造 HTTP 301/302/303 重定向报文，将用户重定向到 IP Farm 中负荷分担选定的 Portal Server；用户在 Portal Server 上完成业务订购/账户/费用管理后，进入 non-captive 模式正常访问 Web Server；captive 模式定时器超时后，用户再次进入 captive 模式被重定向。

> SourcePath: `UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/GWFD-110281 用户Portal特性概述_66655000.md` §定义、§原理概述

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| MS/UE | 终端 | 无特殊要求 | 用户终端设备（需浏览器支持HTTP/WAP重定向） |
| PGW-U / UPF | 用户面（UDG） | UDG 20.0.0 及后续版本 | 定时重定向终端用户的 HTTP/WAP 请求到 Portal Server；执行 captive/non-captive 模式切换 |
| Portal Server | 外部门户服务器 | 无特殊要求 | 提供提醒页面给终端用户，用于广告宣传、业务推广或消息提示；需支持 ICMP 心跳检测应答 |

**applicable_nf_map**（JSON）：
```json
{"UDG": ["PGW-U", "UPF"]}
```

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §适用NF、§可获得性

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|----------|----------|----------|
| 01 | 20.0.0 | 首次发布 |

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §发布历史

### 1.4 License

- **License控制项**：`82209780 LKV3G5CPPT01 用户Portal`
- 必须获得 License 许可后才能获得该特性的服务。

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §可获得性

### 1.5 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | 向用户推送广告等页面，增加广告收入；IP Farm 内支持多个 IP 之间的轮选，意味着多个服务器提供多种 "Portal" 页面，即业务的多样性扩展 |
| 用户 | 了解业务信息；自主选择业务 |

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §客户价值

### 1.6 应用场景

| 场景 | 描述 |
|------|------|
| 用户上线首推欢迎页 | 用户激活后首次使用浏览业务时向用户推送欢迎页面 |
| 定时广告/提醒推送 | 用户浏览网页时定时向用户推送广告或提醒页面（captive 模式定时器超时后再次重定向） |
| 业务订购/账户/费用管理 | Portal Server 提供业务订购、账户管理、费用管理入口 |

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §应用场景

### 1.7 前置条件与依赖（SA协议族 + PCC触发链）

| 关系类型 | 相关特性 | License 控制项 | 说明 |
|----------|----------|----------------|------|
| 依赖 | GWFD-110101 SA-Basic | 82209749 LKV3G5SABS01 SA-Basic | UDG 需要对用户的 Portal 业务进行解析以获得 captive-portal 动作和重定向地址，SA-Basic 是 SA 的基本功能，**必须开启** |
| 依赖 | GWFD-110103 SA-Web Browsing | 82209755 LKV3G5SAWB01 SA-Web Browsing | 对 HTTP、WAP2.0 协议类型的报文进行解析时需要开启 |
| 依赖 | GWFD-110105 SA-Mobile | 82209757 LKV3G5SAMB01 SA-Mobile | 对 WAP1.X 协议类型的报文进行解析时需要开启 |
| 互斥 | GWFD-110201 HTTP2.0 Host 识别 | 82209773 LKV3G5HSHA01 HTTP2.0 Host 识别 | HTTP2.0 为加密报文，不支持 HTTP 重定向处理（互斥） |
| 互斥 | GWFD-110203 HTTPS 业务地址识别 | 82209775 LKV3G5HSBA01 HTTPS 业务地址识别 | HTTPS 为加密报文，不支持重定向处理（互斥） |
| 触发依赖 | GWFD-020351 PCC 基本功能 | 82209825 LKV3G5PCCB01 PCC 基本功能 | RULE.POLICYTYPE=SMARTREDIRECT 与 PCC 规则协同（rule_test2 POLICYTYPE=PCC 负责计费），PCC 触发链为访问限制通用骨架 |

**前置条件**：
- 已完成加载 License（LKV3G5CPPT01）
- UDG 与周边网元的互通配置已完成
- 已完成 SA 协议族激活（SA-Basic 必选；SA-Web Browsing/SA-Mobile 按协议选配）

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §与其他特性的交互
> SourcePath: `配置用户Portal_66620114.md` §必备事项

### 1.8 对系统的影响

需要进行 SA 处理，并基于 SA 结果将用户重定向到个人门户网站，**系统吞吐量将下降**。

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §对系统的影响

### 1.9 应用限制

- 用户Portal 功能要求终端浏览器支持 HTTP/WAP 重定向
- 仅支持对 HTTP、WAP1.X、WAP2.0 协议（Get/Post 请求）的重定向；**不支持 HTTP2.0/HTTPS**（加密报文）
- HTTPS 重定向 URL 命中规则时，建议配置黑名单规则 `ADD BLACKLISTRULE` 放行重定向报文，保证用户重定向后业务可正常处理

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §应用限制
> SourcePath: `配置用户Portal_66620114.md` §操作步骤4 说明

### 1.10 特性规格

| 规格名称 | 规格指标 |
|----------|----------|
| 支持的 IP Farm 个数（整机） | 64 |
| 每个 IP Farm 中支持的 IP 地址个数（整机） | 512 |

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §特性规格

### 1.11 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|----------|----------|----------|
| IETF | 1945 | Hypertext Transfer Protocol -- HTTP/1.0 |
| IETF | 2616 | Hypertext Transfer Protocol -- HTTP/1.1 |
| IETF | - | Wireless Session Protocol Specification-WAP-230-WSP-20010705-a |

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §遵循标准

### 1.12 计费与话单

**本特性不涉及计费与话单**（重定向动作本身不计费；如需对 Portal 业务计费，通过 rule_test2 POLICYTYPE=PCC + URR/URRGROUP 实现）。

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §计费与话单

---

## 2. 激活（License开启命令）

> 与 GWFD-010105 等"配置使能即激活"的特性不同，本特性**必须先打开 License 配置开关**才能获得服务。激活即"License开关 + IP Farm + SMARTREDIRECT规则 + 用户模板"。

打开本特性的 License 配置开关：

```
SET LICENSESWITCH:LICITEM="LKV3G5CPPT01",SWITCH=ENABLE;
```

查询 License 开关状态：

```
LST LICENSESWITCH:LICITEM="LKV3G5CPPT01";
```

> SourcePath: `配置用户Portal_66620114.md` §任务示例
> SourcePath: `调测用户Portal_66620115.md` §操作步骤1

---

## 3. 原理

### 3.1 实现原理：SMARTREDIRECT 动作 + captive/non-captive 双模式交替

配置了用户Portal动作的用户，会交替地处于两种模式：

| 模式 | UDG 行为 | 用户感知 |
|------|---------|---------|
| **captive 模式** | UDG 将用户向 Web Server 发送的 Get/Post 请求**先重定向到 Portal Server**，然后再转发到 Web Server | 用户首次访问被跳转到 Portal 页面 |
| **non-captive 模式** | UDG **不执行**重定向动作到 Portal Server，用户请求直接发送到 Web Server | 用户可正常访问目标网页 |

**模式切换机制**：
- 用户报文重定向后，UDG 根据 captive mode 配置启动定时器（`CAPMODETHRES`，单位分钟），进入 non-captive 模式
- 定时器超时前，UDG 不进行重定向操作并允许用户正常接入业务
- 定时器超时后，用户再次进入 captive 模式，再次访问 Web Server 时会再次被重定向

> 说明：Get/Post 请求属于 HTTP/WAP1.X/WAP2.0 协议。

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §原理概述
> SourcePath: `实现原理_74004638.md`（12步业务流程，含定时器超时后的二次重定向）

### 3.2 重定向服务器选择机制（IP Farm 负荷分担）

若干个服务器的集合称为 **IP Farm**。UDG 的重定向功能会将用户报文重定向到指定服务器上，对于不同的用户报文，可以选择不同的服务器作为重定向的目的地。为平衡 Portal Server 负荷，需在一个 IP Farm 内对服务器进行负荷分担：

| 负荷分担方式（LBMETHOD） | 说明 |
|--------------------------|------|
| ROUND_ROBIN | 轮询方式 |
| LEAST_RECENTLY_USED | 选择最久未被使用的 server |
| LEAST_LOAD | 选择最小负荷 server |

具体模式通过 `SET IPFARMGLOBAL` 命令配置。

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §原理概述

### 3.3 重定向服务器检测机制（ICMP 心跳检测）

UDG 定时向 IP Farm 中的服务器发送 ICMP 报文，服务器收到报文后会对 UDG 做出应答。在报文需要被重定向时，负荷分担功能只会选择状态为 UP 的服务器作为重定向服务器：

- **UP 判定**：UDG 在设置时间内收到服务器应答
- **DOWN 判定**：UDG 在设置时间内连续收不到响应
- **UP→DOWN**：处于 UP 状态的服务器心跳检测连续失败次数达到 `HEALTHFAILLIMIT` 门限 → 状态转化为 DOWN
- **DOWN→UP**：处于 DOWN 状态的服务器心跳检测连续成功次数达到 `HEALTHSUCCLIMIT` 门限 → 状态转化为 UP
- **服务器 DOWN 时报文处理**：如果有用户选定某个服务器为重定向服务器，而该服务器的状态变为 DOWN 之后，**此业务的报文将会被丢弃**，后续的业务将会重新选择状态为 UP 的服务器作为重定向服务器

**心跳检测接口要求**：
- 在做心跳检测时，需要为不同 IP Farm 下的服务器配置不同的心跳检测接口
- 接口与 IP Farm 绑定，作为发送心跳检测消息的源地址
- Portal Server 需要支持心跳检测功能（ICMP 应答）
- **一个 IP Farm 下所有 Portal Server 共用一个心跳检测接口**
- 心跳检测的源地址**建议采用 UDG 上配置的 Phif 接口地址**（取自终端地址池，配置地址池时需预留一个 IP 地址用于 IP Farm 心跳检测）

> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §原理概述

### 3.4 关键信元与协议交互（HTTP 301/302/303 重定向）

#### 3.4.1 HTTP 重定向响应码（通过 SET SRVCOMMONPARA 配置）

UDG 构造的 HTTP 回复报文返回码可在 PGW-U/UPF 上全局配置，其值可设置为 **301、302 或 303**：

| 响应码 | HTTP 语义 | 浏览器行为 |
|--------|----------|-----------|
| 301 | Moved Permanently（永久重定向） | 浏览器缓存重定向，后续直接访问新 URL |
| 302 | Found（临时重定向） | 浏览器跳转到 Location 头指定 URL，不缓存 |
| 303 | See Other（以 GET 获取） | 浏览器以 GET 方法访问新 URL |

通过 `SET SRVCOMMONPARA` 命令全局配置。

#### 3.4.2 captive 模式定时器（CAPMODETHRES，用户模板级）

通过 `ADD USERPROFILE:CAPMODETHRES=<分钟>` 配置。用户报文重定向后，UDG 启动该定时器进入 non-captive 模式；超时后再次进入 captive 模式。

#### 3.4.3 无法重定向时的缺省动作（DEFAULTACT）

| DEFAULTACT 取值 | 行为 |
|----------------|------|
| BLOCK（缺省） | UDG 直接**阻塞**该业务报文（用户无法访问） |
| PASS | 报文正常转发（用户可访问，但未触发 Portal） |

通过 `ADD IPFARMSERVER` / `MOD IPFARMSERVER:DEFAULTACT=PASS` 配置。

> SourcePath: `实现原理_74004638.md` §步骤4、§末尾说明
> SourcePath: `配置用户Portal_66620114.md` §操作步骤4 说明

### 3.5 业务流程（端到端 captive/non-captive 交替）

```
┌─────────────────────────────────────────────────────────────────┐
│ 【首次访问：captive 模式】                                        │
│                                                                  │
│ 1. TCP 连接建立（目的端口 80）                                    │
│    MS/UE → 目标Web Server，目的IP=目标服务器IP，目的端口=80       │
│    PGW-U/UPF 允许 TCP 连接通过                                    │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. MS/UE 发起 HTTP 业务（Get/Post 报文）                         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. UDG 解析 HTTP 报文 + RULE 匹配（关键步骤）                     │
│    PGW-U/UPF 对 HTTP 报文解析 → 匹配 rule_test1                   │
│    rule_test1: POLICYTYPE=SMARTREDIRECT, POLICYNAME=farm_test    │
│    UDG 执行 PCCACTIONPROP 中的用户Portal处理                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. UDG 构建 HTTP 重定向回复报文（301/302/303）发送给 MS/UE        │
│    - 从 IP Farm（farm_test）中按负荷分担（LEAST_LOAD）选 Portal   │
│      Server（如 192.168.10.123 / www.example.com）                │
│    - HTTP 回复报文 Location 头携带 Portal Server URL             │
│    - UDG 启动 captive mode 定时器（CAPMODETHRES=6 分钟）          │
│    - 进入 non-captive 模式                                        │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. 【可选】UDG 构造 TCP RST 报文发给 MS/UE                        │
│    - 通知 MS/UE 断开目标服务器                                    │
│    - 由软参 BIT1473（响应报文方式）和 BIT412（是否发RST）控制     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 6. UDG 给目标 Web Server 发送 TCP RST 报文（避免半连接）         │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 7. MS/UE 根据重定向报文中的 URL 自动获取 DNS                      │
│    发起到 Portal Server 的 TCP 连接                               │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 8. MS/UE 与 Portal Server 正常进行 HTTP 交互                      │
│    用户看到 Portal 页面（业务订购/账户/费用管理/广告）            │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│ 【后续访问：non-captive 模式（定时器未超时）】                    │
│                                                                  │
│ 9. MS/UE 与 Web Server 进行正常的 HTTP 交互                       │
│    UDG 不重定向，报文直接转发                                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │
                               ▼ captive 定时器超时
┌─────────────────────────────────────────────────────────────────┐
│ 【二次重定向：captive 模式恢复】                                  │
│                                                                  │
│ 10. MS/UE 再次访问 Web Server，先发起 TCP 建链                    │
│ 11. MS/UE 发出 URL 请求到 Web Server                             │
│ 12. UDG 解析后发现 captive 定时器超时 → 进入 captive 模式         │
│     再次执行用户Portal处理，重定向到 Portal Server                │
│     UDG 再次启动 captive mode 定时器                             │
└─────────────────────────────────────────────────────────────────┘
```

> SourcePath: `实现原理_74004638.md`（12步完整流程）

### 3.6 与 SMARTREDIRECT 体系的关系（访问限制三轨体系下的定位）

用户Portal 与 HTTP智能重定向（GWFD-110284）、DNS纠错（GWFD-110283）同属 **轨道C（SMARTREDIRECT体系）**，共同特征：
- `ADD RULE:POLICYTYPE=SMARTREDIRECT`
- 动作机制为 L7 URL 重写（HTTP 301/302/303 + Location 头）
- `POLICYNAME` 指向 IP Farm 或重定向目标配置

差异点（用户Portal 独有）：
- **captive/non-captive 双模式交替**：通过 `CAPMODETHRES` 定时器实现周期性重定向（定时推送 Portal）
- **IP Farm 负荷分担**：支持 ROUND_ROBIN / LEAST_RECENTLY_USED / LEAST_LOAD 三种方式选择 Portal Server
- **心跳检测**：ICMP 探测 Portal Server 状态，仅选 UP 服务器

```
              【轨道A：三四层匹配，PCC体系（访问限制通用骨架）】
                    ↓
  ADD FILTER(L34PROTOCOL=TCP) → ADD FLOWFILTER → ADD FLTBINDFLOWF
                    ↓
  ADD L7FILTER(URL=www.huawei.com/*) → ADD PROTBINDFLOWF → SET REFRESHSRV
                    ↓
  ADD USERPROFILE(CAPMODETHRES=6) → ADD RULEBINDING
                    ↓
        会话命中 rule_test1 → 触发 SMARTREDIRECT 动作
                    ↓
═══════════════════════════════════════════════════════
                    ↓
        【轨道C：SMARTREDIRECT体系，URL重写动作】
                    ↓
  UDG 解析 HTTP Get/Post → 构建 301/302/303 重定向报文
                    ↓
  IP Farm 负荷分担选 Portal Server → 携带 Location URL
                    ↓
  captive 定时器启动 → non-captive 模式 → 超时再次重定向
                    ↓
  执行 Portal 重定向（访问限制"重定向族"成员）
```

> 说明：rule_test2 POLICYTYPE=PCC 与 rule_test1 POLICYTYPE=SMARTREDIRECT 并列绑定到同一 USERPROFILE，PCC 规则负责计费属性（URR/URRGROUP/PCCPOLICYGRP），SMARTREDIRECT 规则负责重定向动作，两者协同完成"重定向 + 计费"。

---

## 4. 配置

### 4.1 配置对象总览

本特性配置分为三大块：**IP Farm 重定向基础设施**、**三四层 + 七层过滤条件**、**SMARTREDIRECT 规则与业务策略组合**。

#### 4.1.1 IP Farm 重定向基础设施对象

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| IPFARMGLOBAL | （全局） | 整机 IP Farm 全局参数（服务器类型、心跳阈值、负荷分担方式） | SET IPFARMGLOBAL |
| LOGICINF | phif1/0/0 | IP Farm 心跳检测使用的逻辑接口（Phif 接口） | ADD LOGICINF |
| IPFARM | farm_test | 重定向 IP Farm（Portal Server 集合） | ADD IPFARM |
| IPFARMSERVER | （绑定到 farm_test） | IP Farm 下的 Portal Server（IP + URL + DEFAULTACT） | ADD IPFARMSERVER |
| SRVCOMMONPARA | （全局） | HTTP 重定向响应码（301/302/303） | SET SRVCOMMONPARA |

#### 4.1.2 过滤条件对象（三四层 + 七层）

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| FILTER | filter_test | 三四层过滤条件（L34PROTOCOL=TCP） | ADD FILTER |
| FLOWFILTER | ff_test1 | 流过滤器 | ADD FLOWFILTER |
| FLTBINDFLOWF | （绑定关系） | Filter 与 FlowFilter 绑定 | ADD FLTBINDFLOWF |
| SIGNATUREDB | （特征库） | 协议识别特征库（识别 HTTP 协议） | LOD SIGNATUREDB |
| L7FILTER | l7-test | 七层过滤器（URL=www.huawei.com/*） | ADD L7FILTER |
| PROTBINDFLOWF | （绑定关系） | FlowFilter 与协议 + L7Filter 绑定 | ADD PROTBINDFLOWF |
| REFRESHSRV | （刷新） | 新配置的 Filter/L7Filter 置为生效（60s 自动，可手动） | SET REFRESHSRV |

#### 4.1.3 SMARTREDIRECT 规则与业务策略组合对象

| 对象类型 | 对象名称（示例） | 用途 | 关键命令 |
|----------|------------------|------|----------|
| URR | cbb_test | 使用量上报规则（计费，rule_test2 用） | ADD URR |
| URRGROUP | cp_test | URR 组 | ADD URRGROUP |
| PCCPOLICYGRP | pcc-pg_test | PCC 策略组（绑定 URRGROUP，rule_test2 用） | ADD PCCPOLICYGRP |
| RULE（SMARTREDIRECT） | rule_test1 | **Portal 重定向规则（POLICYTYPE=SMARTREDIRECT）** | ADD RULE |
| RULE（PCC） | rule_test2 | 计费规则（POLICYTYPE=PCC） | ADD RULE |
| USERPROFILE | up_test | 用户模板（含 CAPMODETHRES captive 定时器） | ADD USERPROFILE |
| RULEBINDING | （绑定关系） | UserProfile 与 rule_test1/rule_test2 绑定 | ADD RULEBINDING |
| APN | apn-test | APN 配置 | ADD APN |

> SourcePath: `配置用户Portal_66620114.md` §数据

### 4.2 配置流程

```
1. 打开 License 开关
   SET LICENSESWITCH:LICITEM="LKV3G5CPPT01",SWITCH=ENABLE

2. 配置整机 IP Farm 全局参数
   SET IPFARMGLOBAL（SERVERTYPE=REDIRECT、心跳阈值、LBMETHOD）

3. 配置 IP Farm 心跳检测接口（Phif 接口）
   ADD LOGICINF（IPV4ADDRESS1 取自地址池预留地址）

4. 配置 IP Farm
   a. ADD IPFARM（创建 IP Farm，绑定心跳检测接口）
   b. ADD IPFARMSERVER（添加 Portal Server IP + URL + DEFAULTACT）

5. 配置三四层过滤条件
   a. ADD FILTER（L34PROTOCOL=TCP）
   b. ADD FLOWFILTER
   c. ADD FLTBINDFLOWF

6. 配置协议识别（加载特征库识别 HTTP）
   LOD SIGNATUREDB（LOADMODE=LATEST）

7. 配置七层过滤条件
   a. ADD L7FILTER（URL=www.huawei.com/*）
   b. ADD PROTBINDFLOWF（绑定 http 协议 + L7Filter）
   c. SET REFRESHSRV（可选，立即生效；否则 60s 自动生效）

8. 配置计费属性（rule_test2 用）
   a. ADD URR
   b. ADD URRGROUP

9. 配置 PCC 策略组（rule_test2 用）
   ADD PCCPOLICYGRP

10. 配置业务规则
    a. ADD RULE rule_test1（POLICYTYPE=SMARTREDIRECT, POLICYNAME=farm_test）
    b. ADD RULE rule_test2（POLICYTYPE=PCC, POLICYNAME=pcc-pg_test）

11. 配置业务策略组合
    a. ADD USERPROFILE（CAPMODETHRES=6 captive 定时器）
    b. ADD RULEBINDING（绑定 rule_test1 + rule_test2）
    c. ADD APN
```

> SourcePath: `配置用户Portal_66620114.md` §操作步骤

### 4.3 任务实例（保留原始 MML）

**场景**：
- UDG 使用最小负荷 server 方式（LEAST_LOAD）实现用户Portal 功能
- UDG 将用户首次发往 `www.huawei.com` 的 IPv4 报文重定向到 `www.example.com` 或 `www.vmall.com` 服务器上
- UDG 与重定向服务器之间进行心跳检测

```mml
// 打开本特性的 License 配置开关。
SET LICENSESWITCH:LICITEM="LKV3G5CPPT01",SWITCH=ENABLE;

// 配置整机的用户Portal 参数。
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=LEAST_LOAD;

// 配置 IP Farm 使用的心跳检测接口。
ADD LOGICINF:NAME="phif1/0/0",IPVERSION=IPV4,IPV4ADDRESS1="10.10.10.10",IPV4MASK1="255.255.255.255";

// 配置 IP Farm。
ADD IPFARM:IPFARMNAME="farm_test",IPVERSION=IPV4,HEALTHCHECKFLAG=ENABLE,INTERFACENAME="phif1/0/0";
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="192.168.10.123",URL="www.example.com";
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="192.168.10.124",URL="www.vmall.com";

// 配置用户Portal 业务使用的三四层过滤条件。
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=TCP;
ADD FLOWFILTER:FLOWFILTERNAME="ff_test1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_test1",FILTERNAME="filter_test";

// 配置协议识别。
LOD SIGNATUREDB:LOADMODE=LATEST;

// 配置用户Portal 业务使用的七层过滤条件。
ADD L7FILTER:L7FILTERNAME="l7-test",SUBL7FLTNAME="sub-l7-test",URL="www.huawei.com/*";
ADD PROTBINDFLOWF:FLOWFILTERNAME="ff_test1",PROTOCOLNAME="http",L7FILTERNAME="l7-test";

// 将新配置的信息置为生效。
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;

// 配置用户Portal 业务使用的计费属性。
ADD URR:URRNAME="cbb_test",URRID=1000,USAGERPTMODE=ONLINE;
ADD URRGROUP:URRGROUPNAME="cp_test",UPURRNAME1="cbb_test",DOWNURRNAME1="cbb_test";

// 配置用户Portal 业务使用的 PCC 策略组。
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pcc-pg_test",URRGROUPNAME="cp_test";

// 配置用户Portal 业务使用的业务规则。
// rule_test1: POLICYTYPE=SMARTREDIRECT（用户Portal 重定向，关键）
ADD RULE:RULENAME="rule_test1",POLICYTYPE=SMARTREDIRECT,FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="ff_test1",PRIORITY=10,POLICYNAME="farm_test";
// rule_test2: POLICYTYPE=PCC（计费）
ADD RULE:RULENAME="rule_test2",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="ff_test1",PRIORITY=20,POLICYNAME="pcc-pg_test";

// 配置用户Portal 业务使用的业务策略组合。
ADD USERPROFILE:USERPROFILENAME="up_test",CAPMODETHRES=6;
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test1";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test2";
ADD APN:APN="apn-test";
```

> SourcePath: `配置用户Portal_66620114.md` §任务示例

### 4.4 关键 MML 命令列表

#### 4.4.1 IP Farm 相关命令

| 命令 | 用途 |
|------|------|
| SET LICENSESWITCH | 打开/关闭 License 开关 |
| SET IPFARMGLOBAL | 设置 IP Farm 全局参数（类型、心跳阈值、负荷分担方式） |
| SET SRVCOMMONPARA | 设置业务公共参数（含 HTTP 重定向响应码 301/302/303） |
| ADD LOGICINF | 增加逻辑接口（Phif 心跳检测接口） |
| ADD IPFARM | 增加 IP Farm |
| ADD IPFARMSERVER | 增加 IP Farm 服务器（Portal Server） |
| MOD IPFARMSERVER | 修改 IP Farm 服务器（含 DEFAULTACT） |

#### 4.4.2 过滤条件相关命令

| 命令 | 用途 |
|------|------|
| LOD SIGNATUREDB | 加载协议特征库（识别 HTTP 协议） |
| ADD FILTER | 增加三四层过滤器 |
| ADD FLOWFILTER | 增加流过滤器 |
| ADD FLTBINDFLOWF | 增加流过滤器的过滤器绑定关系 |
| ADD L7FILTER | 增加七层过滤器（URL） |
| ADD PROTBINDFLOWF | 增加流过滤器协议绑定关系 |
| SET REFRESHSRV | 业务刷新（Filter/L7Filter 生效） |
| ADD BLACKLISTRULE | 增加黑名单规则（HTTPS 重定向放行用） |

#### 4.4.3 规则与业务策略组合命令

| 命令 | 用途 |
|------|------|
| ADD URR | 增加使用量上报规则 |
| ADD URRGROUP | 增加 URR 组 |
| ADD PCCPOLICYGRP | 增加 PCC 策略组 |
| ADD RULE | 增加业务规则（POLICYTYPE=SMARTREDIRECT 触发 Portal） |
| ADD USERPROFILE | 增加用户模板（含 CAPMODETHRES） |
| ADD RULEBINDING | 增加 UserProfile 与 Rule 绑定 |
| ADD APN | 添加 APN 配置 |

> SourcePath: `GWFD-110281 用户Portal参考信息_77079045.md` §命令

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

#### 4.5.3 ADD IPFARMSERVER 参数（Portal Server）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| IPFARMNAME | farm_test | 所属 IP Farm |
| IPVERSION | IPV4 | IP 协议版本 |
| SERVERIPV4 | 192.168.10.123 | Portal Server IPv4 地址 |
| URL | www.example.com | Portal Server URL（重定向目标） |
| DEFAULTACT | BLOCK / PASS | 无法重定向时缺省动作（BLOCK 阻塞/PASS 放行） |

#### 4.5.4 ADD RULE 参数（SMARTREDIRECT 关键）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| RULENAME | rule_test1 | 规则名称 |
| POLICYTYPE | **SMARTREDIRECT** | **策略类型=SMARTREDIRECT 触发用户Portal 重定向动作（轨道C）** |
| FILTERINGMODE | FLOWFILTER | 流过滤器或流过滤器组选择（FLOWFILTER / FLOWFILTERGRP） |
| FLOWFILTERNAME | ff_test1 | 流过滤器名称 |
| PRIORITY | 10 | 全局优先级 |
| POLICYNAME | farm_test | 策略名称（SMARTREDIRECT 下为 IP Farm 名称） |

#### 4.5.5 ADD USERPROFILE 参数（captive 定时器）

| 参数 | 取值样例 | 说明 |
|------|----------|------|
| USERPROFILENAME | up_test | 用户模板名称 |
| CAPMODETHRES（Captive模式时间阈值，分） | 6 | captive 模式定时器，超时后用户再次进入 captive 模式被重定向 |

> SourcePath: `配置用户Portal_66620114.md` §数据

### 4.6 软参

| 软参 | 说明 |
|------|------|
| BIT1473 | 控制系统重定向动作的响应报文方式 |
| BIT412 | 控制重定向时系统是否向手机发送 RST 拆链报文 |
| BIT467 | 控制系统是否检测终端 APN 的 VPN 与 IP Farm 配置的 VPN 的一致性 |

> SourcePath: `GWFD-110281 用户Portal参考信息_77079045.md` §软参

### 4.7 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| IP 版本一致性 | IPv4 用户Portal 规则：IP Farm、Virtual IP、VPN、Server IP、心跳检测接口 IP、Filter 都必须使用 IPv4 形式；IPv6 同理。可通过 `DSP RULECHECK` 检查 |
| 心跳检测接口独立 | 不同 IP Farm 下的服务器需要配置不同的心跳检测接口 |
| 心跳检测地址预留 | 心跳检测的本端 IP 一般从终端地址池获取，配置地址池时需预留一个 IP 地址用于 IP Farm 心跳检测 |
| 服务器状态门槛 | IP Farm 配置完成后，需保证至少有一个 server 状态为 up（`LST IPFARMSERVER` 验证） |
| 协议限制 | 仅支持 HTTP、WAP1.X、WAP2.0；不支持 HTTP2.0/HTTPS 重定向 |
| HTTPS 处理 | 重定向 URL 采用 HTTPS 协议且命中规则时，需配置 `ADD BLACKLISTRULE` 放行重定向报文 |
| SET REFRESHSRV 延迟 | 系统自动 60s 后将配置的 L7Filter 置为生效；如需立即生效需手动执行 SET REFRESHSRV |
| 互斥特性 | 与 GWFD-110201 HTTP2.0 Host 识别、GWFD-110203 HTTPS 业务地址识别互斥（加密报文不支持重定向） |

---

## 5. 配置案例

### 5.1 场景一：基础 Portal 重定向（LEAST_LOAD，301/302/303）

**场景描述**：UDG 使用最小负荷 server 方式实现用户Portal 功能。用户首次发往 `www.huawei.com` 的 IPv4 报文被重定向到 `www.example.com` 或 `www.vmall.com` 服务器。UDG 与重定向服务器之间进行心跳检测。

**MML 命令序列**：见 §4.3 任务实例（原样保留产品文档）。

> SourcePath: `配置用户Portal_66620114.md` §任务示例

### 5.2 场景二：负荷分担方式变体（ROUND_ROBIN 轮询）

**场景描述**：与场景一差异 —— 采用轮询方式选择 Portal Server，适用于 Portal Server 性能均等、简单均衡场景。

**MML 命令序列（差异部分）**：

```
// 负载均衡模式改为 ROUND_ROBIN（轮询）
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=ROUND_ROBIN;

// 其余配置同场景一
```

> 来源：基于 `GWFD-110281 用户Portal特性概述_66655000.md` §原理概述（LBMETHOD 三选一）+ 场景一配置变体

### 5.3 场景三：负荷分担方式变体（LEAST_RECENTLY_USED 最近最少使用）

**场景描述**：与场景一差异 —— 选择最久未被使用的 Portal Server，避免单台 server 长时间空闲。

**MML 命令序列（差异部分）**：

```
// 负载均衡模式改为 LEAST_RECENTLY_USED
SET IPFARMGLOBAL:SERVERTYPE=REDIRECT,TIMETHRESHOLD=10,HEALTHSUCCLIMIT=2,HEALTHFAILLIMIT=4,LBMETHOD=LEAST_RECENTLY_USED;
```

> 来源：基于 §原理概述 LBMETHOD 选项

### 5.4 场景四：无法重定向时放行变体（DEFAULTACT=PASS）

**场景描述**：缺省情况下 UDG 无法重定向时阻塞报文（BLOCK）。本场景改为放行（PASS），确保 Portal Server 全部 DOWN 时用户仍可访问 Web Server（虽然失去 Portal 推送能力）。

**MML 命令序列（差异部分）**：

```
// 修改 IP Farm Server 的 DEFAULTACT 为 PASS（无法重定向时放行）
MOD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="192.168.10.123",URL="www.example.com",DEFAULTACT=PASS;
MOD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV4,SERVERIPV4="192.168.10.124",URL="www.vmall.com",DEFAULTACT=PASS;
```

> 说明：ADD IPFARMSERVER 创建时缺省 DEFAULTACT=BLOCK；如需 PASS 需通过 MOD 修改或创建时显式指定。
> SourcePath: `实现原理_74004638.md` §末尾说明、`配置用户Portal_66620114.md` §操作步骤4 说明

### 5.5 场景五：captive 定时器周期变体（CAPMODETHRES 调整）

**场景描述**：调整 captive 模式定时器周期，控制 Portal 推送频率。短周期（如 1 分钟）适合频繁推送广告；长周期（如 60 分钟）适合低打扰。

**MML 命令序列（差异部分）**：

```
// 调整 captive 模式时间阈值为 30 分钟（低打扰场景）
ADD USERPROFILE:USERPROFILENAME="up_test",CAPMODETHRES=30;
```

> 来源：基于 `ADD USERPROFILE` CAPMODETHRES 参数语义 + 调整用户Portal参数/修改Captive模式时间的间隔 文档

### 5.6 场景六：HTTP 重定向响应码变体（301/302/303）

**场景描述**：调整 HTTP 重定向响应码。302（临时重定向）为常用配置，避免浏览器缓存；303（See Other）强制以 GET 访问；301（永久重定向）会被浏览器缓存（不推荐用于动态 Portal）。

**MML 命令序列（差异部分）**：

```
// 设置 HTTP 重定向响应码为 302（临时重定向，推荐）
SET SRVCOMMONPARA:...REDIRECTCODE=302;  // 参数名以 SET SRVCOMMONPARA 命令参考为准
```

> 说明：具体参数名以 `SET SRVCOMMONPARA` 命令参考为准。实现原理文档明确返回码可设置为 301、302 或 303。
> SourcePath: `实现原理_74004638.md` §步骤4

### 5.7 场景七：IPv6 变体（IPv6 Portal 规则）

**场景描述**：配置 IPv6 用户Portal 规则，所有 IP 地址（IP Farm、Virtual IP、VPN、Server IP、心跳检测接口 IP、Filter）必须使用 IPv6 形式。

**MML 命令序列（差异部分）**：

```
// IPv6 心跳检测接口
ADD LOGICINF:NAME="phif1/0/0",IPVERSION=IPV6,IPV6ADDRESS1="FC00::10",IPV6MASK1=128;

// IPv6 IP Farm 与 Server
ADD IPFARM:IPFARMNAME="farm_test",IPVERSION=IPV6,HEALTHCHECKFLAG=ENABLE,INTERFACENAME="phif1/0/0";
ADD IPFARMSERVER:IPFARMNAME="farm_test",IPVERSION=IPV6,SERVERIPV6="FC00:1234::100",URL="www.example.com";

// 通过 DSP RULECHECK 检查 IPv6 一致性
DSP RULECHECK:RULENAME="rule_test1",POLICYTYPE=SMARTREDIRECT;
```

> SourcePath: `配置用户Portal_66620114.md` §数据 说明（IPv4/IPv6 一致性约束）

### 5.8 场景变体对照表

| 变体 | 核心差异命令 | 关键参数 | 适用场景 |
|------|------------|---------|---------|
| LEAST_LOAD（场景一） | SET IPFARMGLOBAL LBMETHOD | LBMETHOD=LEAST_LOAD | Portal Server 性能不均（默认/推荐） |
| ROUND_ROBIN（场景二） | SET IPFARMGLOBAL LBMETHOD | LBMETHOD=ROUND_ROBIN | Portal Server 性能均等 |
| LEAST_RECENTLY_USED（场景三） | SET IPFARMGLOBAL LBMETHOD | LBMETHOD=LEAST_RECENTLY_USED | 避免单台 server 空闲 |
| DEFAULTACT=PASS（场景四） | MOD IPFARMSERVER DEFAULTACT | DEFAULTACT=PASS | Portal 全 DOWN 时放行（不阻塞） |
| CAPMODETHRES（场景五） | ADD USERPROFILE CAPMODETHRES | CAPMODETHRES=30 | 调整 Portal 推送频率 |
| HTTP 响应码（场景六） | SET SRVCOMMONPARA | REDIRECTCODE=302 | 控制 HTTP 响应码 |
| IPv6（场景七） | IPv6 命令 + DSP RULECHECK | IPVERSION=IPV6 | IPv6 用户面 |

---

## 6. 验证与调测

### 6.1 验证方法

#### 6.1.1 调测前提与目的

当运营商需要部署用户Portal 功能以实现在用户激活后首次使用浏览业务时向用户推送欢迎页面，或在用户浏览网页时定时向用户推送广告或提醒页面时，需对 UDG 的用户Portal 功能进行调测，确保本功能可以正常使用。

> 适用：PGW-U、UPF

#### 6.1.2 调测数据准备

| 类别 | 参数名称 | 取值样例 | 获取方法 |
|------|---------|---------|---------|
| 测试终端使用的 APN | APN 名称（APN） | apn-test | 已配置数据中获取 |
| Captive Portal 触发地址 | URL | www.huawei.com/* | 已配置数据中获取（L7FILTER） |
| Captive Portal 目的地址 | 服务器 IPv4 地址（SERVERIPV4） | 192.168.10.123 / 192.168.10.124 | 已配置数据中获取（IPFARMSERVER） |
| 心跳检测接口 IP | 逻辑接口 IPv4 地址（IPV4ADDRESS1） | 10.10.10.10 | 已配置数据中获取（LOGICINF） |

工具：测试终端、OM Portal、第三方抓包工具

> SourcePath: `调测用户Portal_66620115.md` §必备事项

#### 6.1.3 调测执行步骤

**步骤1**：执行 `LST LICENSESWITCH` 查询 License 开关。

```
LST LICENSESWITCH:LICITEM="LKV3G5CPPT01";
```

预期输出（正常）：
```
-------------------------------
  License Item  =  LKV3G5CPPT01
  Switch        =  ENABLE
-------------------------------
---    END
```

判断：
- License 支持 Portal 功能为 ENABLE → 步骤2
- 为 DISABLE → 执行 `SET LICENSESWITCH:LICITEM="LKV3G5CPPT01",SWITCH=ENABLE;` 开启 License

**步骤2**：打开接入侧/DN 侧镜像接口上的抓包工具，准备抓取测试终端出入报文。

**步骤3**：测试终端使用 `apn-test` APN 接入网络。
- 成功接入 → 步骤4
- 无法接入 → 调测 UDG 的接入功能

**步骤4**：测试终端浏览 Web 业务，访问 `www.huawei.com` 网页，查看镜像接口抓包信息。

预期抓包行为：
- 测试终端首次浏览业务访问 `www.huawei.com`，发送 HTTP GET 请求（消息9）
- UDG **丢弃此请求**并模拟服务器向测试终端发送重定向报文（消息10）
- UDG 模拟测试终端向用户请求的服务器发送拆链报文（消息11）
- UDG 模拟服务器向测试终端发送拆链报文（消息12）
- 此时，测试终端上显示 `www.example.com` 网页
- 重定向报文（消息10）携带重定向 URL（www.example.com）

判断：
- 测试终端看到跳转到 `www.example.com` 或 `www.vmall.com` 页面，抓包与预期一致 → 步骤5
- 测试终端未看到任何页面，或仍显示 `www.huawei.com`，接入侧/DN 侧抓包目的 IP 与源 IP 一样 → 步骤6

**步骤5**：测试终端在 `www.example.com` 或 `www.vmall.com` 页面上重新访问 `www.huawei.com` 网页。
- 看到正常访问 `www.huawei.com` → Captive Portal 业务正常，调测结束
- 仍看到 `www.example.com` 或未看到任何页面 → 步骤9

**步骤6**：检查 APN 下 Captive Portal 业务相关配置。
- a. `LST RULEBINDING:USERPROFILENAME="up_test";` 查询 User Profile 绑定的 Rule

预期输出：
```
-------------------------------
用户模板名称    规则名称       优先级                策略类型
 up_test       rule_test1       10          Captive Portal Smart Redirect
 up_test       rule_test2       20                      PCC
(结果个数 = 2)
---    END
```

- b. `LST RULE:RULENAME="rule_test1",POLICYTYPE=SMARTREDIRECT;` 查询 Rule 配置

预期输出：
```
-------------------------------
                             规则名称  =  rule_test1
                             策略类型  =  Captive Portal Smart Redirect
                        流过滤器名称  =  ff_test1
                             全局优先级  =  10
       Captive Portal IP-Farm名称  =  farm_test
---    END
```

- c. `LST PCCPOLICYGRP:PCCPOLICYGRPNM="pcc-pg_test";` 查询 PCC 策略组

预期输出：
```
-------------------------------
       PCC策略组名称  =  pcc-pg_test
        计费属性名称  =  cp_test
---    END
```

- d. `LST FLOWFILTER` / `LST PROTBINDFLOWF` / `LST L7FILTER` / `LST FLTBINDFLOWF` / `LST FILTER` 查询流过滤信息

预期输出（节选）：
```
LST FLOWFILTER:FLOWFILTERNAME="ff_test1";
       流过滤器名称  =  ff_test1

LST PROTBINDFLOWF:FLOWFILTERNAME="ff_test1";
       流过滤器名称  =  ff_test1
           协议名称  =  http
     七层过滤器名字  =  l7-test

LST L7FILTER:L7FILTERNAME="l7-test";
         七层过滤器名称  =  l7-test
       子七层过滤器名称  =  sub-l7-test
                    URL  =  www.huawei.com/*

LST FILTER:FILTERNAME="filter_test";
                   过滤器名字  =  filter_test
       三四层IPv4协议输入类型  =  字符串类型
           三四层协议类型  =  TCP
                 生效标记  =  是
```

判断：如与规划值不一致 → 参考 `配置用户Portal_66620114.md` 重新配置。

**步骤7**：执行 `LST IPFARM` / `LST IPFARMSERVER` 检查 IP Farm 中 server 的状态。

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
       地址信息  =  192.168.10.123
            URL  =  www.example.com
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

> SourcePath: `调测用户Portal_66620115.md` §操作步骤

### 6.2 验证命令汇总

| 命令 | 用途 |
|------|------|
| LST LICENSESWITCH | 查询 License 开关状态 |
| LST RULEBINDING | 查询 User Profile 绑定的 Rule |
| LST RULE | 查询规则配置（含 Captive Portal IP-Farm 名称） |
| LST PCCPOLICYGRP | 查询 PCC 策略组 |
| LST URRGROUP | 查询 URR 组 |
| LST FLOWFILTER / LST PROTBINDFLOWF / LST L7FILTER | 查询流过滤器与七层过滤信息 |
| LST FLTBINDFLOWF / LST FILTER | 查询过滤器绑定与过滤器配置 |
| LST IPFARM / LST IPFARMSERVER | 查询 IP Farm 及 server 状态（含 up/down） |
| LST LOGICINF | 查询心跳检测接口配置 |
| DSP RULECHECK | 检查规则 IP 版本一致性 |
| EXP MML | 导出 MML 配置脚本（故障信息收集） |

> SourcePath: `调测用户Portal_66620115.md`

### 6.3 告警参考

| 告警ID | 告警名称 | 触发条件 | 影响 |
|--------|---------|---------|------|
| ALM-81034 | IPFarm 无可用 server | IP Farm 内全部 server 状态为 down | Portal 无法重定向，用户报文按 DEFAULTACT 处理（BLOCK 时用户无法访问） |
| ALM-81035 | IPFarm 服务器无响应 | 服务器心跳检测失败（连续失败达 HEALTHFAILLIMIT） | 该 server 被排除出负荷分担候选 |

> SourcePath: `GWFD-110281 用户Portal参考信息_77079045.md` §告警

### 6.4 测量指标

| 指标ID | 指标名称 |
|--------|---------|
| 1914311754 | 用户平面 Captive portal 重定向次数 |
| 1914311755 | 用户平面 Captive portal 重定向成功次数 |

> 关键监控指标：1914311754（重定向次数）持续增长但 1914311755（成功次数）不增长 → 提示 IP Farm server 故障或网络问题。
> SourcePath: `GWFD-110281 用户Portal参考信息_77079045.md` §测量指标

### 6.5 常见问题与排查

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| 用户访问未被重定向（直接看到目标页面） | License 开关未打开 | `LST LICENSESWITCH:LICITEM="LKV3G5CPPT01";` 确认 SWITCH=ENABLE |
| 用户访问未被重定向 | SA 协议族未激活（SA-Basic/SA-Web Browsing 等 License 未开） | 检查 SA 协议族依赖 License；HTTP 报文需 SA-Basic + SA-Web Browsing，WAP1.X 需 SA-Mobile |
| 用户访问未被重定向 | L7Filter 未生效（SET REFRESHSRV 未执行或 60s 未到） | `LST FILTER` 确认生效标记=是；执行 `SET REFRESHSRV:REFRESHTYPE=USERPROFILE;` 立即生效 |
| 重定向未跳转到 Portal | IP Farm 内所有 server 状态为 down | `LST IPFARMSERVER` 查 server 状态；查 ALM-81034；检查心跳检测接口（LST LOGICINF）与 Portal Server ICMP 可达性 |
| 用户看到 Portal 但二次访问仍被重定向 | captive 定时器 CAPMODETHRES 设置过短或定时器未生效 | `LST USERPROFILE` 确认 CAPMODETHRES；检查定时器是否正常启动 |
| 用户二次访问不被重定向（应周期性重定向） | captive 定时器超时机制异常或处于 non-captive 模式 | 属预期行为（定时器未超时）；调大 CAPMODETHRES 会延长 non-captive 期 |
| HTTPS 流量 Portal 不生效 | HTTPS 为加密报文不支持重定向；或重定向 URL 为 HTTPS 未配黑名单 | 互斥限制：HTTPS 不支持重定向；重定向 URL 为 HTTPS 时配 `ADD BLACKLISTRULE` 放行 |
| 用户报文被阻塞（无法访问任何页面） | DEFAULTACT=BLOCK 且当前无法重定向 | `MOD IPFARMSERVER:DEFAULTACT=PASS` 改为放行；或修复 Portal Server |
| IPv6 规则不生效 | IP 版本不一致（IP Farm/Server/Filter/接口混用 IPv4/IPv6） | `DSP RULECHECK:RULENAME="rule_test1",POLICYTYPE=SMARTREDIRECT;` 检查一致性 |
| 重定向报文未携带正确 URL | ADD IPFARMSERVER 未配 URL 或 URL 错误 | `LST IPFARMSERVER` 确认 URL 字段（www.example.com） |
| PCC 触发链未生效 | rule_test2 POLICYTYPE 不是 PCC，或 FLOWFILTER 未绑定 | `LST RULE:RULENAME="rule_test2",POLICYTYPE=PCC;` 确认；`LST FLTBINDFLOWF` 确认绑定 |
| TCP 半连接堆积 | UDG 未向目标 Web Server 发送 TCP RST（软参 BIT412 配置） | 检查软参 BIT412（控制是否向手机发 RST）、BIT1473（响应报文方式） |

---

## 7. 参考信息

### 7.1 与其他特性的关系（特性关系网）

| 关联特性 | 特性ID | 关系说明 |
|---------|--------|---------|
| SA-Basic | GWFD-110101（UDG） | **强依赖**：UDG 解析 HTTP/WAP 报文的基础，必须开启 |
| SA-Web Browsing | GWFD-110103（UDG） | **协议依赖**：HTTP、WAP2.0 协议解析必需 |
| SA-Mobile | GWFD-110105（UDG） | **协议依赖**：WAP1.X 协议解析必需 |
| HTTP2.0 Host 识别 | GWFD-110201（UDG） | **互斥**：HTTP2.0 加密报文不支持重定向 |
| HTTPS 业务地址识别 | GWFD-110203（UDG） | **互斥**：HTTPS 加密报文不支持重定向 |
| PCC 基本功能 | GWFD-020351（UDG） | **触发依赖**：rule_test2 POLICYTYPE=PCC 负责计费属性，PCC 触发链为骨架 |
| HTTP 智能重定向 | GWFD-110284（UDG） | **同体系（轨道C）**：同为 SMARTREDIRECT，差异在用户Portal 独有 captive/non-captive 双模式 + IP Farm 负荷分担 |
| DNS 纠错 | GWFD-110283（UDG） | **同体系（轨道C）**：DNS 层重定向变体 |
| Web Proxy | GWFD-110282（UDG） | **互补（不同轨道）**：WebProxy 为 L3 IP NAT（轨道B 独立），用户Portal 为 L7 URL 重写（轨道C） |
| HTTP 头增强 | GWFD-110261/262/263（UDG） | **配合关系**：Portal 重定向 URL 可携带头增强的用户信息 |
| 增强的 ADC 基本功能 | GWFD-020357（UDG） | **互补关系**：ADC 提供应用级识别，可作为 Portal 触发的前置能力 |
| URL 过滤基本功能 | GWFD-110471（UDG） | **互补关系**：URL 过滤 REDIRECT 动作目标可为 Portal 页面 |

> 说明：GWFD-110284/110283/110282/110261-263/020357/110471 的关系系基于访问限制场景动作语义（轨道A/B/C 三轨体系）+ 产品文档交互表推断。
> SourcePath: `GWFD-110281 用户Portal特性概述_66655000.md` §与其他特性的交互

### 7.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-110281 用户Portal/GWFD-110281 用户Portal特性概述_66655000.md` | 适用NF（PGW-U/UPF）、定义、客户价值、应用场景、可获得性（UDG 20.0.0+、License LKV3G5CPPT01）、与其他特性交互（SA族依赖+HTTP2.0/HTTPS互斥）、对系统影响（吞吐量下降）、应用限制（终端支持HTTP/WAP重定向）、原理概述（captive/non-captive双模式+IP Farm负荷分担+ICMP心跳检测）、计费与话单（不涉及）、特性规格（64 IP Farm/512 IP每组）、遵循标准（HTTP/1.0/1.1+WSP）、发布历史 |
| 2 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110281 用户Portal/实现原理_74004638.md` | 12步完整业务流程（TCP建链→HTTP Get/Post→RULE匹配→SMARTREDIRECT→301/302/303重定向→可选TCP RST→避免半连接→Portal交互→non-captive→定时器超时二次重定向）、DEFAULTACT缺省动作说明、软参BIT1473/BIT412控制RST行为 |
| 3 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110281 用户Portal/配置用户Portal_66620114.md` | 11步操作流程、数据规划表（含完整字段取值）、完整MML脚本（License+IPFARMGLOBAL+LOGICINF+IPFARM+IPFARMSERVER+FILTER+FLOWFILTER+FLTBINDFLOWF+SIGNATUREDB+L7FILTER+PROTBINDFLOWF+REFRESHSRV+URR+URRGROUP+PCCPOLICYGRP+RULE(SMARTREDIRECT+PCC)+USERPROFILE+RULEBINDING+APN）、IPv4/IPv6一致性约束、DSP RULECHECK检查 |
| 4 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110281 用户Portal/调测用户Portal_66620115.md` | 9步调测流程（LST LICENSESWITCH→抓包→接入→访问www.huawei.com→抓包验证重定向→二次访问验证non-captive→LST RULEBINDING/RULE/PCCPOLICYGRP/FLOWFILTER/IPFARM/IPFARMSERVER/LOGICINF→EXP MML）、各步骤预期输出样例（中文） |
| 5 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110281 用户Portal/GWFD-110281 用户Portal参考信息_77079045.md` | MML命令清单（22条核心）、告警（ALM-81034/ALM-81035）、软参（BIT1473/BIT412/BIT467）、测量指标（1914311754/1914311755） |
| 6 | `UDG_Product_Documentation_CH_20.15.2/.../GWFD-110281 用户Portal/调整用户Portal参数/` 目录（7个子文档） | 修改Captive模式时间间隔、修改HTTP重定向响应码、修改IPFarm ServerIP/VIRTUALIP/心跳检测参数/心跳检测接口/负荷分担方式（参数调整操作） |

### 7.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| Portal Server | 个人门户网站服务器 | 提供业务订购、账户管理、费用管理、广告推送的服务器 |
| captive 模式 | 强制门户模式 | UDG 将用户请求重定向到 Portal Server 的状态 |
| non-captive 模式 | 非强制门户模式 | UDG 不重定向，用户直接访问 Web Server 的状态 |
| CAPMODETHRES | Captive Mode Threshold | captive 模式定时器（分钟），控制 captive/non-captive 切换周期 |
| IP Farm | IP 服务器集合 | Portal Server 的负荷分担集合，支持 ROUND_ROBIN/LEAST_RECENTLY_USED/LEAST_LOAD |
| SMARTREDIRECT | 智能重定向 | RULE.POLICYTYPE=SMARTREDIRECT，访问限制轨道C的动作类型（URL 重写级别） |
| DEFAULTACT | 缺省动作 | 无法重定向时的缺省动作（BLOCK 阻塞/PASS 放行） |
| Phif 接口 | 心跳检测逻辑接口 | IP Farm 发送 ICMP 心跳检测的源地址接口 |

---

## 8. 文档一致性说明（feature-doc-list vs 产品文档）

> feature-doc-list/文档清单仅用于定位特性ID，以下记录以产品文档实际内容为准时发现的潜在不一致与笔误，供 Stage 3 横向分析参考。

| # | 维度 | feature-doc-list/旧文档描述 | 产品文档实际内容 | 差异类型 |
|---|------|------------------------------|-----------------|---------|
| 1 | **动作机制归类（重大）** | 旧文档（轮1）未明确归类动作轨道，仅在"访问限制场景中的角色"提及"Portal 重定向核心特性" | 产品文档明确：用户Portal 使用 `POLICYTYPE=SMARTREDIRECT`（配置用户Portal文档任务示例 line 241）、`POLICYNAME=farm_test` 指向 IP Farm，属于 **轨道C（SMARTREDIRECT体系）**，与 GWFD-110284/110283 同体系 | **补全（重大）**：旧文档归类不明确，本文档确认归为轨道C，与 WebProxy（轨道B，POLICYTYPE=WEBPROXY）区分 |
| 2 | captive/non-captive 双模式 | 旧文档已描述 | 产品文档明确：两种模式交替，通过 CAPMODETHRES 定时器切换 | 一致（已强化） |
| 3 | HTTP 重定向响应码 | 旧文档未提及 | 产品文档（实现原理 §步骤4）明确：返回码可设置为 301、302 或 303，通过 SET SRVCOMMONPARA 全局配置 | 补全：响应码可配置，对应场景六变体 |
| 4 | TCP RST 拆链行为 | 旧文档未提及 | 产品文档（实现原理 §步骤5）明确：UDG 是否向 MS/UE 发送 TCP RST 由软参 BIT1473 和 BIT412 控制；§步骤6 UDG 给目标服务器发 TCP RST 避免半连接 | 补全：软参控制 RST 行为 |
| 5 | 无法重定向时缺省动作 | 旧文档未明确 | 产品文档明确：缺省 BLOCK（阻塞）；可通过 ADD/MOD IPFARMSERVER DEFAULTACT=PASS 改为放行 | 补全：对应场景四变体 |
| 6 | L7Filter 生效延迟 | 旧文档未提及 | 产品文档明确：系统自动 60s 后将配置的 L7Filter 置为生效；如需立即生效需手动 SET REFRESHSRV | 补全：60s 延迟机制 |
| 7 | 互斥特性完整性 | 旧文档列出 GWFD-110201/110203 | 产品文档一致：HTTP2.0 Host 识别、HTTPS 业务地址识别均互斥（加密报文不支持重定向） | 一致 |
| 8 | 协议依赖矩阵 | 旧文档列出 SA 族依赖 | 产品文档明确：HTTP/WAP2.0→SA-Web Browsing；WAP1.X→SA-Mobile；SA-Basic 必选 | 一致（已细化） |
| 9 | 遵循标准 | 旧文档未列 | 产品文档明确：IETF 1945（HTTP/1.0）、IETF 2616（HTTP/1.1）、IETF WSP（WAP-230-WSP-20010705-a） | 补全 |
| 10 | 测量指标数量 | 旧文档未列具体指标 | 参考信息明确：1914311754（重定向次数）、1914311755（重定向成功次数）2 项 | 补全 |
| 11 | 现有文档笔误 | （无） | 本次重读产品文档未发现明显笔误（5 份核心文档 + 7 份调整参数文档 MML 脚本参数一致） | 无 |
| 12 | feature_group 归属 | feature-doc-list 标注 feature_group=Portal | 产品文档路径在"智能策略控制功能"下，业务上归属重定向族；feature_group=Portal 与产品路径不冲突 | 一致（业务语义归 Portal 组，归属重定向族） |

---
