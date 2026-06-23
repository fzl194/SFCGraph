# Phase 5 参考文件：配置生成

## ⚠ 阶段执行约束（必须遵守）

**本文件仅用于 Phase 5。执行本文件内容前必须满足以下前置条件，否则 STOP：**

1. **用户必须已确认参数表**：必须已通过 GATE-4（用户在 Phase 4 明确确认了参数表，含动作轨道 A/B 选择与各子轨参数）。如果用户未确认参数，**STOP**，回到 Phase 4 等待用户确认。没有例外。
2. **方案和参数必须已确定**：必须有 Phase 1 输出的匹配结果（场景/方案/决策点/★动作轨道）和 Phase 3 输出的完整参数表（LLD）。缺少任何一个，**STOP**，回到对应阶段补全。
3. **本阶段完成后进入 Phase 6 核查**：生成配置后必须经过 Phase 6 核查和 Phase 6.5 用户确认（GATE-5），不得直接交付给用户。

---

> 本文件定义 Phase 5 的 pipeline 要求、输出模板和排序规则（访问限制场景专属）。
> 业务知识（双轨道参数映射、协议差异、动作对象体系）由 Agent 从图谱和知识库动态加载。
> **域共享规则**（执行时序、跨网元一致性、优先级、SA 前置）见 `../业务感知域规则.md` §1~§5，本文件不复述，仅引用。

---

## 1. Pipeline 步骤

### Step 1: 加载配置规则

**必须加载**：
- `../../访问限制场景/three-layer-graph/04-command-graph.md` — 读取 MMLCommand 定义和 CommandParameter（§5 各命令关键参数集），确认参数枚举值
- `04-command-graph.md` CommandRule (CR-AC-01~14) — 了解命令级约束
- `../kb/02-双轨道动作机制与POLICYTYPE路由.md` — **★ 双轨道+五子轨配置链核心**
- 按匹配的 CS 闭包加载对应 `kb/` 子章节（见 Step 2）

**当 DP-AC-04 包含 SMF/AMF 时额外加载**：
- `../kb/07-接入控制与UNC侧.md` — UNC 侧命令模板和参数差异

### Step 2: 按动作轨道选择配置链模板

**★ 双轨道+五子轨是访问限制场景区别于计费（单轨 CHARGING）的核心架构**。根据 DP-AC-03（动作轨道）和 DP-AC-01（动作类型）选择对应配置链：

| 动作轨道 | POLICYTYPE / ACTION | 配置链模板 | 适用方案 |
|---------|--------------------|----------|---------|
| **轨道 A · PCC 子轨** | POLICYTYPE=PCC | §2.1 PCC 阻塞链 | CS-AC-01 / CS-AC-08 / CS-AC-09 |
| **轨道 A · ADC 子轨** | POLICYTYPE=ADC | §2.2 ADC 链 | ADC 兜底阻塞（CS-AC-01 衍生） |
| **轨道 A · HEADEN 子轨** | POLICYTYPE=HEADEN | §2.3 头增强链 | CS-AC-02 |
| **轨道 A · SMARTREDIRECT 子轨** | POLICYTYPE=SMARTREDIRECT | §2.4 HTTP 重定向链 / §2.5 DNS 纠错链 | CS-AC-03 / CS-AC-04 |
| **轨道 A · WEBPROXY 子轨** | POLICYTYPE=WEBPROXY | §2.6 Portal 链 / §2.7 WebProxy 链 | CS-AC-05 |
| **轨道 B · URL 过滤** | CFTEMPLATE.ACTION / CONTCATEGBIND.ACTION | §2.8 URL 过滤链 | CS-AC-06 |
| **UNC 接入控制** | (UNC 侧，USRLOCATION) | §2.9 接入控制链 | CS-AC-07 / CS-AC-09 |

### Step 3: 按排序规则排列命令（见 §3）

### Step 4: 自检

**必须加载**：
- `01-business-graph.md` BusinessRule (BR-AC-01~10) — 确认业务约束已满足
- `04-command-graph.md` CommandRule (CR-AC-01~14) — 确认命令级约束已满足

