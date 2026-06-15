# Batch-06: 体验感知异厂商组网与版本配套 + 重点业务保障初始配置

> **场景归属**: 带宽控制场景（套餐2）
> **聚焦主题**: GBR保障 / Non-GBR保障 / 智能码率识别等带宽保障配置
> **知识来源**: UDG 产品文档 20.15.2, 体验感知解决方案 + 重点业务保障解决方案
> **网元覆盖**: UDC(NWDAF) / CloudUDN / UDG(UPF) / UNC(AMF/MME, SMF)
> **批次状态**: 已产出

---

## 1. 文档概述

本批次综合 12 篇源文档，覆盖两大主题块：

1. **体验感知异厂商 PCF 场景组网与版本配套**：在现网 PCF 为异厂商时，如何通过双 N7 会话机制接入华为智能 PCF，体验感知/重点业务保障方案对各网元的版本要求是什么。
2. **重点业务保障初始业务配置（CloudUDN / UDC / UDG / UNC 四侧）**：从 License 开启到 GBR 保障、Non-GBR 保障、智能码率识别功能的具体 MML 命令和 OM Portal 操作步骤。

重点业务保障解决方案是带宽控制场景中"业务级精准保障"的核心能力，其通过 NWDAF 分析、PCF 下发策略、SMF/UPF 执行，实现对特定应用（直播、视频会议等）的 GBR（保证比特速率）保障或 Non-GBR（最大比特速率）限速保障，并结合智能码率识别实现带宽档位的动态匹配。这些配置直接决定了带宽控制场景中"哪些业务获得多少带宽保障"。

---

## 2. 核心知识点

### 2.1 体验感知异厂商 PCF 场景组网与接口

#### 2.1.1 组网架构

异厂商 PCF 场景指现网 PCF 为异厂商（非华为），但运营商需要使用华为体验感知/重点业务保障能力。解决方案为**部署一套华为智能 PCF**，由 SMF 创建第二条 N7 会话与智能 PCF 交互。

关键接口（遵循 3GPP 标准）：

| 通信 NF | 接口名称 | 协议 | 接口功能 | 遵循标准 |
|---------|----------|------|----------|----------|
| 异厂商PCF <-> SMF | N7 | HTTP/2 + TLS | SMF 从异厂商 PCF 获取用户会话策略，异厂商 PCF 在 N7 消息中携带智能 PCC Rule | 3GPP TS 29.502 |
| SMF <-> 智能PCF | N7 | HTTP/2 + TLS | SMF 创建第二条 N7 会话，向智能 PCF 发送分析订阅 | 3GPP TS 29.502 |
| 智能PCF <-> NWDAF | N23 | HTTP/2 + TLS | PCF 调用 NWDAF 的 EventsSubscription 服务，订阅 QoS 保障分析功能 | 3GPP TS 29.520 |
| NWDAF <-> SMF | Nsmf | HTTP/2 + TLS | NWDAF 调用 SMF 的 EventExposure 服务，发送 QOS_ANA 事件订阅 | 3GPP TS 29.508 |
| UPF <-> NWDAF | Nupf | HTTP/2 + TLS | UPF 向 NWDAF 通知已订阅用户业务体验监测信息 | 3GPP TS 29.564 |
| NWDAF <-> NRF | Nnrf | HTTP/2 + TLS | NWDAF 生命周期管理及 NF 选择时与 NRF 的交互 | 3GPP TS 29.510 |
| UDC <-> UDN | Nudn | HTTP/2 + TLS | UDC 通过 Nudn 向 UDN 转发 UPF 上报的体验数据 | 私有协议 |
| SMF <-> UPF | N4 | PFCP + GTP-U | SMF 与 UPF 间控制面和用户面，支持通过 SRR 携带私有信元下发业务体验分析事件 | 3GPP TS 23.502 / 29.244 |
| NWDAF <-> 第三方设备 | - | FTP/SFTP | NWDAF 向第三方设备转发体验数据 | RFC 114 / RFC 4253 |

#### 2.1.2 N4 接口在重点业务保障中的特殊能力

N4 接口在标准 PFCP 能力之外，支持 SMF 在 `PFCP Session Modification Request` 消息中通过 SRR（Session Report Rule）携带**私有信元**下发业务体验分析事件信息。这是华为方案的关键差异化能力。

#### 2.1.3 Nudn 接口的作用

当开启重点业务保障用户的体验信息采集功能时，UDC(NWDAF) 通过 Nudn 接口向 UDN 转发 UPF 上报的体验数据。该接口为私有协议。

---

### 2.2 体验感知解决方案版本配套要求

部署体验感知功能涉及以下网元的版本配套：

| 涉及 NF | 版本支持 | 功能描述 |
|---------|----------|----------|
| SMF | UNC 20.13.0 及后续 | 支持根据 NWDAF 订阅上报用户实时位置；支持 Nsmf 接口解析 NWDAF 的 QOS_ANALYSIS、QOS_EXP_ANALYSIS 事件订阅请求；支持 N4 接口转译 NWDAF 请求到 UPF；支持通过 PCF 下发智能规则的方式选择智能 UPF |
| SMF（异厂商 PCF 场景） | **UNC 20.15.0 及后续** | 支持创建第二条 N7 会话用于向智能 PCF 发起分析订阅 |
| NRF | UNC 20.13.0 及后续 | 支持 NWDAF 注册 QOS_ANALYSIS、QOS_EXP_ANALYSIS 事件 |
| UPF | UDG 20.13.0 及后续 | 支持 N4 接口解析 SMF 转译的 NWDAF 请求；支持 Nupf 接口接收 UDN 下发的体验感知信息采集订阅，向 UDC 上报保障用户体验感知消息；支持 NupfR 接口向 UDN 上报体验数据 |
| PCF | UPCF 20.13.0 及后续 | 支持 N23 接口，向 NWDAF 下发 QOS_ANALYSIS、QOS_EXP_ANALYSIS 事件订阅请求 |
| NWDAF（UDC） | UDC 20.13.0 及后续 | 支持 N23 接口接收解析 PCF 订阅；支持 Nsmf 接口向 SMF/UPF 订阅数据；支持 Nupf 接口接收 UPF 上报体验数据；支持 Nudn 接口向 UDN 转发体验数据 |
| NWDAF（UDN） | CloudUDN V100R024C20 及后续 | 使能数据底座功能；支持 Nudn 接口接收 UDC 转发的体验数据；支持 Nupf/NupfR 接口与 UPF 交互 |
| BOSS/SFTP 服务器 | 第三方设备 | 接收 NWDAF 上报的体验感知单据 |

