---
id: ConfigurationSolution@apn-auth
type: ConfigurationSolution
name: 鉴权 AAA
domain: apn-domain
scenario: apn-access
status: draft
---

# 鉴权 AAA

> 对 UE 接入进行鉴权的完整配置链路，覆盖 4 种 AUTHMODE 鉴权方式（TRANS_NON_AUTH / TRANS_AUTH / NON_TRANS / LOC_AUTH）+ 配套的 Radius 服务器配置 + 终端二次鉴权 + Radius 抄送。属于 [APN 接入与会话管理](NetworkScenario@apn-access.md) 场景。编排 UNC 5 核心 feature。
>
> **方案角色**：必选（NS DP-2 实现，4 选 1）。与 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md) / [CS-3 隧道](ConfigurationSolution@apn-tunnel.md) / [CS-4 IP 类型](ConfigurationSolution@apn-ip-typing.md) 是 **AND 关系**。

## 概览

鉴权是 APN 业务域的接入第二步：在地址分配前，先确认 UE 身份合法性。本方案覆盖 4 种鉴权接入方式（4 选 1）+ Radius 服务器组配置 + 终端二次鉴权（UPF 中转 Radius）+ Radius 抄送（AAA 消息 Carbon-copy）。

4 维度的鉴权决策（来源 [APN配置树.md §3 鉴权计费信息实例化](../../../business-graph/APN业务域/APN配置树.md)）：

| AUTHMODE | Radius 鉴权接入 [2-00024](task/UNC/20.15.2/2-00024.md) | Radius 功能 [2-00025](task/UNC/20.15.2/2-00025.md) | 适用 |
|---|---|---|---|
| **TRANS_NON_AUTH**（透明接入）| ✅ 必选 | ❌ 不选 | HSS/UDM 已完成鉴权（普通 Internet 访问）|
| **TRANS_AUTH**（透明鉴权）| ✅ 必选 | ✅ 必选 | 网络侧用户名密码鉴权 |
| **NON_TRANS**（不透明接入）| ✅ 必选 | ✅ 必选 | 用户 PCO 携带用户名密码，企业 AAA 二次鉴权 |
| **LOC_AUTH**（本地鉴权）| ✅ 必选 | ❌ 不选 | UNC 本地配置用户名密码，无 AAA server |

**额外能力**：
- **终端二次鉴权**（[2-00027](task/UNC/20.15.2/2-00027.md)）：UPF 中转 Radius 链路（PRIFLAG=CARBON_COPY）
- **Radius 抄送**（[2-00028](task/UNC/20.15.2/2-00028.md)）：AAA 消息 Carbon-copy 到抄送服务器
- **4 制式鉴权**（[2-00026](task/UNC/20.15.2/2-00026.md)）：2G/3G/4G/5G NAS 信令级鉴权（独立于 Radius 链路）

跨网元协同：纯 UNC 域（鉴权是 C 面主导，UDG 旁路）。SMF/SGSN 触发鉴权 → Radius 链路（经 Diameter/Gx/Gy）→ 鉴权通过后触发地址分配。

## 配置与协同

### 特性关系矩阵

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UNC Radius 鉴权接入 2-00024](task/UNC/20.15.2/2-00024.md) | 核心（方案主体）| 必配 | ACCESSMODE 4 选 1（NS DP-2）；4 种方式都必启用本命令 |
| [UNC Radius 功能 2-00025](task/UNC/20.15.2/2-00025.md) | 维度增强（必选/可选）| 必选（仅 TRANS_AUTH/NON_TRANS）| 配 Radius 服务器组 + 9 链路；TRANS_NON_AUTH/LOC_AUTH 不启 |
| [UNC 鉴权功能 4 制式 2-00026](task/UNC/20.15.2/2-00026.md) | 核心（2G/3G/4G/5G NAS 级）| 必配 | 4 制式鉴权（2G/3G/4G/5G NAS 信令级）；与 Radius 链路并行 |
| [UNC 终端二次鉴权 2-00027](task/UNC/20.15.2/2-00027.md) | 维度增强（可选）| 可选 | UPF 中转 Radius 链路（PRIFLAG=CARBON_COPY）；按需启用 |
| [UNC Radius 抄送 2-00028](task/UNC/20.15.2/2-00028.md) | 维度增强（可选）| 可选 | AAA 消息 Carbon-copy 到抄送服务器；审计/合规场景 |
| **[UNC 会话管理 2-00014](task/UNC/20.15.2/2-00014.md)** | **基础（依赖前提）** | **必配** | PDU/PDN/PDP 会话宿主；鉴权结果写入会话上下文——**配鉴权时已隐含** |
| **[UNC 接入控制 2-00034](task/UNC/20.15.2/2-00034.md)** | **基础（依赖前提）** | **必配（License LKV2USRAC01）** | 接入控制决策；未通过不触发鉴权——配置不重叠 |
| **[UNC UPF 选择 2-00033](task/UNC/20.15.2/2-00033.md)** | **基础（依赖前提）** | **必配** | 终端二次鉴权涉及 UPF 中转；UPF 选择与之耦合 |

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**。

### UNC 控制面：Radius 鉴权接入（[2-00024](task/UNC/20.15.2/2-00024.md) + [2-00025](task/UNC/20.15.2/2-00025.md) + [2-00028](task/UNC/20.15.2/2-00028.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**：

- **ACCESSMODE 4 选 1**（NS DP-2）：
  - `SET APNAUTHATTR: APN="xxx", ACCESSMODE=TRANS_NON_AUTH`（普通 Internet 访问）
  - `SET APNAUTHATTR: APN="xxx", ACCESSMODE=TRANS_AUTH`（网络侧配置用户名密码）
  - `SET APNAUTHATTR: APN="xxx", ACCESSMODE=NON_TRANS`（企业 AAA 二次鉴权）
  - `SET APNAUTHATTR: APN="xxx", ACCESSMODE=LOC_AUTH`（UNC 本地鉴权）