---

## 2. 各轨道配置链模板（UDG 侧，按双轨道五子轨分组）

> **参数值必须从 `04-command-graph.md` §5 CommandParameter 定义中获取枚举值和格式要求，禁止凭记忆填写。**
> **所有示例保留原始 MML 格式，参数值用 `{占位符}` 表示。**

### 2.1 轨道 A · PCC 阻塞链（CS-AC-01）

```mml
!-- 1. 底层过滤条件（如需新建）
ADD FILTER:FILTERNAME="{filter_name}", L34PROTTYPE={...}, L34PROTOCOL={...}, SRCIP="{...}", DSTIP="{...}";
ADD L7FILTER:L7FILTERNAME="{l7_name}", URL="{...}", METHODTYPE={...};  (仅 L7 场景)

!-- 2. 流过滤器与绑定
ADD FLOWFILTER:FLOWFILTERNAME="{ff_name}";
ADD FLTBINDFLOWF:FLOWFILTERNAME="{ff_name}", FILTERNAME="{filter_name}";
ADD PROTBINDFLOWF:FLOWFILTERNAME="{ff_name}", PROTOCOLNAME="http", L7FILTERNAME="{l7_name}";  (仅 L7 场景)

!-- 3. PCC 计费属性（可选，仅当需 URR 绑定时）
ADD URR:URRNAME="{urr_name}", URRID={urr_id}, USAGERPTMODE={...};
ADD URRGROUP:URRGROUPNAME="{urrg_name}", UPURRNAME1="{urr_name}";
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="{ppg_name}", URRGROUPNAME="{urrg_name}";

!-- 4. PCC 阻塞规则（POLICYTYPE=PCC，POLICYNAME 指向 PCCPOLICYGRP）
ADD RULE:RULENAME="{rule_name}", POLICYTYPE=PCC, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{ppg_name}";

!-- 5. 容器与绑定
ADD USERPROFILE:USERPROFILENAME="{up_name}";  (仅新建时)
ADD RULEBINDING:USERPROFILENAME="{up_name}", RULENAME="{rule_name}";

!-- 6. 刷新生效（必须最后，见 ../业务感知域规则.md §1.1）
SET REFRESHSRV:REFRESHTYPE=ALL;
```

### 2.2 轨道 A · ADC 兜底阻塞链（CS-AC-01 衍生）

```mml
!-- ADC 参数（FLOWINFORPT 流信息上报 + ADCHYSTTIMER 迟滞定时器）
ADD ADCPARA:FLOWFILTERNAME="{ff_name}", FLOWINFORPT={...}, ADCHYSTTIMER={...};

!-- ADC 规则（POLICYTYPE=ADC，直接在 RULE，不引用 PCCPOLICYGRP；ADCMUTEFLAG 控制上报开关）
ADD RULE:RULENAME="{rule_adc}", POLICYTYPE=ADC, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", ADCMUTEFLAG={ENABLE|DISABLE};

!-- 兜底机制：业务流匹配不上所有 PCC rule 时，UDG 阻塞业务流（BR-AC-02 类型独立原则）
```

### 2.3 轨道 A · 头增强链（CS-AC-02，跨 HTTP/HTTPS/RTSP 复用）

```mml
!-- 0. SA 前置（仅首次配置时，见 ../业务感知域规则.md §5）
LOD SIGNATUREDB: ...;
LOD PARSERDB: ...;
ADD WELLKNOWNPORT:IDENPROTNAME="{...}", PROTOCOLNAME="http", PORTOP=EQUAL, STARTPORT=80;  (仅头防欺诈识别 HTTP 端口)

!-- 1. 底层过滤（同 §2.1 第 1-2 步）
ADD FILTER / L7FILTER / FLOWFILTER / FLTBINDFLOWF / PROTBINDFLOWF ...

!-- 2. 头增强对象（跨协议复用，含可选 ANTIFRAUD/GRAYLIST 防欺诈子模式）
ADD HEADEN:HEADERENNAME="{headen_name}", DATATYPE={IMSI1|MSISDN1|IMEI1|...}, PREFIXNAME="{X-msisdn}", ENCRYALGORI={MD5|RC4|AES128|AES256|RSA1024|RSA2048|SHA256}, PSWDKEY="{key}", PSWDKEYCONFIRM="{key}", ANTIFRAUD={ENABLE|DISABLE}, GRAYLIST={ENABLE|DISABLE};
SET BASE64: ...;  (base64 编码开关)

!-- 3. 头增强规则（POLICYTYPE=HEADEN，POLICYNAME 指向 HEADEN 对象）
ADD RULE:RULENAME="{rule_headen}", POLICYTYPE=HEADEN, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{headen_name}";

!-- 4. 容器与绑定 + 刷新（同 §2.1 第 5-6 步）
```

