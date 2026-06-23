## 第二章：CAR 限速参数

> BWMCONTROLLER 在 CTRLTYPE=CAR 模式下的参数体系。来源：`three-layer-graph/04-command-graph.md` §5.1、`feature-knowledge/cross-feature-analysis.md` 附录 F、`feature-knowledge/GWFD-110311-基于业务感知的带宽控制.md`。

---

### K201: CAR 令牌桶算法原理 [原理]

CAR（Committed Access Rate，承诺访问速率）使用**双令牌桶三色标记**算法（RFC 2697/2698），对流量进行监管（Policing）：

| 元素 | 含义 | 单位 |
|------|------|------|
| CIR | 承诺信息速率（Committed Information Rate）— GREEN 阈值 | kbps |
| PIR | 峰值信息速率（Peak Information Rate）— YELLOW/RED 边界 | kbps |
| CBS | 承诺突发尺寸（Committed Burst Size） | bytes |
| PBS | 峰值突发尺寸（Peak Burst Size） | bytes |

超额报文：**直接丢弃或重标记**（不缓冲，与 Shaping 关键区别）。

---

### K202: 三色标记规则 [原理]

| 颜色 | 触发条件 | 业务含义 |
|------|---------|---------|
| **GREEN** | 报文消耗令牌后未超 CIR | 正常承诺速率内，优先转发 |
| **YELLOW** | 报文超 CIR 但未超 PIR | 突发流量，有限转发 |
| **RED** | 报文超 PIR | 严重超额，丢弃或重标记 |

---

### K203: GREENACT / YELLOWACT / REDCT 三色动作 [配置]

每个颜色可独立配置动作（枚举值：`PASS` / `REMARK` / `DISCARD`）：

| 业务价值 | 典型组合 | 说明 |
|---------|---------|------|
| 低价值（P2P） | GREEN=PASS, YELLOW=REMARK, RED=DISCARD | 超额直接丢弃 |
| 中价值 | GREEN=PASS, YELLOW=PASS, RED=DISCARD | 给一定突发容忍 |
| 高价值（但非 GBR） | GREEN=PASS, YELLOW=REMARK, RED=REMARK | 尽量不丢，靠无线侧调度 |

**配置实例**：
```mml
ADD BWMCONTROLLER:BWMCNAME="p2p_car",CTRLTYPE=CAR,
  CIR=2048,CBS=256000,PIR=4096,PBS=512000,
  GREENACT=PASS,YELLOWACT=REMARK,REDACT=DISCARD,
  COLORISAWARE=ENABLE;
```

---

### K204: CBS/PBS 推导规则 [配置]

CBS/PBS 决定突发容忍度，过小导致 TCP 窗口频繁收缩，过大会失去限速效果。

**经验推导**：
- CBS ≈ CIR × 时间窗口（通常 1~2 秒等价的字节数）
- PBS ≈ PIR × 时间窗口，且 PBS ≥ CBS
- 示例：CIR=2048kbps → CBS≈256000bytes（约 1 秒），PIR=4096kbps → PBS≈512000bytes

**TCP 友好性**：CBS 过小会导致突发丢弃，TCP 窗口缩小，吞吐下降明显。

---

### K205: COLORISAWARE 颜色感知模式 [配置]

`COLORISAWARE`（ENABLE/DISABLE）控制是否信任报文已带的颜色标记：
- ENABLE：优先保证 GREEN 报文，按已有颜色决策
- DISABLE：重新计算颜色

通常与 PRIORITYISAWARE 配合使用，用于已带 DSCP 标记的报文场景。

---

### K206: CAR 层级支持 [隐性规则]

CAR 支持 BWM 全部三个层级：
- SUBSCRIBER_SPECIFIC（用户级 CAR）
- GROUP_SPECIFIC（组级 CAR）
- GLOBAL（整机级 CAR，通过 BWMRULEGLOBAL）

与 Shaping 关键差异：**Shaping 仅支持用户级**（见 `03-Shaping整形.md`）。

---

### K207: CAR 选型决策矩阵 [方案设计]

| 场景 | 是否选 CAR | 理由 |
|------|-----------|------|
| P2P/迅雷等低价值业务限速 | 是 | 直接丢弃超额，不浪费缓存 |
| 恶意终端异常流量阻断 | 是（配合 Gate=Closed 或 REDACT=DISCARD） | 立即生效阻断 |
| 月套餐超量降速（FUP） | 否（用 FUP URR + PCRF 降速 QoS） | 降速需累计触发，非实时监管 |
| 视频业务抖动敏感 | 否（用 Shaping） | 缓冲比丢弃体验更好 |
| 高价值业务带宽下限保证 | 否（用 GBR） | CAR 是上限控制，非下限保证 |

> 选型依据：CAR = 上限监管 + 超额丢弃；Shaping = 上限整形 + 超额缓冲；GBR = 下限保证；FUP = 累计降速。
