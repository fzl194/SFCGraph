# Phase 2 构建上下文 — feature 2-00001 ~ 2-00010

> 供每个特性 Agent 重建用。依据 `task-build-skill/procedures/compound-extraction.md`(A 段 6 步)+ spec。
> **atom 层冻结**(命令 task / atom 挂 rule/DP 只读)。feature 重建=参照现有校准/演进。

## backbone 复用库(canonical-compounds.md 摘要)

| compound | 相位 | 命令集 | 复用数 |
|---|---|---|---|
| 1-00001 计费三件套 | 计费三件套 | ADD PCCPOLICYGRP, ADD URR, ADD URRGROUP | 20 |
| 1-00002 过滤链 | 过滤链 | ADD FILTER, ADD FILTERIPV6, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD L7FILTER, ADD PROTBINDFLOWF | 22 |
| 1-00003 规则与用户模板绑定 | 规则与用户模板绑定 | ADD RULE, ADD RULEBINDING, ADD USERPROFILE | 25 |
| 1-00004 收尾 | 收尾 | ADD SPECURRGRPLIST, SET REFRESHSRV, SET URRGRPBINDING | 9 |

完整登记表见 `task-assets/UDG/20.15.2/canonical-compounds.md`。

---

## 2-00001 GWFD-020301 — 内容计费基本功能

- task_intent: UPF 内容计费完整配置流程（业务费率→过滤规则→规则→用户模板→缺省费率→刷新）
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020301
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015']
- feature 挂 rule: ['0-00008', '0-00009', '0-00010']
  - 0-00008 (conditional_rule) 防欺诈开启时 URL 类型 RULE 必须同绑三四层 filter
  - 0-00009 (dependency_rule) 内容计费依赖 SA-Basic 与 License
  - 0-00010 (dependency_rule) 本特性命令的 CommandParameter 结构化对象待 CommandGr
- feature 挂 DP: ['0-00003']
  - 0-00003 (boolean) 是否启用计费防欺诈 | options: ['opt-on', 'opt-off']

### md 文件(5 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能_66863836.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/GWFD-020301 内容计费基本功能参考信息_97488215.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/GWFD-020301 内容计费基本功能特性概述_66863837.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/实现原理_66863838.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020301 内容计费基本功能/部署UPF_28493406.md`

---

## 2-00002 GWFD-020300 — 在线计费

- task_intent: Gy 接口在线计费：复用计费 backbone + 在线专属可选命令（默认配额/Credit Pooling/上报失败动作）
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020300
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015', 'UDG@20.15.2@Task@0-00016', 'UDG@20.15.2@Task@0-00017', 'UDG@20.15.2@Task@0-00018']
- feature 挂 rule: ['0-00011']
  - 0-00011 (conditional_rule) Credit Pooling 与 DefaultQuota 不能同时使能
- feature 挂 DP: []

### md 文件(5 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/GWFD-020300 在线计费参考信息_02557786.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/GWFD-020300 在线计费特性概述_66347600.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/配置Gy接口在线计费_83167737.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/实现原理/在线计费流程（用户创建承载时下配额）_66692149.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020300 在线计费/实现原理/在线计费流程（用户创建承载时未下配额）_66692150.md`

---

## 2-00003 GWFD-010171 — 离线计费

- task_intent: Ga 接口离线计费：复用计费 backbone + 离线专属可选命令（URR 上报失败动作）
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-010171
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015', 'UDG@20.15.2@Task@0-00018']
- feature 挂 rule: []
- feature 挂 DP: []

### md 文件(4 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010171 离线计费/GWFD-010171 离线计费参考信息_97563135.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010171 离线计费/GWFD-010171 离线计费特性概述_66342906.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010171 离线计费/实现原理_66342907.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010171 离线计费/配置Ga接口离线计费_31927856.md`

---

## 2-00004 GWFD-010173 — 融合计费

- task_intent: 融合计费：复用计费 backbone；URR 在线+离线共存，SMF 侧 RGAPPLIED 控制
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-010173
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015']
- feature 挂 rule: []
- feature 挂 DP: []

### md 文件(5 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/GWFD-010173 融合计费参考信息_33931912.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/GWFD-010173 融合计费特性概述_70301693.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/实现原理_70301694.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/调测融合计费的费率标识_91966529.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-010173 融合计费/部署UPF_79654301.md`

---

## 2-00005 GWFD-020351 — PCC基本功能

- task_intent: UPF PCC策略控制完整配置流程（License→PCC策略组→过滤链→规则→用户模板绑定→刷新），覆盖动态PCC(有PCRF/PCF)与本地PCC(无PCRF/PCF)两种部署场景
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020351
- 现有 compounds: ['UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00015', 'UDG@20.15.2@Task@0-00019']
- feature 挂 rule: ['0-00012', '0-00013']
  - 0-00012 (dependency_rule) PCC特性 license 与业务感知配置前置依赖
  - 0-00013 (dependency_rule) SET LICENSESWITCH 的 CommandParameter 结构化
- feature 挂 DP: ['0-00007']
  - 0-00007 (single_choice) PCC模式 | options: ['opt-pcc-dynamic', 'opt-pcc-local']

### md 文件(9 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能参考信息_79592737.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/GWFD-020351 PCC基本功能特性概述_47011385.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/调测PCC基本功能_42369277.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/2_3_4_5G PCC功能差异_47013471.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/Event Trigger_47013472.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/业务流程_47013470.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/实现原理/相关概念_72244993.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置动态PCC功能_74096530.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/智能策略控制功能/GWFD-020351 PCC基本功能/激活PCC基本功能/配置本地PCC功能_74096529.md`

---

## 2-00006 GWFD-020307 — TCP重传识别

