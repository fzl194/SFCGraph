# WSFD-107010 UPF选择 知识文档

> 聚焦 APN 业务域网元选择类核心特性：SMF（UNC）为 PDU 会话选择 UPF 的决策机制
> 控制面（C 面）网元选择特性，与地址分配（WSFD-010502/010105）、会话管理（WSFD-010501/010101）形成 APN 域协同

---

## 0. 元数据（三层图谱Schema字段）

| 字段 | 取值 |
|------|------|
| feature_id | WSFD-107010 |
| feature_name | UPF选择 |
| feature_group | 网元选择 |
| parent_feature_id | 文档未涉及（配置树父节点未在文档中明确，Stage 3 验证） |
| applicable_nf_map | `{"UNC": ["SMF", "UPF"]}` |
| variant_dimensions | ["选择条件维度(DNN / S-NSSAI切片 / DNAI / 位置区 / 接口能力 / EPS互通 / 权重 / 负载 / 优先级)", "UPF角色(主锚点 / I-UPF / SGW-U / PGW-U / 合一UPF)", "选择轮次(第一轮必选条件 / 第二轮优选条件 / 第三轮权重)", "接入代绩(5G / 4G互操作 / 2&3G)"] |
| constrained_by | (Stage 4 补充 FeatureRule ID) |
| source_evidence_ids | [EV-FK-01, EV-FK-02, EV-FK-03, EV-FK-04, EV-FK-05, EV-FK-06] |
| license_required | 是（License 控制项：82209917 LKV2USBL01 UPF选择、82200BES LKV2GWUS01 GW-U选择） |

---

## 1. 概述

### 1.1 特性定义（是什么）

在 SMF 选择 UPF 时（例如 PDU 会话建立流程中），SMF 需要根据 **UE 位置、DNN、S-NSSAI** 等信息选择 UPF，建立与 UPF 的连接。UNC 可以根据用户接入的 **DNN、切片和位置信息**，为用户选择满足指定业务的、地理位置贴近用户的 UPF，还可以结合根据 DNN 映射的 **DNAI** 信息、UPF 的**分流能力、接口能力、是否支持与 EPS 的互通、UPF 的优先级、负载、权重**来选择 UPF。

本特性是**控制面（SMF 侧）网元选择决策特性的总集**：SMF 决定"为本次 PDU 会话选哪个 UPF"，据此建立 N4 会话连接。本特性中的 UPF 是指包含了 SGW-U、PGW-U 的 UPF（合一概念）。

本特性包含如下子特性：
- **WSFD-107005 GW-U 选择**
- **WSFD-107006 支持基于位置的 GW-U 选择**
- **WSFD-107008 支持基于权重的 GW-U 选择**

> 来源：`output/UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107010 UPF选择_10789013.md`（"定义"章节）

### 1.2 适用NF（UDG/UNC网元）

| 涉及NF | 网元角色 | 支持版本 | 功能说明 |
|--------|---------|---------|---------|
| SMF | 控制面（UNC，5G） | UNC 20.2.0及后续版本 | 根据用户与 UPF 信息为用户选择满足条件的 UPF（决策方） |
| UPF | 用户面（UDG，5G） | UDG 20.2.0及后续版本 | 实现用户面功能（被选择方，向 SMF 上报负载与接口能力） |

> 注：文档"适用NF"章节标题仅写"SMF"，但"可获得性/涉及NF"表格明确列出 SMF 与 UPF 两个 NF。UPF 作为被选择方，其负载信息（偶联消息上报）与接口能力是 SMF 决策的输入。

> 来源：`WSFD-107010 UPF选择_10789013.md`（"适用NF"、"可获得性/涉及NF"章节）

### 1.3 版本信息

| 特性版本 | 发布版本 | 发布说明 |
|---------|---------|---------|
| 04 | 20.9.0 | 支持根据 ULI For SGW 信元进行 SGW-U 选择 |
| 03 | 20.6.0 | 支持根据负载与优先级选择 UPF |
| 02 | 20.3.2 | 支持根据 DNAI 选择 UPF |
| 01 | 20.2.0 | 首次发布 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"发布历史"章节）

### 1.4 License

**本特性必须获得 License 许可后才能获得该特性的服务**，对应的 License 控制项为：

| License编号 | License名称 |
|------------|------------|
| 82209917 | LKV2USBL01 UPF选择 |
| 82200BES | LKV2GWUS01 GW-U选择 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"可获得性/License 支持"章节）

### 1.5 前置条件与依赖

| 前置条件 | 说明 |
|---------|------|
| License 加载 | 必须加载 License 控制项 82209917 LKV2USBL01 UPF选择（以及 GW-U 选择对应 License） |
| SMF 与 UPF 同厂商 | **SMF 和 UPF 设备必须同时为 HUAWEI 设备**（应用限制硬约束） |
| UPF 已注册到 NRF | 对端 UPF 的 NFProfile 已通过 ADD PNFPROFILE 配置，并在 NRF 注册可被发现 |
| UPF 属性已配置 | DNN/切片/DNAI/位置区/接口能力/EPS互通/权重等属性已按网络规划在 UNC 侧配置（见 §4 配置对象） |
| UPF 负载上报（可选） | 若启用负载均衡选择，需通过 SET UPLOADBALANCE 开启 UNC 处理 UPF 上报负载信息的能力 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"应用限制"、"原理概述/UPF选择原则"、"可获得性"章节综合）

### 1.6 与其他特性的交互

**本特性明确声明"不涉及与其他特性的交互"**（产品文档原文）。

但根据功能语义，UPF 选择是 PDU 会话建立流程的内嵌决策步骤，与会话管理、地址分配存在强语义关联（这些关联由 Stage 3 横向分析补充，非文档明示）：

