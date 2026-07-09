# 网元对接三层图谱 · 第3层：任务原子层（目录原生重构版）

> 文件定位：`three-layer-graph/03-task-layer.md`
> 作用：把目录原生特性拆成可复用 ConfigTask，不再沿用旧版“产品特性引用型 task”。

---

## 1. ConfigTask 总览（14个）

| `task_id` | `task_name` | `task_scope_type` | 来源目录 |
|---|---|---|---|
| `T-ND-01` | 架构认知与角色确认 | `generic` | `了解组网架构/` |
| `T-ND-02` | 加载License | `generic` | `License申请与加载/` |
| `T-ND-03` | 配置基础数据与MTU | `generic` | `基础数据配置/` `修改MTU值_*.md` |
| `T-ND-04` | 配置二次授权与证书开关 | `generic` | `基础数据配置/` `配置网元和网管对接_*.md` |
| `T-ND-05` | 配置网管纳管 | `cross_feature` | `配置网元和网管对接_*.md` |
| `T-ND-06` | 配置N4控制面接口 | `feature_specific` | `配置N4(N4_Sxa_Sxb)接口数据_*.md` |
| `T-ND-07` | 配置业务用户面接口 | `feature_specific` | `配置Sa/Sc/Pa/S11-U/SGi_N6接口数据_*.md` |
| `T-ND-08` | 配置Nupf与切片接口 | `feature_specific` | `配置Nupf接口数据_*.md` + 切片相关小节 |
| `T-ND-09` | 配置会话接入数据 | `feature_specific` | `配置会话接入数据_*.md` |
| `T-ND-10` | 配置VPN与外联口基础 | `generic` | `组网路由配置/` |
| `T-ND-11` | 配置路由协议 | `cross_feature` | `组网路由配置/` |
| `T-ND-12` | 配置BFD与隧道叠加 | `cross_feature` | `组网路由配置/` |
| `T-ND-13` | 配置自动部署或级联口 | `cross_feature` | `组网路由配置/` |
| `T-ND-14` | 典型实例映射与整网调测 | `cross_feature` | `典型配置实例/` `整网调测_*.md` |

---

