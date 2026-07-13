---
id: ConfigurationSolution@apn-ip-typing
type: ConfigurationSolution
name: IP 类型治理
domain: apn-domain
scenario: apn-access
status: draft
---

# IP 类型治理

> UE 获得 IPv4 / IPv6 / 双栈地址的完整配置链路，含 IPv6 承载 / IPv6 Prefix Delegation / 双栈 / 静态地址路由冗余。属于 [APN 接入与会话管理](NetworkScenario@apn-access.md) 场景。编排 UNC 4 + UDG 4 = 8 核心 feature。
>
> **方案角色**：必选（NS DP-4 实现，3 选 1）。与 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md) / [CS-2 鉴权](ConfigurationSolution@apn-auth.md) / [CS-3 隧道](ConfigurationSolution@apn-tunnel.md) 是 **AND 关系**。

## 概览

IP 类型治理是 APN 业务域的"用什么 IP"环节：在地址分配后，UE 获得的 IP 是 IPv4 单栈、IPv6 单栈、还是双栈。本方案覆盖 3 种 IP 类型 + 2 个增强能力（IPv6 承载 / IPv6 PD / 双栈 / 静态地址路由冗余）。

3 维度的 IP 类型决策（来源 [归纳-四维度决策与机制.md §1.1 18 格矩阵](../../../business-graph/APN业务域/归纳-四维度决策与机制.md)）：

| IP 类型 | License（UDG）| License（UNC）| 适用 |
|---|---|---|---|
| **IPv4 单栈** | 无 | 无 | 工控 / IoT / 传统企业（多数场景）|
| **IPv6 单栈** | LKV3G5V6PB01 | WSFD-104001 | 5G 切片 / IoT 演进 |
| **IPv4v6 双栈** | LKV3G5VDSA01 + LKV3G5V6PB01 | WSFD-104002 | 家庭 CPE / VoLTE |

License 依赖链（来源 [归纳-四维度决策与机制.md §1.4 IPv6 承载依赖链](../../../business-graph/APN业务域/归纳-四维度决策与机制.md)）：
```
[GWFD-020401 IPv6 承载上下文] LKV3G5V6PB01
        │（承载基础设施，必装）
        ▼
[GWFD-020403 IPv4v6 双栈接入] LKV3G5VDSA01
        │（双栈能力使能层）
        ▼
[GWFD-020406 IPv6 Prefix Delegation] LKV3G5P6PD01（V6PREFIXLENGTH<64 时触发）
```

## 配置与协同

### 特性关系矩阵

| 特性 | 角色 | 必配? | 关系说明 |
|---|---|---|---|
| [UNC IPv6 承载上下文 2-00018](task/UNC/20.15.2/2-00018.md) | 核心（IPv6 承载）| 必选（选 IPv6 / 双栈时）| IPv6 承载管理基础；独立于地址池机制 |
| [UNC IPv6 前缀代理 2-00019](task/UNC/20.15.2/2-00019.md) | 核心（IPv6 PD）| 必选（V6PREFIXLENGTH<64 时）| 前缀长度 < 64 触发 PD 模式 |
| [UNC IPv4v6 双栈 2-00017](task/UNC/20.15.2/2-00017.md) | 核心（双栈）| 必选（选双栈时）| 双栈能力使能层；4G/2-3G 需 `SET SMFUNC DUALFLAG=YES` |
| [UNC 静态地址用户路由冗余 2-00023](task/UNC/20.15.2/2-00023.md) | 核心（路由冗余）| 必选（IPv4 静态场景）| 主备 UPF 自动切换；Full-Mesh 组网 |
| [UDG IPv6 承载 2-00041](task/UDG/20.15.2/2-00041.md) | 跨网元对端（IPv6）| 必选（IPv6 / 双栈）| U 面对称 |
| [UDG IPv4v6 双栈 2-00043](task/UDG/20.15.2/2-00043.md) | 跨网元对端（双栈）| 必选（双栈时）| U 面对称 |
| [UDG IPv6 Prefix Delegation 2-00046](task/UDG/20.15.2/2-00046.md) | 跨网元对端（IPv6 PD）| 必选（V6PREFIXLENGTH<64）| U 面对称 |
| [UDG 静态地址路由冗余 2-00007](task/UDG/20.15.2/2-00007.md) | 跨网元对端（路由冗余）| 必选（IPv4 静态场景）| U 面对称 |
| **[UNC 会话管理 2-00014](task/UNC/20.15.2/2-00014.md)** | **基础（依赖前提）** | **必配** | IP 类型与 PDU 会话绑定——**配 IP 类型时已隐含** |
| **[UNC UPF 选择 2-00033](task/UNC/20.15.2/2-00033.md)** | **基础（依赖前提）** | **必配** | 主备 UPF 路由冗余需要 UPF 选择决策 |
| **[UNC 用户数据管理 2-00036](task/UNC/20.15.2/2-00036.md)** | **基础（依赖前提）** | **必选** | UDM 签约 IP 类型 + Prefix Delegation |

