## 第五章：FUP 配额降速

> CS-BW-02 方案闭包。来源：`three-layer-graph/04-command-graph.md` §5.4、`01-business-graph.md` §2.2/§10.2、`feature-knowledge/GWFD-020353-基于累计流量的策略控制.md`、`GWFD-110312-基于业务累计流量的策略控制.md`、`topic-knowledge/Batch-01-FUP解决方案-业务级与会话级原理.md`、`Batch-22-UNC-FUP解决方案.md`。

---

### K501: FUP 降速机制原理 [原理]

FUP（Fair Usage Policy）通过 URR 累计用户流量，配额耗尽后由 PCRF/PCF 下发**高优先级降速规则**覆盖原规则，实现套餐超量降速。

**核心机制链**（`01-business-graph.md` §10.2）：
```
URR 累计流量（SESSION_LEVEL 或 PCC_RULE_LEVEL）
  → 配额耗尽触发（VolumeThreshold）
  → SMF 上报 PCRF
  → PCRF 下发高优先级降速 QoS 规则（MBR 降低）
  → 新 PCC 规则覆盖原规则（FlowFilter 完全覆盖）
  → UPF 执行降速 → 用户带宽降低
```

---

### K502: URR — 使用量上报规则 [配置]

**ADD URR 关键参数**（带宽场景 FUP 用途）：
- `URRID`：URR ID，会话内唯一（1-65535）
- `USAGERPTMODE`：`ONLINE`（会话级 FUP）/ `MONITORINGKEY`（业务级 FUP）/ `QOS`（QoS 保证）
- `MEASUREMENTMETHOD`：`VOLUME` / `DURATION` / `EVENT`
- `VOLUMETHRESHOLD`：流量阈值（bytes，FUP 降速触发点）
- `TIMETHRESHOLD`：时长阈值（seconds）

**配置实例**（会话级 FUP）：
```mml
ADD URR:URRID=1,USAGERPTMODE=ONLINE,
  MEASUREMENTMETHOD=VOLUME,VOLUMETHRESHOLD=20000000000;   (20GB 触发降速)
```

---

### K503: FUP 三件套（URR → URRGROUP → PCCPOLICYGRP） [配置]

> TaskRule TR-BW-03：必须按序配置，断裂则 FUP 不生效。

```mml
ADD URR:URRID=1,USAGERPTMODE=ONLINE,MEASUREMENTMETHOD=VOLUME,VOLUMETHRESHOLD=20000000000;
ADD URRGROUP:URRGROUPNAME="session_fup_group",UPURRNAME1="1";
ADD PCCPOLICYGRP:PCCPOLICYGRPNAME="fup_pg",URRGROUPNAME="session_fup_group";
```

> URRGROUP 的 UPURRNAME1/2/3 仅为编号，**无优先级语义**（与计费场景一致）。

---

### K504: 会话级 FUP vs 业务级 FUP [原理]

> DecisionPoint DP-BW-06。

| 维度 | 会话级 FUP（GWFD-020353） | 业务级 FUP（GWFD-110312） |
|------|--------------------------|--------------------------|
| 累计粒度 | 整 PDU 会话所有流量 | per SVC / per APP 独立累计 |
| URR USAGERPTMODE | ONLINE | MONITORINGKEY |
| Monitoring-Level | SESSION_LEVEL | PCC_RULE_LEVEL |
| SA 依赖 | 不依赖 SA | 依赖 SA + BWM 规则匹配 |
| 典型场景 | 月套餐 20GB 总量降速 | 视频业务 10GB 后降速，其他业务不限 |

---

### K505: 降速规则优先级覆盖（BR-BW-02） [隐性规则]

> BusinessRule BR-BW-02。

FUP 降速规则必须满足两条：
1. **PRIORITY 最高**（数值最小）— 确保覆盖原保障规则
2. **FlowFilter 完全覆盖**原保障规则（端口号范围一致）— 确保所有相关流量都降速

违反影响：部分流量降速、部分不受影响，降速不彻底。

---

### K506: UNC 侧 Gx FUP 额外配置 [配置]

> Task T-205。仅 Gx(2/3/4G) 场景需要；N7(5G) 场景仅需 License，阈值由 PCF 侧 umDecs 配置。

```mml
SET PCCFUNC:MKPARSEFORMAT=ENABLE;                       (解析格式)
MOD PCRF:PCRFID=1,FEATURELIST=UMCH;                     (UMCH 拥塞处理特性)
MOD PCCPOLICYGRP:PCCPOLICYGRPNAME="fup_pg",FUPSESSIONEXC=ENABLE;  (会话级 FUP 排除)
```

---

### K507: PCCPOLICYGRP 的 FUPSESSIONEXC 参数 [配置]

`FUPSESSIONEXC`（ENABLE/DISABLE）：会话级 FUP 排除开关。
- ENABLE：该策略组内的会话不参与会话级 FUP 累计
- 用于精细控制哪些用户/会话被 FUP 监控

---

### K508: FUP 降速的 PCRF/PCF 协作 [方案设计]

FUP 降速动作本身**不在 UDG/UNC 本地配置**，而是依赖 PCRF/PCF 动态决策：

1. UDG 侧 URR 累计流量到 VolumeThreshold → 上报 SMF
2. SMF 通过 Gx/N7 上报 PCRF/PCF
3. PCRF/PCF 决策后下发新 PCC 规则（MBR 降低 + 高 PRIORITY）
4. UNC 接收并通过 N4 下发 UDG
5. UDG 执行新 QoS 参数，用户带宽降低

> 因此 FUP 配置重点是 **URR 监控规则**和 **UNC 侧 PCRF 对接**，降速后 QoS 由 PCRF 动态下发。

---

### K509: 双产品 UDG-UNC 对应特性对 [配置]

FUP 场景的 UDG-UNC 配对特性：
| UDG 侧（用户面执行） | UNC 侧（控制面决策） |
|---------------------|---------------------|
| GWFD-020353 会话 FUP | WSFD-109104 会话 FUP |
| GWFD-110312 业务 FUP | WSFD-211009 业务 FUP |

双产品参数必须一致：URRID、VOLUMETHRESHOLD、USAGERPTMODE。