**关键版本约束**：异厂商 PCF 场景（双 N7 会话）需要 SMF 升级到 **UNC 20.15.0 及后续版本**。如果现网 SMF 版本低于 20.15.0，则不支持异厂商 PCF 场景。

---

### 2.3 重点业务保障 CloudUDN 侧配置

#### 2.3.1 Kafka partition 重分配

**操作场景**：当 Kafka Manager 页面出现 Brokers Spread % 没有显示 100% 时，需要执行 partition 重分配。

**操作步骤**：
1. 使用浏览器登录 CloudUDN 业务 Portal 页面（`https://{CloudUDN PBU_C-A虚拟机vNIC2端口IP}:28443`）。
2. 单击右上角 "Kafka Manager"，单击 PSIKafka > Brokers，查看 kafka ID 是否增加。
   - 是 -> 执行重分配步骤。
   - 否 -> 无需继续操作。
3. 单击 PSIKafka > Topics > Generate Partition Assignments，全选后单击生成。
4. 显示 Done 后，进入具体 Topics 页面（如 natlog），单击 Reassign Partitions。
5. 验证：Brokers 总数为总 psikafka 微服务个数，且 Brokers Skew、Under Replicate 两列为 0 表示成功。

**与带宽控制的关系**：Kafka 是 CloudUDN 数据底座的消息中间件。小区负载预测、智能码率识别等带宽保障能力依赖 CloudUDN 数据底座的正常运行，partition 不均衡会导致数据处理的延迟或丢失，间接影响保障决策的实时性。

#### 2.3.2 配置小区负载预测功能

**操作场景**：重点业务保障解决方案中 CloudUDN 侧小区负载预测功能配置。

**前提条件**：已登录 OM Portal；已加载 License 文件。

**License 控制项**（需设置为 On）：
- 无线网络小区日志信息采集
- 无线网络小区负载智能预测
- （可选）用户体验数据开放增值包：同时部署重点业务保障与体验感知解决方案时需开启
- （可选）VVIP 用户体验数据开放增值包：保障用户体验感知业务场景下需开启
- （可选）智能码率识别可视（每 CloudUDN）：UDC 侧开通智能码率识别功能时开启

**训练模型配置参数**：

| 配置项 | 参数 | 取值样例 | 说明 |
|--------|------|----------|------|
| 训练模型配置 | 智能分析获取偏移时长（分钟） | 6 | 建议使用默认值 |
| 训练模型配置 | 训练数据集自动补齐 | 开启 | 针对小区训练数据集缺失比例小于 30% 的场景 |
| 训练模型配置 | 推理数据集自动补齐 | 开启 | 针对推理时所需的前 4 个周期数据缺失场景 |
| 训练模型配置 | 预测退化策略 | 废弃预测结果 | "动态模型配置"开启的情况下才生效 |
| 训练模型配置 | 动态模型配置 | 就近实报值 | 开启小区负载预测功能时需配置为开启模型预测，确保无线工作站时间偏移在一小时内，同步修改与无线工作站的时间偏移为 75 分钟，预测退化策略修改为强制不退化 |
| 训练模型配置 | 小区上行 PRB 默认使用率 | 30 | - |
| 训练模型配置 | 小区下行 PRB 默认使用率 | 30 | - |
| 训练模型配置 | 小区上行容量默认值（Mbps） | 680 | - |
| 训练模型配置 | 小区下行容量默认值（Mbps） | 4500 | - |
| 训练模型配置 | 训练模型密钥 | 空 | 非必选参数，主备需一致 |
| 训练模型配置 | 小区高负载日志记录 | 开启 | - |
| 训练模型配置 | 小区高负载阈值(%) | 80 | - |

**与带宽控制的关系**：小区负载预测是 GBR 保障决策的关键输入。NWDAF 在决定是否发起保障建议时，需要获取小区 PRB 利用率和小区容量信息。CloudUDN 通过负载预测模型提前识别拥塞风险，使保障决策更加前瞻。

---

### 2.4 重点业务保障 UDC 侧配置

UDC 侧是重点业务保障的核心配置节点，涵盖 License、GBR 保障、Non-GBR 保障、智能码率识别、跨 NWDAF 移动等子功能。

#### 2.4.1 开启 License 开关

**前提条件**：已完成 NWDAF 与周边 NF 的接口配置；已登录华为操作维护系统。

**MML 命令（UDC 窗口）**：

```
// 开启端到端用户跟踪 License 控制项。
SET LICENSESWITCH: LICITEM="LKV8ESTUDC01", SWITCH=ENABLE;
// 同时部署体验感知功能时，开启体验信息能力开放 License 控制项。
SET LICENSESWITCH: LICITEM="LKV8EIEEUDC01", SWITCH=ENABLE;
// 开启磁盘故障隔离 License 控制项。
SET LICENSESWITCH: LICITEM="LKV6DIFAUDC01", SWITCH=ENABLE;
// 可选：开启智能码率功能时打开该 License 控制项。
SET LICENSESWITCH: LICITEM="LKV8IBRIUDC01", SWITCH=ENABLE;
```

**关键 License 项**：
| License 项 | 说明 |
|------------|------|
| LKV8ESTUDC01 | 端到端用户跟踪 |
| LKV8EIEEUDC01 | 体验信息能力开放 |
| LKV6DIFAUDC01 | 磁盘故障隔离 |
| LKV8IBRIUDC01 | 智能码率识别（可选，仅开通码率识别时需要） |

#### 2.4.2 配置 GBR 保障

**操作场景**：为应用开启 GBR 保障时，配置保障的最大带宽、小区资源相关阈值。

**前提条件**：已完成 NWDAF 与周边 NF 接口配置；已完成 License 开关开启。

**核心概念**：
- GBR（Guaranteed Bit Rate）：保证比特速率，是带宽控制的**下限保证**
- MBR（Maximum Bit Rate）：最大比特速率，是带宽控制的**上限限制**
- FQI（5QI QoS Identifier）：QoS 标识
- ARP（Allocation and Retention Priority）：分配保留优先级

