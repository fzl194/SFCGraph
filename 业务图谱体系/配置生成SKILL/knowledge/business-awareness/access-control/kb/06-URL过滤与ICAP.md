# 06 · URL 过滤与 ICAP（轨道 B 独立体系）

> **定位**：详解轨道 B（URL 过滤）的 ICAP 互通前置链 + CFTEMPLATE/CONTCATEGBIND 显式动作体系。
> **数据来源**：`访问限制场景/feature-knowledge/GWFD-110471-URL过滤基本功能.md`、`04-command-graph.md`（§2.9/2.10 URL 过滤对象、§3.6 关系边、CR-AC-05/06/09、§5.6 CFTEMPLATE/CONTCATEGBIND 参数）。
> **关联文件**：`02-双轨道动作机制与POLICYTYPE路由.md`（轨道 B 独立动作体系）。

---

## 1. 轨道 B 核心特性

| 特性 | 说明 |
|------|------|
| 动作指定方式 | **显式**（CFTEMPLATE.ACTION / CONTCATEGBIND.ACTION = BLOCK/PERMIT/REDIRECT） |
| 配置对象体系 | **独立于 RULE 体系**（CFTEMPLATE/CONTCATEGBIND/ICAP 系列） |
| 外部依赖 | **必需 ICAP Server**（URL 分类数据库提供方） |
| PERMIT 支持 | **唯一显式支持 PERMIT 的轨道**（BR-AC-10, CR-AC-06） |
| RULE 触发 | POLICYTYPE=PCC 仅作匹配触发，**动作不走 CFTEMPLATE/CONTCATEGBIND，不走 PCCPOLICYGRP**（TR-AC-03） |
| HTTPS 限制 | 仅能基于 SNI 做分类（不能解析完整 URL，CR-AC-10） |

---

## 2. URL 过滤配置链三层结构（TR-AC-05）

```
第 1 层：ICAP 互通前置（TR-AC-05 硬约束，断裂则 URL 过滤不生效）
  VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG → SET CFSRVMODE

第 2 层：CF 业务（轨道 B 核心，显式 ACTION）
  APN → SET APNCFFUNC → CFPROFILE → CFTEMPLATE(ACTION) → SET APNCFTEMPLATE → CFPROFBINDCFT
    → CONTCATEGROUP → CONTCATEGBIND(ACTION) → SET CFCACHEPARA → SET GLBCFFUNC
    → (可选) CFWHITEURLLST / CFIPWHITELIST / CFPFSPECACTION

第 3 层：PCC 触发层（共用计费属性，但动作不走 PCCPOLICYGRP）
  URR → URRGROUP → PCCPOLICYGRP
  FILTER/L7FILTER → FLOWFILTER → RULE(POLICYTYPE=PCC, POLICYNAME=PCCPOLICYGRP，仅触发)
```

---

## 3. ICAP 互通前置对象（轨道 B 独立资源层，OBJ-AC-VPNINST 等）

### 3.1 VPNINST（VPN 实例，OBJ-AC-VPNINST）

| 参数 | 类型 | 说明 |
|------|------|------|
| VPNINSTANCE | string | ICAP 互通专网实例名（URL 过滤独有） |

### 3.2 ICAPSERVER（ICAP 服务器，OBJ-AC-ICAPSERVER）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| ICAPSERVERNAME | string | — | ICAP 服务器名 |
| ICAPSERVERTYPE | enum | **URL_FILTERING** | 服务器类型（轨道 B 必需） |
| ICAPSVRIPTYPE | enum | — | 服务器 IP 类型 |
| ICAPSERVERIPV4 | string | IP | 服务器 IP |
| VPNINSTANCE | string | — | 关联 VPN 实例 |

> ICAP Server 是轨道 B 必需外部依赖（CR-AC-05），URL 分类数据库提供方。

### 3.3 ICAPLOCALINFO（ICAP 本端信息，OBJ-AC-ICAPLOCALINFO）

| 参数 | 类型 | 说明 |
|------|------|------|
| ICAPSERVERTYPE | enum | URL_FILTERING |
| USERAGENT | string | UDG 侧 ICAP 本端标识 |

### 3.4 ICAPSVRGRP（ICAP 服务器组，OBJ-AC-ICAPSVRGRP）

| 参数 | 类型 | 说明 |
|------|------|------|
| ICAPSVRGRPNAME | string | 服务器组名 |
| ICAPSERVERTYPE | enum | URL_FILTERING |