| 交互类型 | 相关特性 | 交互说明（语义推断） |
|---------|---------|---------|
| PDU 会话建立的子决策 | WSFD-010501 会话管理（SMF）、WSFD-010503 多 PDN/PDU | UPF 选择发生在 PDU 会话建立流程中，是会话建立的必要决策环节 |
| 与地址分配的协同 | WSFD-010502 地址分配方式（SMF） | 静态 IP 段→UPF 绑定的 UPF 与 SMF 主锚点 UPF 冲突时，**SMF 选择的主锚点 UPF 优先级更高**（WSFD-010502 §3.2.4 明确引用本特性） |
| 用户面执行方 | GWFD-010101 会话管理（UDG）、GWFD-010105 用户面地址分配 | SMF 选定 UPF 后通过 N4 PFCP 建立会话，UPF 侧执行会话与地址分配 |
| 子特性细化 | WSFD-107005/107006/107008 | 本特性为其父特性（文档明示包含关系） |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"与其他特性的交互"章节，明确声明"不涉及"）；语义关联来自 WSFD-010502 文档对本特性的引用

### 1.7 客户价值

| 受益方 | 受益描述 |
|-------|---------|
| 运营商 | - 满足不同业务场景的差异化部署，为特定用户提供更高质量的业务服务，提升业务竞争力<br>- 贴近用户部署 UPF，缩短业务访问路径，节省骨干网传输资源<br>- 避免 UPF 负载不均，可以混合使用不同容量规格的 UPF，提高 UPF 资源利用率，保护投资，节约成本 |
| 用户 | 享受低时延业务体验 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"客户价值"章节）

### 1.8 应用场景

在以下场景可以使用该特性：

- 当运营商为用户的某些业务规划部署专用的 UPF 设备时（基于 DNN/切片选择专用 UPF）
- 当运营商将 UPF 设备部署到贴近用户的地理位置时（基于位置区选择就近 UPF）
- 当多 UPF 间的负载不均衡时（基于负载/权重选择实现均衡）

> 来源：`WSFD-107010 UPF选择_10789013.md`（"应用场景"章节）

### 1.9 对系统的影响

**本特性对系统无影响**（文档明确声明）。

### 1.10 应用限制

**SMF 和 UPF 设备必须同时为 HUAWEI 设备**（文档明确声明的硬约束）。

> 来源：`WSFD-107010 UPF选择_10789013.md`（"应用限制"章节）

### 1.11 特性规格

**本特性无特殊规格**（文档明确声明）。

### 1.12 计费与话单

**本特性不涉及计费与话单**（文档明确声明）。

### 1.13 遵循标准

| 标准类别 | 标准编号 | 标准名称 |
|---------|---------|---------|
| 3GPP | 29.501 | System Architecture for the 5G System |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"遵循标准"章节）

---

## 2. 原理

### 2.1 UPF 选择的两轮+权重三阶段机制

UPF 选择采用**三轮递进筛选**机制，每一轮逐步缩小候选 UPF 范围：

```
┌──────────────────────────────────────────────────────────────────┐
│ 第一轮：必选条件筛选（所有条件必须同时满足，无优先级之分）           │
│                                                                  │
│   候选 UPF 集合 = 全部已注册 UPF                                 │
│      │                                                           │
│      ├── ① DNN 匹配        (ADD PNFDNN 配置的 UPF 支持的 DNN)    │
│      ├── ② S-NSSAI 切片匹配 (ADD PNFNS 配置的 UPF 支持的切片)    │
│      ├── ③ 位置区匹配       (ADD UPAREA / ADD UPAREABINDN2TAI)    │
│      ├── ④ DNAI 匹配       (ADD PNFDNAI，由 DNN 映射获取)        │
│      ├── ⑤ 接口能力匹配    (UPF 上报，如需 N6 则须支持 N6)        │
│      ├── ⑥ EPS 互通匹配    (ADD PNFUPFINFO，4/5G 互操作场景)     │
│      └── ⑦ 分流能力匹配    (ADD UPNODE 配置的位置特征与分流能力) │
│                                                                  │
│   ★ 若 UPF 均不满足必选条件 → UPF 选择失败                       │
│   ★ 若仅 1 个 UPF 满足 → 选择完成，跳过第二轮                    │
└──────────────────────────────┬───────────────────────────────────┘
                               │ 多个 UPF 满足
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│ 第二轮：优选条件排序（按策略次序进一步筛选，可配置优先级）           │
│                                                                  │
│   由 SET UPSELECTPRI 配置选择策略次序：                           │
│     - 第一优先级（默认 COMBINED 合一UPF）                         │
│     - 第二优先级（默认 LOCS11PRIORITY 位置区或S11口优先级）        │
│                                                                  │
│   由 SET UPSELECTFLAG 控制各开关：                                │
│     - PRIORITYFLAG：是否考虑优先级（DISABLE 时跳过优先级环节）     │
│     - AMBRUPFFLAG：同 DNN 的 PDU 会话是否优先选相同 UPF           │
│     - N3UPFAPNFLAG：选 I-UPF 时 DNN 是否作为选择条件              │
│     - ULISGWFLAG：SGW-U 选择时优先 ULI 还是 S11 接口              │
│                                                                  │
│   由 SET APNUPSELPLY 的 COMBINEPRISTG 配置用户位置区、合一UPF、    │
│   优先级的选择条件顺序                                            │
│                                                                  │
│   ★ 若仅 1 个 UPF 满足 → 选择完成，跳过第三轮                    │
└──────────────────────────────┬───────────────────────────────────┘
                               │ 仍有多个 UPF 满足
                               ▼
┌──────────────────────────────────────────────────────────────────┐
│ 第三轮：权重 + 负载最终选择                                       │
│                                                                  │
│   ① 权重选择（ADD PNFPROFILE 配置的 WEIGHT）                      │
│      - 权重大小代表 UPF 的容量大小                                │
│      - 权重越大，被选中的概率越大（加权随机）                      │
│                                                                  │
│   ② 负载均衡（SET UPLOADBALANCE 开启，UPF 偶联消息上报）          │
│      - 优先选择负载低的 UPF                                       │
│                                                                  │
│   ★ 任一步骤选出唯一 UPF 即选择完成                               │
└──────────────────────────────────────────────────────────────────┘
```

