# Phase 6 参考文件：配置生成内置约束（图谱规则）

> **定位变更**（配置生成 SKILL）：真实配置核查调 `knowledge/common/AI-MML核查流程.md`（coremaster configcheck 接口，直接调接口）。本文档的图谱核查规则（BR-APN / CR-APN / TR-APN）承担两个角色：
> 1. **Phase 5 配置生成时的内置约束** — 生成命令时即遵守，避免核查返工
> 2. 核查阶段直接调 AI 接口（无静态降级）；本规则仅服务 Phase 5 生成约束
>
> 核查直接调 AI MML 接口；本规则作 Phase 5 生成内置约束，不做静态降级。

---

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 6。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **必须有 Phase 5 生成的配置脚本**：必须有已生成的 MML 配置脚本（UDG/UPF 侧 + UNC/SMF 侧）。如果没有，**STOP**，回到 Phase 5 先生成配置。
2. **核查完成后必须 STOP**：核查通过后，**必须将核查报告和配置脚本展示给用户并停止执行**，等待用户在 GATE-5 确认。不得直接交付给用户。

---

> 本文件定义 Phase 6 的 pipeline 要求、SKILL特有的操作安全检查和输出模板。
> 业务规则核查（图谱规则、配置依赖、知识库规则、跨网元一致性）由 Agent 从图谱动态加载执行。
> **真实语法+语义核查**调 `../../common/AI-MML核查流程.md`（coremaster configcheck 接口）。

---

## 1. Pipeline 步骤

### Step 1: 询问用户是否调用 AI MML 核查

Phase 5 生成配置脚本后，**必须询问用户是否调用 AI MML 核查**（流程见 `../../common/AI-MML核查流程.md` §1）：
```
配置文件已生成（UDG/UPF-MML配置.txt / UNC/SMF-MML配置.txt）。
是否需要调用 AI MML 核查能力验证脚本正确性？
- 是 → 进入 AI MML 核查流程（../../common/AI-MML核查流程.md §2~§5）
- 否 → 直接进入图谱规则核查（Step 2~4）+ Phase 6.5 确认
```

### Step 2: 加载核查规则（图谱内置约束）

**必须加载**：
- `01-business-graph.md` §4 BusinessRule（BR-APN-01~16） — 逐条核查
- `04-command-graph.md` §4 CommandRule（CR-APN-01~18） — 逐条核查
- `03-task-layer.md` §10 TaskRule（TR-APN-01~13） — 逐条核查
- `kb/05-U+C不对称与跨侧一致性.md` + `kb/02-License门控.md` — 知识库级约束

> **核查依据必须是图谱中定义的规则实例（BR-APN-xx / CR-APN-xx / TR-APN-xx），不可凭记忆。**

### Step 3: 执行图谱规则核查

逐条检查加载的 BusinessRule / CommandRule / TaskRule，记录通过/违反项。

重点维度（规则来源为图谱，此处仅列出核查方向）：

**业务约束（BR-APN）**：
- 互斥约束：BR-APN-LOC-L2TP-EXCL（位置×L2TP）/ BR-APN-GRE-IPSEC-SRC-EXCL（GRE×IPSec 源地址）/ BR-APN-L2TP-ADDRAUTO-EXCL（L2TP×地址自动检测）
- 级联强依赖：BR-APN-RADIUS-CASCADE（Radius 功能→鉴权→二次鉴权）/ BR-APN-IPV6-CASCADE（IPv6 承载→双栈→PD）
- License 触发：BR-APN-DUALSTACK-NEED-LICENSE / BR-APN-LOC-NEED-LICENSE / BR-APN-L2TP-CU-ASYM（C-U 不对称）
- 协议限制：BR-APN-SECOND-AUTH-PROTO（二次鉴权仅 PAP/CHAP）/ BR-APN-LOC-AUTH-NO-PPP（本地鉴权不支持 PPP）
- 决策一致性：BR-APN-CONCURRENCY-11-15 / BR-APN-ALIAS-DOUBLE-COND / BR-APN-UPF-VENDOR-LOCK / BR-APN-AMF-LOCAL-FIRST / BR-APN-CARDTYPE-NEED-AUTH / BR-APN-DNAAA-IP-UNIQUE

**配置依赖（CR-APN）**：
- 跨侧分离：CR-APN-01（POOL vs ADDRPOOL）/ CR-APN-02（APNL2TPATTR vs APNL2TPCTRL）/ CR-APN-03（L2TPN4KEY vs L2TPKEY 密钥一致）/ CR-APN-04（POOLTYPE 跨侧取值差异）
- IPv6/PD：CR-APN-05（V6PREFIXLENGTH<64 PD 模式）/ CR-APN-06（VPNINSTAF ipv6uni 必需）
- 引用一致：CR-APN-07（APN VPN 与 POOL VPN 一致）
- 强时序：CR-APN-08（UPFRDSSVR 先于 UPFRDSCLIENTIP）/ CR-APN-09（NETWORKINSTVPNMAP 前置）
- IPSec：CR-APN-10（DH 组不能 None）/ CR-APN-11（ACL 仅源/目的 IP）/ CR-APN-12（GRE/IPSec 源地址互斥）
- L2TP 互斥：CR-APN-13（L2TP × 地址自动检测/位置）/ CR-APN-14（本地配置 vs AAA 下发）
- 别名/静态：CR-APN-15（APNACTNUM 阈值）/ CR-APN-16（STATICADDRPARA × SMF 主锚点）/ CR-APN-17（APNALIAS 转换后 APN 必须存在）/ CR-APN-18（MPLS 推导）