> **协议差异约束（CR-AC-10/11，BR-AC-08/09）**：
> - HTTPS 头增强：ENCRYALGORI **无 RSA**，字段按 TLS TLV 格式插入 SSL Extension，触发仅基于 SNI
> - RTSP 头增强：**不支持防欺诈**（ANTIFRAUD=DISABLE 固定，族内唯一例外）
> - HTTP1.x 头增强：不支持 HTTPS/HTTP2.0（加密盲区）
> - 防欺诈使能（ANTIFRAUD=ENABLE）必须 License 双开（HHAS+HTHE，CR-AC-04）

### 2.4 轨道 A · HTTP 智能重定向链（CS-AC-03，SMARTREDIRECT 子轨）

```mml
!-- 1. 多维匹配前置（重定向族独有）
ADD EXTENDEDFILTER:EXTFLTNAME="{extflt_name}", URL="{...}", USERAGENT="{...}", CONTENTTYPE="{...}", URLPOSTFIX="{...}";
ADD ERRORCODE:ERRORCODENAME="{err_name}", ERRORCODEOP=GT, ERRORCODESTART=400;  (HTTP 错误码 GT 400 触发)
ADD REDIRAPPENDINFO:APPENDINFONAME="{append_name}", REQURLFLAG={...}, IMSIFLAG={...}, IMEIFLAG={...};  (可选，携带 MSISDN/IMSI/IMEI)

!-- 2. 底层过滤（同 §2.1 第 1-2 步，L7 场景）
ADD FILTER / L7FILTER / FLOWFILTER / FLTBINDFLOWF / PROTBINDFLOWF ...

!-- 3. HTTP 重定向动作对象
ADD SMARTHTTPREDIR:SMTHTTPREDINAME="{redir_name}", SERVERURL="{target_url}", EXTFLTTYPE1={AND|OR}, EXTFLTNAME1="{extflt_name}", EXTFLTTYPE2={...}, EXTFLTNAME2="{...}", APPENDINFONAME="{append_name}", BINDErrCODENAME="{err_name}";

!-- 4. 重定向规则（POLICYTYPE=SMARTREDIRECT，POLICYNAME 指向 SMARTHTTPREDIR）
ADD RULE:RULENAME="{rule_redir}", POLICYTYPE=SMARTREDIRECT, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{redir_name}";

!-- 5. 容器与绑定 + 刷新（同 §2.1 第 5-6 步）
```

> **协议限制（BR-AC-09）**：HTTP 智能重定向**仅 HTTP1.x**，不支持 HTTPS/HTTP2.0（加密无法获取 HTTP 响应特征）。

### 2.5 轨道 A · DNS 纠错链（CS-AC-04，SMARTREDIRECT 子轨共用）

