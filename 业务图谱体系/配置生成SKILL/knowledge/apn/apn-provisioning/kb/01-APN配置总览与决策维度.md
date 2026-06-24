# 01-APN 配置总览与决策维度

> 数据源：`APN配置树.md` + `APN意图澄清知识库.md` + `three-layer-graph/01-business-graph.md` §2~§3
> 作用：Phase 1 场景识别 / Phase 3 参数收集的总览

---

## 1. APN 配置树三大类

APN 开通（NS-APN-01）单场景，配置树根节点下三大类（详见 `../APN配置树.md`）：

| 大类 | 节点类型 | 子节点 | 说明 |
|------|---------|--------|------|
| 地址分配信息 | OR（择一） | UPF分配 / SMF分配 / UDM分配 / Radius分配 / DHCP分配 / LNS分配 | 决定 IP 来源 |
| 鉴权计费信息 | AND（全选） | Radius鉴权接入(WSFD-011305) + Radius功能(WSFD-011306) | 按鉴权方式决定是否选中 |
| 接入方式信息 | OR（择一） | VPN（直通）/ GRE / IPSec | 决定隧道封装 |

---

## 2. 4 维度决策点（NS-APN-01）

| 决策点 | 问题 | option_set | 影响 |
|--------|------|-----------|------|
| `DP-APN-ADDR-MODE` | UE IP 地址由谁分配 | UDM静态/UPF-APN动态/UPF-LOCATION动态/UPF-SMF动态/SMF本地/RADIUS下发/DHCP代理/LNS | POOLTYPE / POOLGRPMAP 映射粒度 / C-U 决策执行分离 |
| `DP-APN-ADDR-GRANULARITY` | 地址池按什么粒度匹配 | APN-1&LOC-0&SMF-0 等 7 组合 | 三级优先级规则字符串 |
| `DP-APN-ADDR-TYPE` | IPv4/IPv6/双栈 | IPv4/IPv6/IPv4v6 | SECTION 参数 / License 触发 |
| `DP-APN-AUTH-MODE` | 鉴权方式 | TRANS_NON_AUTH/TRANS_AUTH/NON_TRANS/LOC_AUTH | 是否调用 AAA / 账密来源 |
| `DP-APN-ACCESS-MODE` | 接入方式 | 直连/NAT/IPSec/GRE/MPLS/L2TP/GRE-over-IPSec | 隧道封装类型 / C-U 协同模式 |

---

## 3. 9 方案闭包（CS-APN-01~09）

| 方案 | 典型场景 | 地址分配 | 鉴权 | 地址类型 | 接入方式 |
|------|---------|---------|------|---------|---------|
| CS-APN-01 | 工厂工控访问内网 | UDM 静态 | NON_TRANS | IPv4 | IPSec |
| CS-APN-02 | 智慧农业传感器上报 | UPF-APN 动态 | TRANS_NON_AUTH | IPv4 | NAT/直连 |
| CS-APN-03 | 家庭 CPE 宽带 | UPF-SMF 动态 | TRANS_NON_AUTH | IPv4v6 双栈 | NAT/直连 |
| CS-APN-04 | VoLTE 语音 | SMF 本地动态 | TRANS_NON_AUTH | IPv4v6 双栈 | 直连 |
| CS-APN-05 | 企业 AAA 二次鉴权 | RADIUS 下发 | NON_TRANS | IPv4 | GRE/直连 |
| CS-APN-06 | 传统企业 DHCP 迁移 | DHCP 代理 | TRANS_NON_AUTH | IPv4 | 直连 |
| CS-APN-07 | 企业 L2TP VPN | LNS (L2TP) | NON_TRANS | IPv4v6 双栈 | L2TP |
| CS-APN-08 | 区域化运营管理 | UPF-LOCATION 动态 | TRANS_NON_AUTH | IPv4 | 直连 |
| CS-APN-09 | 企业双栈加密接入 | UPF-APN 动态 | TRANS_NON_AUTH | IPv4v6 双栈 | IPSec |

> 端到端方案链路详见 `01-business-graph.md` §9。

---

## 4. 业务规则（BR-APN-01~16）速查

**互斥约束**：
- BR-APN-LOC-L2TP-EXCL：基于位置 × L2TP 互斥
- BR-APN-GRE-IPSEC-SRC-EXCL：GRE × IPSec 源地址互斥
- BR-APN-L2TP-ADDRAUTO-EXCL：L2TP × 地址自动检测互斥

**级联强依赖**：
- BR-APN-RADIUS-CASCADE：Radius 功能(011306) → 鉴权接入(011305) → 二次鉴权(108007)
- BR-APN-IPV6-CASCADE：IPv6 承载(020401) → 双栈(020403) → PD(020406)

**License 触发**：BR-APN-DUALSTACK-NEED-LICENSE / BR-APN-LOC-NEED-LICENSE / BR-APN-L2TP-CU-ASYM

**协议限制**：BR-APN-SECOND-AUTH-PROTO（二次鉴权仅 PAP/CHAP）/ BR-APN-LOC-AUTH-NO-PPP（LOC_AUTH 不支持 PPP）

**决策一致性**：BR-APN-CONCURRENCY-11-15 / BR-APN-ALIAS-DOUBLE-COND / BR-APN-UPF-VENDOR-LOCK / BR-APN-AMF-LOCAL-FIRST / BR-APN-CARDTYPE-NEED-AUTH / BR-APN-DNAAA-IP-UNIQUE

---

## 5. 12 语义对象（SO-APN-*）

| 语义对象 | 含义 |
|---------|------|
| SO-APN-ADDRESS-POOL | 地址分配契约（6 来源 / IPv4/v6/双栈 / 池组 / 段范围 / 生命周期） |
| SO-APN-AUTH-AAA | 鉴权 AAA（三态嵌套：底层 AKA + APN 业务鉴权 + DN 二次鉴权） |
| SO-APN-TUNNEL | 隧道（GRE/IPSec/MPLS/L2TP） |
| SO-APN-QUOTA-LIFECYCLE | 配额/地址生命周期（5 大增值功能） |
| SO-APN-SESSION-CONTEXT | PDU/PDN/PDP 会话上下文（纯描述性底座） |
| SO-APN-SUBSCRIPTION | UNC 签约数据本地缓存 |
| SO-APN-APNACTNUM | 单 APN 并发限制 |
| SO-APN-ALIAS-APN-MAP | 别名 APN 双向映射 |
| SO-APN-PNFPROFILE | UPF NF 实例属性（三轮筛选） |
| SO-APN-AREDNS | 位置区域 DNS 域名定制 |
| SO-APN-ARD-RECORD | 接入限制参数记录（C 面） |
| SO-APN-APNQOSATTR | APN QoS 属性（U 面带宽流控） |
