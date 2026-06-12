## 第十八章：SMF侧对象体系与协同约束

### K256: SMF侧计费对象分层模型 `[原理]`
> 来源: K280, K281, K282, K284, SKILL.md §4.4

SMF侧计费配置对象可分为两层：

1. **系统级对象**：决定SMF是否具备计费、策略和外部网元对接能力，通常在部署期或变更窗口内配置一次。
2. **业务级对象**：按业务、按套餐或按规则创建，与UPF侧三件套共同形成可落地的计费闭环。

**系统级对象集合：**
- 计费/策略开关：`PCCFUNC`、`APNPCCFUNC`、`CHARGECTRL`（全局融合计费使能）、`CHFINIT`（CHF交互使能）
- 接口模式：`CHGMODE`、`APNCHGMODE`
- 计费属性：`CHARGECHAR`、`GLBCHARGECHAR`、`USRPROFCHARGE`、`APNCHARGECTRL`
- CHF接入：`HTTPLEGRP`、`HTTPLE`、`SBIAPLE`、`HTTPCONF`、`TNFINS`、`TNFINSIP`、`TNFGRP`、`TNFBINDGRP`
- CHF选择：`SELECTCHFGBYCC`、`GLBDFTCHFGROUP`
- 模板与触发器：`CCT`、`SELECTCCTBYCC`、`PDUTRIGGER`、`RGTRIGGER`
- 异常处理：`FAILHANDLING`、`CNVRGDCHGPARA`、`N40MSGSTG`

**业务级对象集合：**
- `URR`、`URRGROUP`、`PCCPOLICYGRP`
- `RULE`、`USERPROFILE`、`RULEBINDING`、`URRGRPBINDING`

建模原则：
- 系统级对象决定“能否计费、往哪计费、如何异常处理”。
- 业务级对象决定“哪些流量按什么规则计费”。
- 业务级对象只有在系统级对象已正确就绪时才有意义。

---

### K257: SMF到CHF的N40接入对象链 `[配置]`
> 来源: K280, K297, K308, K309, K310

SMF通过N40对接CHF时，推荐按如下对象链理解配置关系：

`LOGICIP -> HTTPLEGRP -> HTTPLE -> SBIAPLE -> HTTPCONF -> TNFINS -> TNFINSIP -> TNFGRP -> TNFBINDGRP`

各对象角色如下：
- `HTTPLEGRP`：本端HTTP端点组，用于组织一组服务化本端端点
- `HTTPLE`：本端HTTP端点
  - `LETYPE=SERVER`：SMF作为HTTP服务端接收对端请求，需要配置端口
  - `LETYPE=CLIENT`：SMF作为HTTP客户端向CHF发请求，不需要配置端口
- `SBIAPLE`：服务化接口接入点，定义本端NF类型、对端NF类型和服务名
- `HTTPCONF`：HTTP运行参数，如超时、消息体大小、JSON叶子节点数
- `TNFINS/TNFINSIP`：对端CHF实例及其地址
- `TNFGRP/TNFBINDGRP`：把多个CHF实例组织成主备或负荷分担组

关键语义：
- `HTTPLE/HTTPLEGRP/SBIAPLE/HTTPCONF` 解决的是“SMF怎样通过SBI把消息发出去”。
- `TNFINS/TNFGRP/TNFBINDGRP` 解决的是“SMF具体往哪个CHF实例/实例组发消息”。
- 前者偏“传输接入层”，后者偏“对端选择层”。

---

### K258: CHF选择对象链与兜底策略 `[配置]`
> 来源: K08, K145, K155, K156, K281

SMF侧本地选择CHF时，核心对象链为：

`CHARGECHAR/签约CC -> SELECTCHFGBYCC -> TNFBINDGRP -> TNFGRP -> TNFINSIP`

关键规则：
- `SELECTCHFGBYCC` 负责把本地CC值映射到主/备CHF组，是“计费属性到CHF组”的绑定器。
- `TNFBINDGRP` 负责把实例绑定到组，`TNFGRP` 定义组本身，`TNFINSIP` 落到实例地址。
- `GLBDFTCHFGROUP` 是全局兜底CHF组，建议现网始终配置，避免“选不到CHF”。

CHF选择优先级可归纳为：
1. 基于IMSI测试绑定
2. 基于IMSI号段
3. PCF下发FQDN
4. UDM签约CC
5. NRF发现
6. SMF本地CC（`SELECTCHFGBYCC`）
7. 全局缺省CHF组（`GLBDFTCHFGROUP`）

隐性规则：
- 修改IMSI到CHF的绑定后，已激活用户不会立即切换CHF，通常需去活后重新激活。
- `FAILOVERSUP=ENABLE` 不是选择规则，而是主备切换生效前提。
- FQDN路径和本地CC路径是两条不同的选择链，不应混为一个对象。

---

### K259: SMF系统级前置条件三联约束 `[隐性规则]`
> 来源: K115, K117, K137, K138

融合计费场景下，SMF要正常发送N40 Initial并携带正确RG，至少满足以下三联约束：

1. **接口模式正确**：`CHGMODE=NchfMode`
2. **融合计费已使能**：`CHARGECTRL` 或 `USRPROFCHARGE/APNCHARGECTRL` 已在目标粒度生效
3. **CHF交互已使能**：`CHFINIT=SENDREQ`

如果上述三项任一缺失，常见表现包括：
- 不发 `Charging Data Request [Initial]`
- Initial消息不携带预期RG
- 用户表面放通，但未进入预期计费闭环

