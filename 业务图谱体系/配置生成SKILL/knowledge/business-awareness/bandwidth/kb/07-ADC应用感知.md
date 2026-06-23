## 第七章：ADC 应用感知动态带宽

> CS-BW-04 方案闭包。来源：`three-layer-graph/04-command-graph.md` §5.6、`01-business-graph.md` §2.4/§10.4、`feature-knowledge/GWFD-020357-增强的ADC基本功能.md`、`WSFD-109102-ADC基本功能.md`、`topic-knowledge/Batch-27-UNC-E2E方案-业务重定向与ADC带宽差异化.md`。

---

### K701: ADC 动态带宽机制原理 [原理]

ADC（Application Detection and Control）通过 L7 DPI 引擎检测应用启动/停止事件（APP_STA/APP_STO），动态切换**三策略组**（Normal/Start/Stop）实现应用级带宽调整，**无需用户重连**。

**核心机制链**（`01-business-graph.md` §10.4）：
```
ADC 检测应用启动(APP_STA) → SMF 上报 PCF
  → PCF 下发 Start 策略组(GBR QoS)
  → UPF 执行高带宽保障
  → ADC 检测应用停止(APP_STO) → PCF 下发 Stop 策略组
  → 恢复 Normal 策略组(Non-GBR)
  → 三策略组动态切换，用户无感知
```

---

### K702: ADCPARA — ADC 参数 [配置]

**ADD ADCPARA 关键参数**：
- `ADCPARANAME`：ADC 参数名
- `APPNAME`：应用名（如 YouTube、BitTorrent）
- `MATCHMODE`：`EXACT`（精确匹配）/ `FUZZY`（模糊匹配）

```mml
ADD ADCPARA:ADCPARANAME="youtube_adc",APPNAME="YouTube",MATCHMODE=EXACT;
```

---

### K703: ADC 三策略组（TR-BW-05） [配置]

> TaskRule TR-BW-05：ADC 必须配置 Normal/Start/Stop 三个策略组，缺失则 ADC 事件上报不完整。

| 策略组 | EVENT-TRIGGER | 触发时机 | QoS |
|--------|--------------|---------|-----|
| Normal | 持续检测 | 默认 | Non-GBR |
| Start | APPLICATION_START | 应用启动 | GBR（高带宽保障） |
| Stop | APPLICATION_STOP | 应用停止 | 恢复 Non-GBR |

三个策略组通过 `ADD RULE(POLICYTYPE=ADC)` 定义。

---

### K704: ADC 三网元一致性（CR-BW-05） [隐性规则]

ADC 场景的 `FLOWFILTERNAME` 和 appid 必须**在 PCF/SMF/UPF 三处完全一致**（CR-BW-05）。
- 因为 PCF 无 L7 识别能力，ADC 必须用预定义规则
- 三网元规则名/参数不一致 → 策略无法匹配，ADC 带宽调整失效

---

### K705: ADC 与 BWM 的关系 [原理]

ADC 本身不做限速，而是**触发 PCRF/PCF 动态下发新 QoS 策略**：
- ADC 检测事件 → PCF 决策 → 新 PCC 规则（含 QOSPROP 的 MBR/GBR）
- 实际限速/整形由 BWM 或 PCC QER 执行
- ADC 是"触发器"，BWM/QoS 是"执行器"

---

### K706: ADC 带宽差异化 E2E 方案 [方案设计]

> 来源：`topic-knowledge/Batch-27/Batch-28-UNC-E2E方案-ADC带宽差异化与位置区域带宽.md`。

典型 ADC 带宽差异化流程：
1. UDG 侧：配置 ADCPARA + SA 特征库支持该应用识别
2. UNC 侧：配置三策略组 RULE（Normal/Start/Stop）+ QOSPROP
3. PCRF/PCF 侧：配置 ADC 策略决策规则
4. 用户激活应用 → ADC 检测 APP_STA → 动态切换到 Start 策略组 → GBR 保障
5. 用户退出应用 → ADC 检测 APP_STO → 恢复 Normal 策略组
