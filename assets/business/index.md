# index · business（业务层）

> 业务层 typed wiki 全景：业务域(BD) → 场景(NS) → 方案(CS) 树。CS 向下引用 `assets/task/{nf}/{ver}/` 的 feature/compound/atom task。
> 构建 SOP：[业务层级构建SOP](task/业务层级构建SOP.md)。审视：[业务层级wiki审视流程](task/业务层级wiki审视流程.md)。

## 业务域（BD）

- [业务感知](business/business-awareness/BusinessDomain@business-awareness.md) — 对用户报文解析区分业务，实现策略控制与计费控制

## 场景（NS）

### 业务感知
- [计费](business/business-awareness/charging/NetworkScenario@charging.md) — 按业务差异化计费（离线/在线/融合），结合默认计费、免费业务、配额动作完成计费闭环

## 方案（CS）

### 计费
- [融合计费](business/business-awareness/charging/ConfigurationSolution@charging-converged.md) — Nchf 统一接口，双 URR(offline+online)+RGAPPLIED 约束
- [在线计费](business/business-awareness/charging/ConfigurationSolution@charging-online.md) — OCS 实时配额（CCR-I/U/T），URR=ONLINE，UPDEFAULTQUOTA/Credit Pooling 必选一
- [离线计费](business/business-awareness/charging/ConfigurationSolution@charging-offline.md) — Ga 接口后付费，URR=OFFLINE，OFCTemplate 模板
- [内容计费基础](business/business-awareness/charging/ConfigurationSolution@charging-content.md) — SA 业务识别+每业务独立费率三件套（URR→URRGROUP→PCCPOLICYGRP）
- [计量形态增强](business/business-awareness/charging/ConfigurationSolution@charging-metering.md) — 流量/时长/事件三计量（METERINGTYPE），复用统一费率标识链
- [配额降速与体验切换](business/business-awareness/charging/ConfigurationSolution@charging-quota-exhaust.md) — Final-Unit-Action(BLOCK/REDIRECT/RESTRICT/FORWARD)+REAUTHORIZATION
- [兜底默认计费](business/business-awareness/charging/ConfigurationSolution@charging-fallback.md) — 双重兜底（DFTURRGRPNAME/DFTSIGURRGNAME+全局SPECTRAFURRGRP）