> 来源：`WSFD-107010 UPF选择_10789013.md`（"原理概述/UPF 选择原则"，含图1不同角色 UPF 选择过程、图2基于优先级选择 UPF 原理示意图）

### 2.2 14 种 UPF 选择原则详解（文档表1）

文档"原理概述"章节的 **表1 UPF选择原则** 完整列出了 14 个选择维度及其配置命令：

| # | 选择原则 | 说明 | 配置命令 |
|---|---------|------|---------|
| 1 | 用户 DNN 信息 | UNC 配置对端 UPF 支持的 DNN；用户激活时从激活请求获取 DNN，根据 UPF 支持的 DNN 列表筛选 | **ADD PNFDNN**（注：4G 用户接入 EPC 时 SGW-C/PGW-C 选 SGW-U/PGW-U 不使用切片信息，PNFNSINDEX 建议保持默认值 0） |
| 2 | 用户切片信息（S-NSSAI） | UNC 配置对端 UPF 支持的服务切片；用户激活时从激活请求获取切片信息筛选 | **ADD PNFNS** |
| 3 | DNAI 信息 | UNC 配置对端 UPF 支持的 DNAI；用户激活时从 DNN 映射获取 DNAI 筛选 | ADD PNFDNAI |
| 4 | UPF 的位置特征和分流能力 | UNC 配置对端 UPF 的位置特征和分流能力；按网络规划和业务需求选择 | **ADD UPNODE** |
| 5 | UPF 的接口能力 | UNC 根据 UPF 上报的接口能力选择（如需连 DN 网络则须支持 N6 接口） | （UPF 自身上报，无 UNC 侧命令） |
| 6 | UPF 是否支持与 EPS 的互通 | UNC 配置对端 UPF 是否支持与 EPS 互通；选锚点 UPF 时按用户是否支持 4/5G 互操作判断 | **ADD PNFUPFINFO** |
| 7 | 用户位置区信息 | UNC 配置位置区名称及覆盖该位置区的 UPF 设备 ID 列表；从激活请求获取用户位置信息筛选 | **ADD PNFPROFILE**、**ADD PNFSMFSERAREA**、ADD UPAREA、**ADD UPAREABINDN2TAI**、**ADD LOCBINDAREA** |
| 8 | S11 接口 | UNC 配置 UPF 与 S11 接口的绑定关系；5/2/3G 切换到 4G 且 SGW-C 改变且无法获取 ULI 时，按 S11 接口选 SGW-U | **ADD UPBINDS11**（配合 SET UPSELECTFLAG 的 ULISGWFLAG 控制优先 ULI 还是 S11） |
| 9 | Gn/Gp 或 S5/S8 接口 | UNC 配置 GGSN-U/PGW-U 与 Gn/Gp 或 S5/S8 接口的绑定关系，按接口选择 | ADD UPBINDGNGP |
| 10 | 合一的 UPF | UNC 为节约流量、减少信令传输时延，可选合一 UPF（SGW-U/PGW-U 合一、主锚点与 I-UPF 合一、辅锚点与分流节点合一） | （无独立命令，由 UPF 部署形态决定） |
| 11 | 优先级 | UNC 配置各 UPF 设备 ID 列表及优先级；选择优先级更高的 UPF | ADD PNFPROFILE、ADD PNFDNN、ADD PNFDNAI、ADD PNFSMFSERAREA、ADD PNFTAIRANGE、ADD PNFTAI |
| 12 | 负载 | SMF 根据 UPF 在偶联消息中上报的负载信息，优先选负载低的 UPF | SET UPLOADBALANCE（控制 UNC 是否处理 UPF 上报的负载信息） |
| 13 | 权重 | UNC 配置各 UPF 设备 ID 及权重；权重代表容量大小；多 UPF 满足条件时按权重加权随机选择 | **ADD PNFPROFILE** |
| 14 | （隐含）AMBRUPFFLAG 同 DNN 会话选相同 UPF | 对同一用户使用相同 DNN 建立的 PDU 会话，可通过开关控制是否优先选相同 UPF | SET UPSELECTFLAG 的 AMBRUPFFLAG |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"原理概述/表1 UPF 选择原则"）

### 2.3 UPF 选择示例（文档表2 + 图3）

文档给出了一个具体的 UPF 选择示例。假设某 SMF 下共配置 8 个主锚点 UPF：

| UPF | DNN | 切片 | 合一UPF | 位置区 | 权重 |
|-----|-----|------|---------|--------|------|
| UPF1 | dnn1、dnn2、dnn3 | SST=1，SD=010101 | 是 | 0x0000-0x0009 | 6 |
| UPF2 | dnn1、dnn2、dnn3 | SST=1，SD=010101 | 是 | 0x0005-0x00bb | 5 |
| UPF3 | dnn1、dnn3、dnn4 | SST=1，SD=010101 | 否 | 0x0000-0x00cc | 4 |
| UPF4 | dnn1、dnn2、dnn3 | SST=1，SD=010101 | 是 | 0x0000-0x0005 | 4 |
| UPF5 | dnn2、dnn3、dnn4 | SST=1，SD=010101 | 是 | 0x0000-0x0005 | 4 |
| UPF6 | dnn4、dnn5、dnn6 | SST=2，SD=010101 | 否 | 0x0000-0x0005 | 3 |
| UPF7 | dnn4、dnn5、dnn6 | SST=2，SD=010101 | 否 | 0x0000-0x0077 | 3 |
| UPF8 | dnn4、dnn8、dnn9 | SST=2，SD=010101 | 否 | 0x00aa-0x00ff | 2 |