```mml
!-- 1. 多维匹配前置（同 §2.4，但 ERRORCODE 是 DNS 错误码）
ADD EXTENDEDFILTER:EXTFLTNAME="{extflt_name}", URL="{domain}";  (错误域名匹配)
ADD ERRORCODE:ERRORCODENAME="{dns_err_name}", ERRORCODEOP=EQUAL, ERRORCODESTART=3;  (DNS NXDOMAIN=3 触发)

!-- 2. 底层过滤（UDP DNS，同 §2.1 第 1-2 步）

!-- 3. DNS 重写动作对象（含 Platform IP）
ADD DNSOVERWRITING:DNSOVERWRTNAME="{dns_ow_name}", EXTFLTTYPE1=AND, EXTFLTNAME1="{extflt_name}", SERVERIP1="{platform_ip}", BINDERRCODENAME="{dns_err_name}";

!-- 4. DNS 纠错规则（★ POLICYTYPE=SMARTREDIRECT 与 HTTP 重定向共用，区分点在 POLICYNAME 指向 DNSOVERWRITING，CR-AC-03）
ADD RULE:RULENAME="{rule_dns}", POLICYTYPE=SMARTREDIRECT, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{dns_ow_name}";

!-- 5. 容器与绑定 + 刷新
```

> **协议限制（BR-AC-09）**：DNS 纠错**仅 UDP DNS**，不支持 TCP DNS。

### 2.6 轨道 A · Portal captive 链（CS-AC-05 Portal）

```mml
!-- 1. IPFarm 集群前置（Portal+WebProxy 共用）
SET IPFARMGLOBAL:SERVERTYPE={...}, LBMETHOD={ROUND_ROBIN|LEAST_RECENTLY_USED|LEAST_LOAD}, TIMETHRESHOLD={...}, HEALTHSUCCLIMIT={...}, HEALTHFAILLIMIT={...};
ADD LOGICINF:NAME="{logicinf_name}", IPVERSION={...}, IPV4ADDRESS1="{...}", IPV4MASK1="{...}";  (心跳检测接口，不同 IPFarm 必须用不同接口)
ADD IPFARM:IPFARMNAME="{ipfarm_name}", IPVERSION={...}, INTERFACENAME="{logicinf_name}", HEALTHCHECKFLAG=ENABLE;
ADD IPFARMSERVER:IPFARMNAME="{ipfarm_name}", SERVERIPV4="{portal_server_ip}";  (每 Farm 最多 512 IP)

!-- 2. 底层过滤（L7 HTTP，同 §2.1 第 1-2 步）

!-- 3. PCC 计费属性（Portal 共用）
ADD URR / URRGROUP / PCCPOLICYGRP ... (同 §2.1 第 3 步)

!-- 4. Portal 规则（POLICYTYPE=PCC，POLICYNAME 指向 PCCPOLICYGRP）
ADD RULE:RULENAME="{rule_portal}", POLICYTYPE=PCC, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{ppg_name}";

!-- 5. ★ captive 配置在 USERPROFILE（不在 RULE，TR-AC-07）
ADD USERPROFILE:USERPROFILENAME="{up_portal}", CAPMODETHRES={6};  (如 6 分钟 captive 周期)
ADD RULEBINDING:USERPROFILENAME="{up_portal}", RULENAME="{rule_portal}";
ADD APN:APNNAME="{apn_name}", ...;  (Portal/WebProxy/URL 过滤共用)

!-- 6. ★ Portal 全 DOWN 时 DEFAULTACT=BLOCK（兜底阻塞，CR-AC-10）
ADD IPFARM:..., DEFAULTACT=BLOCK;  (或通过其他参数表达兜底)

!-- 7. 刷新生效
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> **协议限制（BR-AC-09）**：Portal **仅 HTTP1.x/WAP**，不支持 HTTPS/HTTP2.0。

### 2.7 轨道 A · WebProxy 链（CS-AC-05 WebProxy，★ 唯一处理加密协议）

```mml
!-- 1. IPFarm 集群前置（同 §2.6 第 1 步，但服务器是 Proxy Server）
SET IPFARMGLOBAL / ADD LOGICINF / ADD IPFARM / ADD IPFARMSERVER(SERVERIPV4="{proxy_server_ip}") ...
ADD BLACKLISTRULE: ...;  (WebProxy 独有黑名单)

!-- 2. 底层过滤（L3 TCP SYN 匹配，不依赖 L7 解析）
ADD FILTER:FILTERNAME="{filter_l3}", ...;  (五元组/TCP SYN)
ADD FLOWFILTER / ADD FLTBINDFLOWF ...

!-- 3. PCC 计费属性（同 §2.6 第 3 步）

