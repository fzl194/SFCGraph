---
id: ConfigurationSolution@access-webproxy
type: ConfigurationSolution
name: WebProxy
domain: business-awareness
scenario: access-control
status: draft
---

# WebProxy

> 将用户业务流重定向到 Proxy Server（L3 IP NAT 级别代理转发），基于目的 IP 匹配，无需 L7 URL 识别。属于[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)场景。

## 概览

WebProxy 把用户业务流重定向到 Proxy Server。核心机制：RULE 经 `POLICYTYPE=WEBPROXY` 直接引用 IP Farm（`POLICYNAME=IPFARMNAME`），独立于 PCC/SMARTREDIRECT 子轨，不经 PCCPOLICYGRP。IP Farm 是 Proxy Server 的负荷分担集合 + ICMP 心跳检测基础设施。WebProxy 的重定向是 **L3 IP NAT 级别**（基于目的 IP 做代理转发），区别于用户Portal 的 SMARTREDIRECT **L7 URL 级别**重定向。

本方案编排 1 个核心特性 + SA-Basic 依赖前提——UDG 侧[WebProxy 110282](task/UDG/20.15.2/2-00015.md)（POLICYTYPE=WEBPROXY + IPFarm，仅 L34 SVRIP 匹配，无 L7）+ [SA-Basic](task/UDG/20.15.2/2-00019.md)（业务识别前提，WebProxy 仅需 L34，不强需 SA-Web Browsing）。与 [用户Portal CS](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) **共享 IPFarm 基础设施**（compound [1-00014](task/UDG/20.15.2/1-00014.md)），但 POLICYTYPE 不同（WEBPROXY vs SMARTREDIRECT），可多 RULE 共存。

## 配置与协同

本方案编排 **2 个特性**：核心 [WebProxy 110282](task/UDG/20.15.2/2-00015.md) + 依赖前提 [SA-Basic](task/UDG/20.15.2/2-00019.md)。

**特性关系矩阵**（★回答"哪些必配 / 可选 / 包含 / 正交"，追溯 feature task 依赖声明 + [1-00014](task/UDG/20.15.2/1-00014.md) 场景差异）：

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [WebProxy 110282](task/UDG/20.15.2/2-00015.md)（GWFD-110282） | 核心（方案主体） | 必配 | POLICYTYPE=WEBPROXY + POLICYNAME=IPFARMNAME（直接引用 IP Farm，不经 PCCPOLICYGRP）；L3 IP NAT 重定向到代理池；仅 L34 SVRIP 匹配（无 L7）；无 captive 模式。**共享 IPFarm 基础设施**与 Portal（同 compound [1-00014](task/UDG/20.15.2/1-00014.md)）。ALGSWITCH（FTP ALG）是 WebProxy 独有 |
| [SA-Basic](task/UDG/20.15.2/2-00019.md)（GWFD-110101） | 基础（依赖前提） | 必配（License 前置） | 业务识别前提：报文解析基础。WebProxy 仅需 L34 匹配，**不强需 SA-Web Browsing**（L34 即可，对比用户Portal 需 SA-Web HTTP URL 识别）。配置**不与核心重叠**——SA 配识别链，WebProxy 配 IPFarm/RULE/USERPROFILE |

> 矩阵规则：①**核心**=方案主体（必配）；②**基础/依赖前提**=核心依赖的底层（必配，配置常与核心重叠）；③**维度增强**=正交维度可选叠加；④**跨网元对端**=另一网元对应特性；⑤**二选一**=互斥路径选其一。
>
> **与用户Portal CS 的关系**（防"互斥"误解）：本 CS 与 [用户Portal](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) **共享 IPFarm 基础设施**（compound [1-00014](task/UDG/20.15.2/1-00014.md)），但 POLICYTYPE 不同（WEBPROXY vs SMARTREDIRECT）。可作**两条不同 POLICYTYPE 的 RULE 绑同一 USERPROFILE 共存**（见 [策略匹配基础 CS](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) 多 RULE 机制）。

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**与**跨特性协同**。

### UDG 用户面：WebProxy（[2-00015](task/UDG/20.15.2/2-00015.md)）

走标准配置方法（见 feature task），**无特性级变种**（本 CS 即该特性的标准应用场景）。activation 主脚本演示 IPv4 + LEAST_LOAD + L34 SVRIP 匹配（发往 192.168.10.123 的 TCP 报文）+ WEBPROXY + PCC 双规则的标准场景。

> **CAPMODETHRES 在 WebProxy 无业务效果**：activation 虽在 ADD USERPROFILE 配 CAPMODETHRES=6，但 WebProxy 无 captive/non-captive 交替语义，该值继承 UP 模板默认（对比 Portal 的 captive 交替需该参数）。

### 跨特性协同：与用户Portal 共享 IPFarm + 差异点

- **共享基础设施**：WebProxy 与用户Portal 共用 compound [1-00014](task/UDG/20.15.2/1-00014.md)（IPFarm 重定向链）。
- **差异点**（[1-00014](task/UDG/20.15.2/1-00014.md) 场景差异 §1-§4）：①触发 POLICYTYPE（WEBPROXY vs SMARTREDIRECT）；②过滤匹配（WebProxy 仅 L34 SVRIP，Portal 需 L7 URL + L34）；③IPFARMSERVER.URL（WebProxy 可选，主要用 SERVERIPV4；Portal 必配）；④captive 模式（WebProxy 无，Portal 独有 CAPMODETHRES）；⑤REFRESHTYPE（WebProxy=ALL 改动到 Filter，Portal=USERPROFILE）。
- **WebProxy 独有**：ALGSWITCH（FTP ALG）仅 WebProxy 涉及（Portal 不涉及）。
- **可共存**：WebProxy RULE（WEBPROXY）与 Portal RULE（SMARTREDIRECT）可绑同一 USERPROFILE 共存。