**默认策略配置**：
- SET UPSELECTPRI 保持初始值：第一优先级 = COMBINED（合一的 UPF），第二优先级 = LOCS11PRIORITY（位置区或 S11 口优先级）
- SET UPSELECTFLAG 的 PRIORITYFLAG 保持初始值 DISABLE（不考虑优先级配置）

**示例结论**（文档图3展示）：当 UE1、UE2 使用相同 DNN、切片但从不同位置接入时，按上述原则会选出不同的 UPF（具体选择过程见图3，文档以示意图形式呈现）。

> 来源：`WSFD-107010 UPF选择_10789013.md`（"原理概述/UPF 选择示例"，表2 + 图3）

### 2.4 UPF 角色（主锚点 / I-UPF / 合一）

文档提及的 UPF 角色体系：

| UPF 角色 | 说明 | 选择时的特殊规则 |
|---------|------|----------------|
| 主锚点 UPF | PDU 会话的主用 UPF（PGW-U 角色） | 选择时根据用户是否支持 4/5G 互操作判断是否要求 EPS 互通能力 |
| I-UPF（中间 UPF / 接入锚点） | 用户接入侧的 UPF（SGW-U 角色） | 选择时根据 SET UPSELECTFLAG 的 N3UPFAPNFLAG 判断 DNN 是否为选择条件 |
| 合一 UPF | SGW-U/PGW-U 合一、主锚点与 I-UPF 合一、辅锚点与分流节点合一 | 第二轮优选条件之一，节约流量减少信令时延 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"原理概述"中提及"接入锚点即为 I-UPF"、"合一的 UPF"概念）

---

## 3. 配置

### 3.1 配置对象（UNC 侧 UPF 属性体系）

