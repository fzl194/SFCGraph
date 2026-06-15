# Batch 02: 一望5G/PCC QoS管理机制 知识草稿

## 来源文件清单

| # | 文件 | UNC路径 |
|---|------|---------|
| 1 | 5G PCC策略—E2E QoS管理机制_32945129 | 5G基础知识/一望5G/5G Core业务解决方案解读：5G PCC策略之E2E QoS管理机制/ |
| 2 | SM策略之QoS的管理机制_32686211 | 同上/5G PCC策略—E2E QoS管理机制/ |
| 3 | SM策略之QoS的下发与执行_33030755 | 同上/SM策略之QoS的管理机制/ |
| 4 | SMF发起的策略更新_85720414 | 同上/SM策略之QoS的更新、下发与执行/ |
| 5 | PCF发起的策略更新_86168492 | 同上/SM策略之QoS的更新、下发与执行/ |
| 6 | AMF功能演进介绍_32945513 | 5G Core业务解决方案解读：5G PCC策略之E2E AM策略实施机制/ (弱相关) |
| 7 | PCF发起的策略更新_85720808 | 同上 (弱相关) |

---

## 一、PCC策略体系

### K24: PCC策略分类
> 来源: 5G PCC策略—E2E QoS管理机制_32945129

**原理知识**

PCC（Policy and Charging Control）策略分3大类：

| 策略类型 | 关键参数 | 功能描述 | 策略下发/执行 |
|---------|---------|---------|-------------|
| SM策略 | QoS Flow级：5QI、ARP、GFBR/MFBR、RQA、**计费参数**等；会话级：Session-AMBR | QoS带宽控制、**计费控制**、短信服务通知、重定向等 | PCF→SMF |
| AM策略(5G新增) | SAR(服务区限制)、RFSP(无线频率选择优先级) | UE允许/禁止接入的区域、无线资源管理 | PCF→AMF/RAN/UE |
| UE策略(5G新增) | ANDSP(选网策略)、URSP(路由选择策略) | 辅助UE选择Non-3GPP接入、路由选择 | PCF→UE |

**SM策略与计费直接相关**：包含计费参数（计费方式、Rating Group等），AM/UE策略与计费无直接关系。

### K25: SM策略中QoS与计费的关联
> 来源: SM策略之QoS的管理机制_32686211

**原理知识**

SM策略的两个维度：
- **Session级QoS策略**：以PDU Session为度量单位，1个PDU Session包含的QoS策略
- **业务级QoS策略**：以用户访问的业务为度量单位，1个业务包含的QoS策略

关系：一个Session级QoS策略可能包含多个业务级QoS策略。

**信令面 vs 数据面：**
- 信令面：将QoS Flow建立起来，侧重QoS策略如何**生成和下发**
- 数据面：基于已建好的QoS Flow做业务，侧重QoS策略如何**实施**

### K26: QoS策略生成机制
> 来源: SM策略之QoS的管理机制_32686211

**方案设计知识**

QoS策略生成流程：
1. 用户上线 → 从UDM获取签约数据（Session-AMBR、ARP、5QI等）
2. 经SMF → 请求消息送达PCF
3. PCF根据切片信息、位置信息等做决策 → **生成QoS策略**（不存在与UDM/SMF协商的过程）
4. PCF将策略下发给SMF → SMF本地安装

**关键差异：PCF vs SMF本地策略**
- PCF：更精细化的策略管控，能根据用户位置、等级、时间段、**配额状态**、节假日等定制
- SMF本地：无PCF或PCF异常时的备选方案

---

## 二、QoS策略下发与执行

### K27: SMF在QoS策略下发中的两个核心职责
> 来源: SM策略之QoS的下发与执行_33030755

**原理知识**

SMF收到PCF下发的QoS参数后需做两件事：
1. **建立QoS Flow**：为数据流传输提供通道，不同通路提供差异化QoS保障
2. **参数映射**：将PCF参数映射为RAN/UPF/UE可识别的参数

**两级映射机制：**
- 数据包 → QoS Flow：通过PFS(Packet Filter Set)对业务识别分类，映射到对应QoS Flow
- QoS Flow → Radio Bearer：由RAN决策调度，RAN根据资源情况动态安排

5G vs 4G映射差异：
- 4G：1:1:1确定关系（城市道路→高速路→城市道路）
- 5G：N:1映射，根据实际"高速路拥堵"情况动态调整，高效利用空口资源

### K28: GBR与Non-GBR QoS的下发差异
> 来源: SM策略之QoS的下发与执行_33030755

**原理知识**

**GBR QoS场景：**
- SMF在PDU Session建立/修改时向UPF/RAN/UE发送QoS Flow信息
- RAN和UE根据收到的信息进行QoS Flow处理

**Non-GBR QoS场景（5G增强）：**
- 新引入**Reflective QoS**机制：UE可自行推导上行QoS Rule
- PCF下发的策略中可以仅有下行流，UE通过反射推导上行
- 节省PDU Session修改信令开销

**RQA vs RQI概念：**
- RQA：定义QoS Flow的反射"属性"，该Flow上的数据包"可能"进行反射
- RQI：定义数据包的反射"指示"，仅对具备RQA的Flow上携带RQI的数据包进行反射

### K29: 传输层DSCP映射
> 来源: SM策略之QoS的下发与执行_33030755

**配置知识**

- 传输层通过端到端DSCP值提供不同SLA保障
- 上行DSCP映射由基站标记，下行DSCP值由核心网标记
- 网络侧可针对不同接口（N3/N6/N9）配置5QI+ARP到DSCP映射的规则

---

## 三、策略更新机制

### K30: SMF发起的策略更新（配额状态触发）
> 来源: SMF发起的策略更新_85720414

**方案设计知识**

**触发条件：**
- PDU Session处于在线状态
- PCF在PDU Session建立时**订阅**了需要SMF上报的变更事件

**可订阅的变更事件包括：**
- 用户位置变更
- UDM发起的Session-AMBR/5QI/ARP变更
- **用户配额使用状态变更**

**更新流程：**
1. 订阅事件发生 → SMF将变更点通过Npcf_SMPolicyControl_Update Request发送给PCF
2. PCF结合UDM签约的全局QoS策略数据 → 匹配条件 → 生成新QoS策略
3. PCF通过Npcf_SMPolicyControl_Update Response通知SMF → 删除旧策略，安装新策略

**实际场景：无限流量套餐限速**
- 20GB以内：10Mbps高速带宽
- 超过20GB：限速至1Mbps
- 配额状态变更 → SMF上报 → PCF匹配新条件 → 下发限速策略

### K31: PCF发起的策略更新（用户属性触发）
> 来源: PCF发起的策略更新_86168492

**方案设计知识**

**触发条件：**
- PDU Session在线
- PCF侧触发的签约数据变更（如用户状态、等级等属性变更）
- 可以从**营帐侧**修改签约数据触发新规则生成

**更新流程：**
1. PCF侧签约数据更新 → 重新匹配规则生成的"条件"
2. 匹配成功 → 通过Npcf_SMPolicyControl_UpdateNotify Request主动下发给SMF
3. SMF删除旧策略，安装新策略

**与SMF发起的区别：**
- SMF发起：SMF感知变更（配额/位置等）→ 上报PCF → PCF决策
- PCF发起：PCF自身签约数据变更 → 直接下发新策略

---

## 知识统计

| 类别 | 数量 |
|------|------|
| 原理知识 | 6 (K24-K28) |
| 方案设计知识 | 3 (K26, K30, K31) |
| 配置知识 | 1 (K29) |
| **合计** | **8条** |
