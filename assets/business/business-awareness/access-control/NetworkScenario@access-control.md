---
id: NetworkScenario@access-control
type: NetworkScenario
name: 访问限制
domain: business-awareness
scenario: access-control
status: draft
---

# 访问限制

> 按业务/URL/位置对用户流量做阻断/重定向/头增强/内容过滤。属于[业务感知](business/business-awareness/BusinessDomain@business-awareness.md)域。含 8 个方案（策略匹配基础 + URL过滤/头增强族/重定向族/位置策略）。

## 概览

访问限制场景对用户访问的业务/URL/位置施加控制动作：阻断（BLOCK）、重定向（REDIRECT，Portal/Proxy/智能重定向）、头增强（HEADEN，插入用户信息给 Web Server）、内容过滤（URL 分类黑白名单）、IP 重定向。

**双轨道架构**（追溯 ADD RULE 命令 + 头增强差异表 + 套餐3实例）：
- **共享 backbone**：所有动作共用 RULE + USERPROFILE + RULEBINDING + 过滤链 + SA-Basic（业务识别前提）。RULE.POLICYTYPE 是动作总开关。
- **轨道 A（POLICYTYPE 隐式）**：RULE.POLICYTYPE 取值决定动作——PCC（策略/计费控制）/ HEADEN（头增强）/ SMARTREDIRECT（智能重定向）/ WEBPROXY（Web代理）/ ADC（应用检测）/ IPREDIR（IP重定向）。**单 RULE 内 POLICYTYPE 互斥；多动作通过多 RULE 绑定同一 USERPROFILE 共存**（套餐3实例：4 业务 4 条 RULE 共存）。
- **轨道 B（CF 显式）**：URL 过滤的 CFTEMPLATE.ACTION 决定动作（允许/阻断/重定向），APN 粒度开启；但流匹配仍走 RULE.POLICYTYPE=PCC backbone（非纯独立轨道）。

**判断依据**：用户需按 URL/业务/位置阻断或重定向，或需向 Web Server 插入用户信息（头增强），或需 URL 分类过滤。**典型产出**：违规 URL 阻断、用户 Portal 重定向（captive portal）、HTTP 头插入 MSISDN/IMSI、HTTPS 头增强、DNS 纠错重定向。

跨网元协同：UDG（用户面）做所有访问限制动作执行（RULE 匹配 + 动作）；UNC（控制面）做位置策略决策（WSFD-211001，PCF 按位置下发 PCC 策略→UDG 执行）。Backbone 共享 SA-Basic + PCC基本功能。

## 边界

- 覆盖：UDG（用户面 RULE 动作执行——头增强/重定向/URL过滤/阻断/IP重定向）+ UNC（控制面位置策略 WSFD-211001）；接口 N4/PFCP、Gx/N7；控制维度：POLICYTYPE（6 子轨）、URL 分类（CF）、协议（HTTP/RTSP/HTTPS/DNS）、位置（ULI）。
- 不覆盖：业务识别基础（属 SA-Basic backbone）、带宽限速（属带宽控制场景，但 PCC 子轨与带宽 PCC 共享 backbone）、计费（属计费场景，PCC 子轨多功能含计费触发）。

## 决策点

场景级方案路由——什么业务诉求选哪个方案。

| 业务诉求 | 推荐方案 | 理由 |
|---|---|---|
| 访问限制基础（RULE+POLICYTYPE 动作机制，所有动作底座） | → [策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) | 共享 backbone + POLICYTYPE 6 子轨动作选择，多 RULE 共存 |
| URL 分类黑白名单过滤（阻断/重定向） | → [URL 过滤](business/business-awareness/access-control/ConfigurationSolution@access-url-filter.md) | 轨道B CF.ACTION + PCC RULE 触发；ICAP 外置分析可选 |
| HTTP/RTSP 报文头插入用户信息 | → [HTTP/RTSP 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md) | POLICYTYPE=HEADEN，共享 ADD HEADEN；RTSP 是协议变种 |
| HTTPS 报文头插入用户信息 | → [HTTPS 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md) | 独立 ADD TLSHEADEN（TLS Extension TLV），非复用 HEADEN |
| Captive Portal 重定向（L7 URL 重定向到 Portal） | → [用户 Portal](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) | POLICYTYPE=SMARTREDIRECT + IPFarm |
| Web 代理重定向（L3 IP NAT 到代理池） | → [WebProxy](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md) | POLICYTYPE=WEBPROXY + IPFarm（与 Portal 共享 IPFarm） |
| HTTP 智能重定向 / DNS 纠错（错误码/DNS 层重定向） | → [智能重定向](business/business-awareness/access-control/ConfigurationSolution@access-smart-redirect.md) | SMARTREDIRECT 动作链（SMARTHTTPREDIR/DNSOVERWRITING），不用 IPFarm |
| 按用户初始接入位置触发策略控制 | → [位置策略](business/business-awareness/access-control/ConfigurationSolution@access-location-policy.md) | UNC WSFD-211001 跨网元，PCF 按位置决策→UDG 执行 |

## 关联

- 上游域：[业务感知](business/business-awareness/BusinessDomain@business-awareness.md)
- 下游方案（8 个）：[策略匹配基础](business/business-awareness/access-control/ConfigurationSolution@access-backbone.md) · [URL 过滤](business/business-awareness/access-control/ConfigurationSolution@access-url-filter.md) · [HTTP/RTSP 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-http.md) · [HTTPS 头增强](business/business-awareness/access-control/ConfigurationSolution@access-headen-https.md) · [用户 Portal](business/business-awareness/access-control/ConfigurationSolution@access-portal.md) · [WebProxy](business/business-awareness/access-control/ConfigurationSolution@access-webproxy.md) · [智能重定向](business/business-awareness/access-control/ConfigurationSolution@access-smart-redirect.md) · [位置策略](business/business-awareness/access-control/ConfigurationSolution@access-location-policy.md)
- 证据：[套餐3访问限制场景实例](evidence/business/access-control/套餐3：访问限制场景_94838086.md)（4业务4RULE共存权威验证）+ [头增强差异表](evidence/business/access-control/头增强功能之间的差异_10706790.md) + [RULE概念](evidence/business/access-control/规则_92407887.md) + [ADD RULE命令](evidence/business/access-control/ADD_RULE_82837266.md) + 各特性激活（URL过滤/Portal/WebProxy/DNS/HTTP重定向/头增强/防欺诈）