**应用组与应用配置参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| ADD APPGROUP | APPGROUPNAME | appgroup1 | 应用组名称 |
| ADD APPGROUP | APPGROUPTYPE | LIVE_VIDEO | 应用组业务保障类型 |
| ADD APPGROUP | FQI | 4 | QoS 标识 |
| ADD APPGROUP | ARPVALUE | 1 | 分配保留优先级 |
| ADD APPGROUP | GBRULVALUE | 3000 | 保证上行带宽(kbit/s) |
| ADD APPGROUP | GBRDLVALUE | 3000 | 保证下行带宽(kbit/s) |
| ADD APPGROUP | MBRULVALUE | 1000000 | 最大上行带宽(kbit/s) |
| ADD APPGROUP | MBRDLVALUE | 1000000 | 最大下行带宽(kbit/s) |
| ADD APP | APPNAME | app1 | 应用名称 |
| ADD APP | APPGROUPNAME | appgroup1 | 绑定到应用组 |
| ADD APP | GBRULVALUE | 3000 | 应用级保证上行带宽(kbit/s) |
| ADD APP | GBRDLVALUE | 3000 | 应用级保证下行带宽(kbit/s) |
| ADD APP | MBRULVALUE | 1000000 | 应用级最大上行带宽(kbit/s) |
| ADD APP | MBRDLVALUE | 1000000 | 应用级最大下行带宽(kbit/s) |
| ADD APP | CHARGINGID | 1030000005 | 计费标识（异厂商 PCF 场景不支持配置该参数） |

**QoS 保障条件参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| SET QOSGUARCOND | NRCELLULGBRTH | 40 | 5G 小区上行 GBR 门限(%)，如小区上行容量 300Mbps，则最多分配 120Mbps 上行 GBR |
| SET QOSGUARCOND | NRCELLDLGBRTH | 40 | 5G 小区下行 GBR 门限(%) |
| SET QOSGUARCOND | INVGUARPRTIMES | 0 | 界定无效保障的质差次数（0=关闭无效保障判断） |
| SET QOSGUARCOND | CELLCONGESW | ENABLE/DISABLE | 小区拥塞是否为保障条件（对接 UDN 时 ENABLE） |
| SET QOSGUARCOND | PRBUSAGE | 90 | 界定小区拥塞的 PRB 利用率(%) |

**小区容量参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| ADD NRCELLCAPACITY | NGBEGINCID / NGENDCID | 225fec55248408 ~ 225fec55248410 | 5G 小区范围 |
| ADD NRCELLCAPACITY | MBRULVALUE | 100 | 小区最大上行带宽(Mbps) |
| ADD NRCELLCAPACITY | MBRDLVALUE | 300 | 小区最大下行带宽(Mbps) |
| SET QOSGUARCOND | NRCELLDFTMBRDL | 300 | 5G 小区缺省最大下行带宽(Mbps)，全局生效，优先级低于 ADD NRCELLCAPACITY |
| SET QOSGUARCOND | NRCELLDFTMBRUL | 100 | 5G 小区缺省最大上行带宽(Mbps) |
| SET UDNCTRL | CELLCAPVT | 0 | 小区容量有效时长(分钟)，未对接 UDN 时设为 0 |
| SET UDNCTRL | CELLPRBVT | 0 | 小区 PRB 利用率有效时长(分钟)，未对接 UDN 时设为 0 |

**4G 小区容量参数**（支持 4G 用户保障时）：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| ADD EPCCELLCAPACITY | EPCBEGINCID / EPCENDCID | 460010001234 ~ 460010005678 | 4G 小区范围 |
| ADD EPCCELLCAPACITY | MBRULVALUE | 60 | 4G 小区最大上行带宽(Mbps) |
| ADD EPCCELLCAPACITY | MBRDLVALUE | 300 | 4G 小区最大下行带宽(Mbps) |
| SET QOSGUARCOND | EPCCELLDFTMBRDL | 300 | 4G 小区缺省最大下行带宽(Mbps) |
| SET QOSGUARCOND | EPCCELLDFTMBRUL | 60 | 4G 小区缺省最大上行带宽(Mbps) |
| SET QOSGUARCOND | EPCCELLULGBRTH | 40 | 4G 小区上行 GBR 门限(%) |
| SET QOSGUARCOND | EPCCELLDLGBRTH | 40 | 4G 小区下行 GBR 门限(%) |
| SET NWDAFCTRL | EPCQOSSW | ENABLE | 4G 质差保障及体验感知信息上报开关 |

**GBR 保障完整配置命令**：

```
// 步骤1：添加应用组及应用信息
ADD APPGROUP: APPGROUPNAME="appgroup1", APPGROUPTYPE=LIVE_VIDEO, FQI=4, ARPVALUE=1, GBRULVALUE=3000, GBRDLVALUE=3000, MBRULVALUE=1000000, MBRDLVALUE=1000000;
ADD APP: APPNAME="app1", APPGROUPNAME="appgroup1", GBRULVALUE=3000, GBRDLVALUE=3000, MBRULVALUE=1000000, MBRDLVALUE=1000000, CHARGINGID=1030000005;

// 步骤2（已对接 UDN 且 UDN 支持预测能力时）：配置开启将小区拥塞作为保障条件
SET QOSGUARCOND: NRCELLULGBRTH=40, NRCELLDLGBRTH=40, CELLCONGESW=ENABLE, PRBUSAGE=90, INVGUARPRTIMES=0;

// 步骤3（未对接 UDN 或 UDN 不支持预测能力时）：设置不将小区拥塞作为保障条件
SET QOSGUARCOND: CELLCONGESW=DISABLE;
SET UDNCTRL: CELLCAPVT=0, CELLPRBVT=0;
SET QOSGUARCOND: NRCELLDFTMBRDL=300, NRCELLDFTMBRUL=100;

// 步骤4（支持 4G 用户保障时）：
ADD EPCCELLCAPACITY: EPCBEGINCID="460010001234", EPCENDCID="460010005678", MBRULVALUE=60, MBRDLVALUE=300;
SET QOSGUARCOND: EPCCELLDFTMBRDL=300, EPCCELLDFTMBRUL=60, EPCCELLULGBRTH=40, EPCCELLDLGBRTH=40;
SET NWDAFCTRL: EPCQOSSW=ENABLE;

// 步骤5：设置向 UDN 上报体验感知信息
SET UDNCTRL: EXPGUAINFORPTSW=ENABLE;

// 步骤6：设置 UDC 向 PCF 发送 N5 消息优先携带 ueIpv6
SET NWDAFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1, VALUE=VALUE_0, POSITION=10;
SET NWDAFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1, VALUE=VALUE_1, POSITION=11;

// 步骤7（异厂商 PCF 支持标准 N5 场景）：关闭私有信元
SET NWDAFPVTEXT: INFOELE=N5_N23SUBID, SWITCH=DISABLE;
SET NWDAFPVTEXT: INFOELE=N5_CHGID, SWITCH=DISABLE;

// 步骤8：设置 UDC 单会话下最大可保障流规格
SET NWDAFSOFTPARA: DT=Byte, BYTENUM=5, BYTEVALUE=7;
```

