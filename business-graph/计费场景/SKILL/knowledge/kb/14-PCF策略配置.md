## 第十四章：PCF策略配置

> 注：K224(ChargingData参数全集)与K144重复已删除，参见第九章K144。
> 注：K226(三种规则类型对比)与K146重复已删除，参见第九章K146。
> 注：K227(5G动态规则必配动作组)与K145重复已删除，参见第九章K145。

### K225: offline/online互斥规则 `[隐性规则]`
> 来源: K158

- offline和online**不能同时为true**，但可同时为false（不计费）
- 优先级：PCF下发 > SMF本地配置
- 两者都不存在或都为false时，使用PDU会话的**默认计费方法**
- sdfHandl仅用于在线计费场景
- meteringMethod为离线专用参数

---

### K228: PCF侧配置流程 `[配置]`
> 来源: K146

PCF融合计费配置流程：
1. 配置配额(Quota) — 名称须与CHF侧一致
2. 配额状态映射 — Sy协议状态(0/1/2/5) → UPCF状态(Normal/Level1/Level2/Exhaust)
3. 配置条件组 — 基于QuotaStatus匹配
4. 配置5G动作组 — PredefinedPccRule类型，pccRuleId指定预定义规则名
5. 配置规则 — 类型"5G Smf Pcc Rule"
6. 配置策略 — 策略类型N7 Policy
7. ADD PSUB(用户) + ADD PSRV(签约业务)

前提：N28接口开关已启用(VRM_SYSWITCH设为1/2/3)。

---

