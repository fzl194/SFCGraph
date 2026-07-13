# APN 业务域构建审计报告

> **报告日期**：2026-07-13
> **构建范围**：APN 业务域（独立 BD）— 1 BD + 1 NS + 4 CS = 6 个 md
> **构建依据**：[业务层级构建SOP.md §0-§8](../../../business/业务层级构建SOP.md) + [业务层级wiki审视流程.md](../../../business/业务层级wiki审视流程.md)
> **前置门**：通过（24 UNC + 13 UDG = 37 feature 全建；R1-R6 critical = 0）

---

## 一、产物清单

| 层级 | ID | 文件 | 行数 | 章节（严格按 SOP §4.2）|
|---|---|---|---|---|
| **BD** | `BusinessDomain@apn-domain` | [BusinessDomain@apn-domain.md](BusinessDomain@apn-domain.md) | 58 | 概览 + 范围与边界 + 约束 + 关联 |
| **NS** | `NetworkScenario@apn-access` | [NetworkScenario@apn-access.md](NetworkScenario@apn-access.md) | 108 | 概览 + 边界 + 决策点 + 关联 |
| **CS-1** | `ConfigurationSolution@apn-addr-allocation`（核心·必选）| [ConfigurationSolution@apn-addr-allocation.md](ConfigurationSolution@apn-addr-allocation.md) | 185 | 概览 + 配置与协同 + 决策点 + 约束 + 关联 |
| **CS-2** | `ConfigurationSolution@apn-auth`（必选 1）| [ConfigurationSolution@apn-auth.md](ConfigurationSolution@apn-auth.md) | 114 | 概览 + 配置与协同 + 决策点 + 约束 + 关联 |
| **CS-3** | `ConfigurationSolution@apn-tunnel`（可选，VPN 直通不启）| [ConfigurationSolution@apn-tunnel.md](ConfigurationSolution@apn-tunnel.md) | 129 | 概览 + 配置与协同 + 决策点 + 约束 + 关联 |
| **CS-4** | `ConfigurationSolution@apn-ip-typing`（必选 1）| [ConfigurationSolution@apn-ip-typing.md](ConfigurationSolution@apn-ip-typing.md) | 122 | 概览 + 配置与协同 + 决策点 + 约束 + 关联 |
| **合计** | | | **716** | **100% SOP §4.2 模板** |

外加：
- `assets/business/index.md` 已加 BD 段 + NS 段 + CS 段
- 24 UNC + 13 UDG = 37 feature task md「## 关联」段已追加"被引用于"行

## 二、SOP §7 验收清单

- [x] **CS 1 md（两段式 ID）**：4 个 CS 全部 `ConfigurationSolution@apn-xxx`
- [x] **前置门通过**：涉及 feature task（UDG+UNC）全建完（Lint R6 critical=0）
- [x] **CS 向下引用 feature/compound/atom task 全有效**：4 CS 引用 37 feature + 3 共享骨架 compound
- [x] **方案特有额外步骤**：本域不需新建（所有必需 task 已建，含本次会话 #46-#51 修复）
- [x] **CS 决策点影响表完整**：CS-1 有 3 个 DP / CS-2/3/4 各有 1 个 DP
- [x] **约束 severity 标注**：CS-1 有 10 条约束（critical/warning）+ BD 有 5 条 + CS-2/3/4 各有 4-5 条
- [x] **证据 markdown 链接列出**（SOP §6）：每个 CS「关联」段都列了对应 evidence 路径
- [x] **双向链接闭环**：37 个 feature task 全部追加"被引用于"行
- [x] **`assets/business/index.md` 同步**：BD/NS/CS 段加 APN 域
- [x] **叙述式（无字段填表）**：所有 6 md 用散文段落，不用旧三层图谱字段
- [x] **跨网元引用全路径**：UDG/UNC task 用资产根路径（`task/{UDG,UNC}/20.15.2/2-XXXXX.md`）
- [x] **License 编号须原始证据交叉验证**（SOP §6 硬约束）：CS 约束段明确说明
- [x] **CS 间关系明确 AND（不是 4 选 1）**：BD 约束 + NS 决策点 + 4 CS「关联」段都说明

## 三、CS 间关系（核心洞察）

按 SOP §4.1 特性关系矩阵的 5 类关系重新设计：

| CS | 角色 | 必配? | 选 1 维度 |
|---|---|---|---|
| **CS-1 地址分配** | 核心（必选）| ✓ 任何 APN 必有 | 6 种分配方式 × 3 种 IP 类型 = 18 格 |
| **CS-2 鉴权 AAA** | 维度增强（必选 1）| ✓ 4 选 1 | 4 种 AUTHMODE |
| **CS-3 隧道接入** | 维度增强（可选）| 5 选 1；**VPN 直通 = 不启本 CS** | 5 种接入方式 |
| **CS-4 IP 类型治理** | 维度增强（必选 1）| ✓ 3 选 1 | IPv4 / IPv6 / 双栈 |

