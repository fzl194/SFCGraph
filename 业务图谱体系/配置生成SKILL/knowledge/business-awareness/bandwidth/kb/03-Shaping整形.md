## 第三章：Shaping 整形

> BWMCONTROLLER 在 CTRLTYPE=SHAPING 模式下的参数体系，含智能 Shaping（GWFD-110313）。来源：`three-layer-graph/04-command-graph.md` §5.1、`feature-knowledge/GWFD-020354-基于业务的Shaping.md`、`GWFD-110313-基于智能Shaping的组级带宽控制.md`、`cross-feature-analysis.md` 附录 D.4/F。

---

### K301: Shaping 整形原理 [原理]

Shaping（整形）使用令牌桶 + **GTS 队列**（Generic Traffic Shaping），对超额报文**缓冲延迟转发**（与 CAR 直接丢弃的关键区别）：

| 参数 | 含义 | 单位 |
|------|------|------|
| RATE | 整形目标速率 | kbps |
| QUEDEPTH | GTS 队列深度 | packets |

超额报文：缓存到队列，按 RATE 平滑输出。

---

### K302: Shaping 与 CAR 关键差异 [原理]

| 维度 | CAR（Policing） | Shaping |
|------|----------------|---------|
| 超额报文 | 直接丢弃或重标记 | 缓存到 GTS 队列延迟转发 |
| 延迟影响 | 不增加延迟 | 增加延迟和抖动 |
| 队列 | 无队列 | GTS 队列（QUEDEPTH 配置深度） |
| TCP 友好性 | 差（突发丢弃导致 TCP 窗口缩小） | 好（平滑输出减少 TCP 重传） |
| 适用业务 | P2P 等低价值业务 | 视频等抖动敏感业务 |
| 层级支持 | 用户级/组级/全局级 | **仅用户级** |
| CTRLTYPE | CAR | SHAPING（固定） |

> CR-BW-03：同一 BWMSERVICE 不可同时绑 CAR 和 Shaping 控制器。

---

### K303: 普通 Shaping 配置 [配置]

**配置实例**（用户级视频整形）：
```mml
ADD BWMCONTROLLER:BWMCNAME="video_shaping",CTRLTYPE=SHAPING,
  RATE=10000,QUEDEPTH=256;
ADD BWMRULE:BWMRULETYPE=SUBSCRIBER_SPECIFIC,
  BWMSERVICENAME="video_svc",
  UPBWMCTRLNAME1="video_shaping",DNBWMCTRLNAME1="video_shaping",
  BWMRULEPRI=2;
```

**QUEDEPTH 推导**：
- 视频等大流量业务：QUEDEPTH=256~512（容忍较大抖动）
- 普通 TCP 业务：QUEDEPTH=64~128
- 队列过浅 → 缓冲溢出仍丢弃；队列过深 → 延迟过大

---

### K304: 智能 Shaping（组级）参数集 [配置]

> 特性 GWFD-110313。来源：`feature-knowledge/GWFD-110313-基于智能Shaping的组级带宽控制.md`、`cross-feature-analysis.md` 附录 D.4。

智能 Shaping 在普通 Shaping 基础上增加**自动调度**能力，支持组级多优先级公平分配。

**额外参数**：
- `WORKMODE`：`AUTO`（自动调优）/ `MANUAL`（手动配置比例）
- `SRVLEVELSPEC`：业务等级规格数（如 10）
- `USERFAIREN`：用户公平使能（ENABLE/DISABLE）
- `ASSUREMODE`：保障模式 — `EXPRATEFIRST`（体验优先）/ `RATEFIRST`（速率优先）
- `MAXPKTLOSTRATE`：最大丢包率（万分之一，AUTO 模式）
- `PKTLOSTRATEDTL`：丢包率差值（AUTO 模式）

**配置实例**（组级智能 Shaping）：
```mml
ADD BWMCONTROLLER:BWMCNAME="group_shaping",CTRLTYPE=SHAPING,
  RATE=10000,QUEDEPTH=256,
  SRVLEVELSPEC=10,USERFAIREN=ENABLE,
  WORKMODE=AUTO,
  MAXPKTLOSTRATE=10000,PKTLOSTRATEDTL=50,
  ASSUREMODE=EXPRATEFIRST;
```

---

### K305: BCSRVLEVELPLY — 服务等级策略 [配置]

智能 Shaping 必须为每个 ServiceLevel 配置整形速率比例（TE-107-1：先 ADD BWMCONTROLLER 再 ADD BCSRVLEVELPLY）。

**ADD BCSRVLEVELPLY 关键参数**：
- `BWMCNAME`：引用 BWMCONTROLLER
- `SERVICELEVEL`：业务等级（1/2/3...）
- `SHAPRATE`：整形速率比例（百分比）

**配置实例**（三级优先级）：
```mml
ADD BCSRVLEVELPLY:BWMCNAME="group_shaping",SERVICELEVEL=1,SHAPRATE=100;  (高优先级 100%)
ADD BCSRVLEVELPLY:BWMCNAME="group_shaping",SERVICELEVEL=2,SHAPRATE=60;   (中优先级 60%)
ADD BCSRVLEVELPLY:BWMCNAME="group_shaping",SERVICELEVEL=3,SHAPRATE=30;   (低优先级 30%)
```

---

### K306: AUTO 模式自动调度算法 [原理]

智能 Shaping AUTO 模式（MANUAL 与普通 Shaping 相同）：

1. 监控各 ServiceLevel 队列的丢包率
2. 计算丢包率差值与目标值（PKTLOSTRATEDTL）的偏差
3. 动态调整各 ServiceLevel 的保障带宽
4. 确保高优先级业务的丢包率显著低于低优先级

**ASSUREMODE 取值**：
- `EXPRATEFIRST`：体验优先，优先保障高优先级业务的丢包率达标
- `RATEFIRST`：速率优先，优先保障整体吞吐

---

### K307: 智能 Shaping 依赖链 [隐性规则]

依赖链：**SA-Basic → BWM → Shaping → 智能 Shaping**（来源：`cross-feature-analysis.md` 附录 E.3）。
- 智能Shaping 需 BWM 20.9.0+ 和 Shaping 20.1.0+ 双基础
- 仅组级（BWMRULETYPE=GROUP_SPECIFIC）支持
- WORKMODE=AUTO 时 MAXPKTLOSTRATE/PKTLOSTRATEDTL 必填
