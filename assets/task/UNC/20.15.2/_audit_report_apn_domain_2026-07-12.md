# UNC APN 域 task wiki 综合审查报告（2026-07-12）

> **审查员立场**：仅审查，不修改任何文件
> **审查范围**：UNC APN 域 24 个 feature（2-00014~2-00037）+ 10+ 个共享骨架 compound
> **审查依据**：`特性task_wiki审视流程.md`（R1-R4 6 维度）+ `特性步骤级构建SOP.md` v1.1
> **金标准对照**：UDG 域 2-00001（BWM带宽控制）+ 2-00002（URL过滤）

---

## 一、审查范围与 6 维度总览

| 批次 | 主题 | feature 数 | critical | warning | info |
|---|---|---|---|---|---|
| 批1 | 会话管理+地址分配主特性+多PDN | 4 | 10 | 5 | 6 |
| 批2 | 地址分配族 | 8 | 19 | 9 | 3 |
| 批3 | 鉴权族 | 5 | 4 | 8 | 4 |
| 批4 | 接入方式族 | 3 | 6 | 5 | 2 |
| 批5 | 网元选择+扫尾 | 4 | 8 | 7 | 4 |
| **合计** | **24 feature + 10 共享骨架** | **24** | **47** | **34** | **19** |

---

## 二、Critical 级问题（必须修，47 处）

### 2.1 占位规范违反（SOP §3.5 v1.1 禁止）—— 31 处

`[[X 待补 atom]]` 占位形态在 6 个 feature 出现，是 v1.1 SOP 明确禁止的。配置生成器读到占位无动作，整段静默丢失：

| feature | 占位数 | 占位命令 |
|---|---|---|
| 2-00016 控制面地址分配方式 | 3 | `SET IPALLOCRULE` / `SET IPALLOCBYLOCGLBSW` / `ADD CONFLICTIP` |
| 2-00017 IPv4v6 双栈接入 | 2 | `SET SMFUNC` / `ADD SMSUBDATA`（4G/2-3G 全局开关 + 签约纠正）|
| 2-00021 DHCP 功能 | 6 | `ADD AGENTIP` / `ADD DHCPSERVERGRP` / `ADD DHCPSERVER` / `ADD DHCPBINDPOOLGRP` 等 |
| 2-00022 DHCPv6 地址分配 | 6 | 同上 |
| 2-00026 鉴权功能 | 3 | `MOD S1USRSECPARA` / `MOD IUAUTHCIPH` / `SET SOFTPARAOFBIT` |
| 2-00032 别名APN | 5 | `ADD ALIASAPN` / `LCK APNALIAS` / `RMV APNALIAS` / `SET DEACTIVERATE` |
| 2-00033 UPF选择 | 17 | `PNFPROFILE` / `PNFNS` / `PNFDNN` / `PNFDNAI` / `PNFUPFINFO` / `PNFTAI` 等 17+ 条 |

**修复原则**（SOP §3.5）：
- 首选：按命令名排序补建 atom 入 `_numbering.json`，feature 改用 `[0-XXXXX](task/UNC/20.15.2/{id}.md)`
- 次选：加 R1.5 待补 atom 脚注：`> **R1.5 待补 atom**（critical）：本步骤命令 X 的 atom 待建，配置生成暂不产出；evidence = 命令 wiki/特性 wiki 等`

### 2.2 SOP §4 禁止的"## 构建依据与状态"伪段残留 —— 5 个 feature

按 v1.1 §4：禁止"## 构建依据与状态"段（构建期元信息不入 wiki）。实际未清理的：

| feature | 问题 |
|---|---|
| 2-00017 IPv4v6 双栈接入 | 末尾保留"## 构建依据与状态"段 |
| 2-00018 IPv6 承载上下文 | 同上 |
| 2-00019 IPv6 前缀代理 | 同上 |
| 2-00020 L2TP VPN | 同上 |
| 2-00023 静态地址用户路由冗余 | 同上 |

