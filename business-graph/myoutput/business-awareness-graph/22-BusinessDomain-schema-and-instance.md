# BusinessDomain Schema 定义与业务感知域实例

## 1. Schema 定义

### 1.1 属性

| 字段 | 类型 | 必选 | 说明 |
|------|------|------|------|
| domain_id | string | 是 | 唯一标识，格式 `{产品缩写}-{域缩写}` |
| domain_name | string | 是 | 域名称 |
| domain_summary | string | 是 | 一句话定义，来自产品文档的定义页 |
| core_mechanism | string | 是 | 核心组织骨架（final_v2 第 2 条条件：稳定的组织骨架） |
| app_scopes | list[string] | 是 | 应用领域，保留产品文档原值，不改 |
| cp_up_split | string | 是 | 控制面/用户面分工模式 |
| product_structure | string | 是 | 产品结构支撑 |
| status | string | 是 | 数据状态 |

### 1.2 边

```
BusinessDomain --contains--> NetworkScenario
  "一个业务域由若干稳定业务场景组成"
```

> 决策依据：
> - D7: BD 不增加 Participant/DSO/Evidence 边，只保留 `BD --contains--> NS`
> - D8: BD 保留 `app_scopes` 字段，与 NS 独立共存

---

## 2. 业务感知域实例

### 2.1 实例

| 字段 | 值 |
|------|-----|
| domain_id | `UDG-SA` |
| domain_name | 业务感知 |
| domain_summary | 在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制 |
| core_mechanism | 过滤条件 --> 规则 --> 策略，PCF/SMF编排+UPF执行的双侧运行链：规则下发 -> 报文解析识别 -> 规则匹配 -> 策略执行 -> 数据转发 -> 使用情况上报 |
| app_scopes | ["内容计费", "带宽控制", "安全防护", "行为分析"] |
| cp_up_split | PCF/SMF 编排规则与策略（控制面），UPF 执行解析、匹配与策略动作（用户面）；控制面与用户面分离，用户面支持分布式部署 |
| product_structure | 5GC 控制面(UNC/SMF/PCF) + 用户面(UDG/UPF) 分工架构；UDG 是用户面网元，可中心部署也可边缘部署；业务感知/计费/QoS/智能策略控制/分布式网络在同一产品能力版图中组合 |
| status | accepted |

### 2.2 证据链

| 字段 | 证据来源 | 关键引用 |
|------|---------|---------|
| domain_id | 人为构造 | 格式 `{产品缩写}-{域缩写}` = `UDG-SA`，UDG 为产品名，SA 为 Service Awareness 缩写 |
| domain_name | 业务感知定义_92407879.md | "业务感知（Service Awareness，简称SA）" |
| domain_summary | 业务感知定义_92407879.md | "是指在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务。" |
| core_mechanism | 业务感知过程_92407889.md | "PCF会下发规则，经过SMF'翻译'后进一步下发到UPF" + "UPF对报文进行解析与识别" + "UPF将报文特征与规则库中的规则进行匹配" + "成功匹配规则的报文，将执行对应规则上绑定的策略" |
| app_scopes | 业务感知定义_92407879.md | "业务感知技术可广泛应用在内容计费、带宽控制、安全防护、行为分析等方面" |
| cp_up_split | 华为5G Core解决方案_73594796.md | "边缘计算的前提是分布式部署，分布式部署是指控制面和用户面的分离，让用户面功能摆脱'中心化'的束缚" + "5G Core解决方案包括UNC...UDG...UPCF等多个产品，提供5G标准协议中AMF、SMF、UPF...等NF的功能" |
| product_structure | 华为5G Core解决方案_73594796.md + 业务功能_29645049.md | "5G Core解决方案包括UNC（Unified Network Controller）、UDG（Unified Distribute Gateway）" + UDG业务功能表中"业务感知功能"、"计费功能"、"QoS功能"、"智能策略控制功能"、"分布式网络功能"并列在同一产品功能版图 |
| status | 人为判定 | final_v2 Section 7 已确认业务感知满足 7 条业务域条件 |

---

## 3. 对应 CSV 更新

### 3.1 business_domains.csv 更新后内容

```csv
domain_id,domain_name,domain_summary,core_mechanism,app_scopes,cp_up_split,product_structure,status
UDG-SA,业务感知,"在用户会话过程中，对用户的数据报文进行解析，从而区分出用户使用的不同业务，以实现策略控制和计费控制","过滤条件->规则->策略；PCF/SMF编排+UPF执行双侧运行链：规则下发->报文解析识别->规则匹配->策略执行->数据转发->使用情况上报","内容计费;带宽控制;安全防护;行为分析","PCF/SMF编排规则与策略（控制面），UPF执行解析、匹配与策略动作（用户面）；控制面与用户面分离，用户面支持分布式部署","5GC控制面(UNC/SMF/PCF)+用户面(UDG/UPF)分工架构；UDG是用户面网元可中心部署也可边缘部署；业务感知/计费/QoS/智能策略控制/分布式网络在同一产品能力版图中组合",accepted
```

---

## 4. 设计决策记录

| 决策ID | 内容 | 理由 |
|--------|------|------|
| D7 | BD 不增加 Participant/DSO/Evidence 边，只保留 `BD --contains--> NS` | BD 作为根对象只负责限定边界，具体参与方/语义对象/证据在 DS 和 NS 层关联 |
| D8 | BD 保留 `app_scopes` 字段，与 NS 独立共存 | app_scopes 来自产品文档定义页，是域级别的应用领域声明；NS 层的语义是场景级别的业务目标，两者粒度不同不应合并 |
