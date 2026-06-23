# 02 · 双轨道动作机制与 POLICYTYPE 路由

> **定位**：详解 RULE.POLICYTYPE 路由决策规则与各子轨的 ConfigObject 指向。
> **数据来源**：`访问限制场景/three-layer-graph/04-command-graph.md`（§3 ConfigObject 关系边、§5.1 ADD RULE 参数、CR-AC-02/03）、`03-task-layer.md`（TR-AC-02/03、T-003 路由）。
> **关联文件**：`01-访问限制动作体系与双轨道.md`（架构总纲）、各子轨道专题（`04-头增强族协议差异.md` / `05-重定向族.md` / `06-URL过滤与ICAP.md`）。

---

## 1. POLICYTYPE 路由总表（CR-AC-02 / TR-AC-02）

RULE.POLICYTYPE 是轨道 A 的动作总开关。根据取值不同，POLICYNAME 指向不同类型的动作对象：

| POLICYTYPE | POLICYNAME 指向对象 | 对象 ConfigObject | 动作语义 | 路由到的 Task |
|-----------|---------------------|------------------|---------|--------------|
| **ADC** | (空，直接在 RULE) + ADCPARA | OBJ-ADCPARA | 应用检测 + 兜底阻塞 | T-AC-101 |
| **PCC** | PCCPOLICYGRP | OBJ-PCCPOLICYGRP (contains URRGROUP → URR) | 标准 PCC（Portal 计费 / 阻塞 / **URL 过滤触发**） | T-AC-105 (Portal) / T-AC-107 (PCC 动作组) / T-AC-108 (URL 过滤触发) |
| **HEADEN** | HEADEN 对象 | OBJ-AC-HEADEN (含 ANTIFRAUD/GRAYLIST) | 头增强（字段插入） | T-AC-102 |
| **SMARTREDIRECT** | SMARTHTTPREDIR / DNSOVERWRITING | OBJ-AC-SMARTHTTPREDIR / OBJ-AC-DNSOVERWRITING | HTTP 重定向 / DNS 纠错（共用 POLICYTYPE，区分点在 POLICYNAME 指向，CR-AC-03） | T-AC-103 / T-AC-104 |
| **WEBPROXY** | IPFARM | OBJ-AC-IPFARM (contains IPFARMSERVER) | Web Proxy（L3 IP NAT） | T-AC-106 |

> **URL 过滤的特殊性（CR-AC-02 / TR-AC-03）**：URL 过滤 RULE 用 POLICYTYPE=PCC 触发匹配，但实际 BLOCK/PERMIT/REDIRECT 动作**不走 PCCPOLICYGRP**，而走 CFTEMPLATE/CONTCATEGBIND（轨道 B）。这是双轨道机制的建模难点。

---

## 2. ADD RULE 关键参数（CR-AC-02）

| 参数 | 类型 | 取值范围 | 说明 |
|------|------|---------|------|
| RULENAME | string | — | 规则名，跨网元一致（CR-AC-01, CR-AC-09）；跨 POLICYTYPE 不能同名 |
| **POLICYTYPE** | enum | **ADC / PCC / HEADEN / SMARTREDIRECT / WEBPROXY** | **★ 双轨道+五子轨决定 POLICYNAME 指向**（CR-AC-02） |
| PRIORITY | int | 0-65535 | 优先级（数字越小越高，见 `../业务感知域规则.md` §3） |
| FILTERINGMODE | enum | FLOWFILTER | 过滤模式 |
| FLOWFILTERNAME | string | — | 引用 FLOWFILTER（CR-AC-07, CR-AC-08） |
| **POLICYNAME** | string | — | 按 POLICYTYPE 引用不同对象（见 §1 路由总表） |
| ADCMUTEFLAG | enum | ENABLE / DISABLE | ADC 规则静默上报开关（POLICYTYPE=ADC 时使用） |

---

## 3. SMARTREDIRECT 子轨的两特性区分（CR-AC-03）

POLICYTYPE=SMARTREDIRECT 是 HTTP 智能重定向和 DNS 纠错**共用**的 POLICYTYPE，区分点在 POLICYNAME 指向：