**任务约束（TR-APN）**：
- TR-APN-01（GRE/IPSec 源地址互斥）/ TR-APN-02（ACCESSMODE × Radius 分支）/ TR-APN-03（UDG/UNC 前缀不对称）/ TR-APN-04（V6PREFIXLENGTH 分水岭）/ TR-APN-05（L2TP C-U License 不对称）/ TR-APN-06（APNL2TPATTR vs APNL2TPCTRL 不对称）/ TR-APN-07（二次鉴权 UPF Radius 链时序）/ TR-APN-08（UPF 选择三轮筛选）/ TR-APN-09（ARD 卡类型控制鉴权前置）/ TR-APN-10（接入控制非 C-U 对称）/ TR-APN-11（IPSec IKE DH/NAT）/ TR-APN-12（别名 APN 双 License 双视角）/ TR-APN-13（MPLS 文档缺口）

### Step 4: 执行 SKILL 独有的操作安全检查

以下检查项不在图谱中，由本 SKILL 独有提供：

| 核查项 | 规则 | 严重级别 |
|--------|------|---------|
| 同名冲突 | 新增 POOL/APN/RDSSVRGRP/GRETUNNEL 等对象名是否与现网已有对象同名 | HIGH |
| 参数覆写 | SET/MOD 命令（如 SET APNADDRESSATTR）是否覆盖了现网中仍在使用的参数 | HIGH |
| 共享对象影响 | 修改被多个 APN 引用的共享对象（如 RDSSVRGRP、VPNINST）时，是否评估影响范围 | HIGH |
| APN 跨域影响 | 修改 APN（跨域共用挂载点）时，是否评估对地址分配/鉴权/L2TP/QoS/多PDN 的影响 | CRITICAL |
| 删除安全 | RMV 命令是否先解绑了上层引用（如 RMV POOL 前先 RMV POOLBINDGROUP/POOLGRPMAP） | CRITICAL |
| REFRESHSRV 位置 | SET REFRESHSRV 是否在配置链最后（UDG 与 UNC 各一个，必须最后） | HIGH |

### Step 5: 跨网元一致性核查（U+C 同时配置时）

**必须加载**：
- `04-command-graph.md` §4 CommandRule CR-APN-01/02/03/04（跨侧分离与一致） — 逐条核查
- `kb/05-U+C不对称与跨侧一致性.md` — U+C 不对称对象族

**CRITICAL 级一致性项**：
- APN/DNN 名（U+C 必须一致）
- SUPPORTIPV4/SUPPORTIPV6（U+C 必须一致）
- POOLTYPE 跨侧取值集（UDG=LOCAL，UNC=UDM，CR-APN-04）
- L2TPN4KEY（U）vs L2TPKEY（C）密钥必须相同（CR-APN-03）
- APNL2TPATTR（U，10+参数）vs APNL2TPCTRL（C，2参数）参数集不匹配需确认两侧都已配置（CR-APN-02）

### Step 6: AI MML 核查结果解析与修正（若用户选择调用）

按 `../../common/AI-MML核查流程.md` §5 解析核查结果：
1. 解压 `check_result.zip`，提取错误提示信息
2. 分析每条错误，回溯到对应的命令/参数/对象
3. 结合图谱规则（Step 3）判断是图谱已覆盖还是新问题
4. 修正动网脚本，告知用户修正内容

### Step 7: 循环修正

- 发现问题 → **自动修正**并告知用户修正内容
- 无法自动修正 → **暂停并要求用户决策**
- 修正后重新从 Step 3 执行，直到全部通过

---

## 2. 输出格式模板

```markdown
## 核查报告

### 核查结果: {通过 / 已修正}

| 维度 | 规则来源 | 检查项数 | 通过 | 修正 | 待确认 |
|------|---------|---------|------|------|--------|
| BusinessRule | 01-business-graph.md §4 | {n} | {n} | {n} | {n} |
| CommandRule | 04-command-graph.md §4 | {n} | {n} | {n} | {n} |
| TaskRule | 03-task-layer.md §10 | {n} | {n} | {n} | {n} |
| 操作安全 | ref-phase6 §1.4 | {n} | {n} | {n} | {n} |
| 跨网元一致性 | ref-phase6 §1.5 + kb/05 | {n} | {n} | {n} | {n} |
| AI MML 核查 | common/AI-MML核查流程.md | {n} | {n} | {n} | {n} |

### 修正日志
1. [{规则ID}] {问题描述} → {修正动作}
2. ...
```

---

## 3. 注意事项

- 每条违反项必须标注对应的规则 ID（BR-APN-xx / CR-APN-xx / TR-APN-xx），不可笼统描述
- 图谱规则是业务准确性的保障，必须从图谱原文加载执行，不可省略或简化
- **真实语法+语义核查调 AI MML 接口**（`../../common/AI-MML核查流程.md`），无静态降级
- 操作安全检查（§1.4）是图谱未覆盖的生产环境保护，同样不可跳过
- **APN 跨域共用挂载点**的修改影响范围最广，必须全面扫描地址分配/鉴权/L2TP/QoS/多PDN 引用（CRITICAL 级）
- 跨网元一致性检查中，U+C 不对称对象族（POOL↔ADDRPOOL、APNL2TPATTR↔APNL2TPCTRL、L2TPN4KEY↔L2TPKEY）任一不一致都必须修正
- License 串联（IPv6 承载→双栈→PD）任一级缺失都会导致功能不生效，必须逐级核查