### 3.5 ICAPSVRBINDISG（服务器与组绑定，OBJ-AC-ICAPSVRBINDISG）

| 参数 | 类型 | 说明 |
|------|------|------|
| ICAPSVRGRPNAME | string | 服务器组名 |
| ICAPSERVERNAME | string | 服务器名 |

---

## 4. CF 业务层对象（轨道 B 核心动作体系）

### 4.1 CFPROFILE（内容过滤策略，OBJ-AC-CFPROFILE）

| 参数 | 类型 | 说明 |
|------|------|------|
| CFPROFILENAME | string | 策略载体名（与 CONTCATEGBIND 共同决定分类级动作） |

### 4.2 ★ CFTEMPLATE（内容过滤模板，OBJ-AC-CFTEMPLATE）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| CFTEMPLATENAME | string | — | 模板名 |
| ICAPSRVGMNAME | string | — | 引用 ICAPSVRGRP（模板关联 ICAP） |
| **ACTION** | enum | **BLOCK / PERMIT / REDIRECT** | **★ 模板级缺省动作**（PERMIT 仅轨道 B，CR-AC-06） |

> CFTEMPLATE 是 RULE 不引用的独立对象，独立于 RULE 体系。

### 4.3 CFPROFBINDCFT（策略-模板绑定，OBJ-AC-CFPROFBINDCFT）

| 参数 | 类型 | 说明 |
|------|------|------|
| CFTEMPLATENAME | string | 模板名 |
| CFPROFILENAME | string | 策略名 |

### 4.4 APNCFTEMPLATE（APN-模板绑定）

| 参数 | 类型 | 说明 |
|------|------|------|
| APNNAME | string | APN 名 |
| CFTEMPLATENAME | string | 模板名 |

### 4.5 CONTCATEGROUP（内容分类组，OBJ-AC-CONTCATEGROUP）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| CONTCATEGNAME | string | — | 分类组名 |
| CATEGORYTYPE | enum | SPECIFIC | 分类类型 |
| CATEGORYID | int | — | URL 分类 ID（来自 ICAP Server，CR-AC-09 三处一致） |

### 4.6 ★ CONTCATEGBIND（策略与分类组绑定，OBJ-AC-CONTCATEGBIND）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| CFPROFILENAME | string | — | 归属策略 |
| CONTCATEGNAME | string | — | 分类组 |
| **ACTION** | enum | **BLOCK / PERMIT / REDIRECT** | **★ 分类级精确动作**（覆盖 CFTEMPLATE 模板级缺省） |

---

## 5. 动作优先级与 PERMIT 唯一性

### 5.1 动作决策优先级

```
1. CONTCATEGBIND.ACTION（分类级精确动作，最高优先级）
   ↓ 未命中分类
2. CFTEMPLATE.ACTION（模板级缺省动作）
   ↓ 未命中模板
3. 默认放行（无动作）
```

### 5.2 PERMIT 唯一性（BR-AC-10, CR-AC-06）

- **仅轨道 B（URL 过滤）显式支持 PERMIT**
- 轨道 A 特性只能"不做动作（隐式放行）"或"做阻塞/重定向"，**无显式 PERMIT**
- 家长控制/企业白名单场景必须用 URL 过滤（轨道 B）
- 轨道 A 场景下显式 PERMIT 配置无效

---

## 6. URL 过滤其他配置对象

| 命令 | 对象 | 说明 |
|------|------|------|
| SET APNCFFUNC | APNCFFUNC | APN 粒度内容过滤开关 |
| SET CFSRVMODE | CFSRVMODE | URL 过滤业务模式 |
| SET CFCACHEPARA | CFCACHEPARA | 缓存参数（减少 ICAP 交互） |
| SET GLBCFFUNC | GLBCFFUNC | 全局内容过滤开关 |
| ADD CFWHITEURLLST | CFWHITEURLLST | URL 白名单列表（轨道 B 白名单机制） |
| ADD CFIPWHITELIST | CFIPWHITELIST | 内容过滤 IP 白名单 |
| ADD CFPFSPECACTION | CFPFSPECACTION | 指定策略特殊场景动作 |

---

## 7. URL 过滤 RULE 触发层（TR-AC-03）

URL 过滤的 RULE 虽用 POLICYTYPE=PCC 触发匹配，但实际动作**不走 PCCPOLICYGRP**：

