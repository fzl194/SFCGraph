---
id: ConfigurationSolution@access-portal
type: ConfigurationSolution
name: 用户 Portal
domain: business-awareness
scenario: access-control
status: draft
---

# 用户 Portal

> 将用户首次访问的 HTTP 请求自动重定向到个人门户网站（Portal Server），支持 captive/non-captive 双模式交替。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

用户 Portal 把用户上线后首次访问的 HTTP 请求重定向到 Portal Server，是 SMARTREDIRECT 子轨的典型应用。核心机制：RULE 经 `POLICYTYPE=SMARTREDIRECT` 直接引用 IP Farm（`POLICYNAME=IPFARMNAME`），独立于 PCC/HEADEN 子轨，不经 PCCPOLICYGRP。IP Farm 是 Portal Server 的负荷分担集合 + ICMP 心跳检测基础设施（LBMETHOD 选 Portal Server）。

本方案编排 1 个核心特性 + SA-Basic 依赖前提——UDG 侧[用户Portal 110281](task/UDG/20.15.2/2-00014.md)（POLICYTYPE=SMARTREDIRECT + IPFarm，L7 URL 重定向到 Portal；captive/non-captive 双模式由 USERPROFILE.CAPMODETHRES 定时器控制交替）+ [SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提，含 SA-Web Browsing HTTP URL 识别）。与 [WebProxy CS](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md) **共享 IPFarm 基础设施**（compound [1-00014](task/UDG/20.15.2/1-00014.md)），但 POLICYTYPE 不同（SMARTREDIRECT vs WEBPROXY），可多 RULE 共存。

## 配置与协同

本方案编排 **2 个特性**：核心 [用户Portal 110281](task/UDG/20.15.2/2-00014.md) + 依赖前提 [SA-Basic](task/UDG/20.15.2/2-00019.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 feature task 依赖声明 + [1-00014](task/UDG/20.15.2/1-00014.md) 场景差异）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [用户Portal 110281](task/UDG/20.15.2/2-00014.md)（GWFD-110281） | 核心（方案主体） | 必配 | POLICYTYPE=SMARTREDIRECT + POLICYNAME=IPFARMNAME（直接引用 IP Farm，不经 PCCPOLICYGRP）；L7 URL 重定向到 Portal（构造 HTTP 301/302/303）；captive/non-captive 双模式交替。**共享 IPFarm 基础设施**与 WebProxy（同 compound [1-00014](task/UDG/20.15.2/1-00014.md)） |
| [SA-Basic](task/UDG/20.15.2/2-00019.md)（GWFD-110101） | 基础（依赖前提） | 必配（License 前置） | 业务识别前提：HTTP 报文解析基础（SA-Basic）+ SA-Web Browsing（GWFD-110103，HTTP/WAP2.0 URL 识别必需）。配置**不与核心重叠**——SA 配识别链（SIGNATUREDB/PARSERDB），用户Portal 配 IPFarm/RULE/USERPROFILE |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加；④**跨网元对端**=另一网元对应特性；⑤**二选一**=互斥路径选其一。
>
> **与 WebProxy CS 的关系**（防"互斥"误解）：本 CS 与 [WebProxy](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md) **共享 IPFarm 基础设施**（compound [1-00014](task/UDG/20.15.2/1-00014.md)），但 POLICYTYPE 不同（SMARTREDIRECT vs WEBPROXY）。**单条 RULE 内 POLICYTYPE 互斥**——但 Portal 与 WebProxy 可作为**两条不同 POLICYTYPE 的 RULE 绑同一 USERPROFILE 共存**（见 [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) 多 RULE 机制）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：用户Portal（[2-00014](task/UDG/20.15.2/2-00014.md)）

走标准配置方法（见 feature task），**无特性级变种**（本 CS 即该特性的标准应用场景）。activation 主脚本演示 IPv4 + LEAST_LOAD + L7 URL 触发（www.huawei.com/*）+ SMARTREDIRECT + PCC 双规则 + CAPMODETHRES=6 的标准场景，使用者直接按 feature task 决策点组合。

### 跨特性协同：与 WebProxy 共享 IPFarm

- **共享基础设施**：用户Portal 与 WebProxy 共用 compound [1-00014](task/UDG/20.15.2/1-00014.md)（IPFarm 重定向链）——SET IPFARMGLOBAL + ADD LOGICINF + ADD IPFARM + ADD IPFARMSERVER。两者 RULE 的 POLICYNAME 都指向同一 IPFARMNAME，差异仅在 POLICYTYPE（SMARTREDIRECT vs WEBPROXY）。
- **差异点**（[1-00014](task/UDG/20.15.2/1-00014.md) 场景差异 §1-§4）：①触发 POLICYTYPE（SMARTREDIRECT vs WEBPROXY）；②过滤匹配（用户Portal 需 L7 URL 匹配 + L34，WebProxy 仅 L34 SVRIP）；③IPFARMSERVER.URL（用户Portal 必配 Portal Server URL，WebProxy 主要用 SERVERIPV4）；④captive 模式（用户Portal 独有 CAPMODETHRES，WebProxy 无此语义）。
- **可共存**：Portal RULE（SMARTREDIRECT）与 WebProxy RULE（WEBPROXY）可绑同一 USERPROFILE 共存，分别处理不同业务流。

## 决策点

### DP-1：重定向目标选择（选 CS）

| 选项/场景 | 影响（POLICYTYPE / 机制 / 承载 CS） |
|---|---|
| Captive Portal（L7 URL 重定向到 Portal Server）| POLICYTYPE=SMARTREDIRECT + IPFarm（L7 URL 重写，构造 HTTP 301/302/303）；本 CS |
| Web 代理（L3 IP NAT 到代理池）| POLICYTYPE=WEBPROXY + IPFarm（L3 IP 代理转发，无 L7）；→ [WebProxy CS](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md) |
| HTTP/DNS 智能重定向（错误码触发）| POLICYTYPE=SMARTREDIRECT + 动作链（SMARTHTTPREDIR/DNSOVERWRITING，**不用 IPFarm**）；→ [智能重定向 CS](business/business-awareness/access-control/ConfigurationSolution@access-smart-redirect.md) |

### DP-2：Portal 部署维度（特性级，详见 [2-00014](task/UDG/20.15.2/2-00014.md) 决策点）

| 维度 | 选项 | 影响 |
|---|---|---|
| 负荷分担 LBMETHOD | LEAST_LOAD（默认）/ ROUND_ROBIN / LEAST_RECENTLY_USED | 选 Portal Server 策略，SET IPFARMGLOBAL（[1-00014](task/UDG/20.15.2/1-00014.md) 场景差异 §5） |
| captive 交替 | CAPMODETHRES（定时器分钟，activation=6） | captive/non-captive 双模式交替；WebProxy 无此语义 |
| HTTP 响应码 | HTTPREDIRCODE=RSP_CODE_301/302/303 | SET SRVCOMMONPARA（[0-00065](task/UDG/20.15.2/0-00065.md)），activation 未演示 |
| HTTPS 重定向 URL | BLACKLISTRULE 放行 | UDG 不支持 HTTPS 重定向，需旁路（[0-00293](task/UDG/20.15.2/0-00293.md)） |

## 约束

- **用户Portal License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5CPPT01` — 未开则用户Portal 不生效（License 编号交叉验证自 [2-00014](task/UDG/20.15.2/2-00014.md) 约束段，非推断）。
- **SA-Basic License 前置**（critical）：开启 `LKV3G5SABS01`（控制项 82209749）+ SA-Web Browsing `LKV3G5SAWB01`（GWFD-110103）— HTTP URL 识别必需（交叉验证自 [2-00019](task/UDG/20.15.2/2-00019.md) + [2-00014](task/UDG/20.15.2/2-00014.md) 约束段）。
- **POLICYTYPE=SMARTREDIRECT 触发条件**（critical）：RULE.POLICYTYPE=SMARTREDIRECT + POLICYNAME=IPFARMNAME（直接引用 IP Farm，PCC 策略组名称=NULL）— 指错则重定向不触发。
- **IP 版本全链路一致**（critical）：IPFARM/SERVER/LOGICINF/Filter/接口须同 v4 或同 v6 — `DSP RULECHECK` 检查；不一致则重定向失效。
- **仅 HTTP/WAP，不支持 HTTPS/HTTP2.0**（warning）：HTTPS 需 BLACKLISTRULE 旁路放行（[0-00293](task/UDG/20.15.2/0-00293.md)）；HTTP2.0 不支持。
- **至少一 Server 状态 up**（warning）：`LST IPFARMSERVER` 须保证至少一个 server 状态 up — 否则重定向无可用目标。
- **不同 IP Farm 需不同心跳接口**（warning）：心跳检测接口不共享。
- **REFRESHSRV 时序**（critical）：`SET REFRESHSRV` 在所有 ADD/SET 完成后最后执行；`PROTBINDFLOWF` 后需等待 60 秒。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 编排特性（feature task，优先）：[2-00014 用户Portal](task/UDG/20.15.2/2-00014.md) · [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)
- 复用步骤/命令（compound/atom，按需）：[1-00014](task/UDG/20.15.2/1-00014.md) IPFarm重定向链（与 WebProxy 共享）· [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链（L34+L7）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套（可选 PCC 双规则）· [0-00065](task/UDG/20.15.2/0-00065.md) SRVCOMMONPARA（HTTP 响应码）· [0-00293](task/UDG/20.15.2/0-00293.md) BLACKLISTRULE（HTTPS 旁路）
- 基础 CS：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（backbone + POLICYTYPE 6 子轨）
- 同族 CS：[WebProxy](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md)（共享 IPFarm，POLICYTYPE=WEBPROXY）· [智能重定向](business/business-awareness/access-control/ConfigurationSolution@access-smart-redirect.md)（同 SMARTREDIRECT 但不用 IPFarm）
- 证据：[配置用户Portal](evidence/business/access-control/配置用户Portal_66620114.md)（数据规划表 + 任务示例脚本，主源）