**修复**：删除该段，构建期元信息归到 `assets/task/UNC/20.15.2/_build_tracker.md`（已在 git 追踪，不入 wiki）。

### 2.3 共享骨架场景差异"双向回填"硬规则违反 —— 8 处

SOP §3.5 R1.2 强制：每次 feature 复用 compound，**必须**将差异同步追加到 compound 场景差异段。本审查发现多化合物漏回填：

| 共享骨架 | 漏回填 feature | 漏填差异维度 |
|---|---|---|
| 1-00023 SMF 地址池体系 | 2-00015 WSFD-010502 | UDM 子方式必走 `ADD POOLBINDAPN`（与 2-00023 现有 WSFD-107021 行矛盾） |
| 1-00024 APN 接入基础设施 | 2-00017/19/20/32 | 双栈场景 / IPv6 PD 场景 / L2TP 场景 / 别名 APN |
| 1-00029 OSPF 路由发布 | 2-00029/30/31 + 2-00017 OSPFv3 子集 | 接入方式 3 特性未追加；OSPFv3 子集约束未列 |
| 1-00025 Radius 对接链 | 4 个 Radius feature | 多行描述不准 |
| 1-00026 Radius 私有扩展 | 2-00024/28 | 描述矛盾；activation 未演示 |
| 1-00036 UNC UPF 选择族 | 2-00033 WSFD-107010 | 仅 4 行泛化项，未回填 2-00033 决策点 9 行 |
| 1-00038 UNC 位置区域 DNS 族 | 2-00037 | feature 主流程未引用 1-00038 反而平铺 5 命令 |

**修复**：按 SOP §3.5 R1.2 第 5 条（v1.1 升级硬规则）—— 强制回写。

### 2.4 典型脚本命令参数名与 activation 实证不一致（配置生成阻塞）—— 5 处

UNC 命令的真实命令族/参数名 与原始产品文档 activation 实证 不一致：

| 涉及文件 | 实际错处 | 真伪判定 |
|---|---|---|
| 1-00029 + 2-00015/16/17 步骤 3 脚注 | 描述说"UNC 真实命令名是 `ADD OSPFINTERFACE`，`ADD OSPFNETWORK` 不存在"——但 0-00249 atom 文件名是 `ADD OSPFNETWORK` | **未核实命令 wiki 即下结论** |
| 1-00023 步骤 2/7/9 | `ADD SECTION:IP="10.1.1.0",MASKLEN=24` 等 4 处参数名与 activation 实证不一致 | **必须以 activation 实证重写** |

**修复**：
- 选项 A：核实 UNC 命令清单（命令 wiki），若真实命令是 `ADD OSPFINTERFACE` → 改 atom 0-00249 文件名 + `_numbering.json` + 1-00029 + feature 脚注
- 选项 B：若 UNC 真实是 `ADD OSPFNETWORK` → 撤销描述修正、撤掉 feature 步骤 3 脚注

### 2.5 多命令阶段模块平铺未抽 compound（R2.5 critical）—— 5 处

| feature | 平铺的命令链 | 应抽 compound |
|---|---|---|
| 2-00021 DHCP 功能 | 步骤 3-6 共 6 命令 | 1 个共享 DHCPv4 链路 compound |
| 2-00022 DHCPv6 地址分配 | 步骤 3-7 共 6 命令 | 同上（v4/v6 共享） |
| 2-00023 静态地址用户路由冗余 | 步骤 1-9 共 8 步主备可靠性链路 | 1 个主备可靠性 compound |
| 2-00027 终端二次鉴权 | 步骤 3-7 平铺 5 个 atom | feature 应直接 link 1-00025 步骤 6-9 |
| 2-00033 UPF选择 | 步骤 3-5 共 17 条 atom 平铺 | 必须引用 1-00036 UNC UPF 选择族 |