与之配套的第二层约束：
- `RGAPPLIED` 必须与业务侧 `URR.USAGERPTMODE` 匹配
- `RGAPPLIED=DEFAULT` 时，不应在同一 `URRGROUP` 中为相同RG同时绑定在线和离线URR
- `RGSOURCE=CTXSTARTRATING` 时，应确保 `CTXSTARTRATING -> URRGROUP -> URR` 链路完整

这组约束适合作为SMF侧融合计费的首轮配置核查入口。

---

### K260: CCT模板与本地Trigger协同模型 `[配置]`
> 来源: K137, K138, K152

`CCT` 负责定义融合计费模板，`PDUTRIGGER/RGTRIGGER` 负责定义本地触发条件，两者共同决定SMF何时向CHF交互、何时触发Update。

协同关系如下：
- `CCT` 关注“会话创建和配额管理模板”
  - `CCRINITRGNUM`：Initial阶段预申请的RG个数
  - `RGSOURCE`：RG来源（`DEFAULT` / `CTXSTARTRATING`）
- `PDUTRIGGER` 关注Session级触发事件
- `RGTRIGGER` 关注RG级触发事件，如 `QUOTATHRESHOLD`、`VT`、`QHT`

优先级规则：
- CHF下发的Trigger优先级高于SMF本地 `PDUTRIGGER/RGTRIGGER`
- Session级与RG级同名Trigger冲突时，Session级优先

建模建议：
- `CCT` 应视作模板类配置对象
- `PDUTRIGGER/RGTRIGGER` 应视作触发器类配置对象
- 二者不应混并成一个“触发配置”对象

---

### K261: SMF与UPF跨网元一致性核查矩阵 `[隐性规则]`
> 来源: K144, K149, K258, SKILL.md §9.2.5

UPF负责执行计费规则，SMF负责编排和上报，两侧必须满足关键对象一致性：

| 校验项 | 一致性要求 | 影响 |
|--------|------------|------|
| `USERPROFILENAME` | SMF与UPF一致 | 否则同名业务容器无法对齐 |
| `RULENAME` | SMF与UPF一致 | 否则规则链断裂 |
| `RULE.POLICYTYPE + POLICYNAME` | SMF与UPF一致 | 否则同一业务绑定到不同策略组 |
| `URRID` | SMF与UPF一致 | 否则PFCP Usage Report无法与SMF侧计费对象关联 |
| `USAGERPTMODE` | SMF与UPF一致 | 否则在线/离线计费方式失配 |
| `ONLMETERINGTYPE/OFFMETERINGTYPE` | SMF与UPF一致 | 否则统计口径不一致 |
| `RG` | SMF与UPF一致 | 否则CHF批价与UPF统计脱节 |

核查顺序建议：
1. `LST RULEBINDING` → `LST RULE`
2. `LST PCCPOLICYGRP` → `LST URRGROUP`
3. `LST URR`
4. 再对照UPF侧同名对象核查 `URRID/RG/USAGERPTMODE/METERINGTYPE`

这组规则的本质是：
- UPF侧负责“识别和计量”
- SMF侧负责“编排和上报”
- 名称、ID和计费模式的一致性是两侧协同的最小闭包

---

## 知识统计

| 章 | 标题 | 编号范围 | 数量 |
|----|------|----------|------|
| 第十二章 | 融合计费配置全景 | K201-K213 | 13 |
| 第十三章 | 计费三件套配置 | K214-K223 | 10 |
| 第十四章 | PCF策略配置 | K225, K228 | 2 |
| 第十五章 | 方案设计知识 | K229-K234 | 6 |
| 第十六章 | 特殊场景 | K235-K241 | 7 |
| 第十七章 | 故障案例与运维 | K242-K255 | 14 |
| 第十八章 | SMF侧对象体系与协同约束 | K256-K261 | 6 |
| **合计** | | K201-K261 | **58** |

### 融合去重记录

| 新编号 | 合并来源 | 融合说明 |
|--------|----------|----------|
| K205 | K135 + K272 + K273 + K274 + K275 + K276 + K277 | 计费接口模式：K135基础定义 + K272优先级 + K273终端类型 + K274互操作指示 + K275 V/I-SMF + K276 PCF实例 + K277策略模式 |
| K206 | K136 + K259 + K260 + K261 | CC属性：K136标准取值 + K259四级优先级 + K260本地/签约选择 + K261制式来源 |
| K213 | K145 + K155 + K156 | CHF选择：K145选择优先级 + K155 IMSI三层配置 + K156实时生效限制 |
| K235 | K167 + K168 + K262 | ULCL计费：K167独立配额 + K168系统约束 + K262架构原理 |
| K252 | K289 + K290 + K291 + K292 + K293 + K294 | 7个告警条目合入速查表，K291(ALM-100530)补充处理要点 |
| —(删除) | K224 = K144重复 | ChargingData参数全集，已删除K224，保留第九章K144 |
| —(删除) | K226 ⊂ K146重复 | 三种规则类型对比，已删除K226，保留第九章K146完整版 |
| —(删除) | K227 = K145重复 | 5G动态规则必配动作组，已删除K227，保留第九章K145 |

### 按类型统计

| 类型 | 数量 | 编号 |
|------|------|------|
| [配置] | 21 | K203, K204, K205, K206, K207, K208, K209, K210, K211, K212, K213, K214, K215, K216, K219, K222, K223, K228, K257, K258, K260 |
| [原理] | 5 | K220, K229, K236, K239, K256 |
| [方案设计] | 13 | K202, K218, K221, K230, K231, K232, K233, K234, K235, K237, K238, K240, K241 |
| [隐性规则] | 5 | K201, K217, K225, K259, K261 |
| [故障案例] | 10 | K242-K251 |
| [运维] | 4 | K252, K253, K254, K255 |
