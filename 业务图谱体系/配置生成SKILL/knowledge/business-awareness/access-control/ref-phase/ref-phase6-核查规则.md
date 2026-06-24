# Phase 6 参考文件：配置生成内置约束（图谱规则）

> **定位变更**（配置生成 SKILL）：真实配置核查调 `knowledge/common/AI-MML核查流程.md`（coremaster configcheck 接口，直接调接口）。本文档的图谱核查规则（BR-AC / CR-AC / TR-AC）承担两个角色：
> 1. **Phase 5 配置生成时的内置约束** — 生成命令时即遵守，避免核查返工
> 2. 核查阶段直接调 AI 接口（无静态降级）；本规则仅服务 Phase 5 生成约束
>
> 核查直接调 AI MML 接口；本规则作 Phase 5 生成内置约束，不做静态降级。

---

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 6。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **必须有 Phase 5 生成的配置脚本**：必须有已生成的 MML 配置脚本。如果没有，**STOP**，回到 Phase 5 先生成配置。
2. **核查完成后必须 STOP**：核查通过后，**必须将核查报告和配置脚本展示给用户并停止执行**，等待用户在 GATE-5 确认。不得直接交付给用户。

---

> 本文件定义 Phase 6 的 pipeline 要求、SKILL 特有的操作安全检查和输出模板（访问限制场景专属）。
> 业务规则核查（双轨道图谱规则、配置依赖、知识库规则、跨网元一致性）由 Agent 从图谱动态加载执行。
> 域共享核查规则（REFRESHSRV 时序、跨网元一致性、优先级）见 `../业务感知域规则.md`，本文件不复述。

---

## 1. Pipeline 步骤

### Step 1: 加载核查规则

**必须加载**：
- `../../访问限制场景/three-layer-graph/01-business-graph.md` — 读取 BusinessRule (BR-AC-01~10)，逐条核查
- `../../访问限制场景/three-layer-graph/04-command-graph.md` — 读取 CommandRule (CR-AC-01~14)，逐条核查
- `../../访问限制场景/three-layer-graph/03-task-layer.md` — 读取 TaskRule (TR-AC-01~08)，逐条核查
- `../kb/02-双轨道动作机制与POLICYTYPE路由.md` — 双轨道核查依据（轨道 A vs B 动作体系分离）
- 按匹配的 CS 闭包加载对应 `kb/` 章节（如 `kb/04-头增强族协议差异.md` 核查协议限制）

> **核查依据必须是图谱中定义的规则实例（BR-AC-xx / CR-AC-xx / TR-AC-xx），不可凭记忆。**

### Step 2: 执行图谱规则核查

逐条检查加载的 BusinessRule / CommandRule / TaskRule，记录通过/违反项。

重点维度（规则来源为图谱，此处仅列出核查方向）：

**业务约束（BR-AC-01~10）**：
- 预定义规则三网元一致性（BR-AC-01）
- 规则匹配类型独立原则（BR-AC-02，双轨并存基础）
- 一条规则绑定一条策略（BR-AC-03）
- License 前置门控（BR-AC-04，含头防欺诈 License 双开）
- REFRESHSRV 必须最后执行（BR-AC-05，见 `../业务感知域规则.md` §1.1）
- 头防欺诈依赖头增强（BR-AC-06）
- ★ RULE.POLICYTYPE 决定动作轨道（BR-AC-07，双轨道+五子轨核心）
- 头增强字段加密与编码约束（BR-AC-08，HTTPS 无 RSA、TLS TLV 格式）
- 加密协议仅 WebProxy 可处理（BR-AC-09）
- ★ PERMIT 唯一性（BR-AC-10，仅 URL 过滤显式支持）

**配置依赖（CR-AC-01~14）**：
- RULENAME 跨 POLICYTYPE 不冲突（CR-AC-01）
- ★ POLICYTYPE 决定动作对象链（CR-AC-02，五子轨 POLICYNAME 指向）
- SMARTREDIRECT 两特性共用 POLICYTYPE（CR-AC-03，区分点在 POLICYNAME 指向）
- 头防欺诈强依赖头增强（CR-AC-04，License 双开）
- ICAP Server 必需（CR-AC-05，URL 过滤前置）
- ★ URL 过滤 PERMIT 动作唯一性（CR-AC-06）
- FLOWFILTER 必须绑定 FILTER（CR-AC-07）
- RULE 必须引用已存在的对象（CR-AC-08）
- 预定义规则名三网元一致（CR-AC-09）
- HTTPS/HTTP2.0 加密协议盲区（CR-AC-10）
- RTSP 不支持头防欺诈（CR-AC-11）
- 配置变更后必须 SET REFRESHSRV（CR-AC-12）
- REFRESHSRV 后 60 秒禁改 Filter（CR-AC-13）
- ★ 双轨可并存（CR-AC-14）

**任务约束（TR-AC-01~08）**：
- REFRESHSRV 时序约束（TR-AC-01）
- ★ POLICYTYPE 动作路由规则（TR-AC-02，五子轨路由）
- ★ 双轨动作分离规则（TR-AC-03，轨道 A POLICYTYPE 隐式 vs 轨道 B CFTEMPLATE.ACTION 显式）
- 头防欺诈强耦合依赖（TR-AC-04）
- URL 过滤 ICAP 互通前置（TR-AC-05）
- WebProxy 双规则约束（TR-AC-06）
- Portal captive 配置位置约束（TR-AC-07，CAPMODETHRES 在 USERPROFILE 不在 RULE）
- 位置触发动态/本地 PCC 分支（TR-AC-08）

