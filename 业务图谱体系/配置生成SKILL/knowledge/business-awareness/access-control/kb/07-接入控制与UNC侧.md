# 07 · 接入控制与 UNC 侧（CS-AC-07/09）

> **定位**：详解 UNC（SMF/AMF）侧接入控制、位置触发、PCRF 管理、PCC 骨架配置。
> **数据来源**：`访问限制场景/feature-knowledge/WSFD-211001-基于初始接入位置的策略控制.md`、`04-command-graph.md`（§2.11 USRLOCATION、§1.12~1.15 UNC 命令、§3.7 接入控制边、CR-AC-09、§5.7 USRLOCATION 参数）。
> **关联文件**：`02-双轨道动作机制与POLICYTYPE路由.md`（UNC 侧 PCC 骨架）。

---

## 1. 接入控制方案（CS-AC-07）

在注册/会话阶段基于 SAR（服务区域限制）/ 区域漫游 / ODB（所有权闭锁）/ 位置触发等执行粗粒度接入控制，决策"是否允许接入"。

| 控制机制 | 网元 | 阶段 | 说明 |
|---------|------|------|------|
| SAR（Service Area Restriction） | AMF | 注册阶段 | TAI 允许/禁止列表 |
| 区域漫游限制 | AMF | 注册阶段 | RAT / 核心网 / 区域 |
| ODB（Operator Determined Barring） | AMF/HSS | 注册阶段 | 所有权闭锁，欠费禁用 |
| 服务区域限制 | SMF | 会话阶段 | WSFD-105006 |
| 位置触发 | SMF/PCF | 会话阶段 | USRLOCATION 匹配位置组，触发策略下发 |

> UNC 侧接入控制是**粗粒度**（注册/会话阶段），与 UDG 侧业务流**细粒度**控制（CS-AC-01~06）构成完整访问限制链路。

---

## 2. UNC 侧 PCC 骨架命令（CMD-UNC-001~011）

### 2.1 基础配置（CMD-UNC-001~007）

| 命令 | 说明 |
|------|------|
| SET LICENSESWITCH | License 开关（UNC 侧 PCIAL/PCC 等，前缀 LKV2/LKV3W9） |
| SET PCCFUNC | PCC 功能全局设置 |
| SET PCCFAILACTION | PCC 故障处理策略（CONTINUE / REDIRECT，DP-AC-08） |
| SET POLICYMODE | 接口模式（Gx 4G / N7 5G） |
| SET N7RCVATTRCTRL | N7 接收属性控制（5G） |
| SET N7SNDATTRCTRL | N7 发送属性控制（5G） |
| SET FHBYPASS | 紧急旁路 |

### 2.2 PCRF 管理（CMD-UNC-008~011）

| 命令 | 说明 |
|------|------|
| ADD PCRF | PCRF 定义（Gx 对端或 N7 PCF FQDN） |
| ADD PCRFGROUP | PCRF 组（主备/轮询/百分比/GROUPID+PRIORITY 模式） |
| ADD PCRFBINDGRP | PCRF 组绑定 |
| SET DFTGLBPCRFGRP | 缺省全局 PCRF 组 |

---

## 3. UNC 侧规则模板绑定链（CMD-UNC-012~018）

| 命令 | 说明 |
|------|------|
| ADD RULE | UNC 侧规则定义（POLICYTYPE=BWM/PCC/QOS/ADC，间接被位置触发特性引用） |
| ADD USERPROFILE | 用户模板 |
| ADD RULEBINDING | 规则绑定到 UserProfile |
| ADD USRPROFGROUP | 用户模板组（位置触发特性使用） |
| ADD UPBINDUPG | 模板绑定到组（含 LOCGROUPNAME 位置组字段） |
| MOD UPBINDUPG | ★ 修改模板绑定（位置触发场景：UPBINDTYPE=SPECIFIC + LOCGROUPNAME） |
| ADD APNUSRPROFG | APN/DNN 绑定用户模板组 |

> **★ MOD UPBINDUPG 关键**：位置触发场景使用 MOD 而非 ADD，含 LOCGROUPNAME 字段引用位置组。

---

## 4. ★ 位置触发独有命令（CMD-UNC-019~020，访问限制 UNC 侧独有）

### 4.1 USRLOCATION（用户位置，OBJ-AC-USRLOCATION）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| LOCATIONNAME | string | — | 位置名 |
| **LOCATIONTYPE** | enum | **CGI / ECGI / NCGI** | 位置类型（2/3G=CGI、4G=ECGI、5G=NCGI） |
| MCC | string | — | 移动国家码 |
| MNC | string | — | 移动网络码 |
| LAC / ECI / NCI | string | — | 位置区/小区标识（按 LOCATIONTYPE） |

### 4.2 USRLOCATIONGRP（用户位置组，OBJ-AC-USRLOCATIONGRP）

| 参数 | 类型 | 说明 |
|------|------|------|
| LOCGROUPNAME | string | 位置组名（UPBINDUPG.LOCGROUPNAME 引用此） |
| LOCATIONNAME | string | 批量绑定 USRLOCATION |

---

## 5. ★ 动态 PCC vs 本地 PCC 分支（TR-AC-08）