```
┌─────────────────────────────────────────────────────────────────────┐
│ UNC 侧 UPF 选择配置体系（按选择维度组织的多组对象）                    │
│                                                                     │
│ 【NF 实例基础信息层】                                                 │
│   ┌──────────────┐                                                  │
│   │ PNFPROFILE   │ ← 对端 NF 实例概述（含权重、优先级、NF 类型）      │
│   │ (UPF实例基础) │   ADD PNFPROFILE                                 │
│   └──────┬───────┘                                                  │
│          │                                                          │
│          ├── ① 业务能力属性（必选条件）                               │
│          │   ├── ADD PNFDNN       → UPF 支持的 DNN 列表              │
│          │   ├── ADD PNFNS        → UPF 支持的切片(S-NSSAI)列表      │
│          │   ├── ADD PNFDNAI      → UPF 支持的 DNAI 列表             │
│          │   ├── ADD PNFUPFINFO   → UPF 是否支持与 EPS 互通          │
│          │   └── ADD UPNODE       → UPF 位置特征与分流能力           │
│          │                                                          │
│          ├── ② 位置区属性（必选条件）                                 │
│          │   ├── ADD PNFSMFSERAREA → 对端 SMF 服务区域               │
│          │   ├── ADD PNFTAIRANGE  → 对端 NF 的 TAI 范围              │
│          │   ├── ADD PNFTAI       → 对端 NF 的 TAI 信息              │
│          │   ├── ADD UPAREA       → UPF 服务区                      │
│          │   ├── ADD UPAREABINDN2TAI → UPF 服务区绑定的 5G TAI 范围  │
│          │   └── ADD LOCBINDAREA  → UPF 位置信息与优先服务区绑定     │
│          │                                                          │
│          └── ③ 接口绑定属性（必选条件，代际互操作场景）                │
│              ├── ADD UPBINDS11    → SGW-U 与 SGW-C 侧 S11 接口绑定   │
│              └── ADD UPBINDGNGP   → GGSN/PGW-U 与 Gn/Gp 或 S5/S8 绑定│
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ UNC 侧 UPF 选择策略控制层（全局开关与次序配置）                        │
│                                                                     │
│   ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐ │
│   │ SET UPSELECTPRI  │  │ SET UPSELECTFLAG │  │ SET APNUPSELPLY  │ │
│   │ (选择策略次序)    │  │ (选择条件开关)    │  │ (APN粒度选择策略) │ │
│   │                  │  │                  │  │                  │ │
│   │ 第一优先级        │  │ PRIORITYFLAG     │  │ COMBINEPRISTG    │ │
│   │ 第二优先级        │  │ AMBRUPFFLAG      │  │                  │ │
│   │                  │  │ N3UPFAPNFLAG     │  │                  │ │
│   │                  │  │ ULISGWFLAG       │  │                  │ │
│   └──────────────────┘  └──────────────────┘  └──────────────────┘ │
│                                                                     │
│   ┌──────────────────┐                                              │
│   │ SET UPLOADBALANCE│  ← 负载均衡总开关（是否处理 UPF 上报的负载）   │
│   └──────────────────┘                                              │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.2 MML 命令清单

#### 3.2.1 NF 实例与业务能力配置命令（必选条件输入）

| 命令 | 用途 | 对应选择原则 |
|------|------|-------------|
| **ADD PNFPROFILE** | 增加对端 NF 实例概述信息（含权重、优先级） | 权重、优先级、位置区、合一UPF（基础对象） |
| **ADD PNFDNN** | 增加对端 NF 的 DNN 信息 | 用户 DNN 信息 |
| **ADD PNFNS** | 增加对端 NF 的切片信息 | 用户切片信息（S-NSSAI） |
| ADD PNFDNAI | 增加对端 NF 的 DNAI 信息 | DNAI 信息 |
| **ADD PNFUPFINFO** | 增加对端 UPF 信息（含是否支持 EPS 互通） | UPF 是否支持与 EPS 互通 |
| **ADD UPNODE** | 增加UPF节点（含位置特征与分流能力） | UPF 位置特征和分流能力 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"原理概述/表1"，原文以超链接形式指向各命令的 OM 参考文档）

#### 3.2.2 位置区配置命令（必选条件输入）

| 命令 | 用途 |
|------|------|
| ADD PNFSMFSERAREA | 增加对端 NF 的 SMF 服务区域信息 |
| ADD PNFTAIRANGE | 增加对端 NF 的 TAI 范围 |
| ADD PNFTAI | 增加对端 NF 的 TAI 信息 |
| ADD UPAREA | 增加 UPF 服务区 |
| ADD UPAREABINDN2TAI | 增加 UPF 服务区名称绑定的 5G TAI 范围 |
| ADD LOCBINDAREA | 增加 UPF 位置信息与该 UPF 优先支持的服务区的绑定关系 |

#### 3.2.3 接口绑定配置命令（代际互操作场景）

| 命令 | 用途 |
|------|------|
| ADD UPBINDS11 | 增加 SGW-U 与 SGW-C 侧 S11 接口的绑定关系 |
| ADD UPBINDGNGP | 增加 GGSN 与 Gn/Gp 接口或 PGW-U 与 S5/S8 接口的绑定关系 |

#### 3.2.4 UPF 选择策略控制命令（第二轮优选与第三轮权重/负载）

| 命令 | 用途 | 关键参数 |
|------|------|---------|
| **SET UPSELECTPRI** | 设置 UPF 选择策略次序 | 第一优先级（默认 COMBINED）、第二优先级（默认 LOCS11PRIORITY） |
| **SET UPSELECTFLAG** | 设置 UPF 选择条件开关 | PRIORITYFLAG、AMBRUPFFLAG、N3UPFAPNFLAG、ULISGWFLAG |
| SET APNUPSELPLY | 设置 APN 粒度的 UP 选择策略 | COMBINEPRISTG（用户位置区、合一UPF、优先级的选择顺序） |
| SET UPLOADBALANCE | 设置 UP 负载均衡功能 | 控制 UNC 是否处理 UPF 上报的负载信息 |

#### 3.2.5 调测查询命令

文档未提供独立的调测章节与查询命令清单。以下为推断（Stage 3 补充）：

| 推断命令 | 用途 |
|---------|------|
| LST PNFPROFILE | 查询已配置的对端 NF 实例信息 |
| LST PNFDNN / LST PNFNS / LST PNFDNAI | 查询各业务能力配置 |
| DSP PDUSESSION | 显示 PDU 会话（查实际选中的 UPF） |
| EXP MML | 导出 MML 配置文件 |

### 3.3 关键参数说明

#### 3.3.1 ADD PNFPROFILE 关键参数（权重与优先级）

| 参数 | 取值 | 说明 |
|------|------|------|
| NFINSTANCENAME | 字符串（如 UPF_Instance_1） | UPF 实例名称，后续 ADD PNFDNN/UPNODE 等命令引用此名称 |
| NF TYPE | UPF / SGW-U / PGW-U 等 | NF 类型 |
| WEIGHT | 整数（如 1~10） | UPF 权重，代表容量大小；多 UPF 满足条件时加权随机选择，权重越大被选中概率越大 |
| PRIORITY | 整数 | UPF 优先级（需配合 PRIORITYFLAG=ENABLE 生效） |

> 注：文档未给出参数级取值细节，上述为基于表1说明的推断，Stage 3 以 OM 命令手册为准。

#### 3.3.2 SET UPSELECTPRI 关键参数（选择策略次序）

| 参数 | 取值 | 说明 |
|------|------|------|
| 第一优先级 | COMBINED（默认） / LOCS11PRIORITY / 其他 | 第一轮必选后，第二轮首先按此维度优选 |
| 第二优先级 | LOCS11PRIORITY（默认） / COMBINED / 其他 | 第一优先级仍有多个 UPF 时，按此维度进一步优选 |

#### 3.3.3 SET UPSELECTFLAG 关键参数（选择条件开关）

| 参数 | 默认值 | 说明 |
|------|--------|------|
| PRIORITYFLAG | DISABLE | 是否考虑 UPF 优先级配置；DISABLE 时跳过优先级环节 |
| AMBRUPFFLAG | （文档未明示默认值） | 同一用户相同 DNN 的 PDU 会话是否优先选相同 UPF |
| N3UPFAPNFLAG | （文档未明示默认值） | 选 I-UPF 时 DNN 是否作为选择条件 |
| ULISGWFLAG | （文档未明示默认值） | SGW-C 选 SGW-U 时优先使用 ULI For SGW 信元还是 S11 接口 |

#### 3.3.4 ADD PNFDNN 的 PNFNSINDEX 参数（4G 接入特殊处理）

| 参数 | 建议取值 | 说明 |
|------|---------|------|
| PNFNSINDEX | 0（默认值） | 4G 用户接入 EPC 时，SGW-C/PGW-C 选 SGW-U/PGW-U 不使用切片信息，建议保持默认值 0 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"原理概述/表1"，ADD PNFDNN 行的特别说明）

### 3.4 约束条件

| 约束类型 | 约束内容 |
|---------|---------|
| 同厂商约束（硬） | **SMF 和 UPF 设备必须同时为 HUAWEI 设备**（应用限制明确声明） |
| 必选条件全部满足 | 第一轮所有必选条件必须同时满足；若 UPF 均不满足必选条件，UPF 选择失败 |
| 必选条件无优先级 | 第一轮必选条件之间无优先级之分（区别于第二轮优选条件） |
| UPF 整网规划 | 不同角色的 UPF（主锚点/I-UPF/合一）需要整网规划，且配置不同（参考 UDG 初始配置与调测） |
| 4G 接入切片处理 | 4G 用户接入 EPC 时，SGW-C/PGW-C 选 SGW-U/PGW-U 不使用切片信息，ADD PNFDNN 的 PNFNSINDEX 保持默认 0 |
| 负载信息来源 | UPF 负载信息来自偶联消息上报，需 SET UPLOADBALANCE 开启 UNC 处理能力 |
| 权重生效前提 | 权重选择仅在"前两轮选择后仍有多个 UPF 满足条件"时触发 |

> 来源：`WSFD-107010 UPF选择_10789013.md`（"应用限制"、"原理概述"综合）

---

## 4. 配置案例

**文档未提供独立的 MML 配置脚本案例**。

文档仅以 **表2（8 个 UPF 属性表）+ 图3（UPF 选择过程示例）** 的形式给出了选择原则的应用示例，但未提供端到端 MML 激活脚本。

### 4.1 文档示例：8 UPF 多维属性选择（文档表2 + 图3）

**场景描述**：某 SMF 下配置 8 个主锚点 UPF（属性见表2），默认策略次序（第一优先级 COMBINED，第二优先级 LOCS11PRIORITY，PRIORITYFLAG=DISABLE），UE1、UE2 使用相同 DNN、切片从不同位置接入。

**文档未提供的 MML 脚本**（Stage 3 补充）：实际激活需配置以下命令序列（推断框架）：

```
（推断框架，文档未提供完整 MML 脚本）