- **Radius 服务器组**（[2-00025](task/UNC/20.15.2/2-00025.md)）：9 链路（主备 + 负荷分担）——仅 TRANS_AUTH/NON_TRANS 必配
- **Radius 抄送**（[2-00028](task/UNC/20.15.2/2-00028.md)）：ADD RDSSVRGRP + RDSSVR + APNRDSSVRGRP（PRIFLAG=CARBON_COPY）——可选
- **4 制式鉴权**（[2-00026](task/UNC/20.15.2/2-00026.md)）：SET NGMMPROCTRL（5G NGMM）/ SET MMECOMMONCTRL（4G S1）/ SET SGSNCOMMONCTRL（3G/2G）——按接入制式配
- **排除** `ADD ABMIP`（不属鉴权范畴）
- **排除** `MOD PUCTRL`（不属鉴权范畴）

### 跨网元/跨特性协同

- **顺序**：
  1. UNC 侧 APN 基础信息（[1-00024](task/UNC/20.15.2/1-00024.md)）先就绪
  2. UNC 侧鉴权配置（ACCESSMODE + Radius 服务器组）就绪
  3. UE 附着触发鉴权：N1 NAS Authentication Request（5G）/ S6a Authentication Information Request（4G）
  4. SMF/SGSN 触发 Radius 链路（经 Diameter/Gx/Gy）
  5. 鉴权通过后触发 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md)
- **与其他 CS 的协同**（AND 关系）：
  - 与 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md)：Radius 下发模式时，Radius 链路必须先就绪
  - 与 [CS-3 隧道](ConfigurationSolution@apn-tunnel.md)：企业 AAA 模式常配合 IPSec/L2TP 隧道
  - 与 [CS-4 IP 类型](ConfigurationSolution@apn-ip-typing.md)：4 制式鉴权按 IP 类型配不同协议
- **License 链**：接入控制 [2-00034](task/UNC/20.15.2/2-00034.md) 必开 LKV2USRAC01

> **方案优先复用已有 compound**：[1-00024](task/UNC/20.15.2/1-00024.md) / [1-00025](task/UNC/20.15.2/1-00025.md) / [1-00027](task/UNC/20.15.2/1-00027.md)，**不新建 atom/compound**。

## 决策点

### DP-1：鉴权方式（4 选 1，必选）

| 选项 | ACCESSMODE | Radius 服务器组 | 适用 |
|---|---|---|---|
| **TRANS_NON_AUTH** | TRANS_NON_AUTH | 不配 | 普通 Internet 访问，HSS/UDM 已完成鉴权 |
| **TRANS_AUTH** | TRANS_AUTH | 必配 | 网络侧配置用户名密码鉴权 |
| **NON_TRANS** | NON_TRANS | 必配 | 用户 PCO 携带，企业 AAA 二次鉴权 |
| **LOC_AUTH** | LOC_AUTH | 不配 | UNC 本地用户名密码，无 AAA server |

## 约束

- **4 选 1 ACCESSMODE**（critical）：同一 APN 不可同时配 2 种方式
- **Radius 服务器组必选性**（critical）：TRANS_AUTH/NON_TRANS 必须配 Radius 完整
- **鉴权后必触发地址分配**（critical）：鉴权失败时不触发地址分配
- **License 完整性**（critical）：接入控制 LKV2USRAC01 必开
- **跨域协同**（critical）：与 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md) 严格顺序——鉴权失败时地址分配不发生

## 关联

- **上游场景**：[NS APN 接入与会话管理](NetworkScenario@apn-access.md) — 本 CS 所属场景
- **下游（同场景其他 CS，AND 关系）**：
  - [CS 地址分配](ConfigurationSolution@apn-addr-allocation.md) — NS DP-1（鉴权后触发）
  - [CS 隧道接入](ConfigurationSolution@apn-tunnel.md) — NS DP-3
  - [CS IP 类型治理](ConfigurationSolution@apn-ip-typing.md) — NS DP-4
- **编排特性**：见上文"特性关系矩阵"段（5 核心 + 3 基础 = 8 feature）
- **共享骨架**：[1-00024 APN 接入域基础设施](task/UNC/20.15.2/1-00024.md) / [1-00025 Radius 完整骨架](task/UNC/20.15.2/1-00025.md) / [1-00027 终端二次鉴权骨架](task/UNC/20.15.2/1-00027.md)
- **业务层 SOP**：[业务层级构建SOP.md](../业务层级构建SOP.md) §4.2 CS 模板
- **APN 域专题知识**：[APN配置树.md §3 鉴权计费信息实例化](../../../business-graph/APN业务域/APN配置树.md) / [归纳-四维度决策与机制.md §2 鉴权维度](../../../business-graph/APN业务域/归纳-四维度决策与机制.md)
- **证据**（原始产品文档）：[WSFD-011305 Radius 鉴权接入 md](assets/evidence/UNC/20.15.2/WSFD-011305/) / [WSFD-011306 Radius 功能 md](assets/evidence/UNC/20.15.2/WSFD-011306/) / [WSFD-010301 鉴权功能 4 制式 md](assets/evidence/UNC/20.15.2/WSFD-010301/) / [WSFD-108007 终端二次鉴权 md](assets/evidence/UNC/20.15.2/WSFD-108007/) / [WSFD-011307 Radius 抄送 md](assets/evidence/UNC/20.15.2/WSFD-011307/)
