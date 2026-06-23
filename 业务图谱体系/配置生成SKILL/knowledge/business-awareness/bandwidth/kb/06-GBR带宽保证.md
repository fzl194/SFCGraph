## 第六章：GBR 带宽保证

> CS-BW-03 方案闭包。来源：`three-layer-graph/04-command-graph.md` §5.5、`01-business-graph.md` §2.3/§10.3、`feature-knowledge/GWFD-020358-业务触发的QoS保证.md`、`WSFD-109107-业务触发的QoS保证.md`、`cross-feature-analysis.md` 附录 D.3。

---

### K601: GBR 保证机制原理 [原理]

GBR（Guaranteed Bit Rate，保证比特率）通过 SA 识别高价值业务，触发专有承载/QoS Flow 建立，**分配专用资源保证带宽下限**。

**核心机制链**（`01-business-graph.md` §10.3）：
```
SA 识别高价值业务
  → URR(USAGERPTMODE=QOS) 检测上报
  → SMF 触发专有承载/QoS Flow 建立
  → QOSPROP(5QI + GBR-UL/DL + ARP) 下发
  → RAN 侧预留 GBR 资源
  → UPF 标记 DSCP/FPI
  → 无线侧优先调度 → 带宽下限保证
```

---

### K602: QOSPROP — QoS 属性核心命令 [配置]

**ADD QOSPROP 关键参数**：
- `QOSPROPNAME`：QoS 属性名
- `QOSTYPE`：`QOS_FLOW_PARA`（5G）/ `QOS_BEARER_PARA`（2/3/4G）— TR-BW-07
- `FQI`：QoS Flow Identifier（5G，0-255，QOS_FLOW_PARA 时使用）
- `QCIVALUE`：QCI 值（2/3/4G，1-9，QOS_BEARER_PARA 时使用）
- `MBRUL` / `MBRDL`：最大比特率上下行（kbps）
- `GBRUL` / `GBRDL`：保证比特率上下行（kbps）— GBR 保证核心
- `ARP`：分配保留优先级（1-15）

---

### K603: QOSTYPE 分支（5G vs 2/3/4G） [配置]

> TaskRule TR-BW-07。来源：`03-task-layer.md` T-301 note。

| 接口 | QOSTYPE | 关键参数 | UNC 角色 |
|------|---------|---------|---------|
| N7 (5G) | `QOS_FLOW_PARA` | FQI（QoS Flow Identifier） | SMF |
| Gx (2/3/4G) | `QOS_BEARER_PARA` | QCIVALUE（QCI） | PGW-C / SGW-C / GGSN |

**配置实例（5G）**：
```mml
ADD QOSPROP:QOSPROPNAME="video_gbr",
  QOSTYPE=QOS_FLOW_PARA,
  FQI=5,
  MBRUL=10000,MBRDL=10000,
  GBRUL=5000,GBRDL=5000,
  ARP=5;
```

**配置实例（2/3/4G）**：
```mml
ADD QOSPROP:QOSPROPNAME="video_gbr_4g",
  QOSTYPE=QOS_BEARER_PARA,
  QCIVALUE=5,
  MBRUL=10000,MBRDL=10000,
  GBRUL=5000,GBRDL=5000,
  ARP=5;
```

---

### K604: URR QoS 上报模式（TR-BW-04） [配置]

GBR 保证场景的 URR 必须用 `USAGERPTMODE=QOS`，不可与 FUP 混用：

```mml
ADD URR:URRID=100,USAGERPTMODE=QOS;
```

SA 识别业务后通过该 URR 上报，触发 UNC 侧专载/QoS Flow 建立信令。

---

### K605: 专有 QoS Flow 空闲定时器与去活策略 [配置]

> Task T-302 / T-303。来源：`feature-knowledge/WSFD-109107-业务触发的QoS保证.md`。

避免专有 QoS Flow 长期空闲占用资源：

```mml
SET APNIDLETIME:APNNAME="video_apn",DEDQFIDLETIMER=300;  (空闲 5 分钟释放)
ADD APNDEACTQFPLCY:APNNAME="video_apn",DEACTPOLICY=DELAY_RELEASE;  (延迟释放)
```

`DEACTPOLICY` 枚举：`DELAY_RELEASE`（延迟释放）/ `IMMEDIATE_RELEASE`（立即释放）。

---

### K606: ARP 分配保留优先级 [原理]

`ARP`（Allocation and Retention Priority，1-15）决定专有承载在资源紧张时的建立/抢占/释放优先级：
- 数值越小优先级越高
- 高 ARP 业务可抢占低 ARP 业务的 GBR 资源
- 与 MBR/GBR 共同决定 QoS 等级

---

### K607: GBR vs MBR vs CAR vs Shaping 边界 [隐性规则]

| 机制 | 控制方向 | 作用层 |
|------|---------|--------|
| GBR | 下限保证 | RAN 侧资源预留 + 无线调度 |
| MBR | 上限限制 | QoS Flow 级（PCC QER 执行） |
| CAR | 上限监管 | 用户面 BWM（丢弃超额） |
| Shaping | 上限整形 | 用户面 BWM（缓冲超额） |
| FUP | 累计降速 | 触发新 QoS（降低 MBR） |

> GBR 保证的是带宽下限，CAR/Shaping 控制的是带宽上限，两者可共存（高价值业务：GBR 下限 + MBR 上限）。