### Step 3: 执行 SKILL 独有的操作安全检查

以下检查项不在图谱中，由本 SKILL 独有提供：

| 核查项 | 规则 | 严重级别 |
|--------|------|---------|
| 同名冲突 | 新增对象名是否与现网已有对象同名（特别注意跨 POLICYTYPE 的 RULENAME 唯一性，CR-AC-01） | HIGH |
| 参数覆写 | SET/MOD 命令是否覆盖了现网中仍在使用的参数（特别是 MOD UPBINDUPG 改 LOCGROUPNAME 影响位置触发） | HIGH |
| 共享对象影响 | 修改被多个 RULE 引用的共享对象（FLOWFILTER/PCCPOLICYGRP/HEADEN）时，是否评估影响范围 | HIGH |
| 删除安全 | RMV 命令是否先解绑了上层引用（特别是 ICAP 链路、IPFarm 集群） | CRITICAL |
| ★ 双轨道动作体系混淆 | 轨道 A 对象（POLICYTYPE/POLICYNAME/HEADEN/IPFARM）与轨道 B 对象（CFTEMPLATE/CONTCATEGBIND/ICAP）是否误配在同一 RULE（CR-AC-02, TR-AC-03） | CRITICAL |
| ★ WebProxy 双规则缺失 | WebProxy 场景是否同时配 POLICYTYPE=WEBPROXY + POLICYTYPE=PCC 两条 RULE（TR-AC-06） | HIGH |
| ★ URL 过滤 ICAP 链路完整 | URL 过滤是否配齐 VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG（TR-AC-05） | CRITICAL |
| ★ 头防欺诈 License 双开 | ANTIFRAUD=ENABLE 时是否同时开 HHAS + HTHE 两个 License（CR-AC-04, TR-AC-04） | HIGH |
| ★ Portal captive 位置 | Portal 的 CAPMODETHRES 是否配在 USERPROFILE 而非 RULE（TR-AC-07） | MEDIUM |

### Step 4: 跨网元一致性核查（仅 DP-AC-04 包含 UPF+SMF 时）

**必须加载**：
- `04-command-graph.md` CommandRule CR-AC-09（预定义规则名三网元一致） — 逐条核查
- `../业务感知域规则.md` §2（跨网元一致性） — 逐条核查

重点：
- RULENAME / FLOWFILTERNAME 在 PCF、SMF、UPF 三处一致（预定义规则场景）
- URRID / RG / RULENAME / USERPROFILENAME 在 UPF ↔ SMF 一致（共用参数）
- CGI/ECGI/NCGI 位置信息在 UNC + RAN + PCRF/PCF 三处一致（接入控制场景）
- URL 过滤 CATEGORYID 在 UDG + ICAP Server + PCRF/PCF 三处一致

### Step 5: 循环修正

- 发现问题 → **自动修正**并告知用户修正内容
- 无法自动修正 → **暂停并要求用户决策**
- 修正后重新从 Step 2 执行，直到全部通过

---

## 2. 输出格式模板

```markdown
## 核查报告

### 核查结果: {通过 / 已修正}

| 维度 | 规则来源 | 检查项数 | 通过 | 修正 | 待确认 |
|------|---------|---------|------|------|--------|
| BusinessRule | 01-business-graph.md | {n} | {n} | {n} | {n} |
| CommandRule | 04-command-graph.md | {n} | {n} | {n} | {n} |
| TaskRule | 03-task-layer.md | {n} | {n} | {n} | {n} |
| 操作安全 | ref-phase6 §1.3 | {n} | {n} | {n} | {n} |
| 跨网元一致性 | ref-phase6 §1.4 + 业务感知域规则 §2 | {n} | {n} | {n} | {n} |

### 双轨道专项核查
- 轨道 A 对象清单: {POLICYTYPE/POLICYNAME/HEADEN/IPFARM/SMARTREDIR}
- 轨道 B 对象清单: {CFTEMPLATE/CONTCATEGBIND/ICAP 系列}
- 双轨混淆检查: {通过/发现 N 处混淆}
- WebProxy 双规则: {齐全/缺失 PCC 规则/缺失 WEBPROXY 规则}
- URL 过滤 ICAP 链路: {完整/断裂于 {节点}}
- 头防欺诈 License 双开: {双开/仅开 HHAS/仅开 HTHE/未开}

### 修正日志
1. [{规则ID}] {问题描述} → {修正动作}
2. ...
```

---

## 3. 注意事项

- 每条违反项必须标注对应的规则 ID（BR-AC-xx / CR-AC-xx / TR-AC-xx），不可笼统描述
- 图谱规则是业务准确性的保障，必须从图谱原文加载执行，不可省略或简化
- 操作安全检查（§1.3）是图谱未覆盖的生产环境保护，同样不可跳过
- **双轨道专项核查是本场景特有**：必须逐条核对轨道 A/B 对象是否误配在同一 RULE（CR-AC-02, TR-AC-03），这是访问限制场景最易错点
- 跨网元一致性检查中，预定义规则三网元一致（CR-AC-09）、位置三处一致、CATEGORYID 三处一致均为 CRITICAL 级别，任一不一致都必须修正
- 核查直接调 `knowledge/common/AI-MML核查流程.md` 的 coremaster configcheck 接口（语法 + 语义核查），无降级