| POLICYNAME 指向 | 对象 | 子类型 | 协议限制 |
|----------------|------|--------|---------|
| SMARTHTTPREDIR 对象名 | OBJ-AC-SMARTHTTPREDIR | HTTP 智能重定向（CS-AC-03） | 仅 HTTP1.x，不支持 HTTPS/HTTP2.0 |
| DNSOVERWRITING 对象名 | OBJ-AC-DNSOVERWRITING | DNS 纠错（CS-AC-04） | 仅 UDP DNS，不支持 TCP DNS |

**配置示例**：
```mml
!-- HTTP 智能重定向
ADD RULE:RULENAME="{rule_http_redir}", POLICYTYPE=SMARTREDIRECT, ..., POLICYNAME="{smarthttpredir_name}";

!-- DNS 纠错（共用 POLICYTYPE=SMARTREDIRECT）
ADD RULE:RULENAME="{rule_dns}", POLICYTYPE=SMARTREDIRECT, ..., POLICYNAME="{dnsoverwriting_name}";
```

---

## 4. 轨道 A 各子轨 ConfigObject 关系链（来自 04-command-graph §3）

### 4.1 通用结构边（五子轨共用）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| USERPROFILE | contains | RULE | 通过 RULEBINDING（含 Portal captive 绑定） |
| RULE | contains | FLOWFILTER | 规则引用流过滤器（FILTERINGMODE=FLOWFILTER） |
| FLOWFILTER | contains | FILTER | 通过 FLTBINDFLOWF |
| FLOWFILTER | contains | L7FILTER | 通过 PROTBINDFLOWF（含协议绑定） |
| FLOWFILTERGRP | contains | FLOWFILTER | OR 关系组合（多条件 OR） |

### 4.2 PCC 子轨（POLICYTYPE=PCC）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(PCC) | refers_to | PCCPOLICYGRP | POLICYNAME 指向；ADC/Portal/WebProxy 计费/URL 过滤触发共用 |
| PCCPOLICYGRP | contains | URRGROUP | PCC 策略组包含 URR 组 |
| URRGROUP | contains | URR | UPURRNAME1/2/3 |

### 4.3 ADC 子轨（POLICYTYPE=ADC）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(ADC) | depends_on | ADCPARA | ADC 规则依赖 ADC 参数（FLOWINFORPT + ADCHYSTTIMER） |

### 4.4 HEADEN 子轨（POLICYTYPE=HEADEN）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(HEADEN) | refers_to | HEADEN | POLICYNAME 指向 HEADEN 对象名 |
| HEADEN | activates | (头防欺诈检测) | ANTIFRAUD=ENABLE 时内嵌防欺诈前置检测；非独立对象 |
| HEADEN(ANTIFRAUD=ENABLE) | depends_on | HEADEN(头增强主特性) | **强耦合**：启用防欺诈必须开启头增强（License 双开） |
| HEADEN | conflicts_with | (RTSP 协议) | 头防欺诈仅支持 HTTP/HTTPS，RTSP 不支持（族内唯一例外） |

### 4.5 SMARTREDIRECT 子轨（POLICYTYPE=SMARTREDIRECT）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(SMARTREDIRECT) | refers_to | SMARTHTTPREDIR / DNSOVERWRITING | POLICYNAME 指向（区分 HTTP 重定向 vs DNS 纠错） |
| SMARTHTTPREDIR | contains | (EXTENDEDFILTER 引用) | EXTFLTTYPE1/2 + EXTFLTNAME1/2（多维 AND 组合） |
| SMARTHTTPREDIR | contains | (ERRORCODE 引用) | BINDErrCODENAME（HTTP 错误码 GT 400 触发） |
| SMARTHTTPREDIR | refers_to | REDIRAPPENDINFO | APPENDINFONAME（携带 MSISDN/IMSI/IMEI） |
| DNSOVERWRITING | contains | (EXTENDEDFILTER 引用) | EXTFLTTYPE1 + EXTFLTNAME1（域名匹配） |
| DNSOVERWRITING | contains | (ERRORCODE 引用) | BINDERRCODENAME（DNS 错误码 EQUAL 3 NXDOMAIN 触发） |
| SMARTHTTPREDIR | conflicts_with | (HTTPS/HTTP2.0 协议) | 加密协议不支持 HTTP 重定向 |