**4 CS 在 APN 完整配置中是 AND 关系**——一个完整 APN 实例通常同时需要 4 个 CS（CS-1 必选核心 + CS-2 必选维度增强 + CS-3 按需 + CS-4 必选维度增强），**不是 NS 决策点"4 选 1"互斥**。

## 四、特性分配核对（37 feature 100% 覆盖）

| CS | 核心 feature 数 | 跨网元对端 | 基础（依赖前提）|
|---|---|---|---|
| **CS-1 地址分配** | 5 UNC + 6 UDG = 11 | UDG 4 子方式 | 2-00014/32/33/34/35/36/37 |
| **CS-2 鉴权 AAA** | 5 UNC = 5 | 无 | 2-00014/33/34 |
| **CS-3 隧道接入** | 4 UNC + 4 UDG = 8 | UDG IPSec 对端 | 2-00014/33 |
| **CS-4 IP 类型治理** | 4 UNC + 4 UDG = 8 | UDG IPv6/双栈/PD | 2-00014/33/36 |
| **跨 CS 散矩阵** | | | 2-00014/32/33/34/35/36/37 |

**4 CS 核心 = 11+5+8+8 = 32 + 5 基础 = 37 feature 全分配**。

## 五、已充分引用的已有文件

每个 md 都引用：
- ✅ [APN配置树.md](../../../business-graph/APN业务域/APN配置树.md)（4 大配置组 + 实例化规则）
- ✅ [归纳-四维度决策与机制.md](../../../business-graph/APN业务域/归纳-四维度决策与机制.md)（4 维度横向归纳 + 18 格矩阵 + License 链）
- ✅ [归纳-APN底座三维度.md](../../../business-graph/APN业务域/归纳-APN底座三维度.md)（3 底座支撑）
- ✅ [cross-topic-analysis.md](../../../business-graph/APN业务域/cross-topic-analysis.md)
- ✅ [业务层级构建SOP.md](../../../business/业务层级构建SOP.md) + [业务层级wiki审视流程.md](../../../business/业务层级wiki审视流程.md)
- ✅ 范本（[业务感知域融合计费 CS](../business-awareness/charging/ConfigurationSolution@charging-converged.md)）
- ✅ 37 个 feature task md（带 .md 全路径）
- ✅ 3 个共享骨架 compound
- ✅ evidence 文档路径（用 markdown 链接，不直接搬内容）

## 六、章节严格度

按 SOP §4.2 模板逐项对照：

| 文件 | SOP §4.2 模板 | 实际章节（严格匹配）|
|---|---|---|
| BD | 概览 + 范围与边界 + 决策点(可选) + 约束(可选) + 关联 | ✓ 概览 + 范围与边界 + 约束 + 关联（域级决策罕见，未加决策点段）|
| NS | 概览 + 边界 + 决策点 + 约束(可选) + 关联 | ✓ 概览 + 边界 + 决策点 + 关联 |
| CS | 概览 + 配置与协同 + 决策点 + 约束 + 关联 | ✓ 概览 + 配置与协同 + 决策点 + 约束 + 关联（4 CS 全一致）|

**未在 SOP §4.2 模板中的章节（已删除）**：
- ❌ "Agent 接手指南"——SOP 模板中没有，删除
- ❌ 拆分的"证据 / 知识来源 / 范本" 段——按 SOP §6 "证据在「关联」段以 markdown 链接列出"——全部并入"关联"段

**允许的扩展（仍按 SOP 严格度）**：
- NS 决策点段内含"完整 APN 方案示例"小节（决策点表的扩展内容，仍在"## 决策点"段内）
- CS 概览中含结构化展示（4 维度的地址分配决策等，仍是叙述式散文，非字段表格）

## 七、Lint 复查

- **UNC 域**：critical=0（197 R6 info 已标 R1.5 待核，合规）
- **UDG 域**：critical=0（139 R6 info 已标 R1.5 待核，合规）
- **本次双回填**（37 feature task 追加"被引用于"行）**未引入任何新违例**

## 八、已知限制与后续建议