- task_intent: 在内容计费 backbone 基础上识别 TCP重传报文并按 URR 组计费。完整配置 = 部署UPF backbone（License→计费三件套→过滤链→规则与用户模板绑定→收尾）+ TCP重传差量 （为 UserProfile 绑定 TCP重传 URR 组、打开 TCP重传计费）。md 明示"详细配置参考 部署UPF，此处仅描述差异"。
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020307
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015', 'UDG@20.15.2@Task@0-00019']
- feature 挂 rule: ['0-00015']
  - 0-00015 (dependency_rule) TCP重传识别 license 与内容计费前置依赖
- feature 挂 DP: []

### md 文件(4 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020307 TCP重传识别/GWFD-020307 TCP重传识别参考信息_35158195.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020307 TCP重传识别/GWFD-020307 TCP重传识别特性概述_88618762.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020307 TCP重传识别/实现原理_88458836.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020307 TCP重传识别/激活TCP重传识别_88299168.md`

---

## 2-00007 GWFD-020308 — 7层流量统计

- task_intent: 配置APN仅统计7层应用层流量（APPLAYERVOLUME=ENABLE），不统计L3/L4承载层流量
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020308
- 现有 compounds: []
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00020']
- feature 挂 rule: ['0-00017']
  - 0-00017 (dependency_rule) 7层流量统计前置与统计口径影响
- feature 挂 DP: []

### md 文件(3 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020308 7层流量统计/GWFD-020308 7层流量统计参考信息_13282496.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020308 7层流量统计/GWFD-020308 7层流量统计特性概述_59642319.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020308 7层流量统计/激活7层流量统计_13442390.md`

---

## 2-00008 GWFD-020305 — 终端异常下行流量检测

- task_intent: 在APN下开启终端异常下行流量检测（含基于流行为的检测）
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020305
- 现有 compounds: []
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00019', 'UDG@20.15.2@Task@0-00021']
- feature 挂 rule: ['0-00016']
  - 0-00016 (dependency_rule) 终端异常下行流量检测 license 与APN前置依赖
- feature 挂 DP: []

### md 文件(4 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/GWFD-020305 终端异常下行流量检测参考信息_02455578.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/GWFD-020305 终端异常下行流量检测特性概述_02456812.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/激活终端异常下行流量检测_02455576.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/业务感知功能/GWFD-020305 终端异常下行流量检测/调测终端异常流量下行检测_02455577.md`

---

## 2-00009 GWFD-020302 — 基于业务时长的计费

- task_intent: UPF 按业务时长计费（metering=TIME 变体）；命令集与内容计费 backbone 完全重合，差异仅在 ADD URR 的 OFFMETERINGTYPE/ONLMETERINGTYPE 取 TIME
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020302
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015', 'UDG@20.15.2@Task@0-00019']
- feature 挂 rule: ['0-00018']
  - 0-00018 (dependency_rule) 基于业务时长计费 license 与内容计费前置依赖
- feature 挂 DP: []

### md 文件(11 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费_69143989.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/GWFD-020302 基于业务时长的计费参考信息_97488216.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/GWFD-020302 基于业务时长的计费特性概述_69148027.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/部署UPF_79813617.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）_69148029.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）_69148032.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于融合计费）_33943344.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）/在线时长计费方式_69148030.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于在线计费）/在线时长计费流程_69148031.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）/离线时长计费方式_69148033.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020302 基于业务时长的计费/实现原理/基于业务时长的计费（适用于离线计费）/离线时长计费流程_69148034.md`

---

## 2-00010 GWFD-020303 — 基于业务流量的计费

- task_intent: UPF 按业务流量计费（metering=VOLUME 变体，内容计费默认形态）；命令集与内容计费 backbone 完全重合
- status: inferred | ref: UDG@20.15.2@Feature@GWFD-020303
- 现有 compounds: ['UDG@20.15.2@Task@1-00001', 'UDG@20.15.2@Task@1-00002', 'UDG@20.15.2@Task@1-00003', 'UDG@20.15.2@Task@1-00004']
- 现有 direct atoms: ['UDG@20.15.2@Task@0-00001', 'UDG@20.15.2@Task@0-00002', 'UDG@20.15.2@Task@0-00003', 'UDG@20.15.2@Task@0-00004', 'UDG@20.15.2@Task@0-00005', 'UDG@20.15.2@Task@0-00006', 'UDG@20.15.2@Task@0-00007', 'UDG@20.15.2@Task@0-00008', 'UDG@20.15.2@Task@0-00009', 'UDG@20.15.2@Task@0-00010', 'UDG@20.15.2@Task@0-00011', 'UDG@20.15.2@Task@0-00012', 'UDG@20.15.2@Task@0-00013', 'UDG@20.15.2@Task@0-00014', 'UDG@20.15.2@Task@0-00015', 'UDG@20.15.2@Task@0-00019']
- feature 挂 rule: ['0-00019']
  - 0-00019 (dependency_rule) 基于业务流量计费 license 与内容计费前置依赖
- feature 挂 DP: []

### md 文件(4 个,必须全读)

- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费_69695706.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费/GWFD-020303 基于业务流量的计费参考信息_97488217.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费/GWFD-020303 基于业务流量的计费特性概述_67144065.md`
- `output/UDG_Product_Documentation_CH_20.15.2/特性部署/特性指南/UDG特性指南/计费功能/GWFD-020303 基于业务流量的计费/部署UPF_28813738.md`

---

## 域级 generalized 4-00001 计费配置(B 段,本域特性齐了再做)

- condition DP: 0-00004(计费方式)
- relations: 2-00001 → {2-00002, 2-00003, 2-00004}(内容计费基础 → 在线/离线/融合,按计费方式叠加)
- 2-00009/10(时长/流量计费)也可挂此 generalized,看 md