**GBR 门限计算逻辑**：NRCELLULGBRTH/NRCELLDLGBRTH 表示小区 GBR 资源占比上限。例如某 5G 小区上行容量为 300Mbps，NRCELLULGBRTH=40%，则该小区最多只能分配 120Mbps 的上行 GBR 给 QoS 保障。

#### 2.4.3 配置 Non-GBR 保障

**操作场景**：为应用开启 Non-GBR 保障时，配置最大带宽限速参数。

**与 GBR 保障的核心区别**：
- Non-GBR 保障**不配置 GBR 值**（无 GBRULVALUE/GBRDLVALUE 参数）
- 仅配置 MBR（最大带宽）作为上限限制
- ADD APPGROUP 命令中通过 `GUARANTEETYPE=Non-GBR` 标识保障类型
- 典型 FQI 取值不同：Non-GBR 示例为 7（GBR 示例为 4）

**Non-GBR 保障配置命令**：

```
// 步骤1：添加应用组及应用信息（注意 GUARANTEETYPE=Non-GBR，无 GBR 参数）
ADD APPGROUP: APPGROUPNAME="appgroup1", GUARANTEETYPE=Non-GBR, APPGROUPTYPE=LIVE_VIDEO, FQI=7, ARPVALUE=1, MBRULVALUE=6000, MBRDLVALUE=6000;
ADD APP: APPNAME="app1", APPGROUPNAME="appgroup1", CHARGINGID=1030000005;

// 步骤2：设置 QoS 保障条件
SET QOSGUARCOND: CELLCONGESW=ENABLE, PRBUSAGE=80;

// 步骤3：关闭向 UDN 获取小区容量功能
SET UDNCTRL: CELLCAPVT=0;
```

**Non-GBR 保障参数对比**：

| 参数 | GBR 保障 | Non-GBR 保障 |
|------|----------|--------------|
| GUARANTEETYPE | 未显式指定（默认 GBR） | Non-GBR |
| FQI（示例） | 4 | 7 |
| GBRULVALUE / GBRDLVALUE | 有（如 3000 kbit/s） | 无 |
| MBRULVALUE / MBRDLVALUE | 有（如 1000000 kbit/s） | 有（如 6000 kbit/s） |
| PRBUSAGE（示例） | 90 | 80 |

**带宽控制语义**：Non-GBR 保障本质上是对非保证速率业务的**最大带宽限速**。MBR 值是应用在该保障下可使用的最大带宽上限。Non-GBR 的 MBR 示例值(6000 kbit/s)远小于 GBR 的 MBR 示例值(1000000 kbit/s)，说明 Non-GBR 是更严格的带宽上限控制。

#### 2.4.4 配置智能码率识别功能

**操作场景**：为直播应用开启智能码率识别功能，实现带宽档位的动态匹配。

**前提条件**：**仅为应用开通了 GBR 保障功能时，才支持配置智能码率识别功能**。已完成配置 GBR 保障。

**核心概念**：
- 智能码率识别：NWDAF 通过 AI 算法训练，自动识别应用的实际码率，动态匹配带宽档位
- 带宽档位：为应用配置多个带宽区间，NWDAF 根据实时码率匹配对应档位的保障带宽
- 档位匹配优先级：智能算法训练 > 配置带宽档位 > 默认最高档位

**License 要求**：需开启 `LKV8IBRIUDC01`（智能码率识别）License 控制项。

**配置参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| MOD APP | APPNAME | app1 | 应用名称 |
| MOD APP | APPGROUPNAME | appgroup1 | 应用组名称 |
| MOD APP | CODETRAINSW | ENABLE | 智能算法训练开关 |
| SET CODETRAINRULE | STARTTRAINTIME | 02&30 | 每日训练启动时间（02:30），pool 内各 NWDAF 不重叠 |
| ADD BANDWIDBNDAPP | BITRATESTART | 1000 | 带宽档位起始值(kbit/s) |
| ADD BANDWIDBNDAPP | BITRATEEND | 2000 | 带宽档位终止值(kbit/s) |
| SET BANDMATCHPOLICY | CODETRAIN | FIRST_PRIORITY | 智能算法训练优先级 |
| SET BANDMATCHPOLICY | FROMCONFIG | SECOND_PRIORITY | 配置带宽档位优先级 |
| SET BANDMATCHPOLICY | DEFAULTMBR | THIRD_PRIORITY | 默认最高档位保障优先级 |
| ADD APPBANDMATCHPLY | APPNAME | app1 | 应用级带宽档位匹配规则（优先级高于全局） |

**智能码率识别完整配置命令**：

```
// 步骤1：开启需要智能码率识别的 APP 功能开关
MOD APP: APPNAME="app1", APPGROUPNAME="appgroup1", CODETRAINSW=ENABLE;

// 步骤2：设置智能码率训练规则
SET CODETRAINRULE: STARTTRAINTIME=02&30;

// 步骤3：增加应用带宽档位（4 个档位示例）
ADD BANDWIDBNDAPP: APPNAME="app1", APPGROUPNAME="appgroup1", BITRATESTART=1000, BITRATEEND=2000;
ADD BANDWIDBNDAPP: APPNAME="app1", APPGROUPNAME="appgroup1", BITRATESTART=2001, BITRATEEND=5000;
ADD BANDWIDBNDAPP: APPNAME="app1", APPGROUPNAME="appgroup1", BITRATESTART=5001, BITRATEEND=10000;
ADD BANDWIDBNDAPP: APPNAME="app1", APPGROUPNAME="appgroup1", BITRATESTART=10001, BITRATEEND=15000;

// 步骤4：设置带宽档位匹配规则优先级（全局）
SET BANDMATCHPOLICY: CODETRAIN=FIRST_PRIORITY, FROMCONFIG=SECOND_PRIORITY, DEFAULTMBR=THIRD_PRIORITY;

// 步骤5：设置带宽档位匹配规则优先级（应用级，优先级高于全局）
ADD APPBANDMATCHPLY: APPNAME="app1", APPGROUPNAME="appgroup1", CODETRAIN=FIRST_PRIORITY, FROMCONFIG=SECOND_PRIORITY, DEFAULTMBR=THIRD_PRIORITY;
```