```mml
ADD RULE:RULENAME="{rule_url}", POLICYTYPE=PCC, PRIORITY={p}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff}", POLICYNAME="{ppg}";
!-- ★ 此 RULE 仅触发匹配，实际 BLOCK/PERMIT/REDIRECT 动作走 CFTEMPLATE/CONTCATEGBIND
```

---

## 8. 完整配置链示例（URL 过滤 BLOCK）

```mml
!-- 第 1 层：ICAP 互通前置
ADD VPNINST:VPNINSTANCE="{vpn_icap}";
ADD LOGICINF:NAME="{logicinf_icap}", IPVERSION=IPV4, IPV4ADDRESS1="{...}", IPV4MASK1="{...}", VPNINSTANCE="{vpn_icap}";
ADD ICAPSERVER:ICAPSERVERNAME="{icap_svr}", ICAPSERVERTYPE=URL_FILTERING, ICAPSVRIPTYPE=IPV4, ICAPSERVERIPV4="{icap_ip}", VPNINSTANCE="{vpn_icap}";
ADD ICAPLOCALINFO:ICAPSERVERTYPE=URL_FILTERING, USERAGENT="{udg_agent}";
ADD ICAPSVRGRP:ICAPSVRGRPNAME="{icap_grp}", ICAPSERVERTYPE=URL_FILTERING;
ADD ICAPSVRBINDISG:ICAPSVRGRPNAME="{icap_grp}", ICAPSERVERNAME="{icap_svr}";
SET CFSRVMODE: ...;

!-- 第 2 层：CF 业务
ADD APN:APNNAME="{apn}", ...;
SET APNCFFUNC:APNNAME="{apn}", CFSWITCHVALUE=ENABLE;
ADD CFPROFILE:CFPROFILENAME="{cf_profile}";
ADD CFTEMPLATE:CFTEMPLATENAME="{cf_tpl}", ICAPSRVGMNAME="{icap_grp}", ACTION=BLOCK;  (★ 模板级缺省 BLOCK)
SET APNCFTEMPLATE:APNNAME="{apn}", CFTEMPLATENAME="{cf_tpl}";
ADD CFPROFBINDCFT:CFTEMPLATENAME="{cf_tpl}", CFPROFILENAME="{cf_profile}";
ADD CONTCATEGROUP:CONTCATEGNAME="{categ_gambling}", CATEGORYTYPE=SPECIFIC, CATEGORYID=18;  (赌博分类)
ADD CONTCATEGBIND:CFPROFILENAME="{cf_profile}", CONTCATEGNAME="{categ_gambling}", ACTION=BLOCK;  (★ 分类级精确 BLOCK)
SET CFCACHEPARA: ...;
SET GLBCFFUNC: ..., CFSWITCHVALUE=ENABLE;
ADD CFWHITEURLLST: ..., URL="{allowed_url}";  (可选白名单)

!-- 第 3 层：PCC 触发层
ADD URR / ADD URRGROUP / ADD PCCPOLICYGRP ...
ADD FILTER / L7FILTER / FLOWFILTER / FLTBINDFLOWF / PROTBINDFLOWF ...
ADD RULE:RULENAME="{rule_url}", POLICYTYPE=PCC, PRIORITY={p}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff}", POLICYNAME="{ppg}";  (★ 仅触发)

!-- 容器与绑定 + 刷新
ADD USERPROFILE / ADD RULEBINDING ...
SET REFRESHSRV:REFRESHTYPE=ALL;
```

---

## 9. 关键规则索引

| 规则 ID | 规则名 | 核查要点 |
|---------|--------|---------|
| BR-AC-10 | PERMIT 唯一性 | 白名单场景必须用 URL 过滤（轨道 B） |
| CR-AC-05 | ICAP Server 必需 | URL 过滤前置，链路断裂则不生效 |
| CR-AC-06 | URL 过滤 PERMIT 动作唯一性 | 轨道 A 场景显式 PERMIT 配置无效 |
| CR-AC-09 | 预定义规则名三网元一致 | CATEGORYID 需 UDG + ICAP Server + PCRF/PCF 一致 |
| CR-AC-10 | HTTPS/HTTP2.0 加密协议盲区 | HTTPS 场景 URL 过滤仅基于 SNI |
| TR-AC-03 | 双轨动作分离规则 | URL 过滤 RULE 用 PCC 触发但动作走 CFTEMPLATE |
| TR-AC-05 | URL 过滤 ICAP 互通前置 | 必须先配 ICAP 链路再配 CF 业务 |
