# index · business（业务层）

> 业务层 typed wiki 全景：业务域(BD) → 场景(NS) → 方案(CS) 树。CS 向下引用 `assets/task/{nf}/{ver}/` 的 feature/compound/atom task。
> 构建 SOP：[业务层级构建SOP](business/业务层级构建SOP.md)。审视：[业务层级wiki审视流程](business/业务层级wiki审视流程.md)。

## 业务域（BD）

- [业务感知](business/business-awareness/BusinessDomain@business-awareness.md) — 对用户报文解析区分业务，实现策略控制与计费控制

## 场景（NS）

### 业务感知
- [计费](business/business-awareness/charging/NetworkScenario@charging.md) — 按业务差异化计费（离线/在线/融合），结合默认计费、免费业务、配额动作完成计费闭环
- [带宽控制](business/business-awareness/bandwidth-control/NetworkScenario@bandwidth-control.md) — 按业务差异化限速/整形/FUP 降速/GBR 保证（BWM 主干 + Shaping/FUP/QoS/无线资源等变种）

## 方案（CS）

### 计费
- [融合计费](business/business-awareness/charging/ConfigurationSolution@charging-converged.md) — Nchf 统一接口，双 URR(offline+online)+RGAPPLIED 约束
- [在线计费](business/business-awareness/charging/ConfigurationSolution@charging-online.md) — OCS 实时配额（CCR-I/U/T），URR=ONLINE，UPDEFAULTQUOTA/Credit Pooling 必选一
- [离线计费](business/business-awareness/charging/ConfigurationSolution@charging-offline.md) — Ga 接口后付费，URR=OFFLINE，OFCTemplate 模板
- [内容计费基础](business/business-awareness/charging/ConfigurationSolution@charging-content.md) — SA 业务识别+每业务独立费率三件套（URR→URRGROUP→PCCPOLICYGRP）
- [计量形态增强](business/business-awareness/charging/ConfigurationSolution@charging-metering.md) — 流量/时长/事件三计量（METERINGTYPE），复用统一费率标识链
- [配额降速与体验切换](business/business-awareness/charging/ConfigurationSolution@charging-quota-exhaust.md) — Final-Unit-Action(BLOCK/REDIRECT/RESTRICT/FORWARD)+REAUTHORIZATION
- [兜底默认计费](business/business-awareness/charging/ConfigurationSolution@charging-fallback.md) — 双重兜底（DFTURRGRPNAME/DFTSIGURRGNAME+全局SPECTRAFURRGRP）

### 带宽控制
- [BWM 基础限速/带宽控制](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-bwm.md) — 主干范本：BWMSERVICE→BWMCONTROLLER→BWMUSERGROUP→BWMRULE 层次化 CAR/Shaping，9 子场景共用骨架
- [业务整形 Shaping](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-shaping.md) — 业务/端口整形（2-00023/24），平滑缓存削峰，复用 BWM 控制器链
- [FUP 累计流量策略控制](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fup.md) — 会话级/业务级 FUP 达量降速（2-00026/27），周期累计触发策略切换
- [QoS 触发保证 GBR](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-qos-trigger.md) — QoS 触发保证（2-00029），GBR 承载保证带宽
- [终端系统码率差异化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-coderate-terminal.md) — 终端系统码率差异化（2-00025），复用 BWM 全对象链
- [视频承载信令控制](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-video-bearer.md) — 视频承载上下行解耦（2-00030），SDF 级保证带宽
- [FPI 业务流标识无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-fpi-optimization.md) — FPI 业务流标识无线优化（2-00031），精细流标识驱动调度
- [小区负荷无线优化](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-cell-load-optimization.md) — 小区负荷无线优化（2-00032），按无线负荷动态调整
- [IM 业务无线管控](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-im-radio.md) — IM 业务无线管控（2-00022），IM 业务识别+无线协同
- [ADC 应用检测触发](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-adc-trigger.md) — 增强应用检测 ADC 触发（2-00028），应用级检测驱动带宽策略
- [异常流量检测](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-anomaly-detection.md) — 异常下行流量检测（2-00021），本质安全/可触发阻断
- [接入点策略控制](business/business-awareness/bandwidth-control/ConfigurationSolution@bandwidth-apn-strategy.md) — 接入点策略控制（UNC 2-00009），APN/DNN 级差异化策略
