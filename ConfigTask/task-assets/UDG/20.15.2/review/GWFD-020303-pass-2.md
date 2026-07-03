# GWFD-020303 基于业务流量的计费 — pass-2(A 段重建)

> 串行第 10 个特性(10 特性 A 段收尾)。依据 `task-build-skill/procedures/compound-extraction.md` +
> `docs/superpowers/specs/2026-07-02-compound-feature-extraction-design.md`。
> **atom 层冻结**:task-0-* + atom 挂 rule/dp 只读,未改。

## 自审发现

### 形态判定:STEP-OK
- backbone 1-00001(计费三件套) / 1-00002(过滤链) / 1-00003(规则与用户模板绑定) / 1-00004(收尾)
  **全复用**,直挂 0-00019(SET LICENSESWITCH) license 前置。
- 无新建 compound、无新建 atom、无新建 feature DP(详见"流量计费差异如何表达")。

### 4 md 全读结论
1. **部署 md(部署UPF_28813738.md)**:操作步骤 1-12 + 数据规划表 4 场景(URL/IMS/any/异常),
   命令集与 2-00001 内容计费 backbone **字节级同构**(任务示例脚本全用 VOLUME,与 2-00009 时长计费
   字节级相同——2-00009 notes 已明示"部署 md 任务示例全用 VOLUME,与 2-00010 字节级同构")。
2. **特性概述(67144065.md)**:License 82209824 LKV3G5VBCS01;依赖 GWFD-020301 内容计费 + SA-Basic;
   原理概述分离线/在线/融合三段,统计由 UNC 话单(datavolumeFBCUplink)/OCS CCA(CC-Total-Octets)/
   CHF 信元(totalVolume)承载——非 UPF MML。
3. **参考信息(97488217.md)**:11 命令清单(与 2-00001 同),软参 BYTE301 控制强制归并流量计费方式
   (全局软参非 UPF MML)。
4. **主配置 md(69695706.md)**:仅 1 行标题,无操作内容(占位 md)。

### 复用判定证据(top-3,Jaccard + 相位)
| 候选 | 命中 backbone | Jaccard | 相位 intent | 推荐动作 |
|---|---|---|---|---|
| 三件套(URR/URRGROUP/PCCPOLICYGRP) | 1-00001 | **1.0** | 计费三件套(完全同义) | 复用 as-is |
| 过滤链(FILTER/FILTERIPV6/L7FILTER/FLOWFILTER/FLTBINDFLOWF/PROTBINDFLOWF) | 1-00002 | **1.0** | 过滤链(完全同义) | 复用 as-is |
| 规则与用户模板绑定(RULE/USERPROFILE/RULEBINDING) | 1-00003 | **1.0** | 规则与用户模板绑定(完全同义) | 复用 as-is |
| 收尾(SPECURRGRPLIST/URRGRPBINDING/REFRESHSRV) | 1-00004 | **1.0** | 收尾(完全同义) | 复用 as-is |

双闸全过:Jaccard≥0.75 **且**相位同义 → 复用。无新建 compound。

### 流量计费差异如何表达(三层判定)
- **参数级(atom DP,冻结)**:UPF 侧 metering 差异 = ADD URR 的 `OFFMETERINGTYPE`/`ONLMETERINGTYPE`
  取 VOLUME(默认值)。由 atom 0-00001(ADD URR)挂的 DP 0-00001(option opt-offline/opt-online
  的 effect_detail 已含 "VOLUME/TIME/EVENT/FREE 取值")覆盖。**纯参数 impact(target_type=parameter)**,
  不改命令集出现/缺失 → 不进 variants 枚举(spec §4.2)。
- **关键差异(对比 2-00009)**:VOLUME 是内容计费默认形态,**本特性连参数级差量都没有**。2-00009 时长
  计费至少在 metering=TIME 有参数值差量(TIME≠默认),本特性 VOLUME=默认值。命令集与参数值均与
  2-00001 内容计费 100% 一致。本特性本质是内容计费 backbone 的"按流量计费"专项命名。
- **feature DP**:无。本特性部署 md 仅走 backbone,无 feature 级可选命令(对比 2-00002 三可选 /
  2-00003/04 各一可选 SET URRFAILACTION)。流量计费的统计由 UNC 话单/OCS CCA 信元/CHF 信元承载
  (特性概述 §原理概述 离线/在线/融合三段:datavolumeFBCUplink/CC-Total-Octets/totalVolume 等
  AVP 字段),非 UDG UPF MML,不构成本特性的 UPF 命令集分叉。
- **rule**:feature 挂 rule 0-00019(dependency_rule,license 82209824 + 内容计费前置)已存在并核实
  正确,指向 0-00019 + 2-00001,OFFMETERINGTYPE/ONLMETERINGTYPE=VOLUME 由 DP 0-00001 option
  opt-offline/opt-online 覆盖。**无需新增 rule**(md 未揭示新 UPF 级约束:License 82209824 由 atom
  0-00019 LICITEM 变量投影;BYTE301 软参是全局软参非 UPF MML 命令约束)。

## 改动记录

