## 第一章：BWM 控制体系（带宽控制独有三级架构）

> 带宽控制场景的核心独有对象族。来源：`three-layer-graph/04-command-graph.md` §1.2/§2.1、`feature-knowledge/cross-feature-analysis.md` 附录 D.1、`feature-knowledge/GWFD-110311-基于业务感知的带宽控制.md`、`topic-knowledge/Batch-19-UDG业务感知-套餐2带宽控制配置与规则全景.md`。

---

### K101: BWM 三级控制模型 [原理]

BWM（Bandwidth Management）采用**三级控制体系**，与计费三件套（URR/URRGROUP/PCCPOLICYGRP）平行独立：

| 层级 | 对象 | 作用 | 命令 |
|------|------|------|------|
| L1 业务实例 | BWMSERVICE | 将 SA 识别的 SVC/APP 映射为 BWM 控制对象 | ADD BWMSERVICE |
| L2 控制器 | BWMCONTROLLER | 定义令牌桶/整形参数（CAR 或 Shaping 参数集） | ADD BWMCONTROLLER |
| L3 用户组+规则 | BWMUSERGROUP → BWMRULE | 用户分组 + 规则绑定（关联 L1 业务与 L2 控制器） | ADD BWMUSERGROUP / ADD BWMRULE |

依赖链（TR-BW-02）：**必须先 ADD BWMSERVICE，再 ADD BWMCONTROLLER，BWMRULE 同时引用两者**。

---

### K102: BWMSERVICE — 业务实例 [配置]

定义 BWM 要控制的业务实例，承接 SA 识别结果。

**ADD BWMSERVICE 关键参数**：
- `NAME`：BWM 服务实例名（被 BWMRULE.BWMSERVICENAME 引用）
- `BWMSERVICETYPE`：业务类型（如 NONTOS）
- `PROTOCOLNAME`：协议名（如 bittorrent、youtube）

**配置实例**：
```mml
ADD BWMSERVICE:NAME="p2p_svc",BWMSERVICETYPE=NONTOS,PROTOCOLNAME="bittorrent";
```

---

### K103: BWMCONTROLLER — 控制器 [配置]

定义限速/整形参数。`CTRLTYPE` 决定参数集（CR-BW-02），CAR 与 SHAPING 参数集互斥。

**CTRLTYPE=CAR 参数集**（令牌桶三色标记，详见 `02-CAR限速参数.md`）：
- `CIR`（承诺信息速率，kbps）、`PIR`（峰值信息速率，kbps）
- `CBS`（承诺突发尺寸，bytes）、`PBS`（峰值突发尺寸，bytes）
- `GREENACT` / `YELLOWACT` / `REDACT`（三色报文动作：PASS/REMARK/DISCARD）

**CTRLTYPE=SHAPING 参数集**（整形队列，详见 `03-Shaping整形.md`）：
- `RATE`（整形速率，kbps）、`QUEDEPTH`（GTS 队列深度，packets）

**公共参数**：`COLORISAWARE`（颜色感知）、`WORKMODE`（AUTO/MANUAL，智能 Shaping）。

**配置实例**（CAR）：
```mml
ADD BWMCONTROLLER:BWMCNAME="p2p_car",CTRLTYPE=CAR,
  CIR=2048,CBS=256000,PIR=4096,PBS=512000,
  GREENACT=PASS,YELLOWACT=REMARK,REDACT=DISCARD;
```

**配置实例**（Shaping）：
```mml
ADD BWMCONTROLLER:BWMCNAME="video_shaping",CTRLTYPE=SHAPING,
  RATE=10000,QUEDEPTH=256;
```

---

### K104: BWMUSERGROUP — 用户组 [配置]

定义 BWM 控制对象的用户分组，支持用户级与组级控制。

**ADD BWMUSERGROUP 关键参数**：
- `USERGROUPTYPE`：`SPECIFIC_GROUP`（特定用户组） / `GLOBAL`（全局）
- `USERGROUPNAME`：用户组名
- `USERGROUPPRI`：用户组优先级
- `USERLEVSRVTYPE`：用户级业务类型（如 NONTOS）

**配置实例**：
```mml
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,
  USERGROUPNAME="gold_users",USERGROUPPRI=1,USERLEVSRVTYPE=NONTOS;
```

---

### K105: BWMRULE / BWMRULEGLOBAL — 规则 [配置]

建立 BWM 规则，关联 BWMSERVICE（匹配业务）与 BWMCONTROLLER（执行控制）。