**带宽档位匹配逻辑**：
1. 首先尝试智能算法训练结果匹配（FIRST_PRIORITY）
2. 其次使用配置的带宽档位进行区间匹配（SECOND_PRIORITY）
3. 最后回退到默认最高档位保障（THIRD_PRIORITY）

**与带宽控制的关系**：智能码率识别是带宽控制中"精细化差异化保障"的关键能力。通过 AI 训练自动匹配带宽档位，避免固定 GBR 值导致的资源浪费（档位过高）或体验不足（档位过低），实现带宽资源的动态精准分配。

#### 2.4.5 配置跨 NWDAF 服务区域移动

##### 场景 A：省间跨 NWDAF 服务区域漫游（UDC 20.15.0 及以后）

**操作场景**：支持用户省间跨 NWDAF 服务区域漫游。NWDAF 间通信不涉及注册新服务。

**核心参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| SET NWDAFCTRL | ROAMINGSW | ENABLE | 漫游目标方案开关 |
| SET NWDAFCTRL | ALWAYSROAMINGSW | DISABLE/ENABLE | Always 漫游开关（见策略说明） |
| SET NODEIDX | NBEGIN | 5 | 区域标识起始位置（UUID 第 5 位） |
| SET NODEIDX | NEND | 6 | 区域标识终止位置（UUID 第 6 位） |
| ADD ROAMSRVPROV | PROVINCEID | d7 | 省份白名单（ALWAYSROAMINGSW=DISABLE 时配置） |
| ADD ROAMSRVAMF | AMFINSTANCEID | UUID | AMF 白名单 |
| ADD ROAMBLKPROV | PROVINCEID | a7 | 省份黑名单（ALWAYSROAMINGSW=ENABLE 时配置） |
| ADD ROAMBLKAMF | AMFINSTANCEID | UUID | AMF 黑名单 |
| SET ROAMINGCTRL | RETRYTIMES | 1 | 目标 NWDAF 异常重选最大次数 |
| SET ROAMINGCTRL | RETRYINHIBITSW | ENABLE | 目标 NWDAF 异常重选抑制功能 |
| SET ROAMINGCTRL | RETRYINHIBITIMER | 10 | 异常重选抑制定时器时长(分钟) |

**白名单/黑名单策略选择**：
- **白名单模式**（ALWAYSROAMINGSW=DISABLE）：当支持 NWDAF 的省份较少时使用。根据 AMF ID / 省份白名单判断当前区域是否支持 NWDAF 服务，不支持直接跳过服务发现。
- **黑名单模式**（ALWAYSROAMINGSW=ENABLE）：当大部分省份支持 NWDAF、少量不支持时使用。除黑名单外默认进行服务发现。

**省间漫游配置命令**：

```
// 步骤1：设置省份标识位（UUID 后 12 位中的第 5 到 6 位代表省份标识）
SET NODEIDX: NBEGIN=5, NEND=6;

// 步骤2A（白名单模式）：仅少量省份支持 NWDAF 时
SET NWDAFCTRL: ROAMINGSW=ENABLE, ALWAYSROAMINGSW=DISABLE;
ADD ROAMSRVPROV: PROVINCEID="d7";
ADD ROAMSRVAMF: AMFINSTANCEID="6d25a684-9558-11e9-efccd7a0659b";

// 步骤2B（黑名单模式）：仅少量省份不支持 NWDAF 时
SET NWDAFCTRL: ROAMINGSW=ENABLE, ALWAYSROAMINGSW=ENABLE;
ADD ROAMBLKPROV: PROVINCEID="a7";
ADD ROAMBLKAMF: AMFINSTANCEID="7d25a684-9558-11e9-efcca7a0659b";

// 步骤3：设置 NWDAF 向 SMF 订阅 SAREA_CH 和 SCNN_CH 事件
SET NWDAFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1, VALUE=VALUE_1, POSITION=4;
SET NWDAFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1, VALUE=VALUE_1, POSITION=5;

// 步骤4（可选）：开启 I-NWDAF 失败重选功能
SET ROAMINGCTRL: RETRYTIMES=1;
SET ROAMINGCTRL: RETRYINHIBITSW=ENABLE, RETRYINHIBITIMER=10;
```

##### 场景 B：省内跨 NWDAF 服务区域漫游（建设初期）

**操作场景**：支持用户省内跨 NWDAF 服务区域漫游。若 UDC 已升级到 20.15.0 及以后版本且需支持省间漫游，跳过此章节。

**核心参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| ADD SRVTAI | MCC | 460 | 移动国家代码 |
| ADD SRVTAI | MNC | 01 | 移动网号 |
| ADD SRVTAI | TAC | 000001 | 跟踪区域码 |
| ADD SRVTAIRANGE | INDEX | 1 | 索引 |
| ADD SRVTAIRANGE | RANGESTART | 022200 | 起始号段 |
| ADD SRVTAIRANGE | RANGEEND | 022500 | 终止号段 |

**省内漫游配置命令**：

```
// 步骤1：添加本省 NWDAF 支持的 TAI
ADD SRVTAI: MCC="460", MNC="01", TAC="000001";

// 步骤2：添加本省 NWDAF 支持的 TAI 范围
ADD SRVTAIRANGE: INDEX=1, MCC="460", MNC="02", RANGESTART="022200", RANGEEND="022500";

// 步骤3：设置向 SMF 订阅 SAREA_CH 事件
SET NWDAFSOFTPARAOFBIT: DT=Dw, DWORDNUM=1, VALUE=VALUE_1, POSITION=4;

// 步骤4：设置用户在拜访地使用 GBR 配额的阈值
SET NWDAFSOFTPARA: DT=Byte, BYTENUM=3, BYTEVALUE=10;
```

**与带宽控制的关系**：跨 NWDAF 漫游配置确保用户在移动过程中，GBR 保障或 Non-GBR 保障策略能够连续生效。如果漫游配置不正确，用户在跨区域移动后可能丢失保障，导致带宽控制策略中断。

---

### 2.5 重点业务保障 UDG 侧配置

UDG（UPF）侧配置是质差检测和体验数据上报的核心节点。