| 文件 | 操作 | 说明 |
|---|---|---|
| `tasks/task-2-00010.yaml` | 编辑 | source_evidence_ids 补全 4 md 路径;notes 增 pass-2 分析(三层表达 + 同构关系 + 缺口);task_relations 复用 backbone(as-is,无新增边) |
| `task_rules/rule-0-00019.yaml` | 未改 | 已正确指向 0-00019 + 2-00001 + DP 0-00001 option 覆盖 metering |
| `decision_points/dp-0-00002.yaml` | 未改(本特性引用) | opt-basic-l34 option(2-00002 pass-2 新增)供本特性选 |
| `review/GWFD-020303-variants.yaml` | 新写 | 1 变体(opt-basic-l34 + opt-off) |
| `review/GWFD-020303-pass-2.md` | 新写 | 本文件 |
| `review/compound-review-queue-计费.md` | 追加 | 纯复用·无新事件记录(spec §10.1) |

**未改动**(核实现状合理):
- `tasks/task-1-00001~04.yaml`:4 个 backbone 全复用 as-is,无演进。
- atom 层全部只读未动(task-0-*.yaml + dp-0-00001.yaml + 各 atom 挂 rule)。

## 复用判定证据(详见"自审发现"表)
4 候选全 Jaccard=1.0 + 相位完全同义 → 复用 as-is,无新建/演进 compound。

## 覆盖校验结果

```
=== 覆盖校验:feature 2-00010 (GWFD-020303) ===
结构命令集(16):['ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF',
  'ADD L7FILTER', 'ADD PCCPOLICYGRP', 'ADD PROTBINDFLOWF', 'ADD RULE', 'ADD RULEBINDING',
  'ADD SPECURRGRPLIST', 'ADD URR', 'ADD URRGROUP', 'ADD USERPROFILE', 'SET LICENSESWITCH',
  'SET REFRESHSRV', 'SET URRGRPBINDING']
变体校验数:1
结果:✓ 覆盖通过
EXIT=0
```

**变体清单**:基础(按业务流量计费,IPv4 三四层基础过滤)—— 共 1 变体。
**DP 收敛**:opt-basic-l34 excludes FILTERIPV6/L7FILTER/PROTBINDFLOWF(3 命令)+
 opt-off excludes SPECURRGRPLIST(1 命令)= 4 命令收敛;结构 16 − 4 收敛 = active 12,加 LICENSESWITCH
 直挂 = md_required 13。精确匹配。

## 缺口
1. **【文档侧·非 Task 层错误】部署 md 任务示例与 2-00009 字节级同构(均用 VOLUME)**:作为"流量计费"
   特性示例自洽(VOLUME 即本特性语义),无文档缺口。但 2-00009 时长计费 md 同样用 VOLUME(无 TIME
   示例)是文档侧缺口(已记录于 2-00009 pass-2)。**影响**:2-00009/10 两 feature task_intent 仅靠
   特性名语义区分,命令层无差量证据。建议向文档 owner 反馈(2-00009 md 补 TIME 示例)。
2. **【atom 层缺口·冻结】SET SPECTRAFURRGRP 无 atom**:部署 md 步骤10"配置全局缺省URR组
   SET SPECTRAFURRGRP"在任务示例脚本(部署UPF_28813738.md L389)有 1 行,但 atom 层未建该 atom
   (mml_commands.jsonl 含该命令但 tasks/task-0-*.yaml 无)。A 段硬边界(atom 层冻结),本特性不新建。
   md_required 不含 SET SPECTRAFURRGRP,与 2-00001 pass-2 / 2-00003 / 2-00004 / 2-00009 同族特性处理
   一致。已记录于 CONSOLIDATION-BACKLOG.md(atom 演进债),待 atom 层统一补建。
3. **【演进建议·不执行】ADD URR atom 0-00001 的 metering type 取值枚举**:当前 DP 0-00001 option
   effect_detail 已含 "VOLUME/TIME/EVENT/FREE 取值",本特性(VOLUME 默认值)已被覆盖,**无需演进**。

## 10 特性 A 段收尾总结

本特性是 10 特性(2-00001~2-00010)A 段重建的最后一个。收尾状态:
- **STEP-OK 形态特性(纯复用 backbone + 直挂 LICENSE,单变体)**:2-00009(时长)/ 2-00010(流量)
- **backbone owner 特性(多变体,4 场景穷举)**:2-00001(内容计费)
- **专属可选命令特性(新建 feature DP)**:2-00002(在线,3 可选)/ 2-00003(离线,1 可选)/
  2-00004(融合,1 可选)
- **非计费 backbone 特性**:2-00005(PCC)/ 2-00006(TCP重传)/ 2-00007(7层统计)/ 2-00008(异常检测)

计费域攒批人审队列:5 待审条目(2 变更 + 3 新建 DP)+ 3 透明记录(2-00005/09/10 纯复用)。

## 人工校准
- 意见:(待人工填写)
  影响:2-00010 / rule-0-00019 / GWFD-020303-variants.yaml
  反哺Skill条款:(待人工填写)