步骤1：配置各 UPF 的 NF 实例概述（含权重）
  └── ADD PNFPROFILE: NFINSTANCENAME="UPF1", NF TYPE=UPF, WEIGHT=6, ...;
  └── ADD PNFPROFILE: NFINSTANCENAME="UPF2", WEIGHT=5, ...;
  └── ...（UPF1~UPF8 共8条）

步骤2：配置各 UPF 支持的 DNN 列表
  └── ADD PNFDNN: NFINSTANCENAME="UPF1", DNN="dnn1", PNFNSINDEX=0;
  └── ADD PNFDNN: NFINSTANCENAME="UPF1", DNN="dnn2", ...;
  └── ...（按表2的 DNN 列表配置）

步骤3：配置各 UPF 支持的切片
  └── ADD PNFNS: NFINSTANCENAME="UPF1", SST=1, SD=010101, ...;
  └── ...

步骤4：配置各 UPF 的位置区/服务区
  └── ADD UPAREA: ...;
  └── ADD UPAREABINDN2TAI: ...;

步骤5：配置 UPF 节点（位置特征、分流能力、合一属性）
  └── ADD UPNODE: NFINSTANCENAME="UPF1", ...;

步骤6：配置 UPF 选择策略次序（保持默认值）
  └── SET UPSELECTPRI: 第一优先级=COMBINED, 第二优先级=LOCS11PRIORITY;

步骤7：配置 UPF 选择条件开关（保持默认值）
  └── SET UPSELECTFLAG: PRIORITYFLAG=DISABLE;

步骤8（可选）：开启负载均衡
  └── SET UPLOADBALANCE: ENABLE;