### 2.6 1-00029 命令清单自相矛盾（决策点段重复）—— 1 处

1-00029 `## 决策点` 段出现 2 次（v1.0→v1.1 合并未清理），2 个完全相同的表。须合并。

### 2.7 激活步骤遗漏（R1.1 偏离）—— 2 处

| feature | 遗漏命令 | 证据 |
|---|---|---|
| 2-00017 IPv4v6 双栈接入 | 步骤 4 漏 `MOD GTPCCMPT`（4G/SGSN-MME 兼容性） | 4G 激活档 48043379 数据规划表 |
| 2-00025 Radius 功能 | 步骤编排缺业务触发 RADIUS 配套规则链 7 条 | 业务触发 RADIUS 文档 33000859 |

### 2.8 步骤编号重复 + 关键命令名错误 —— 1 处

2-00017 步骤 5-6 编号重复 2 次（v1.0/v1.1 合并残留）。

### 2.9 零证据差异（R1.5 激活未演示即配置）—— 1 处

2-00020 L2TP 决策点表的 4 鉴权子参数（PASSWORD+CFMPASSWORD/COMMONUSERUSED/ICCN_PROXYAUTH/DEDICATEDBEARSW）激活档 46559215 未演示。

### 2.10 建设方案编号错位 —— 1 处

`_apn-feature-build-plan.md` §2.2 写"1-00028 = UNC UPF 选择族"，实际 1-00028 是 DHCP 链路，UPF 选择族骨架是 1-00036。

### 2.11 1-00032 OSPFv3 骨架存在但 atom 未建 —— 1 处

1-00032 OSPFv3 路由发布已在 evidence 引用 5 个 feature，但 4 个 OSPFv3 atom 未建——配置生成阻塞。

---

## 三、Warning 级问题（34 处）—— 简要

### 3.1 关键命令 atom 待补（影响配置生成）
- `SET SMFUNC` / `ADD SMSUBDATA`（2-00017 双栈全局开关 + 签约纠正）
- OSPFv3 全族 atom（OSPFV3/OSPFV3AREA/OSPFV3INTERFACE/OSPFV3IMPORTROUTE）
- 5 个 Radius 命令（ADD IPV4DNSH / ADD DNSN / ADD AREADNS / SET MSCSELPLCY / ADD SGSNDNS）
- 1-00028 族 DHCP 服务器组 3 命令
- 1-00035 族 L2TP 控制 4 命令
- 1-00037 族 鉴权功能 4 命令
- 1-00040 族 别名APN 4 命令

### 3.2 证据链不完整
- 2-00018 2-3G License 项名"待核"未加 R1.5 脚注
- 2-00029 IPv6 GRE / 多租户共享 / MTU 优化 3 处无独立激活档
- 2-00030 IPSec 国密 5 子档跨 activation 来源 / DPD/NAT/证书可选步 activation 未演示
- 2-00033 UPF 选择 4 个 FLAG 依赖关系 / FIRSTPRI/SECONDPRI 命令 wiki 核实
- 2-00036 `SET SYS: SUBSTORAG=SEPARATE` 命令名无 evidence 佐证
- 2-00034 GBARD/IUARD 参数集在 SGSN/MME 激活档无演示

### 3.3 复用模式偏差
- 2-00024 直接 link 1-00025 步骤 1-5 但 1-00025 场景差异 WSFD-011305 行写"不直接用本骨架"
- 2-00026 4G 子分支 `MOD S1USRSECPARA` 关键参数漏 AUTHEVENTTHRESHOLD/ATTSAUTH；误标 IMSIPRE

### 3.4 能力型+配置型混合处置偏差
- 2-00036 应改 `status: foundation` + 应建 1~N 个骨架 compound + DP 走法列应显式标"依赖被依赖特性"