## 2. ConfigTask 实例

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-01` |
| `task_name` | `架构认知与角色确认` |
| `task_summary` | 从目录中的架构章节抽取当前部署角色、参考点、逻辑接口抽象和组网前提 |
| `scope_type` | `generic` |
| `goal` | 为所有后续 task 提供统一的角色、接口和组网上下文 |
| `input` | 部署角色、接口抽象策略、参考点理解 |
| `output` | 部署角色判定、接口范围清单 |
| `command_refs` | `[]` |
| `source_evidence_ids` | `["EV-TK-01"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-02` |
| `task_name` | `加载License` |
| `task_summary` | 完成 License 上传、激活和控制项可用性确认 |
| `scope_type` | `generic` |
| `goal` | 使目录后续章节所需能力可用 |
| `input` | ESN、License文件、加载路径 |
| `output` | License 已激活状态 |
| `command_refs` | `["DSP RVKLICINFO"]` |
| `source_evidence_ids` | `["EV-TK-01"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-03` |
| `task_name` | `配置基础数据与MTU` |
| `task_summary` | 完成 NTP、网元基本信息、公共参数、MTU 等基础配置 |
| `scope_type` | `generic` |
| `goal` | 形成稳定可纳管、可对接、可转发的基础状态 |
| `input` | NTP地址、ME/OMIP、公共参数值、MTU规划 |
| `output` | 基础数据配置完成 |
| `command_refs` | `["SET NTP","MOD ME","SET OMIP","SET SIGDSCP","SET UDPCHECKSUM","SET SRVCOMMONPARA","SET QOSCAR","SET IPV6FRAGPLCY","SET CPTEIDUALLOC","SET TZ","SET ANTIFRAUD","SET FWDPARA","SET HEADENGLBPARA","SET MSFAULTALARM","SET FABRICMTU","MOD INTERFACE","SET IFIPV6ENABLE"]` |
| `source_evidence_ids` | `["EV-TK-02"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-04` |
| `task_name` | `配置二次授权与证书开关` |
| `task_summary` | 完成高危命令授权闭环和证书相关前置开关 |
| `scope_type` | `generic` |
| `goal` | 避免后续高危命令或证书相关操作被阻断 |
| `input` | 授权用户、命令成员、证书需求 |
| `output` | 安全接入前置完成 |
| `command_refs` | `["SET SECAUTH","ADD USRSECAUTH","ADD SECAUTHMEM","SET NEWCERTSWITCH"]` |
| `source_evidence_ids` | `["EV-TK-02"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-05` |
| `task_name` | `配置网管纳管` |
| `task_summary` | 完成北向用户、SNMPv3、适配层和创建网元闭环 |
| `scope_type` | `cross_feature` |
| `goal` | 使网元可被 MAE/U2020 纳管 |
| `input` | 北向密码、SNMPv3 密钥、适配层版本、网元参数 |
| `output` | 网元纳管成功 |
| `command_refs` | `["LST ME"]` |
| `source_evidence_ids` | `["EV-TK-02"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-06` |
| `task_name` | `配置N4控制面接口` |
| `task_summary` | 配置 N4if、VPN_Signaling 和 UPF 标识 |
| `scope_type` | `feature_specific` |
| `goal` | 建立 N4 控制面入口 |
| `input` | N4 地址、信令 VPN、HOSTNAME |
| `output` | N4if 就绪 |
| `command_refs` | `["ADD VPNINST","ADD LOGICINF","SET UPINFO"]` |
| `source_evidence_ids` | `["EV-TK-03"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-07` |
| `task_name` | `配置业务用户面接口` |
| `task_summary` | 配置 Sa/Sc/Pa/S11-U/SGi/N6 等业务接口 |
| `scope_type` | `feature_specific` |
| `goal` | 建立业务面承载路径 |
| `input` | 接口清单、IP版本、接口地址 |
| `output` | 业务逻辑接口就绪 |
| `command_refs` | `["ADD VPNINST","ADD LOGICINF"]` |
| `source_evidence_ids` | `["EV-TK-03"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-08` |
| `task_name` | `配置Nupf与切片接口` |
| `task_summary` | 配置 Nupf 服务化接口和切片绑定 |
| `scope_type` | `feature_specific` |
| `goal` | 处理需要 Nupf 或切片场景的分支接口能力 |
| `input` | 是否启用 Nupf、切片参数 |
| `output` | Nupf 或切片绑定完成 |
| `command_refs` | `["ADD SNSSAIUPINTF","ADD LOGICIP","ADD HTTPLEGRP","ADD HTTPLE","ADD SBIAPLE","SET HTTPCONF"]` |
| `source_evidence_ids` | `["EV-TK-03"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-09` |
| `task_name` | `配置会话接入数据` |
| `task_summary` | 配置 APN、地址池、地址段、绑定关系和 IP 分配规则 |
| `scope_type` | `feature_specific` |
| `goal` | 形成会话接入数据闭环 |
| `input` | APN/DNN、地址池类型、地址段、分配规则 |
| `output` | 会话接入数据可用 |
| `command_refs` | `["ADD APN","SET APNSGLPASS","ADD POOL","ADD SECTION","ADD POOLGROUP","ADD POOLBINDGROUP","ADD POOLGRPMAP","SET IPALLOCRULE"]` |
| `source_evidence_ids` | `["EV-TK-03"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-10` |
| `task_name` | `配置VPN与外联口基础` |
| `task_summary` | 配置路由侧 VPN 实例、地址族、目标和外联口基础设施 |
| `scope_type` | `generic` |
| `goal` | 为后续路由协议与隧道叠加提供容器和承载口 |
| `input` | VPN名、地址族、外联口方案 |
| `output` | 外联基础完成 |
| `command_refs` | `["ADD L3VPNINST","ADD VPNINSTAF","MOD VPNINSTAF","ADD VPNTARGET","ADD IPBINDVPN"]` |
| `source_evidence_ids` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-11` |
| `task_name` | `配置路由协议` |
| `task_summary` | 按分支实施 OSPF/OSPFv3、静态路由、BGP over OSPF、BGP over静态、MPLS VPN 等协议链 |
| `scope_type` | `cross_feature` |
| `goal` | 让路由在当前组网模式下稳定收敛 |
| `input` | 路由协议、IP版本、部署方式、组网模式 |
| `output` | 路由协议生效 |
| `command_refs` | `["ADD OSPF","ADD OSPFAREA","ADD OSPFNETWORK","ADD OSPFINTERFACE","ADD OSPFIMPORTROUTE","ADD OSPFV3","ADD OSPFV3AREA","ADD OSPFV3INTERFACE","ADD OSPFV3IMPORTROUTE","SET BGP","ADD BGPVRF","ADD BGPVRFAF","ADD BGPPEER","ADD BGPPEERAF","ADD IMPORTROUTE","ADD NETWORKROUTE","ADD SRROUTE","ADD SRROUTE6"]` |
| `source_evidence_ids` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-12` |
| `task_name` | `配置BFD与隧道叠加` |
| `task_summary` | 按分支实施 BFD、IPsec、GRE、MPLS 全局与接口 |
| `scope_type` | `cross_feature` |
| `goal` | 提供快速故障检测和隧道增强能力 |
| `input` | BFD模式、隧道类型、MPLS需求 |
| `output` | BFD和隧道侧生效 |
| `command_refs` | `["SET BFD","ADD BFDSESSION","ADD GRETUNNEL","MOD GRETUNNEL","SET MPLSSITE","ADD MPLSIF","SET DHCP6CLIENTDUID","ADD IPsec 系列命令"]` |
| `source_evidence_ids` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-13` |
| `task_name` | `配置自动部署或级联口` |
| `task_summary` | 按是否自动部署、是否 NP100/加速卡进入 AUTOSCALING 或级联口路径 |
| `scope_type` | `cross_feature` |
| `goal` | 完成自动部署模板下发或硬件级联准备 |
| `input` | 自动/手工、硬件类型、模板参数 |
| `output` | 自动部署模板或级联口可用 |
| `command_refs` | `["LST AUTOCONFIG","DSP OPSASSISTSTATE","SET AUTOCONFIG","ADD AUTOSCALINGETHTRUNK","ADD AUTOSCALINGSERVICE","MOD AUTOSCALINGSERVICE","ADD AUTOSCALINGBFD","ADD AUTOSCALINGSRBFD","ADD AUTOSCALINGSRROUTE","ADD AUTOSCALINGBGPLF","ADD AUTOSCALINGIPREACH","ADD AUTOSCALINGMPLS","ADD NPDIRECTCONNECTPORT"]` |
| `source_evidence_ids` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |

| 字段 | 值 |
|---|---|
| `task_id` | `T-ND-14` |
| `task_name` | `典型实例映射与整网调测` |
| `task_summary` | 将目录实例模板映射到当前方案，并完成路由验证、FirstCall 和整网调测 |
| `scope_type` | `cross_feature` |
| `goal` | 给出可验证的端到端上线结果 |
| `input` | 实例模板、调测路径、验收标准 |
| `output` | 实例套用完成，FirstCall 验证通过 |
| `command_refs` | `["LST LOGICINF","LST VPNINST","LST APN","LST OSPF","LST BGPPEER","DSP BGPPEERINFO","DSP ROUTE","DSP ROUTE6","DSP SRROUTE","DSP OSPFROUTING","DSP OSPFPEER","DSP BFDSESSION","DSP IFSTATUS","DSP SESSIONINFO","NGPING","PING","SRVPING","SRVTRACERT","DSP SERVICERUSTATE","EXP MML"]` |
| `source_evidence_ids` | `["EV-TK-07"]` |

---

## 3. TaskRule（12条）

| `rule_id` | `task_ref` | `rule_name` | `rule_type` | `rule_logic` | `source_evidence_ids` |
|---|---|---|---|---|---|
| `TR-ND-01` | `T-ND-01` | 架构先定后配 | `selection_rule` | 未确认角色和接口抽象前不进入目录后续配置 | `["EV-TK-01"]` |
| `TR-ND-02` | `T-ND-02` | License先于能力使用 | `dependency_rule` | 需要 License 的组网能力必须先完成加载和激活 | `["EV-TK-01"]` |
| `TR-ND-03` | `T-ND-03` | 基础数据成组执行 | `input_output_rule` | 时间、身份、公共参数、MTU 应视为同一组基础任务 | `["EV-TK-02"]` |
| `TR-ND-04` | `T-ND-04` | 高危命令前置授权 | `dependency_rule` | 涉及高危命令的后续操作依赖授权闭环 | `["EV-TK-02"]` |
| `TR-ND-05` | `T-ND-05` | 网管纳管依赖网元身份 | `dependency_rule` | 创建网元前，名称和 IP 必须已确定 | `["EV-TK-02"]` |
| `TR-ND-06` | `T-ND-06` | N4单独不可闭环 | `validation_rule` | N4 配完后仍需用户面接口配合才能形成完整对接 | `["EV-TK-03"]` |
| `TR-ND-07` | `T-ND-07` | 用户面接口按场景裁剪 | `selection_rule` | 不是所有接口都必配，按角色和场景裁剪 | `["EV-TK-03"]` |
| `TR-ND-08` | `T-ND-09` | 地址池模式二选一 | `scope_rule` | LOCAL/EXTERNAL 两类模式不可混淆 | `["EV-TK-03"]` |
| `TR-ND-09` | `T-ND-11` | 协议链服从目录分支 | `selection_rule` | 协议组合由目录分支给定，不自由混搭 | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TR-ND-10` | `T-ND-12` | BFD与隧道按模式叠加 | `reuse_rule` | BFD、IPsec、GRE、MPLS VPN 是路由主链的可选增强，不是永远并列必做 | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TR-ND-11` | `T-ND-13` | 自动部署有严格时序 | `dependency_rule` | 自动部署必须遵守开关和模板顺序 | `["EV-TK-04"]` |
| `TR-ND-12` | `T-ND-14` | 调测以实例模板为主线 | `validation_rule` | 调测优先沿实例模板映射，不脱离实例链路 | `["EV-TK-07"]` |

---

## 4. FeatureTaskOrderEdge（12条）

| `edge_id` | `owner_ref` | `from_task_ref` | `to_task_ref` | `relation_type` | `requiredness` | `source_evidence_ids` |
|---|---|---|---|---|---|---|
| `FE-ND-01` | `ND-FEAT-01` | `T-ND-01` | `T-ND-02` | `precedes` | `required` | `["EV-TK-01"]` |
| `FE-ND-02` | `ND-FEAT-02` | `T-ND-02` | `T-ND-03` | `precedes` | `required` | `["EV-TK-01","EV-TK-02"]` |
| `FE-ND-03` | `ND-FEAT-03` | `T-ND-04` | `T-ND-05` | `precedes` | `required` | `["EV-TK-02"]` |
| `FE-ND-04` | `ND-FEAT-04` | `T-ND-05` | `T-ND-06` | `depends_on` | `required` | `["EV-TK-02","EV-TK-03"]` |
| `FE-ND-05` | `ND-FEAT-05` | `T-ND-06` | `T-ND-07` | `precedes` | `required` | `["EV-TK-03"]` |
| `FE-ND-06` | `ND-FEAT-05` | `T-ND-07` | `T-ND-08` | `fallback_to` | `optional` | `["EV-TK-03"]` |
| `FE-ND-07` | `ND-FEAT-06` | `T-ND-07` | `T-ND-09` | `depends_on` | `required` | `["EV-TK-03"]` |
| `FE-ND-08` | `ND-FEAT-07` | `T-ND-10` | `T-ND-11` | `precedes` | `required` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `FE-ND-09` | `ND-FEAT-07` | `T-ND-11` | `T-ND-12` | `precedes` | `optional` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `FE-ND-10` | `ND-FEAT-07` | `T-ND-10` | `T-ND-13` | `fallback_to` | `optional` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `FE-ND-11` | `ND-FEAT-08` | `T-ND-11` | `T-ND-14` | `depends_on` | `required` | `["EV-TK-07"]` |
| `FE-ND-12` | `ND-FEAT-08` | `T-ND-12` | `T-ND-14` | `depends_on` | `optional` | `["EV-TK-07"]` |

---

## 5. TaskCommandOrderEdge（26条，按任务聚合）

| `edge_id` | `task_ref` | `from_command_ref` | `to_command_ref` | `relation_type` | `source_evidence_ids` |
|---|---|---|---|---|---|
| `TE-ND-03-01` | `T-ND-03` | `SET NTP` | `MOD ME` | `precedes` | `["EV-TK-02"]` |
| `TE-ND-03-02` | `T-ND-03` | `MOD ME` | `SET OMIP` | `precedes` | `["EV-TK-02"]` |
| `TE-ND-03-03` | `T-ND-03` | `SET OMIP` | `SET SIGDSCP` | `precedes` | `["EV-TK-02"]` |
| `TE-ND-03-04` | `T-ND-03` | `SET SIGDSCP` | `SET FABRICMTU` | `precedes` | `["EV-TK-02"]` |
| `TE-ND-04-01` | `T-ND-04` | `SET SECAUTH` | `ADD USRSECAUTH` | `precedes` | `["EV-TK-02"]` |
| `TE-ND-04-02` | `T-ND-04` | `ADD USRSECAUTH` | `ADD SECAUTHMEM` | `precedes` | `["EV-TK-02"]` |
| `TE-ND-06-01` | `T-ND-06` | `ADD VPNINST` | `ADD LOGICINF` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-06-02` | `T-ND-06` | `ADD LOGICINF` | `SET UPINFO` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-07-01` | `T-ND-07` | `ADD VPNINST` | `ADD LOGICINF` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-08-01` | `T-ND-08` | `ADD LOGICIP` | `ADD HTTPLEGRP` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-08-02` | `T-ND-08` | `ADD HTTPLEGRP` | `ADD HTTPLE` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-08-03` | `T-ND-08` | `ADD HTTPLE` | `ADD SBIAPLE` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-09-01` | `T-ND-09` | `ADD APN` | `ADD POOL` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-09-02` | `T-ND-09` | `ADD POOL` | `ADD SECTION` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-09-03` | `T-ND-09` | `ADD SECTION` | `ADD POOLGROUP` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-09-04` | `T-ND-09` | `ADD POOLGROUP` | `ADD POOLBINDGROUP` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-09-05` | `T-ND-09` | `ADD POOLBINDGROUP` | `ADD POOLGRPMAP` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-09-06` | `T-ND-09` | `ADD POOLGRPMAP` | `SET IPALLOCRULE` | `precedes` | `["EV-TK-03"]` |
| `TE-ND-10-01` | `T-ND-10` | `ADD L3VPNINST` | `ADD VPNINSTAF` | `precedes` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TE-ND-10-02` | `T-ND-10` | `ADD VPNINSTAF` | `ADD VPNTARGET` | `precedes` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TE-ND-11-01` | `T-ND-11` | `ADD OSPF` | `ADD OSPFAREA` | `precedes` | `["EV-TK-04"]` |
| `TE-ND-11-02` | `T-ND-11` | `SET BGP` | `ADD BGPVRF` | `precedes` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TE-ND-11-03` | `T-ND-11` | `ADD BGPVRF` | `ADD BGPPEER` | `precedes` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TE-ND-12-01` | `T-ND-12` | `SET BFD` | `ADD BFDSESSION` | `precedes` | `["EV-TK-04","EV-TK-05","EV-TK-06"]` |
| `TE-ND-13-01` | `T-ND-13` | `SET AUTOCONFIG` | `ADD AUTOSCALINGSERVICE` | `precedes` | `["EV-TK-04"]` |
| `TE-ND-13-02` | `T-ND-13` | `ADD AUTOSCALINGSERVICE` | `DSP OPSASSISTSTATE` | `must_be_last` | `["EV-TK-04"]` |

---

## 6. 合规声明

- Task 只作为目录原生配置动作原子存在
- Task 通过 `invokes` 落命令层
- Task 不直接持有参数细节，参数差异由 `04-command-graph.md` 表达