**前提条件**：
- 已完成 UPF 与周边 NF 的接口配置
- 已开启业务感知功能
- 协议识别库和协议解析库已成功加载
- 已完成加载 License

**配置逻辑（质差检测及上报）**：
1. 加载协议特征库
2. 开启 License 开关
3. 设置重点业务保障基本功能
4. 配置质差检测策略（POLICYCONDITION）
5. 配置基于协议的质差检测策略（SSUPROTCOLGROUP）
6. 配置基于应用的质差上报策略（APPPOLICYCTRL）

**License 控制项（UDG 侧）**：

| License 项 | 说明 |
|------------|------|
| LKV3G5ANAR01 | 重点用户质差监测和保障，同时上报体验信息 |
| LKV3G5EXPR01 | 重点用户质差监测和保障，同时上报体验信息 |
| LKV3G5IBIC01 | 智能板订阅和采集 |
| LKV3G5TDIR01 | TCP/UDP 传输分析上报 |
| LKV3G5IARG01 | 报表功能相关 |
| LKV3G5FSFR01 | 报表功能相关 |
| LKV3G5SARS01 | 报表功能相关 |
| LKV3G5RSLR01 | 报表功能相关 |

**质差检测策略关键参数**：

| 类别 | 参数名称 | 取值样例 | 说明 |
|------|----------|----------|------|
| SET VVIPBASICFUNC | SWITCH | ENABLE | 重点业务保障基本功能开关 |
| SET VVIPBASICFUNC | QOERPTPERIOD | 5 | 质差上报周期(秒) |
| SET VVIPBASICFUNC | NONQOERPTPERIOD | 300 | 非质差上报周期(秒) |
| SET VVIPBASICFUNC | REPORTSCOPE | ALL_QOE_REPORT | 质差报表上报范围（发生质差时改为 ONLY_QOE_REPORT） |
| SET VVIPBASICFUNC | SAMPLEPERIOD | 5 | 采集单据周期(秒) |
| SET VVIPBASICFUNC | RPTUSERTYPE | RPT_FOR5GUSER | 上报用户类型（支持 4G+5G 时改为 RPT_FOR45GUSER） |
| SET SSUBIGFLOWCTRL | VVIPFLOWRATE | 800 | VVIP 业务大流速率阈值(kbit/s) |
| ADD POLICYCONDITION | UPLINKAVGRATE | 300 | 上行平均速率基线(kbit/s) |
| ADD POLICYCONDITION | UPFLOWTHRD | 800 | 上行大流阈值(kbit/s) |
| ADD POLICYCONDITION | MULTIKPIJUDGE | SOME_COND_NOT_MATCHED | 多指标质差判断逻辑 |

**版本注意**：UDG 20.13.2.10 之前版本，ADD POLICYCONDITION 命令中速率基线、大流阈值参数单位为**千字节/秒**；20.13.2.10 及后续版本变更为**千比特/秒**。升级时需检查配置。

**UDG 侧完整配置命令**：

```
// 步骤1：加载协议特征库（版本低于 01.0002.1661.01 需加载）
SET SOFTPARA: DT=BYTE, BYTENUM=687, BYTEVALUE=1;
LOD SIGNATUREDB: LOADMODE=LATEST;
SET SOFTPARA: DT=BYTE, BYTENUM=687, BYTEVALUE=0;

// 步骤2：开启必选 License
SET LICENSESWITCH: LICITEM="LKV3G5ANAR01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5EXPR01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5IBIC01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5TDIR01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5IARG01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5FSFR01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5SARS01", SWITCH=ENABLE;
SET LICENSESWITCH: LICITEM="LKV3G5RSLR01", SWITCH=ENABLE;

// 步骤3：设置重点业务保障基本功能（仅 5G 用户）
SET VVIPBASICFUNC: SWITCH=ENABLE, QOERPTPERIOD=5, NONQOERPTPERIOD=300, REPORTSCOPE=ALL_QOE_REPORT, SAMPLEPERIOD=5, RPTUSERTYPE=RPT_FOR5GUSER;

// 步骤4：配置质差检测策略
ADD POLICYCONDITION: POLICYCNDNAME="policytestname", UPLINKAVGRATE=300, UPFLOWTHRD=15, MULTIKPIJUDGE=SOME_COND_NOT_MATCHED;
ADD SSUPROTCOLGROUP: DEFPRTGRPNAME="live_video", PROTOCOLNAME="taobao_live", POLICYCNDNAME="policytestname", QOEDETECTCOND=UP_BIGFLOW_CHECK;

// 步骤5：增加基于应用的质差上报策略
ADD APPPOLICYCTRL: APPIDNAME="appgroup1", SUBAPPIDNAME="app1", DEFPRTGRPNAME="live_video";

// 步骤6：设置 SSU 老化时间
SET SSUAGINGCFG: SESSAGINGTIME=60, FLOWAGINGTIME=61;

// 步骤7：开启 100% 抽样率
SET RPTGLBPARA: FLOWSAMPLERATE=1000;

// 步骤8：开启 TCP UDP 分析
SET RPTGLBCFG: TCPINSIGHTSW=ENABLE, UDPINSIGHTSW=ENABLE;

// 步骤9（可选，智能码率识别时）：打开上报瞬时速率的软参开关
SET SOFTPARA: DT=BIT, BITNUM=3785, BITVALUE=1;

// 步骤10（可选，独立计费时）：开启 NWDAF 专有承载计费 PCC 控制
SET SOFTPARA: DT=BIT, BITNUM=2576, BITVALUE=1;
```

**与带宽控制的关系**：UDG 侧质差检测是带宽保障的**触发条件**。当 UPF 检测到应用流量出现质差（速率低于基线等），会上报体验数据给 NWDAF，NWDAF 分析后向 PCF 发起保障建议，PCF 下发 QoS 策略到 SMF/UPF 执行带宽保障。整个闭环中，UDG 的质差检测策略参数（速率基线、大流阈值）直接决定了"什么时候触发保障"。

---

### 2.6 重点业务保障 UNC 侧配置：AMF/MME 选择 SMF/GW-C

**操作场景**：SM-PCF 异厂商重点业务保障解决方案中 AMF/MME 侧的增量业务配置。

**核心目标**：保障用户接入时，AMF/MME 为用户选择智能 SMF（支持双 N7 会话）接入，触发智能 SMF 与智能 PCF 建立第二个 N7 会话。