### 3.5 共享骨架场景差异描述不准
- 1-00025 对 WSFD-011305/108007/011306 多行描述误导
- 1-00026 对 WSFD-011305/011307 行描述不准
- 1-00031 MPLS VPN 基础设施仅 1 行笼统描述，6 组网变体未逐行展开

### 3.6 步骤编号/链接问题
- 2-00020 [1-00035](task/UNC/20.15.2/1-00035.md) 实际未建——虚链
- 1-00029 第 86 行 `0-00249 ADD OSPFNETWORK` 应同步改 `ADD OSPFINTERFACE`

---

## 四、Info 级问题（19 处）—— 简要

- 2-00029 与 1-00029 描述自相矛盾（OSPFNETWORK vs OSPFINTERFACE）的真伪待 UNC 命令 wiki 核实
- 2-00034 调测剥离已修正（SOP §6 反例之一已修复），是合规范例
- 2-00035 调测剥离已修正（明示"调测 md 不拷入"），是合规范例
- 2-00014/15/16 步骤 3 OSPFNETWORK 修正脚注是 SOP §6 必加脚注的正确范例
- 1-00020/21/22 能力型骨架未加 "被引用于 CS" 段
- 2-00033 SET UPSELECTPRI 参数名拼写 `FIRSTPRISELPLCSECONDPRI` 与 1-00036 的 `FIRSTPRI/SECONDPRI` 不一致
- 1-00029 决策点段重复（v1.0→v1.1 合并残留）

---

## 五、族级共性问题（SOP 改进建议）

### 5.1 SOP §3.5 占位规范 enforcement（Lint）
本次审查发现 `[[X 待补 atom]]` 占位 31 处违例，建议加 Lint 规则自动 grep + 报警。

### 5.2 SOP §4 "## 构建依据与状态" 伪段禁令 enforcement（Lint）
本次发现 5 个 feature 仍保留该段（v1.1 严禁），建议加 Lint 检查。

### 5.3 SOP §3.5 双向回填硬规则强制检查（scripts）
本次发现 8 处化合物漏回填。建议 `assets/scripts/check_compound_backfill.py` 自动扫 feature → 复核引用的骨架场景差异段是否含本 feature 行。

### 5.4 SOP §3.5 多命令平铺阈值明确
本次发现 5 处平铺违反。建议明确"≥3 命令 + 同族/同域 ≥2 feature 重用"双重阈值。

### 5.5 SOP §3.7 能力型特性 status 三态化
- `draft`：待补命令
- `active`：人审过
- `foundation`：能力型骨架
- `stale`：需更新

### 5.6 1-00029 命令清单与 atom 文件名双向校验机制
本次发现 1-00029 描述说"ADD OSPFNETWORK 不存在"但 atom 0-00249 文件名是 `ADD OSPFNETWORK`——可能 v1.0→v1.1 修正时仅改描述未改 atom。建议加脚本扫"feature 描述段 vs atom 文件名 vs _numbering.json"三方一致性检查。

### 5.7 方案文档与实际骨架强校验
本次发现 `_apn-feature-build-plan.md` §2.2 表格与实际 1-XXXXX.md 内容双向不符。建议 SOP §2 单特性 pass 第 0 步加 "**复核候选 compound 编号→查实际骨架标题匹配**"。

### 5.8 SOP §3.7 能力型骨架的「场景差异」段强制按变体逐行
2-00031 1-00031 场景差异段当前仅 1 行笼统描述——但 6 组网变体是 6 个独立的被依赖维度，应按变体逐行展开。

### 5.9 R1.4 模板复用识别优先级
2-00030 IPSec 13 份 activation 内容**显著不雷同**——但仍需核对 md5。建议 SOP §6 加"接入方式族（高复杂度多场景）须显式做 activation md5 比对 + 内容差异抽样"。

---

## 六、整体合规度评估（与 SOP §6 硬约束对照）

