## 第九章：UNC 控制面协同

> UNC 侧策略规则、PCRF 管理、PCC 功能、故障定时器、N7 属性。来源：`three-layer-graph/04-command-graph.md` §1.6~1.10、`feature-knowledge/WSFD-109101-PCC基本功能.md`、`topic-knowledge/Batch-31-UNC-5G基础知识-PCC策略QoS管理与静态规则.md`。

---

### K901: UNC 侧 PCC 框架角色 [原理]

UNC（SMF/PGW-C/GGSN-C）作为控制面 PCEF-C，承担：
- 接收 PCRF/PCF 的 QoS 策略（Gx Diameter / N7 HTTP/2）
- 规则生命周期管理（建立/更新/终止）
- 通过 N4/PFCP 向 UDG 下发执行规则
- Event Triggers 处理（USAGE_REPORT / QOS_CHANGE / APP_STA/STO 等）

---

### K902: PCRF 组冗余体系 [配置]

> Task T-501，TaskCommandOrderEdge TE-501-1~3。

```mml
ADD PCRF:PCRFID=1,FQDN="{fqdn}",IPADDR="{ip}",FEATURELIST=UMCH;
ADD PCRFGROUP:PCRFGROUPNAME="{pg_name}",SELECTMODE={MAIN_STANDBY|POLLING|PERCENTAGE|GROUPID_PRIORITY};
ADD PCRFBINDGRP:PCRFGROUPNAME="{pg_name}",PCRFID=1,PRIORITY=1;
ADD PCRFBINDGRP:PCRFGROUPNAME="{pg_name}",PCRFID=2,PRIORITY=2;   (备)
SET DFTGLBPCRFGRP:PCRFGROUPNAME="{pg_name}";   (缺省全局 PCRF 组，可选)
```

**SELECTMODE 模式**：
- `MAIN_STANDBY`：主备模式
- `POLLING`：轮询模式
- `PERCENTAGE`：百分比模式
- `GROUPID_PRIORITY`：GROUPID+PRIORITY 模式

---

### K903: PCRF FEATURELIST（UMCH） [配置]

`FEATURELIST=UMCH`：PCRF 的 UMCH（Usage Monitoring Congestion Handling）特性，Gx 场景 FUP 必需。
- 使能 PCRF 的拥塞处理能力
- 与 SET PCCFUNC:MKPARSEFORMAT 配合使用

---

### K904: PCC 功能使能 [配置]

> Task T-502。

```mml
SET PCCFUNC:MKPARSEFORMAT=ENABLE,FUPSESSIONEXC={ENABLE|DISABLE};
SET APNPCCFUNC:APNNAME="{apn}",PCCSWITCH=ENABLE;   (按 APN 粒度)
```

**SET PCCFUNC 关键参数**：
- `MKPARSEFORMAT`：解析格式使能（Gx FUP 场景需 ENABLE）
- `FUPSESSIONEXC`：会话级 FUP 排除开关

---

### K905: PCC 故障与定时器 [配置]

> Task T-503。

```mml
SET PCCFAILACTION:FACTION={CONTINUE|REDIRECT};
SET PCCTIMER:TXTIMER={seconds},TXTIMERRETRY={seconds};
```

- `FACTION=CONTINUE`：PCRF 故障时放通（保障业务可用性）
- `TXTIMER`：Tx 定时器超时（秒）

---

### K906: 接口模式选择（POLICYMODE） [配置]

> DecisionPoint DP-BW-04。Task T-504（N7 属性，仅 5G）。

```mml
SET POLICYMODE:POLICYMODE={Gx|N7};   (UNC 侧)
```

5G 场景额外配置 N7 属性控制：
```mml
SET N7RCVATTRCTRL:...;   (N7 接收属性控制)
SET N7SNDATTRCTRL:...;   (N7 发送属性控制)
```

**仅 N7(5G) 场景需要**；Gx(2/3/4G) 场景不使用。用于适配 PCF 的 QoS 参数格式映射。

---

### K907: UNC 侧标准绑定链 [配置]

> Task T-005，TaskCommandOrderEdge TE-005-1~4。按 APN/DNN 生效的标准绑定链。

```mml
ADD USERPROFILE:UPNAME="{up_name}",UPTYPE=PCC;
ADD RULEBINDING:UPNAME="{up_name}",RULENAME="{rule_name}";
ADD USRPROFGROUP:UPGNAME="{upg_name}";
ADD UPBINDUPG:UPGNAME="{upg_name}",UPNAME="{up_name}";
ADD APNUSRPROFG:APNNAME="{apn}",UPGNAME="{upg_name}";
```

顺序：USERPROFILE → RULEBINDING → USRPROFGROUP → UPBINDUPG → APNUSRPROFG（必须按此序，propagated_context 逐级传递 UPNAME/UPGNAME/APNNAME）。

---

### K908: PCCTEMPLATE — PCC 模板 [配置]

```mml
ADD PCCTEMPLATE:TEMPLATENAME="{tpl_name}",POLICYTYPE={BWM|PCC|QOS|ADC};
```

PCC 模板用于规则复用，POLICYTYPE 标识策略类型分支。

---

### K909: UNC 侧无 REFRESHSRV [隐性规则]

UNC 侧策略**即时生效**，无 REFRESHSRV（与 UDG 侧约 60 秒延迟不同）。
- UDG 侧 SET REFRESHSRV + PROTBINDFLOWF 60 秒定时器（见 `../业务感知域规则.md §1.1`）
- UNC 侧配置完成即下发 N4 到 UDG

---

### K910: 双产品协作的 N4 下发链路 [方案设计]

UDG-UNC 双产品协作的 N4 下发：
```
PCRF/PCF（策略决策）→ Gx/N7 → UNC（PCEF-C）
  → N4/PFCP → UDG（PCEF-U 执行）
  → UDG SA 识别 + BWM 限速/整形 + URR 上报
```

> CS-BW-01/02/03/04/05 均依赖此链路。RULENAME 必须三网元一致（BR-BW-01/CR-BW-05）。