各特性未变化的配置走其**标准配置方法**（见各 feature task），以下仅说明本方案的**特性级变种/排除项**。

### UNC 控制面：IP 类型（[2-00018](task/UNC/20.15.2/2-00018.md) / [2-00019](task/UNC/20.15.2/2-00019.md) / [2-00017](task/UNC/20.15.2/2-00017.md) / [2-00023](task/UNC/20.15.2/2-00023.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**：

- **IPv6 承载**（[2-00018](task/UNC/20.15.2/2-00018.md)）：`SET SMFUNC` 配 IPv6 承载管理 + APN 配 IPv6 capability
- **IPv6 PD**（[2-00019](task/UNC/20.15.2/2-00019.md)）：`SET APNPD` 配 V6PREFIXLENGTH<64 触发 PD
- **双栈**（[2-00017](task/UNC/20.15.2/2-00017.md)）：4G/2-3G 需 `SET SMFUNC DUALFLAG=YES`；5G 由 UDM 签约驱动
- **静态地址路由冗余**（[2-00023](task/UNC/20.15.2/2-00023.md)）：11 步 UPF 主备链路（ADDRPOOL+ADDRPOOLGRP+POOLBINDAPN+UPNODE+ADDRUPGROUP+UPFBINDGRP+POOLGRPMAP）
- **排除** `SET NGMMPROCTRL`（5G NGMM 流程控制不属 IP 类型）

### UDG 用户面：U 面对称配置（[2-00041](task/UDG/20.15.2/2-00041.md) / [2-00043](task/UDG/20.15.2/2-00043.md) / [2-00046](task/UDG/20.15.2/2-00046.md) / [2-00007](task/UDG/20.15.2/2-00007.md)）

走标准配置方法（见 feature task），但有以下**变种/排除**：

- **IPv6 承载**（[2-00041](task/UDG/20.15.2/2-00041.md)）：UPF 配 IPv6 转发
- **双栈**（[2-00043](task/UDG/20.15.2/2-00043.md)）：UPF 配 IPv4+IPv6 双协议栈
- **IPv6 PD**（[2-00046](task/UDG/20.15.2/2-00046.md)）：UPF 配 PD 客户端
- **静态地址路由冗余**（[2-00007](task/UDG/20.15.2/2-00007.md)）：UPF 主备自动切换
- **排除** `MOD N4CHGMSGCTRL`（N4 PFCP 消息控制不属 IP 类型）

### 跨网元/跨特性协同

- **顺序**：
  1. UNC 侧 IP 类型基础就绪（IPv6 承载 / 双栈使能 / 静态地址主备 UPF）
  2. UNC 触发 UDG 侧对称配置
  3. UE 触发时按 PDU Session Type（IPv4/IPv6/IPv4v6）走对应路径