**AMF 选择 SMF 支持的场景**（5G 接入）：
1. 基于 SNSSAIS 选择 SMF
2. 基于 DNN 选择 SMF
3. 基于目标 PLMN 选择 SMF
4. 基于支持的 PGW 域名信息和接入类型选择 SMF
5. 基于 locality 选择 SMF
6. 基于 TAI 选择 SMF
7. 基于不同用户（群）使用差异化的条件选择 SMF

**MME 选择 SMF/GW-C**（4G 接入）：基于 APN 选择 SMF。流程：
1. UDM 签约 APN-OI-REPLACEMENT
2. DNS 上配置 SMF 主机名和 IP 关系
3. MME 用签约 APN-OI-REPLACEMENT 替代 APN-OI
4. MME 使用替换后的域名进行 DNS 查询，获取目标 SMF 地址
5. 用户接入到目标 SMF

**关键 MML 命令（UNC 窗口）**：

```
// 基于 SNSSAIS 选择 SMF
ADD PNFNS: INDEX=1, NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", SST=1, SD="010101";

// 基于 DNN 选择 SMF
ADD PNFDNN: INDEX=1, NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", DNN="huawei.com", PNFNSINDEX=1;

// 基于目标 PLMN 选择 SMF
ADD PNFPLMN: NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", MCC="123", MNC="00";
ADD PNFPLMNRANGE: INDEX=1, NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", QUERYTYPE=START_END, RANGESTART="123000", RANGEEND="123003";

// 基于支持的 PGW 域名信息和接入类型选择 SMF
ADD PNFSMFINFO: NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", PGWFQDN="smf1.cluster1.net2.smf.5gc.mnc000.mcc123.3gppnetwork.org";

// 基于 locality 选择 SMF
ADD NFLOC: NFTYPE=NfAMF, TGTNFTYPE=SMF, LOCTYPE=PREFERRED_LOCALITY;
SET NFDISCPLCY: LOCSELECT=LOCSELECT_DATACENTER;

// 基于 TAI 选择 SMF
ADD PNFTAI: NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", TAI="123001000001";
ADD PNFTAIRANGE: INDEX=1, NFINSTANCEID="a6a61c6f-0d3a-4221-b1da-424eda3ccf67", MCC="123", MNC="00", QUERYTYPE=START_END, RANGESTART="123000", RANGEEND="123003";

// 基于不同用户（群）使用差异化的条件选择 SMF
ADD SMFSELPLCY: SUBRANGE=HOME_USER, SMFLIST=INSTANCEID_PREF;
```

**与带宽控制的关系**：AMF/MME 选择正确的智能 SMF 是带宽保障的前置条件。如果用户接入到非智能 SMF（不支持双 N7 会话），则无法触发智能 PCF 的 QoS 保障分析，整个带宽保障链路将无法建立。

---

## 3. 配置与调测要点

### 3.1 GBR 保障配置要点

1. **先开 License 再配置**：UDC 侧必须先执行 `SET LICENSESWITCH` 开启 LKV8ESTUDC01 等 License 项。
2. **UDN 对接判断**：是否对接 UDN 决定了 CELLCONGESW、CELLCAPVT、CELLPRBVT 的取值。对接且支持预测：ENABLE / 非0；未对接或不支持：DISABLE / 0。
3. **小区容量优先级**：`ADD NRCELLCAPACITY`（小区级）优先于 `SET QOSGUARCOND` 的 NRCELLDFTMBRDL/UL（全局缺省级）。
4. **GBR 门限计算**：NRCELLULGBRTH=40 表示小区 GBR 资源占比上限为 40%，不是绝对带宽值。
5. **CHARGINGID 限制**：异厂商 PCF 场景不支持配置 CHARGINGID 参数。
6. **单会话保障流规格**：`SET NWDAFSOFTPARA: DT=Byte, BYTENUM=5, BYTEVALUE=7` 设置单会话下最大可保障流规格。

### 3.2 Non-GBR 保障配置要点

1. **GUARANTEETYPE=Non-GBR**：ADD APPGROUP 命令必须显式指定保障类型为 Non-GBR。
2. **无 GBR 参数**：Non-GBR 保障不配置 GBRULVALUE/GBRDLVALUE。
3. **MBR 即限速**：MBRULVALUE/MBRDLVALUE 的值即为最大带宽限制，取值通常远小于 GBR 保障的 MBR。
4. **关闭小区容量获取**：Non-GBR 示例中 `SET UDNCTRL: CELLCAPVT=0` 关闭向 UDN 获取小区容量。

### 3.3 智能码率识别配置要点

1. **前提条件**：必须先完成 GBR 保障配置（仅 GBR 保障支持智能码率识别）。
2. **额外 License**：需开启 `LKV8IBRIUDC01`（UDC 侧）和 CloudUDN 侧的"智能码率识别可视"License。
3. **UDG 侧联动**：UDC 侧开通智能码率识别时，UDG 侧需执行 `SET SOFTPARA:DT=BIT,BITNUM=3785,BITVALUE=1` 打开上报瞬时速率开关。
4. **训练时间**：pool 场景下，pool 内各 NWDAF 的训练启动时间（STARTTRAINTIME）建议不重叠。
5. **档位匹配优先级**：应用级（ADD APPBANDMATCHPLY）优先级高于全局级（SET BANDMATCHPOLICY）。
6. **匹配逻辑三档**：FIRST_PRIORITY（智能算法训练）> SECOND_PRIORITY（配置带宽档位）> THIRD_PRIORITY（默认最高档位）。

### 3.4 UDG 侧质差检测配置要点

1. **协议特征库版本**：版本低于 01.0002.1661.01 需要加载，加载后用 DSP SIGNATUREDB 确认。
2. **单位变更注意**：20.13.2.10 版本前后 ADD POLICYCONDITION 命令中速率参数单位从千字节/秒变更为千比特/秒。
3. **抽样率**：`SET RPTGLBPARA: FLOWSAMPLERATE=1000` 表示 100% 抽样。
4. **SSU 老化时间**：会话老化 60 分钟，流表老化 61 秒。

### 3.5 异厂商 PCF 场景配置要点

1. **版本要求**：SMF 需要 UNC 20.15.0 及后续版本支持双 N7 会话。
2. **关闭私有信元**：异厂商 PCF 场景需执行 `SET NWDAFPVTEXT` 关闭 N5 接口私有信元（N5_N23SUBID、N5_CHGID）。
3. **不支持 CHARGINGID**：异厂商 PCF 场景不支持配置 CHARGINGID 参数。