!-- 4. ★ WebProxy 双规则约束（TR-AC-06）：必须同时配两条 RULE
ADD RULE:RULENAME="{rule_webproxy}", POLICYTYPE=WEBPROXY, PRIORITY={p1}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{ipfarm_name}";  (重定向，POLICYNAME 指向 IPFarm)
ADD RULE:RULENAME="{rule_pcc}", POLICYTYPE=PCC, PRIORITY={p2}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{ppg_name}";  (计费，POLICYNAME 指向 PCCPOLICYGRP)
!-- 注意：两条 RULE 共用同一 FLOWFILTER，RULENAME 不能同名（CR-AC-01）

!-- 5. 容器与绑定 + APN + 刷新（同 §2.6 第 5-7 步）
```

> **协议优势（BR-AC-09）**：WebProxy 在 L3 工作（IP NAT），**唯一支持 HTTPS/HTTP2.0/任意 TCP** 的重定向族特性。

### 2.8 轨道 B · URL 过滤链（CS-AC-06，★ 独立动作体系）

```mml
!-- ========== 第 1 层：ICAP 互通前置（TR-AC-05 硬约束，断裂则 URL 过滤不生效）==========
ADD VPNINST:VPNINSTANCE="{vpn_inst}";  (ICAP 互通专网)
ADD LOGICINF:NAME="{logicinf_icap}", IPVERSION={...}, IPV4ADDRESS1="{...}", IPV4MASK1="{...}", VPNINSTANCE="{vpn_inst}";  (可与 Portal/WebProxy 共用 LOGICINF 类)
ADD ICAPSERVER:ICAPSERVERNAME="{icap_svr}", ICAPSERVERTYPE=URL_FILTERING, ICAPSVRIPTYPE={...}, ICAPSERVERIPV4="{icap_ip}", VPNINSTANCE="{vpn_inst}";
ADD ICAPLOCALINFO:ICAPSERVERTYPE=URL_FILTERING, USERAGENT="{...}";
ADD ICAPSVRGRP:ICAPSVRGRPNAME="{icap_grp}", ICAPSERVERTYPE=URL_FILTERING;
ADD ICAPSVRBINDISG:ICAPSVRGRPNAME="{icap_grp}", ICAPSERVERNAME="{icap_svr}";
SET CFSRVMODE: ...;  (URL 过滤业务模式)

!-- ========== 第 2 层：CF 业务（轨道 B 核心，显式 ACTION）==========
ADD APN:APNNAME="{apn_name}", ...;
SET APNCFFUNC:APNNAME="{apn_name}", CFSWITCHVALUE=ENABLE;  (APN 粒度开关)
ADD CFPROFILE:CFPROFILENAME="{cf_profile}";  (策略载体)
ADD CFTEMPLATE:CFTEMPLATENAME="{cf_tpl}", ICAPSRVGMNAME="{icap_grp}", ACTION={BLOCK|PERMIT|REDIRECT};  (★ 模板级缺省动作，PERMIT 仅轨道 B)
SET APNCFTEMPLATE:APNNAME="{apn_name}", CFTEMPLATENAME="{cf_tpl}";  (APN-模板绑定)
ADD CFPROFBINDCFT:CFTEMPLATENAME="{cf_tpl}", CFPROFILENAME="{cf_profile}";  (策略-模板绑定)
ADD CONTCATEGROUP:CONTCATEGNAME="{categ_grp}", CATEGORYTYPE=SPECIFIC, CATEGORYID={categ_id};  (URL 分类 ID，来自 ICAP Server)
ADD CONTCATEGBIND:CFPROFILENAME="{cf_profile}", CONTCATEGNAME="{categ_grp}", ACTION={BLOCK|PERMIT|REDIRECT};  (★ 分类级精确动作，覆盖模板级缺省)
SET CFCACHEPARA: ...;  (缓存参数，减少 ICAP 交互)
SET GLBCFFUNC: ..., CFSWITCHVALUE=ENABLE;  (全局内容过滤开关)
ADD CFWHITEURLLST / ADD CFIPWHITELIST / ADD CFPFSPECACTION: ...;  (可选白名单/特殊场景)