| 场景 | PCRF/PCF | 位置触发配置 | 说明 |
|------|---------|-------------|------|
| 动态 PCC（Gx 4G / N7 5G） | 有 | **跳过 USRLOCATION 配置** | 仅 License + ULI 透传，PCRF/PCF 决策 |
| 本地 PCC（无 PCRF） | 无 | **完整配置 USRLOCATION + USRLOCATIONGRP + MOD UPBINDUPG** | UNC 本地决策 |

**配置决策**：
- DP-AC-03（任务层）接口类型决定走动态还是本地
- 动态 PCC：UNC 将 ULI 透传 PCRF/PCF，由 PCRF/PCF 决策并下发 PCC 规则
- 本地 PCC：UNC 本地配置位置匹配能力，用户激活时匹配 ULI 触发策略下发

---

## 6. 接入控制配置链（本地 PCC 场景）

```mml
!-- 1. UNC PCC 骨架（首次配置，已存在则跳过）
SET LICENSESWITCH: ..., LKV2PCIAL01=ENABLE;  (位置触发 License)
SET PCCFUNC: ...;
SET PCCFAILACTION:FAILACTION={CONTINUE|REDIRECT};  (PCF 容灾 DP-AC-08)
SET POLICYMODE:MODE={GX|N7};  (接口模式)
ADD PCRF / ADD PCRFGROUP / ADD PCRFBINDGRP / SET DFTGLBPCRFGRP ...

!-- 2. 规则与用户模板（与 UPF 侧 RULENAME 一致，BR-AC-01）
ADD RULE:RULENAME="{rule_name}", ...;
ADD USERPROFILE:USERPROFILENAME="{up_name}", ...;
ADD RULEBINDING:USERPROFILENAME="{up_name}", RULENAME="{rule_name}";

!-- 3. ★ 位置触发链（仅本地 PCC 场景）
ADD USRLOCATION:LOCATIONNAME="{loc_cg1}", LOCATIONTYPE=CGI, MCC="460", MNC="00", LAC="{lac1}";  (2/3G)
ADD USRLOCATION:LOCATIONNAME="{loc_ec1}", LOCATIONTYPE=ECGI, MCC="460", MNC="00", ECI="{eci1}";  (4G)
ADD USRLOCATION:LOCATIONNAME="{loc_nc1}", LOCATIONTYPE=NCGI, MCC="460", MNC="00", NCI="{nci1}";  (5G)
ADD USRLOCATIONGRP:LOCGROUPNAME="{loc_grp_area1}", LOCATIONNAME="{loc_cg1},{loc_ec1},{loc_nc1}";
ADD USRPROFGROUP:USERPROFGNAME="{upg_area1}", ...;
MOD UPBINDUPG:USERPROFGNAME="{upg_area1}", USERPROFILENAME="{up_name}", UPBINDTYPE=SPECIFIC, LOCGROUPNAME="{loc_grp_area1}";  (★ MOD 含 LOCGROUPNAME)
ADD APNUSRPROFG:APN="{apn}", USERPROFGNAME="{upg_area1}";
```

> **动态 PCC 场景**：跳过第 3 步，仅靠 License + ULI 透传。

---

## 7. UNC 侧与 UDG 侧的协作（跨 UDG-UNC 解耦）

UNC 侧配置（USRLOCATION + USRLOCATIONGRP + MOD UPBINDUPG）后：
1. 用户激活时携带 ULI（User Location Information）
2. UNC 匹配位置组（本地 PCC）或透传 PCRF/PCF（动态 PCC）
3. UNC 下发 PCC 策略（经 N4 PFCP）
4. **UDG 侧动作由 USERPROFILE 绑定的规则定义**（T-AC-101~T-AC-108）

> UNC 侧位置触发**本身不产生访问限制动作**，动作由 UDG 侧执行（CU 解耦）。

---

## 8. ★ 三网元位置一致性（CR-AC-09）

位置信息一致性要求：
- CGI/ECGI/NCGI 取值需 **UNC + RAN + PCRF/PCF 三处一致**
- 跨网元位置不一致导致策略无法匹配，访问限制失效（critical 级）

其他三网元一致性（见 `../业务感知域规则.md` §2）：
- RULENAME / FLOWFILTERNAME 在 PCF、SMF、UPF 三处一致（预定义规则场景）
- URL 过滤 CATEGORYID 在 UDG + ICAP Server + PCRF/PCF 三处一致
- ADC 场景 FLOWFILTERNAME / appid 三网元一致

---

## 9. PCF 容灾决策（DP-AC-08）

| 选项 | 语义 | 影响 |
|------|------|------|
| 回落本地 PCC（SET PCCFAILACTION=CONTINUE） | PCF 故障时回落本地 PCC 策略 | 本地 PCC 精细化程度低于 PCF 策略 |
| 会话失败（严格模式） | PCF 故障时会话失败 | 严格但影响可靠性 |
| DNN 粒度混合（动态+本地） | 部分 DNN 动态，部分本地 | 灵活但配置复杂 |

---

## 10. 关键规则索引

| 规则 ID | 规则名 | 核查要点 |
|---------|--------|---------|
| BR-AC-01 | 预定义规则三网元一致性 | RULENAME/URRID/FLOWFILTER 三网元一致 |
| BR-AC-04 | License 前置门控 | WSFD-211001 需 PCC + BWM（无 PCRF 场景） |
| CR-AC-09 | 预定义规则名三网元一致 | 位置信息 CGI/ECGI/NCGI 三处一致 |
| TR-AC-08 | 位置触发动态/本地 PCC 分支 | 动态跳过 USRLOCATION，本地完整配置 |