## 决策点

### DP-1：重定向目标选择（选 CS）

| 选项/场景 | 影响（POLICYTYPE / 机制 / 承载 CS） |
|---|---|
| Web 代理（L3 IP NAT 到代理池）| POLICYTYPE=WEBPROXY + IPFarm（L3 IP 代理转发，仅 L34 SVRIP）；本 CS |
| Captive Portal（L7 URL 重定向）| POLICYTYPE=SMARTREDIRECT + IPFarm（L7 URL 重写）；→ [用户Portal CS](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) |
| HTTP/DNS 智能重定向（错误码触发）| POLICYTYPE=SMARTREDIRECT + 动作链（**不用 IPFarm**）；→ [智能重定向 CS](business/business-awareness/access-control/ConfigurationSolution@access-smart-redirect.md) |

### DP-2：WebProxy 部署维度（特性级，详见 [2-00015](task/UDG/20.15.2/2-00015.md) 决策点）

| 维度 | 选项 | 影响 |
|---|---|---|
| 负荷分担 LBMETHOD | LEAST_LOAD（默认）/ ROUND_ROBIN / LEAST_RECENTLY_USED | 选 Proxy Server 策略（[1-00014](task/UDG/20.15.2/1-00014.md) 场景差异 §5） |
| 过滤匹配 | L34 SVRIP（标准）/ +FLOWFILTERGRP | 仅 L34，无 L7；FLOWFILTERGRP 变体（[0-00294](task/UDG/20.15.2/0-00294.md)） |
| 无法重定向缺省 | DEFAULTACT=BLOCK（默认）/ PASS | ADD/MOD IPFARMSERVER（[1-00014](task/UDG/20.15.2/1-00014.md) 决策点） |

## 约束

- **WebProxy License 前置**（critical）：SET LICENSESWITCH 开启 `LKV3G5WEBP01` — 未开则 WebProxy 不生效（License 编号交叉验证自 [2-00015](task/UDG/20.15.2/2-00015.md) 约束段，非推断）。
- **SA-Basic License 前置**（critical）：开启 `LKV3G5SABS01` — 报文解析基础（交叉验证自 [2-00019](task/UDG/20.15.2/2-00019.md) + [2-00015](task/UDG/20.15.2/2-00015.md) 约束段）。WebProxy 不强需 SA-Web Browsing（L34 即可）。
- **POLICYTYPE=WEBPROXY 触发条件**（critical）：RULE.POLICYTYPE=WEBPROXY + POLICYNAME=IPFARMNAME（直接引用 IP Farm，PCC 策略组名称=NULL）— 指错则重定向不触发。
- **仅 L34 匹配，无 L7**（warning）：WebProxy 仅基于 FILTER 的 SVRIP 服务器IP匹配，不需 L7FILTER/LOD SIGNATUREDB — 若配 L7 过滤条件则语义偏离。
- **DNS 等非 TCP/七层协议不能用 WebProxy**（warning）：WebProxy 仅适配 L34 TCP 业务流，绑定 DNS 等协议的流过滤器不能触发 WebProxy。
- **IP 版本全链路一致**（critical）：IPFARM/SERVER/LOGICINF/Filter/接口须同 v4 或同 v6 — `DSP RULECHECK` 检查。
- **至少一 Server 状态 up**（warning）：`LST IPFARMSERVER` 须保证至少一个 server 状态 up。
- **不同 IP Farm 需不同心跳接口**（warning）：心跳检测接口不共享。
- **REFRESHTYPE=ALL**（info）：WebProxy 改动到 Filter（含 SVRIP），故 REFRESHSRV 用 ALL（全集刷新），区别于 Portal 的 USERPROFILE。

## 关联

- 上游场景：[访问限制](business/business-awareness/access-control/NetworkScenario@access-control.md)
- 编排特性（feature task，优先）：[2-00015 WebProxy](task/UDG/20.15.2/2-00015.md) · [2-00019 SA-Basic](task/UDG/20.15.2/2-00019.md)
- 复用步骤/命令（compound/atom，按需）：[1-00014](task/UDG/20.15.2/1-00014.md) IPFarm重定向链（与 Portal 共享）· [1-00009](task/UDG/20.15.2/1-00009.md) 过滤链（仅 L34 段）· [1-00011](task/UDG/20.15.2/1-00011.md) 规则绑定 · [1-00010](task/UDG/20.15.2/1-00010.md) 计费三件套（可选 PCC 双规则）· [0-00294](task/UDG/20.15.2/0-00294.md) FLOWFILTERGRP（可选）· [0-00293](task/UDG/20.15.2/0-00293.md) BLACKLISTRULE（HTTPS 旁路）
- 基础 CS：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md)（backbone + POLICYTYPE 6 子轨）
- 同族 CS：[用户Portal](business/business-awareness/access-control/ConfigurationSolution@access-portal.md)（共享 IPFarm，POLICYTYPE=SMARTREDIRECT）· [智能重定向](business/business-awareness/access-control/ConfigurationSolution@access-smart-redirect.md)（不用 IPFarm）
- 证据：[配置Web Proxy](evidence/business/access-control/配置Web-Proxy_66987339.md)（数据规划表 + 操作步骤 + 任务示例脚本，主源）
