# R6: 可靠性管理/HA — 规则挖掘

## 0. 探索范围

| 领域 | 核心命令 |
|------|---------|
| 容灾组 | ADD DRGROUPINFO |
| DC 间通信 | ADD DRDCI |
| 故障隔离 | ADD DRSEPINTERFACE |
| Pod 自愈 | ADD PODBLACKLIST, ADD PODHEALCPUTHR |
| 人工倒换 | STR NFDREXE, STR NFDRSWOVER |

---

## 1. 命令链路图

```
ADD DRGROUPINFO (容灾组: DRGROUPID + DRGROUPNAME + 本端/对端实例)
  ├→ ADD DRDCI (DC间通信通道: 引用DRGROUPID + VPN实例 + 心跳参数)
  ├→ ADD DRSEPINTERFACE (故障隔离接口: 引用DRGROUPID)
  ├→ ADD PODBLACKLIST (Pod自愈黑名单: 阻止自愈的Pod)
  ├→ ADD PODHEALCPUTHR (Pod自愈CPU阈值)
  └→ STR NFDREXE / STR NFDRSWOVER (人工容灾倒换/倒回)
```

---

## 2. 显式规则

| # | 规则 | 来源 | 严重度 |
|---|------|------|--------|
| R6-E01 | DRGROUPINFO 只允许 1 条记录 | ADD DRGROUPINFO | 错误 |
| R6-E02 | DRGROUPINFO 的 DRGROUPID 和 DRGROUPNAME 必须与对端节点一致 | ADD DRGROUPINFO | 错误 |
| R6-E03 | DRDCI 是高危命令，可能导致业务中断 | ADD DRDCI | 风险 |
| R6-E04 | DRDCI 的 VPNINSTANCE 必须已存在 | ADD DRDCI | 错误 |
| R6-E05 | DRDCI 最大 16 条记录 | ADD DRDCI | 警告 |
| R6-E06 | DRSEPINTERFACE 最大 65535 条 | ADD DRSEPINTERFACE | 警告 |
| R6-E07 | DRGROUPINFO 只用于冷备/热备容灾模式 | ADD DRGROUPINFO | 约束 |
| R6-E08 | DRSEPINTERFACE 只用于热备容灾模式 | ADD DRSEPINTERFACE | 约束 |

---

## 3. 隐式规则

### 3.1 对端节点对称性（paired_node_symmetry）

**发现**：容灾组的配置在本端和对端必须完全对称。DRGROUPID、DRGROUPNAME 必须匹配，本端实例ID(LDRINSTID)对应对方的对端实例ID(PDRINSTID)。

**证据**：
- ADD DRGROUPINFO: "DRGROUPID 和 DRGROUPNAME 必须与对端节点一致"
- LDRINSTID 和 PDRINSTID 是互换关系

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R6-I01 | 本端 LDRINSTID = 对端 PDRINSTID，本端 PDRINSTID = 对端 LDRINSTID | DRGROUPINFO | 跨网元一致性 |
| R6-I02 | DRGROUPID 不匹配 → 容灾倒换失败 | DRGROUPINFO | 跨网元一致性 |
| R6-I03 | DRDCI 的对端 IP 必须与对端节点的本端 IP 一致 | DRDCI | 跨网元一致性 |

### 3.2 心跳参数超时计算（heartbeat_timeout_calculation）

**发现**：DRDCI 的故障检测时间由 HBINTERVAL × HBTIMES 计算。

**证据**：
- HBINTERVAL: 心跳间隔（1-100，单位 100ms，即 0.1-10 秒）
- HBTIMES: 心跳重试次数（1-30）
- 故障检测时间 = HBINTERVAL × 100ms × HBTIMES

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R6-I04 | 最大检测时间 = 10s × 30 = 300s，如果设得太大 → 故障发现慢 | DRDCI | 定量计算 |
| R6-I05 | 本端和对端的 HBINTERVAL 和 HBTIMES 应一致，否则一端先判定故障导致非对称倒换 | DRDCI | 跨网元一致性 |

### 3.3 容灾模式约束传播（dr_mode_constraint_propagation）

**发现**：DRGROUPINFO 的容灾模式（冷备/热备）约束了下游命令的行为：
- DRSEPINTERFACE 只用于热备模式
- DRDCI 的 DATABKMODE 在热备时才支持 Active-Standby_Hot_Backup

**证据**：
- ADD DRSEPINTERFACE: "只用于热备容灾模式"
- ADD DRDCI: DATABKMODE 枚举值含 Active-Standby_Hot_Backup

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R6-I06 | DRGROUPINFO 配置为冷备时，DRSEPINTERFACE 的配置无意义（热备专用） | DRGROUPINFO + DRSEPINTERFACE | 属性兼容约束 |
| R6-I07 | 热备模式下应有至少一个 DRDCI 通道，否则心跳无法传递 | DRGROUPINFO + DRDCI | 引用可达性 |

### 3.4 VPN 实例复用（vpn_instance_reuse）

**发现**：DRDCI 引用 VPNINSTANCE，与 IP 地址管理链的 VPNINST 是同一对象。

**证据**：
- ADD DRDCI: VPNINSTANCE 参数，"必须已存在"
- 默认值: "_public_"

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R6-I08 | DRDCI 使用的 VPN 实例应与容灾对端可达（跨 DC 的 VPN 路由正确） | DRDCI + VPNINST | 跨链依赖 |