!-- ========== 第 3 层：PCC 触发层（共用计费属性，但动作不走 PCCPOLICYGRP，TR-AC-03）==========
ADD URR / URRGROUP / PCCPOLICYGRP ... (同 §2.1 第 3 步)
ADD FILTER / L7FILTER / FLOWFILTER / FLTBINDFLOWF / PROTBINDFLOWF ... (同 §2.1 第 1-2 步)

!-- 4. URL 过滤触发规则（★ POLICYTYPE=PCC 仅触发匹配，实际 BLOCK/PERMIT/REDIRECT 动作走 CFTEMPLATE/CONTCATEGBIND）
ADD RULE:RULENAME="{rule_url}", POLICYTYPE=PCC, PRIORITY={priority}, FILTERINGMODE=FLOWFILTER, FLOWFILTERNAME="{ff_name}", POLICYNAME="{ppg_name}";

!-- 5. 容器与绑定 + 刷新
ADD USERPROFILE / ADD RULEBINDING ...
SET REFRESHSRV:REFRESHTYPE=ALL;
```

> **轨道 B 核心约束**：
> - **PERMIT 唯一性（BR-AC-10, CR-AC-06）**：显式 PERMIT 仅本方案支持，轨道 A 无法显式 PERMIT
> - **ICAP Server 必需（CR-AC-05）**：URL 过滤前置，链路断裂则不生效
> - **HTTPS 限制（CR-AC-10）**：HTTPS 场景仅能基于 SNI 做分类（不能解析完整 URL）
> - **三网元一致（CR-AC-09）**：CATEGORYID 需 UDG + ICAP Server + PCRF/PCF 一致

### 2.9 UNC 侧接入控制链（CS-AC-07/09，仅本地 PCC 场景）

```mml
!-- 1. UNC 侧 PCC 骨架（首次配置，已存在则跳过）
SET LICENSESWITCH: ...;
SET PCCFUNC: ...;
SET PCCFAILACTION:FAILACTION={CONTINUE|REDIRECT};  (PCF 容灾决策 DP-AC-08)
SET POLICYMODE: ...;  (Gx/N7 接口)
ADD PCRF / ADD PCRFGROUP / ADD PCRFBINDGRP / SET DFTGLBPCRFGRP: ...;

!-- 2. 规则与用户模板（与 UPF 侧 RULENAME 一致，BR-AC-01）
ADD RULE:RULENAME="{rule_name}", ...;  (UNC 侧 POLICYTYPE=BWM/PCC/QOS/ADC，间接被位置触发引用)
ADD USERPROFILE:USERPROFILENAME="{up_name}", ...;
ADD RULEBINDING: ...;