**ADD BWMRULE 关键参数**：
- `BWMRULETYPE`：`SUBSCRIBER_SPECIFIC`（用户级） / `GROUP_SPECIFIC`（组级） / `GLOBAL`（全局）
- `BWMSERVICENAME`：引用 BWMSERVICE
- `UPBWMCTRLNAME1` / `DNBWMCTRLNAME1`：上行/下行 BWM 控制器（引用 BWMCONTROLLER）
- `BWMRULEPRI`：规则优先级（0-65535，数字越小越高）
- `USERGROUPNAME`：所属用户组（GROUP_SPECIFIC 时必填）

**配置实例**：
```mml
ADD BWMRULE:BWMRULETYPE=SUBSCRIBER_SPECIFIC,
  BWMSERVICENAME="p2p_svc",
  UPBWMCTRLNAME1="p2p_car",DNBWMCTRLNAME1="p2p_car",
  BWMRULEPRI=1;
```

**ADD BWMRULEGLOBAL**（整机级业务带宽控制，无需 USERGROUPNAME）：
```mml
ADD BWMRULEGLOBAL:BWMSERVICENAME="p2p_svc",
  UPBWMCTRLNAME1="p2p_car",DNBWMCTRLNAME1="p2p_car";
```

---

### K106: APN 绑定与按 DNN 生效 [配置]

通过 APNBINDBWMUSRG 将 BWM 用户组绑定到 APN/DNN，使 BWM 控制按接入点生效。

```mml
ADD APNBINDBWMUSRG:APNNAME="internet",BWMUSERGROUPNAME="gold_users";
```

---

### K107: BWM 全局使能与前置门控 [配置]

BWM 功能全局使能，是所有 BWM 策略生效的前提：

```mml
SET BANDWIDTHMNG:SWITCH=ENABLE;
```

前置门控：License + SA 特征库加载 + BWM 全局使能（详见 `08-License前置门控.md`）。

---

### K108: BWM 与 PCC 的独立匹配关系 [隐性规则]

> 对应 BusinessRule BR-BW-03。来源：`feature-knowledge/cross-feature-analysis.md` §5、`topic-knowledge/Batch-18-UDG业务感知专题-规则匹配流程与套餐配置.md`。

- BWM 规则与 PCC 规则在 SA 七步流程中**独立匹配，互不干扰**，可叠加执行
- **BWM 管有线侧（用户面限速整形），PCC 管无线侧（QoS 调度）**
- 误以为两者冲突而删除其一，会导致某一段带宽失控
- POLICYTYPE=BWM 标识 BWM 规则，与 POLICYTYPE=PCC/QOS/ADC 通过 RULE 名空间区分（CR-BW-01）

---

### K109: CAR 与 Shaping 不可同对象叠加 [隐性规则]

> 对应 CommandRule CR-BW-03。来源：`feature-knowledge/GWFD-110311-基于业务感知的带宽控制.md`、`GWFD-020354-基于业务的Shaping.md`。

- 同一业务流（同一 BWMSERVICE）**不能同时绑定 CAR 控制器和 Shaping 控制器**
- 选型规则：低价值业务（P2P）用 CAR 直接丢弃超额；高价值业务（视频）用 Shaping 缓冲
- 叠加会导致流量被双重控制，业务中断或性能劣化

---

### K110: BWM 三级控制端到端配置链路 [方案设计]

> 来源：`feature-knowledge/cross-feature-analysis.md` 附录 D.1。

```
基础门控(License + SA特征库 + SET BANDWIDTHMNG)
  → BWMSERVICE（业务实例）
  → BWMCONTROLLER（CAR 或 Shaping 参数集）
  → BWMUSERGROUP（用户分组）
  → BWMRULE（关联 Service + Controller + UserGroup）
  → APNBINDBWMUSRG（按 APN 生效）
  → SET REFRESHSRV（刷新生效，约 60 秒）
```

UNC 侧（双产品协作时）追加：`RULE(POLICYTYPE=BWM) → USERPROFILE → RULEBINDING → USRPROFGROUP → UPBINDUPG → APNUSRPROFG`。

---

### K111: BWM 修改命令链 [配置]

新业务带宽策略调测失败时，按层级修改：
```
MOD BWMCONTROLLER → MOD BWMRULE → MOD BWMUSERGROUP → SET REFRESHSRV
```

体现 BWMSERVICE → BWMCONTROLLER → BWMUSERGROUP → BWMRULE 的层级修改顺序。