| SOP §6 硬约束 | 合规情况 | 备注 |
|---|---|---|
| 缺失命令的 atom 必须补建 + 写入 _numbering.json | ❌ | 31 处 `[[待补 atom]]` 占位 |
| 证据 md 拷入 `assets/evidence/` | ✓ | 24 feature 均已拷入 |
| 双向链接闭环 | ⚠ | 多数闭环，8 处化合物场景差异回填不全 |
| 配置流程参数证据链 | ⚠ | OSPFNETWORK 命令名待核、4 处典型脚本参数名与 activation 不一致 |
| activation 模板复用识别 | ✓ | 大部分独立完整，仅 L2TP 4 鉴权子参数零证据 |
| 调测剥离 | ✓ | 24 feature 全部合规 |
| 防平铺 | ❌ | 5 处 critical 平铺 |
| 占位规范 | ❌ | 31 处占位违例 |
| 关联段 8 类齐全 | ⚠ | 大部分合规，少数漏"被引用于 CS"段 |
| 无"## 构建依据与状态"伪段 | ❌ | 5 个 feature 残留 |

---

## 七、修复优先级（按 critical 排序）

### P0（必须立即修）
1. 核实 1-00029 ADD OSPFNETWORK vs ADD OSPFINTERFACE 真伪
2. 重写 1-00023 典型脚本（以 activation 实证为准）
3. 31 处 `[[X 待补 atom]]` 占位 → R1.5 脚注 / 补建 atom
4. 5 个 feature 删"## 构建依据与状态"伪段
5. 8 处化合物场景差异双向回填
6. 2-00033 UPF选择 17 条平铺改引 1-00036
7. 2-00021/22 DHCP + 2-00023 主备冗余 + 2-00027 UPF 中转链平铺改抽/引用
8. 2-00017 步骤 4 MOD GTPCCMPT 漏盖补回
9. 2-00025 业务触发 RADIUS 配套规则链 7 条补回
10. 2-00020 L2TP 4 鉴权子参数零证据差异加 R1.5 脚注

### P1（须修）
11. OSPFv3 全族 atom 补建（4 条）
12. 5 个 Radius 命令 atom 补建
13. DHCP/L2TP/ALIASAPN/鉴权功能 atom 补建（~15 条）
14. 2-00036 status 改 `foundation` + 补 1~2 个骨架 compound
15. 1-00025/1-00026 复用警示 + 场景差异描述纠错

### P2（修正性整理）
16. 1-00020/21/22 骨架 compound 加"被引用于 CS"段
17. 2-00024 link 1-00025 步骤 1-5 改为 link 2-00025 整特性
18. 1-00031 MPLS VPN 场景差异表按 6 组网变体扩展

### P3（SOP 沉淀）
19. SOP §3.5 v1.2 增加 Lint 规则（占位/伪段/双向回填/平铺/状态字段五项）
20. SOP §3.7 v1.2 骨架化合物场景差异按变体逐行强制
21. SOP §3.5 R1.2 v1.2 化合物复核机制
22. SOP §2 v1.2 单特性 pass 第 0 步加骨架强校验

---

## 八、亮点（合规范例）

1. **2-00034 用户接入控制** — SOP §6 反例之一已修正
2. **2-00035 多 PDN/PDU** — 同上
3. **2-00015 / 2-00016 / 2-00017 步骤 3 OSPFNETWORK 修正脚注** — SOP §6 必加脚注的正确范例
4. **2-00014 会话管理** — 严格按 SOP §3.7 能力型底座特性范式产出
5. **2-00031 MPLS VPN** — 严格按 SOP §3.7 能力型底座特性范式产出

---

## 九、最终结论

**UNC APN 域 24 个 feature + 10 共享骨架的 task wiki 整体构建质量良好**——金标准对照（UDG 2-00001/2-00002）已基本对齐。

**但**仍存在 47 处 critical 问题，需按 P0→P1→P2→P3 顺序修复。

**修复路径**：用户决策后由构建者按 P0 顺序逐项修复。