1. **evidence md 未实际拷贝**：按 SOP §6 "在「关联」段以 markdown 链接列出"——已在 CS 关联段用 markdown 路径引用 `assets/evidence/{UDG,UNC}/20.15.2/{WSFD,GWFD,IPFD}-xxxxx/`，未做物理文件拷贝。**如需自包含剥离**，可后续按需 cp（不在本次范围）
2. **#40 阶段 G 待办**：APN 域 R6 info 中 13 个真实未登记命令（ADD L2TPGROUP / ADD NGPLMN / DSP NPNODE 等 7 个真未实现 + 6 个笔误已修）——属 #40 P1 后续专项
3. **网元对接业务域待建**：APN 域 BD 边界划定中提到"网元对接业务域（N4 PFCP 偶联 / Diameter / SBI）"——但该 BD 还未建，APN 域已建好对它的引用（按 [BusinessDomain@network-element-docking.md](BusinessDomain@network-element-docking.md) 引用，文件暂不存在）
4. **batch-14 业务场景未使用**：旧图谱 [topic-knowledge/Batch-14-业务场景方案.md](../../../business-graph/APN业务域/topic-knowledge/Batch-14-业务场景方案.md) 9 个业务场景（工厂工控/智慧农业/家庭宽带/VoLTE/企业AAA/传统DHCP/企业L2TP/区域化/企业双栈）——本次未采用（用户决策："Batch-14 方案不合理"），APN 域按"配置族"组织不按业务场景

## 九、Commit 计划

按本次会话的 6 md + 1 index 修改 + 37 task md 修改，预计 commit 1 个综合提交：

```
feat(business): APN 业务域构建—1 BD + 1 NS + 4 CS（按 SOP §4.2 严格模板）

- BD@apn-domain：APN 域定义（UE 接入与会话管理 + 4 维度决策 + 3 底座支撑）
- NS@apn-access：APN 接入与会话管理场景（4 DP 独立决策，4 CS AND 关系）
- CS-1 地址分配（核心·必选，6 选 1 × 3 选 1 = 18 格矩阵）
- CS-2 鉴权 AAA（必选 1，4 种 AUTHMODE）
- CS-3 隧道接入（可选，5 选 1，VPN 直通不启）
- CS-4 IP 类型治理（必选 1，IPv4/IPv6/双栈）
- index.md 同步：加 BD 段 + NS 段 + CS 段
- 双向回填：37 feature task md 「## 关联」段追加"被引用于"4 CS

依据 SOP：业务层级构建SOP.md §0-§8
构建知识源：business-graph/APN业务域/ 4 文件
构建核查：SOP §7 验收清单 100% 通过
章节严格度：100% SOP §4.2 模板
```

## 十、Agent 接手指南（★本节是用户特别要求"充分引用"的核心——Agent 可据此续接）

如果你（Agent）需要在 APN 域做以下操作：

### 场景 A：判断某业务诉求该选哪个 CS
- 看 [NetworkScenario@apn-access.md §决策点](NetworkScenario@apn-access.md)——4 个独立 DP（不是 4 选 1）
- 4 DP 各自选变种，组合出完整 APN 方案
- 完整 APN 方案 = CS-1（必选）+ CS-2（必选 1）+ CS-3（可选，VPN 直通不启）+ CS-4（必选 1）+ 基础 feature 矩阵

### 场景 B：新增第 5 个 CS（如有）
- 按 [业务层级构建SOP.md §2](../../../business/业务层级构建SOP.md) 单方案构建流程
- 前置门：确认新 CS 涉及 feature 全建完
- 模板：严格按 SOP §4.2 CS 模板（概览 + 配置与协同 + 决策点 + 约束 + 关联）
- CS 间保持 **AND 关系**——不要改成 OR
- 双向回填 4 CS 关联的所有 task md
- 更新 [index.md](index.md) 加新 CS 段
- 更新 [NS 决策点表](NetworkScenario@apn-access.md) 加新 DP

### 场景 C：CS-1/2/3/4 升级（如新增 1 种方式）
- 在该 CS「## 决策点」DP 表加新选项
- 在「## 配置与协同」特性关系矩阵"维度增强"行加新 feature（如有）
- 写"UNC 控制面：xxx"和"UDG 用户面：xxx"详述新选项
- 同步 [NS 决策点表](NetworkScenario@apn-access.md) 路由
- 双向回填新 feature task「## 关联」段
- 更新 [index.md](index.md) CS 描述

### 场景 D：跨域协同排查
- APN 域做"接入与会话"，业务感知域做"识别+策略/计费控制"
- 交叉点：APN 域的地址分配结果作为业务感知域 PCC 策略决策的输入
- 跨域一致性约束：APN 名 / 地址池名 / UPF 实例名 / N4 PFCP Node ID 全网唯一

### 场景 E：License 编号核查
- **不可按命名规律推断**（如 LKV3G5ABNT01 是从 ABNTraffic 推的，错了）
- 必须从 `assets/evidence/UDG/20.15.2/{GWFD}-xxxxx/特性概述_xxxxx.md` 的 License 表交叉验证
- License 依赖链：IPv6 → LKV3G5V6PB01 → 双栈 → LKV3G5VDSA01 → PD → LKV3G5P6PD01
- 详见 [BusinessDomain@apn-domain.md §约束](BusinessDomain@apn-domain.md) + [业务层级构建SOP.md §6](../../../business/业务层级构建SOP.md)