- **License 完整性**（critical）：IPv6 / 双栈 License 链必须完整
- **与其他 CS 的协同**（AND 关系）：
  - 与 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md)：IP 类型决定地址池类型（IPv4/IPv6 SECTION）
  - 与 [CS-2 鉴权](ConfigurationSolution@apn-auth.md)：4 制式鉴权按 IP 类型配不同协议
  - 与 [CS-3 隧道](ConfigurationSolution@apn-tunnel.md)：双栈时隧道需 IPv4+IPv6 双协议栈支持

> **方案优先复用已有 compound**：[1-00024](task/UNC/20.15.2/1-00024.md) / [1-00029](task/UNC/20.15.2/1-00029.md)，**不新建 atom/compound**。

## 决策点

### DP-1：IP 类型（3 选 1，必选）

| 选项 | UNC | UDG | License | 适用 |
|---|---|---|---|---|
| **IPv4 单栈** | 不启 IPv6 / 双栈 | 不启 IPv6 / 双栈 | 无 | 工控 / IoT / 传统企业 |
| **IPv6 单栈** | [2-00018](task/UNC/20.15.2/2-00018.md) | [2-00041](task/UDG/20.15.2/2-00041.md) | LKV3G5V6PB01 | 5G 切片 / IoT 演进 |
| **IPv4v6 双栈** | [2-00017](task/UNC/20.15.2/2-00017.md) | [2-00043](task/UDG/20.15.2/2-00043.md) | LKV3G5VDSA01 + LKV3G5V6PB01 | 家庭 CPE / VoLTE |

## 约束

- **3 选 1 IP 类型**（critical）：同一 APN 不可同时配 2 种 IP 类型
- **License 完整性**（critical）：IPv6 / 双栈 License 必须完整（链式依赖）
- **前缀长度 64 是 PD 分水岭**（critical）：V6PREFIXLENGTH<64 触发 PD 模式
- **与其他 CS 协同**（critical）：与 [CS-1 地址分配](ConfigurationSolution@apn-addr-allocation.md) 严格对应（IP 类型决定地址池类型）
- **License 编号核查**（critical）：必须从原始产品文档交叉验证（**不可按命名规律推断**）

## 关联

- **上游场景**：[NS APN 接入与会话管理](NetworkScenario@apn-access.md)
- **下游（同场景其他 CS，AND 关系）**：
  - [CS 地址分配](ConfigurationSolution@apn-addr-allocation.md) — IP 类型决定地址池类型
  - [CS 鉴权 AAA](ConfigurationSolution@apn-auth.md)
  - [CS 隧道接入](ConfigurationSolution@apn-tunnel.md) — 双栈时隧道需双协议栈
- **编排特性**：见上文"特性关系矩阵"段（8 核心 + 3 基础 = 11 feature）
- **共享骨架**：[1-00024 APN 接入域基础设施](task/UNC/20.15.2/1-00024.md) / [1-00029 OSPF 路由发布](task/UNC/20.15.2/1-00029.md)
- **业务层 SOP**：[业务层级构建SOP.md](../业务层级构建SOP.md) §4.2 CS 模板
- **APN 域专题知识**：[归纳-四维度决策与机制.md §1.1 18 格矩阵 + §1.4 IPv6 承载依赖链](../../../business-graph/APN业务域/归纳-四维度决策与机制.md)
- **证据**（原始产品文档）：[WSFD-104001 IPv6 承载 md](assets/evidence/UNC/20.15.2/WSFD-104001/) / [WSFD-104002 双栈 md](assets/evidence/UNC/20.15.2/WSFD-104002/) / [WSFD-104004 IPv6 PD md](assets/evidence/UNC/20.15.2/WSFD-104004/) / [WSFD-107021 静态地址路由冗余 md](assets/evidence/UNC/20.15.2/WSFD-107021/) + UDG 对应
