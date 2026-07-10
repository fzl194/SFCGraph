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
- [[charging-online]] — 在线计费（OCS 实时配额，URR=ONLINE）·待建
- [[charging-offline]] — 离线计费（Ga 接口后付费，URR=OFFLINE）·待建
- [[charging-content]] — 内容计费基础（SA 识别+费率三件套）·待建
- [[charging-metering]] — 计量形态增强（流量/时长/事件）·待建
- [[charging-quota-exhaust]] — 配额降速与体验切换·待建
- [[charging-fallback]] — 兜底默认计费（DFTURRGRPNAME）·待建