```

### 4.2 场景变体对照

| 变体 | 核心差异 | 关键命令/参数 | 文档覆盖度 |
|------|---------|--------------|-----------|
| 基于 DNN+切片选择专用 UPF | 必选条件筛选 | ADD PNFDNN + ADD PNFNS | 仅原则，无完整脚本 |
| 基于位置区选择就近 UPF | 位置区必选条件 | ADD UPAREA + ADD UPAREABINDN2TAI + ADD LOCBINDAREA | 仅原则，无完整脚本 |
| 基于权重选择（混合容量） | 第三轮权重加权随机 | ADD PNFPROFILE WEIGHT | 表2示例覆盖属性，无脚本 |
| 基于负载均衡 | 第三轮负载优先 | SET UPLOADBALANCE | 仅原则，无脚本 |
| 基于 DNAI 选择（MEC/分流） | 必选条件 DNAI | ADD PNFDNAI | 仅原则，无脚本 |
| 4G/5G 互操作（EPS 互通） | 必选条件 EPS 互通 | ADD PNFUPFINFO | 仅原则，无脚本 |
| 5/2/3G 切 4G 且无 ULI | S11 接口选择 SGW-U | ADD UPBINDS11 + ULISGWFLAG | 仅原则，无脚本 |

> **文档覆盖度结论**：本特性仅 1 篇产品文档（特性概述），**未提供任何完整 MML 激活脚本**。所有配置需参考 OM 参考文档中各命令的独立说明（文档以超链接形式引用），以及 UDG 产品手册的初始配置与调测。Stage 3 需补充完整激活脚本。

---

## 5. 验证与调测

### 5.1 验证方法

**文档未提供独立的调测章节**（与 WSFD-010502 等特性不同，本特性无"调测xxx功能"文档）。

以下为基于功能语义的推断（Stage 3 补充）：

| 验证目的 | 推断命令 | 说明 |
|---------|---------|------|
| 查询 NF 实例配置 | LST PNFPROFILE | 查看已配置的 UPF 实例及权重、优先级 |
| 查询 UPF 业务能力 | LST PNFDNN / LST PNFNS / LST PNFDNAI | 查看 DNN/切片/DNAI 配置 |
| 查询实际选中 UPF | DSP PDUSESSION | 通过 IMSI 查 PDU 会话实际选用的 UPF（参考 WSFD-010502 调测方法） |
| 查询选择策略 | LST UPSELECTPRI / LST UPSELECTFLAG | 查看当前策略次序与开关 |
| 导出配置 | EXP MML | 故障收集 |

### 5.2 告警参考

**文档未涉及**（本特性概述文档未列告警章节，文档无"参考信息"独立文件）。

### 5.3 测量指标

**文档未涉及**。

### 5.4 软参

**文档未涉及**。

### 5.5 常见问题与排查（推断）

| 问题现象 | 可能原因 | 排查方法 |
|---------|---------|---------|
| UPF 选择失败（无 UPF 满足必选条件） | ADD PNFDNN/PNFNS 配置与用户 DNN/切片不匹配 | LST PNFDNN/PNFNS 核对 UPF 支持的 DNN/切片是否覆盖用户请求 |
| 选错 UPF（非预期） | 位置区配置错误或 UPAREABINDN2TAI 绑定错误 | 核对 ADD UPAREA / ADD UPAREABINDN2TAI 与用户 TAI 的匹配关系 |
| 负载不均衡 | SET UPLOADBALANCE 未开启或 UPF 未上报负载 | 检查 SET UPLOADBALANCE 开关；检查 N4 偶联消息是否携带负载信息 |
| 静态 IP 用户未选到绑定 UPF | SMF 主锚点 UPF 优先级 > 静态 IP 段绑定 UPF（WSFD-010502 已明确） | 确认预期：SMF 选择优先；需切换则调整 SMF 选择策略或 SET STATICADDRPARA |
| 4G 互操作选不到 UPF | ADD PNFUPFINFO 未配置 EPS 互通能力 | 配置 ADD PNFUPFINFO 标记支持 EPS 互通的 UPF |
| 切换场景 SGW-U 选择异常 | ULI 信元为空且未配置 S11 绑定 | 配置 ADD UPBINDS11；调整 SET UPSELECTFLAG ULISGWFLAG |

> 来源：推断表，基于 §2 选择机制与 §3.4 约束条件推导，Stage 3 验证

---

## 6. 参考信息

### 6.1 与其他特性的关系

| 关联特性 | 特性ID | 关系说明 | 文档明示/推断 |
|---------|--------|---------|--------------|
| GW-U 选择 | WSFD-107005（UNC） | 本特性包含的子特性 | **文档明示**（定义章节列出） |
| 支持基于位置的 GW-U 选择 | WSFD-107006（UNC） | 本特性包含的子特性 | **文档明示** |
| 支持基于权重的 GW-U 选择 | WSFD-107008（UNC） | 本特性包含的子特性 | **文档明示** |
| 会话管理 | WSFD-010501（UNC） | UPF 选择是 PDU 会话建立的子决策环节 | 推断（语义关联） |
| 地址分配方式 | WSFD-010502（UNC） | 静态 IP 段绑定 UPF 与 SMF 主锚点 UPF 冲突时，SMF 选择优先 | **WSFD-010502 文档明示引用本特性** |
| 多 PDN/PDU 功能 | WSFD-010503（UNC） | 多 PDU 会话场景的 UPF 选择 | 推断 |
| 会话管理（UDG 侧） | GWFD-010101（UDG） | SMF 选定 UPF 后 N4 建立会话，UPF 侧执行 | 推断 |
| 用户面地址分配 | GWFD-010105（UDG） | SMF 选定 UPF 后指示 UPF 执行地址分配 | 推断 |
| UNC UPF 选择专题 | （业务专题文档） | 更深入的 UPF 选择专题介绍 | **文档明示引用**（`UNC UPF选择专题/特性映射与交互_72976829.md`） |

### 6.2 知识来源清单

| 序号 | 来源文件（相对 output/ 的路径） | 主要贡献内容 |
|------|---------|-------------|
| 1 | `UNC 20.15.2 产品文档(裸机容器) 05/网络部署/特性部署/UNC特性指南/分布式网络功能/WSFD-107010 UPF选择_10789013.md` | 本特性唯一产品文档（特性概述，165行）。贡献内容：适用NF（SMF+UPF，UNC 20.2.0+/UDG 20.2.0+）、定义（基于 UE 位置/DNN/S-NSSAI 选择 UPF，结合 DNAI/分流能力/接口能力/EPS互通/优先级/负载/权重）、包含的子特性（WSFD-107005/107006/107008）、客户价值（差异化部署/贴近用户/负载均衡）、应用场景（专用UPF/地理贴近/负载不均衡）、License（82209917 LKV2USBL01 + 82200BES LKV2GWUS01）、应用限制（SMF 与 UPF 必须同为 HUAWEI）、原理概述（图1不同角色UPF选择过程、图2基于优先级选择UPF原理、表1 14种UPF选择原则含14+条MML命令）、UPF选择示例（表2 8个UPF属性、图3选择过程）、遵循标准（3GPP 29.501）、发布历史（v01 20.2.0/v02 20.3.2 DNAI/v03 20.6.0 负载与优先级/v04 20.9.0 ULI For SGW）、与其他特性交互（不涉及）、对系统影响（无）、特性规格（无）、计费与话单（无） |

### 6.3 关键术语

| 术语 | 全称 | 说明 |
|------|------|------|
| UPF | User Plane Function | 5G 用户面功能，本特性中含 SGW-U、PGW-U |
| SMF | Session Management Function | 5G 会话管理功能，UPF 选择的决策方 |
| DNN | Data Network Name | 5G 数据网络名称（4G 中对应 APN） |
| S-NSSAI | Single Network Slice Selection Assistance Information | 5G 单网络切片选择辅助信息 |
| DNAI | DN Access Identifier | 数据网络接入标识，由 DNN 映射获取 |
| NRF | Network Repository Function | 网络存储库功能，UPF 注册与发现 |
| N4 | 5G N4 接口 | SMF 与 UPF 间接口（PFCP 协议） |
| N6 | 5G N6 接口 | UPF 与 DN（数据网络）间接口 |
| I-UPF | Intermediate UPF | 中间 UPF，用户接入锚点（文档称"接入锚点"） |
| 主锚点 UPF | PSA (PDU Session Anchor) | PDU 会话锚点，主用 UPF（PGW-U 角色） |
| 合一 UPF | Combined UPF | SGW-U/PGW-U 合一，或主锚点与 I-UPF 合一 |
| ULI | User Location Information | 用户位置信息信元 |
| ULI For SGW | 专为 SGW-U 选择使用的 ULI | v04 新增支持 |
| AMBR | Aggregate Maximum Bit Rate | 聚合最大比特率，AMBRUPFFLAG 控制同 DNN 会话选相同 UPF |
| EPS | Evolved Packet System | 4G 演进分组系统，UPF 是否支持与 EPS 互通用于 4/5G 互操作场景 |

---

## 7. 文档一致性说明（配置树 vs 产品文档）

> 配置树仅用于定位特性 ID，以下记录以产品文档实际内容为准时发现的信息。

### 7.1 与配置树/文档清单的差异

| # | 维度 | 配置树/文档清单描述 | 产品文档实际内容 | 差异类型 |
|---|------|---------------------|-----------------|---------|
| 1 | 文档数量 | 文档清单列 **1 个文件** | 实际仅 1 篇特性概述文档（无独立参考信息、激活、调测文档） | 一致：清单与文档匹配，但覆盖度精简 |
| 2 | 文档覆盖度 | 标注"[★核心]" | 仅特性概述，**无完整 MML 激活脚本**、**无独立调测章节**、**无告警/软参/测量指标**（参考信息章节） | **重大缺口**：作为网元选择类核心特性，文档精简至仅原理与原则表，配置实操需参考 OM 命令手册与业务专题 |
| 3 | 子特性关系 | 文档清单未提及子特性 | 产品文档明确包含 WSFD-107005/107006/107008 三个子特性 | 补全：文档提供了子特性分解 |
| 4 | License要求 | 文档清单标注"[★核心]" | 产品文档明确 **2 个 License 控制项**（82209917 + 82200BES） | 一致：★核心需 License |
| 5 | 命令清单完整性 | 文档清单标题仅"SMF为PDU会话选择UPF" | 表1 列出 **20+ 条 MML 命令**（以超链接形式引用 OM 手册），涵盖 NF 实例、业务能力、位置区、接口绑定、策略控制 5 大类 | 补全：命令清单丰富但分散在表1中 |
| 6 | 业务专题引用 | 文档清单未提及 | 产品文档引用 `UNC UPF选择专题/特性映射与交互_72976829.md` | 补全：存在独立业务专题文档（Stage 3 应补充阅读） |
| 7 | 示例丰富度 | - | 表2（8 UPF 属性表）+ 图1/图2/图3（3 张示意图） | 一致：示例以图表形式呈现，无 MML 脚本 |

### 7.2 与地址分配（WSFD-010502）的协同关系

| # | 维度 | WSFD-010502（地址分配） | WSFD-107010（UPF选择） | 协同说明 |
|---|------|------------------------|------------------------|---------|
| 1 | 角色定位 | 地址来源决策方 | UPF 实例决策方 | 两个正交维度的决策：选地址 + 选 UPF |
| 2 | 冲突协调 | 静态 IP 段→UPF 绑定 | SMF 主锚点 UPF 选择 | **冲突时 SMF 选择优先**（WSFD-010502 §3.2.4 明确引用 WSFD-107010） |
| 3 | 文档引用方向 | WSFD-010502 → WSFD-107010（单向引用） | WSFD-107010 文档"不涉及与其他特性的交互" | **单向引用**：地址分配侧感知冲突，UPF 选择侧声明独立 |
| 4 | 共用配置对象 | ADD UPNODE（ADDRALLOCMODE=INHERIT） | ADD UPNODE（位置特征与分流能力） | **共用 ADD UPNODE 命令**，但参数维度不同（地址分配 vs 位置分流） |

### 7.3 与会话管理（WSFD-010501）的协同关系

| # | 维度 | 协同说明 |
|---|------|---------|
| 1 | 流程嵌套 | UPF 选择发生在 PDU 会话建立流程中（WSFD-010501 的 PDU 会话建立步骤内嵌 UPF 选择决策） |
| 2 | 文档明示 | WSFD-107010 文档"与其他特性的交互"章节明确声明"不涉及"，但"定义"章节明示"在 PDU 会话建立流程中" |
| 3 | 推断结论 | 流程嵌套关系由"定义"章节隐含，交互独立性声明可能仅指配置层面无依赖 |

---

## 附录 A：文档缺口标注（Stage 3 补充清单）

> 本特性仅 1 篇产品文档，以下信息缺口需 Stage 3 横向分析或 OM 命令手册补充：

| # | 缺口项 | 影响 | 补充来源建议 |
|---|--------|------|-------------|
| 1 | 无完整 MML 激活脚本 | 配置实操无端到端参考 | OM 命令手册各命令独立说明 + UDG 初始配置与调测 |
| 2 | 无独立调测章节 | 调测方法无标准化流程 | 参考 WSFD-010502 调测方法（DSP PDUSESSION） |
| 3 | 无告警/软参/测量指标 | 运维观测点缺失 | 可能在 UDG 侧（GWFD-010101 等）或独立参考信息文档 |
| 4 | SET UPSELECTFLAG 各开关默认值未明示 | AMBRUPFFLAG/N3UPFAPNFLAG/ULISGWFLAG 默认值未知 | OM 命令手册 SET UPSELECTFLAG |
| 5 | UPF 权重取值范围未明示 | WEIGHT 参数规格未知 | OM 命令手册 ADD PNFPROFILE |
| 6 | 表2 示例的选择结果未文字化（仅在图3示意图） | 无法纯文本理解选择结果 | 业务专题文档 `UNC UPF选择专题/特性映射与交互_72976829.md` |
| 7 | UPF 角色体系（主锚点/I-UPF/合一）详细定义未展开 | 角色边界不清 | 业务专题文档 + UDG 产品手册 |
| 8 | 配置树父节点关系未提及 | feature_group 归属待验证 | Stage 3 配置树分析 |