!-- 3. ★ 位置触发（仅本地 PCC 场景，TR-AC-08）
ADD USRLOCATION:LOCATIONNAME="{loc_name}", LOCATIONTYPE={CGI|ECGI|NCGI}, MCC="{mcc}", MNC="{mnc}", LAC="{lac}"|ECI="{eci}"|NCI="{nci}";
ADD USRLOCATIONGRP:LOCGROUPNAME="{loc_grp}", LOCATIONNAME="{loc_name}";
ADD USRPROFGROUP:USERPROFGNAME="{upg_name}", ...;
MOD UPBINDUPG:USERPROFGNAME="{upg_name}", USERPROFILENAME="{up_name}", UPBINDTYPE=SPECIFIC, LOCGROUPNAME="{loc_grp}";  (★ MOD 含 LOCGROUPNAME 位置组绑定)
ADD APNUSRPROFG:APN="{apn_name}", USERPROFGNAME="{upg_name}";
```

> **动态 PCC vs 本地 PCC 分支（TR-AC-08）**：
> - 动态 PCC（有 PCRF/PCF）：**跳过位置触发链**，仅 License + ULI 透传（PCRF 决策）
> - 本地 PCC（无 PCRF/PCF）：执行完整 USRLOCATION + USRLOCATIONGRP + MOD UPBINDUPG 配置
> - **三网元位置一致（CR-AC-09）**：CGI/ECGI/NCGI 需 UNC + RAN + PCRF/PCF 三处一致

---

## 3. 排序规则

> 域共享排序原则见 `../业务感知域规则.md` §1.2（配置链依赖顺序）。本节给出访问限制场景的具体顺序。

### 3.1 UPF(UDG)侧（严格顺序，双轨道统一）

```
0.  LOD SIGNATUREDB / LOD PARSERDB          (SA 前置，仅首次，见 ../业务感知域规则.md §5)
1.  SET LICENSESWITCH                         (License 前置门控，BR-AC-04)
2.  FILTER / L7FILTER / EXTENDEDFILTER / ERRORCODE  (底层过滤 + 多维匹配)
3.  FLOWFILTER                                (中间容器)
4.  FLTBINDFLOWF / PROTBINDFLOWF              (绑定)
5.  ★ 轨道 A 动作对象（按子轨分组建）：
    - ADC: ADCPARA
    - HEADEN 子轨: WELLKNOWNPORT → HEADEN → SET BASE64
    - SMARTREDIRECT 子轨: REDIRAPPENDINFO → SMARTHTTPREDIR / DNSOVERWRITING
    - WEBPROXY 子轨: IPFARMGLOBAL → LOGICINF → IPFARM → IPFARMSERVER → BLACKLISTRULE
    - PCC 子轨: URR → URRGROUP → PCCPOLICYGRP
6.  ★ 轨道 B 动作对象（URL 过滤独立链，TR-AC-05 顺序）：
    - VPNINST → LOGICINF → ICAPSERVER → ICAPLOCALINFO → ICAPSVRGRP → ICAPSVRBINDISG → SET CFSRVMODE
    - APN → SET APNCFFUNC → CFPROFILE → CFTEMPLATE → SET APNCFTEMPLATE → CFPROFBINDCFT → CONTCATEGROUP → CONTCATEGBIND → SET CFCACHEPARA → SET GLBCFFUNC
7.  ADD APN                                    (Portal/WebProxy/URL 过滤共用)
8.  RULE                                       (汇聚，POLICYTYPE 路由到对应动作对象，CR-AC-02)
9.  USERPROFILE                                (容器，仅新建时；Portal 含 CAPMODETHRES)
10. RULEBINDING                                (规则绑定)
11. SET REFRESHSRV:REFRESHTYPE=ALL             (★ 必须最后，见 ../业务感知域规则.md §1.1)
```

### 3.2 SMF(UNC)侧

```
1. 系统级命令（PCC 骨架 + PCRF 管理，仅检查，已存在则跳过）
2. 规则 + 用户模板 + 绑定链（ADD RULE / ADD USERPROFILE / ADD RULEBINDING）
3. ★ 位置触发（仅本地 PCC 场景）：
   USRLOCATION → USRLOCATIONGRP → USRPROFGROUP → MOD UPBINDUPG (含 LOCGROUPNAME) → ADD APNUSRPROFG