---

## 4. 与带宽控制的关系

### 4.1 GBR 保障 = 带宽下限保证

GBR（Guaranteed Bit Rate）保障确保特定应用获得**不低于 GBR 值的带宽**。在带宽控制场景中：
- GBRULVALUE/GBRDLVALUE 是带宽保障的**下限**
- MBRULVALUE/MBRDLVALUE 是带宽保障的**上限**
- 小区 GBR 门限（NRCELLULGBRTH/NRCELLDLGBRTH）限制了小区整体可分配给保障业务的资源比例，防止保障业务挤占普通业务资源
- 保障触发条件包括小区拥塞（CELLCONGESW）、PRB 利用率（PRBUSAGE）等，确保在资源紧张时优先保障高优先级应用

### 4.2 Non-GBR 保障 = AMBR 限速

Non-GBR 保障本质上是对非保证速率业务的**最大带宽限速**：
- 仅设置 MBR 作为上限，不保证下限
- 适用于对延迟不敏感但需要带宽控制的应用
- 通过 GUARANTEETYPE=Non-GBR 与 GBR 保障区分

### 4.3 智能码率识别 = 差异化带宽

智能码率识别通过 AI 训练动态匹配带宽档位，实现精细化差异化带宽控制：
- 为同一应用配置多个带宽档位（如 1-2M、2-5M、5-10M、10-15M）
- 根据实时码率自动匹配，避免固定 GBR 的资源浪费或不足
- 档位匹配优先级确保最优匹配策略

### 4.4 质差检测 = 保障触发器

UDG 侧的质差检测策略（POLICYCONDITION）是带宽保障的**触发机制**：
- 速率基线（UPLINKAVGRATE）定义了"什么是质差"
- 大流阈值（UPFLOWTHRD/SSUBIGFLOWCTRL 的 VVIPFLOWRATE）定义了"什么流量值得关注"
- 质差上报后触发 NWDAF 分析 -> PCF 策略下发 -> SMF/UPF 执行保障的完整闭环

### 4.5 端到端带宽保障链路

```
应用流量 -> UDG 质差检测 -> UDC(NWDAF) 分析 -> PCF 策略决策 -> SMF 规则下发 -> UPF 执行带宽保障
     |                    |                       |                  |                    |
  POLICYCONDITION     GBR/Non-GBR配置        N23/N5接口         N4接口              QoS执行
  SSUPROTCOLGROUP     智能码率档位           QOS_ANALYSIS       PFCP Session        GBR/MBR限速
```

---

## 5. 关键概念术语

| 术语 | 全称/含义 | 作用 |
|------|-----------|------|
| GBR | Guaranteed Bit Rate，保证比特速率 | 带宽保障的下限值 |
| MBR | Maximum Bit Rate，最大比特速率 | 带宽保障的上限值 |
| Non-GBR | 非保证比特速率业务 | 仅限速不限速下限的保障类型 |
| FQI | 5QI QoS Identifier，QoS 标识 | 标识 QoS 流的 5QI 值，决定 QoS 特性 |
| ARP | Allocation and Retention Priority，分配保留优先级 | 决定资源分配和抢占优先级 |
| NWDAF | Network Data Analytics Function | 网络数据分析功能，重点业务保障的分析大脑 |
| PCF | Policy Control Function | 策略控制功能，下发 QoS 策略 |
| SMF | Session Management Function | 会话管理功能，执行 QoS 规则下发 |
| UPF | User Plane Function | 用户面功能，执行带宽限速/保障 |
| AMF | Access and Mobility Management Function | 接入和移动性管理功能，选择 SMF |
| UDC | Huawei UDC（含 NWDAF 功能） | 华为控制面节点，承载 NWDAF |
| CloudUDN | Huawei CloudUDN（含 NWDAF 数据底座） | 华为用户面数据节点，承载 NWDAF 数据分析 |
| PRB | Physical Resource Block | 物理资源块，衡量无线资源利用率 |
| SAREA_CH | Service Area Change | 服务区域位置变更事件 |
| SCNN_CH | Serving CN Node Change | 服务 CN 节点内的位置变更事件 |
| VVIP | Very Very Important Person | 重点业务保障用户 |
| SSU | Service Insight Unit | 智能板业务分析单元 |
| QoE | Quality of Experience | 用户体验质量 |
| CODETRAINSW | 智能算法训练开关 | 控制是否开启 AI 码率训练 |
| GUARANTEETYPE | 保障类型 | GBR 或 Non-GBR |
| CELLCAPVT | 小区容量有效时长 | 控制是否向 UDN 获取小区容量 |
| CELLCONGESW | 小区拥塞保障条件开关 | 是否将小区拥塞作为发起保障的判断条件 |
| INVGUARPRTIMES | 无效保障质差次数 | PCF 保障成功后 1 分钟内收到多少次质差认为无效 |
| NupfR | UPF 到 UDN 的体验数据上报接口 | 华为私有接口扩展 |

---

## 6. 知识来源

| 序号 | 源文档名称 | 原始路径 |
|------|-----------|----------|
| 1 | 异厂商PCF场景组网与接口 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/组网与接口/异厂商PCF场景组网与接口_95378622.md |
| 2 | 解决方案版本配套要求 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 体验感知解决方案/解决方案版本配套要求_90690558.md |
| 3 | Kafka进行partition重分配 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/CloudUDN侧配置/Kafka进行partition重分配_65827357.md |
| 4 | 配置小区负载预测功能 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/CloudUDN侧配置/配置小区负载预测功能_89149846.md |
| 5 | 开启License开关 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/开启License开关_99140330.md |
| 6 | 配置GBR保障 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置GBR保障_38159968.md |
| 7 | 配置Non-GBR保障 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置Non-GBR保障_78014166.md |
| 8 | 配置智能码率识别功能 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置智能码率识别功能_24013085.md |
| 9 | 配置跨NWDAF服务区域移动 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置跨NWDAF服务区域移动_06323488.md |
| 10 | 配置跨NWDAF服务区域移动（建设初期） | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDC侧配置/配置跨NWDAF服务区域移动（建设初期）_24516677.md |
| 11 | UDG侧配置 | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UDG侧配置_61101881.md |
| 12 | 配置AMF/MME选择SMF/GW-C | output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/5G Core 重点业务保障解决方案/业务部署与调测/初始业务配置/UNC侧配置/配置AMF_MME选择SMF_GW-C_06542597.md |