### 4.6 WEBPROXY 子轨（POLICYTYPE=WEBPROXY）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| RULE(WEBPROXY) | refers_to | IPFARM | POLICYNAME 指向 IPFARM → L3 IP NAT 重定向到 Proxy |
| IPFARM | contains | IPFARMSERVER | 整机 64 Farm × 512 IP |
| IPFARM | depends_on | LOGICINF | 心跳检测接口（不同 IPFarm 必须用不同接口） |
| IPFARMGLOBAL | activates | IPFARM | 全局 LBMETHOD/心跳阈值约束所有 IPFarm 实例 |
| USERPROFILE(CAPMODETHRES) | activates | (Portal captive 周期) | Portal captive 配置在 USERPROFILE（非 RULE） |
| IPFARM(Portal 全 DOWN) | activates | (DEFAULTACT=BLOCK) | Portal 兜底阻塞 |
| IPFARM(WEBPROXY) | contains | BLACKLISTRULE | WebProxy 黑名单规则归属于 IPFARM 体系 |

---

## 5. 轨道 B ConfigObject 关系链（URL 过滤独立体系）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| ICAPSVRGRP | contains | ICAPSERVER | 通过 ICAPSVRBINDISG |
| ICAPSERVER | depends_on | VPNINST | ICAP 互通专网 |
| ICAPSERVER | depends_on | LOGICINF | ICAP 互通接口（与 Portal/WebProxy 心跳检测共用 LOGICINF 类） |
| ICAPSVRGRP | refers_to | CFTEMPLATE | CFTEMPLATE.ICAPSRVGMNAME 指向 ICAP 服务器组 |
| CFTEMPLATE | composed_by | (CFPROFILE via CFPROFBINDCFT) | 模板与策略绑定 |
| CONTCATEGBIND | refers_to | CONTCATEGROUP | 分类级动作绑定到内容分类组（CATEGORYID） |
| CONTCATEGBIND | refers_to | CFPROFILE | 分类级动作归属策略（覆盖 CFTEMPLATE 模板级缺省） |
| CFTEMPLATE | refers_to | APNCFTEMPLATE | APN 级模板绑定 |
| RULE(PCC, URL 过滤触发) | activates | CFTEMPLATE/CONTCATEGBIND | URL 过滤 RULE 用 POLICYTYPE=PCC 仅作匹配触发，**实际动作不走 PCCPOLICYGRP** |
| CFTEMPLATE(ACTION=PERMIT) | activates | (独立白名单放行) | 轨道 B 独有 PERMIT |

---

## 6. POLICYTYPE 路由决策流程（配置生成时）

```
Step 1: 读取 DP-AC-01（动作类型）和 DP-AC-03（动作轨道）
  ├─ 动作 = PERMIT → 必须轨道 B（URL 过滤，BR-AC-10）
  ├─ 动作 = DISCARD + PCC 体系 → POLICYTYPE=PCC（CS-AC-01）
  ├─ 动作 = DISCARD + ADC 兜底 → POLICYTYPE=ADC
  ├─ 动作 = HEADEN → POLICYTYPE=HEADEN（CS-AC-02）
  ├─ 动作 = REDIRECT + HTTP → POLICYTYPE=SMARTREDIRECT + POLICYNAME=SMARTHTTPREDIR（CS-AC-03）
  ├─ 动作 = REDIRECT + DNS → POLICYTYPE=SMARTREDIRECT + POLICYNAME=DNSOVERWRITING（CS-AC-04）
  ├─ 动作 = REDIRECT + Portal → POLICYTYPE=PCC + USERPROFILE.CAPMODETHRES（CS-AC-05 Portal）
  ├─ 动作 = REDIRECT + WebProxy(加密) → POLICYTYPE=WEBPROXY（CS-AC-05 WebProxy）
  └─ 动作 = BLOCK/PERMIT/REDIRECT + URL 分类 → 轨道 B CFTEMPLATE/CONTCATEGBIND.ACTION（CS-AC-06）

Step 2: 根据 POLICYTYPE 确定 POLICYNAME 指向对象（见 §1 路由总表）

Step 3: 加载对应子轨 Task（T-AC-101~T-AC-108）生成配置链
```