4. 无 REFRESHSRV（SMF 侧策略即时生效）
```

> **详细依赖链请加载 `03-task-layer.md` §7 TaskCommandOrderEdge（32+ 编排边）确认。**

---

## 4. 配置决策指南

以下场景需要 Agent 从图谱/知识库获取业务规则后做出实现决策：

### 4.1 ★ 双轨道选择（DP-AC-03，本场景核心路由）

| 用户需求 | 动作轨道 | 配置体系 |
|---------|---------|---------|
| 阻塞非法内容/IP（PCC 体系） | 轨道 A · PCC/ADC 子轨 | RULE.POLICYTYPE=PCC/ADC |
| 头增强（插 MSISDN/IMSI） | 轨道 A · HEADEN 子轨 | RULE.POLICYTYPE=HEADEN |
| HTTP/DNS 重定向 | 轨道 A · SMARTREDIRECT 子轨 | RULE.POLICYTYPE=SMARTREDIRECT |
| Portal captive / WebProxy | 轨道 A · PCC/WEBPROXY 子轨 | RULE.POLICYTYPE=PCC/WEBPROXY |
| URL 分类过滤（含**白名单 PERMIT**） | **轨道 B** | CFTEMPLATE/CONTCATEGBIND.ACTION |
| 接入控制（SAR/区域/位置） | UNC 侧 | USRLOCATION + MOD UPBINDUPG |

> **PERMIT 唯一性（BR-AC-10）**：用户说"放行白名单"必须走轨道 B（URL 过滤），轨道 A 无法显式 PERMIT。

### 4.2 ★ 双轨并存（CR-AC-14）

同一用户业务流可先后被轨道 A 和轨道 B 检查（如头增强 + URL 过滤），双轨独立配置，互不干扰。最终动作取决于配置优先级和规则匹配顺序。

### 4.3 ★ SMARTREDIRECT 两子类型区分（CR-AC-03）

POLICYTYPE=SMARTREDIRECT 时，POLICYNAME 指向区分：
- 指向 SMARTHTTPREDIR → HTTP 智能重定向（CS-AC-03）
- 指向 DNSOVERWRITING → DNS 纠错（CS-AC-04）

### 4.4 ★ WebProxy 双规则约束（TR-AC-06）

WebProxy 必须同时配置两条 RULE：
- POLICYTYPE=WEBPROXY（POLICYNAME=IPFarm）做重定向
- POLICYTYPE=PCC（POLICYNAME=PCCPOLICYGRP）做计费
- 两条 RULE 共用同一 FLOWFILTER，RULENAME 不能同名（CR-AC-01）

### 4.5 ★ 头防欺诈强耦合（CR-AC-04, TR-AC-04）

启用头防欺诈（ANTIFRAUD=ENABLE）必须：
1. License 双开（HHAS `LKV3G5HHAS01` + HTHE `LKV3G5HTHE01`）
2. 内嵌于 HEADEN 对象（不独立产生动作）
3. 执行顺序：防欺诈检测 → 字段纠正/冗余清理 → 头增强插入
4. **RTSP 头增强不支持防欺诈**（族内唯一例外，CR-AC-11）

### 4.6 OR 条件：FLOWFILTERGRP vs 多 RULE

| 方案 | 适用场景 |
|------|---------|
| FLOWFILTERGRP | 多个条件执行**完全相同**的动作 |
| 多 RULE | 需要不同优先级或后续可能分化 |

**默认**：使用 FLOWFILTERGRP（更简洁）。同 `../业务感知域规则.md`。

### 4.7 加密协议场景（BR-AC-09, CR-AC-10）

HTTPS/HTTP2.0 场景的动作选择：
- **仅 WebProxy 可处理**（L3 IP NAT 不依赖 L7 解析）
- HTTPS 头增强：通过 SSL Extension 部分支持（无 RSA）
- URL 过滤：仅基于 SNI 做分类（不能解析完整 URL）
- HTTP 智能重定向 / Portal / HTTP 头增强：**不支持**（加密盲区）

---

## 5. 注意事项

- 每个参数的枚举值必须从 `04-command-graph.md` §5 CommandParameter 获取，不可自行推断
- **双轨道参数体系严格区分**：轨道 A（POLICYTYPE/POLICYNAME/HEADEN/IPFARM/SMARTREDIR）与轨道 B（CFTEMPLATE.ACTION/CONTCATEGBIND.ACTION/ICAP 系列）不可混用
- 各子轨协议差异（HTTP/HTTPS/RTSP/DNS/任意 TCP）必须加载 `kb/` 对应章节确认
- 排序错误会导致配置失败，REFRESHSRV 必须在最后（仅 UPF 侧）
- 策略链独立原则：每条业务的动作链彼此独立，不可跨业务复用（同 `../业务感知域规则.md` §4）
- 两侧共用参数（RULENAME、USERPROFILENAME、URRID 等）必须一致（仅当 UNC 侧涉及，BR-AC-01）
- WebProxy 双规则、SMARTREDIRECT 两子类型、头防欺诈强耦合、URL 过滤 ICAP 前置——这四项是访问限制场景易错点，配置时必须逐项核对
