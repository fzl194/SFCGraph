# Batch-20: UDG业务感知专题 -- 规则配置实例、License开关与六类调测

---

## 1. 概述

本批文档涵盖 UDG 业务感知专题中的两大核心知识域：

**规则配置实例域（4篇）**：
- 三四层业务阻塞功能：基于IP/协议/TCP端口的报文丢弃配置
- 三四层重定向功能：基于三四层特征的IP重定向配置
- 规则配置实例总览：业务感知全部配置实例的全景索引
- 特性License开关：SA特性可用性的前置管控

**调测方法域（6篇）**：
- 七层Remark功能调测：基于URL匹配的DSCP值重标记
- 七层重定向功能调测：基于URL匹配的HTTP重定向
- 七层阻塞功能调测：基于URL匹配的业务阻断
- 三四层Remark功能调测：基于IP/协议的DSCP值重标记
- 三四层重定向功能调测：基于IP/协议的IP重定向
- 三四层阻塞功能调测：基于IP/协议的业务阻断

上述文档系统性地呈现了 UDG 业务感知在三四层（L3/L4）和七层（L7）两个维度的三大动作类型（阻塞、重定向、Remark），共六个功能场景的完整配置链和调测链。

适用网元：SGW-U、PGW-U、UPF。

---

## 2. 核心知识点

### 2.1 三四层业务阻塞功能

**定义**：UDG 通过对用户三四层报文（IP地址、协议类型、TCP/UDP端口）进行解析，过滤掉符合配置特征的用户报文，实现业务阻塞。

**配置链**（端到端6步）：
```
ADD FILTER（三四层过滤条件）
  -> ADD FLOWFILTER + ADD FLTBINDFLOWF（流过滤器组装）
    -> SET REFRESHSRV（刷新生效，必须执行）
      -> ADD PCCACTIONPROP（PCC动作属性，关键参数UPINITDNGATE=DISCARD）
        -> ADD PCCPOLICYGRP（PCC策略组，可绑定URR组实现计费）
          -> ADD RULE + ADD USERPROFILE + ADD RULEBINDING（规则与用户模板绑定）
```

**关键技术点**：
- 阻塞动作通过 PCC 策略实现，策略类型为 `PCC`
- 核心参数 `UPINITDNGATE=DISCARD` 表示上行发起时下行报文丢弃
- Filter 过滤维度：`L34PROTTYPE`（协议输入类型）、`L34PROTOCOL`（协议如TCP）、`SVRIP`（服务器IP）、`SVRIPMASK`（反掩码，0.0.0.0表示精确匹配）
- 当需要计费时，PCCPOLICYGRP 绑定 `URRGROUPNAME` 参数

**脚本示例**：
```
ADD FILTER:FILTERNAME="filter_test",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IP,SVRIP="10.11.11.11",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0";
ADD FLOWFILTER:FLOWFILTERNAME="ff_test";
ADD FLTBINDFLOWF:FLOWFILTERNAME="ff_test",FILTERNAME="filter_test";
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
ADD PCCACTIONPROP:PCCACTPROPNAME="pap_test",UPINITDNGATE=DISCARD;
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="ppg_test",PCCACTPROPNAME="pap_test",URRGROUPNAME="urrgroup1";
ADD RULE:RULENAME="rule_test",POLICYTYPE=PCC,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="ff_test",POLICYNAME="ppg_test";
ADD USERPROFILE:USERPROFILENAME="up_test";
ADD RULEBINDING:USERPROFILENAME="up_test",RULENAME="rule_test";
```

### 2.2 三四层重定向功能

**定义**：UDG 对用户三四层报文进行解析，当用户访问某些特定IP时，重定向到其他IP地址。

**与阻塞功能的关键差异**：
- 策略类型不同：重定向使用 `POLICYTYPE=IPREDIR`，阻塞使用 `POLICYTYPE=PCC`
- 重定向无需 PCCACTIONPROP 和 PCCPOLICYGRP，直接在 RULE 中配置重定向目标IP
- RULE 额外参数：`REDIRIPVERFLAG=IPV4`（重定向IP版本）、`IPREDIRECTIP`（重定向目标IP）
- RULE 支持全局优先级参数 `PRIORITY`

**配置链**（端到端5步）：
```
ADD FILTER（三四层过滤条件）
  -> ADD FLOWFILTER + ADD FLTBINDFLOWF（流过滤器组装）
    -> SET REFRESHSRV（刷新生效）
      -> ADD RULE（POLICYTYPE=IPREDIR，含重定向IP参数）
        -> ADD USERPROFILE + ADD RULEBINDING（用户模板绑定）
```

**脚本示例**：
```
ADD FILTER:FILTERNAME="filter_ipred",L34PROTTYPE=STRING,L34PROTOCOL=TCP,SVRIPMODE=IP,SVRIP="10.21.21.21",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0";
ADD FLOWFILTER:FLOWFILTERNAME="flowfilter_ipred";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilter_ipred",FILTERNAME="filter_ipred";
SET REFRESHSRV:REFRESHTYPE=ALL;
ADD RULE:RULENAME="rule_ipred",POLICYTYPE=IPREDIR,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilter_ipred",PRIORITY=2048,REDIRIPVERFLAG=IPV4,IPREDIRECTIP="10.200.200.200";
ADD USERPROFILE:USERPROFILENAME="up_ipred";
ADD RULEBINDING:USERPROFILENAME="up_ipred",RULENAME="rule_ipred";
```

### 2.3 规则配置实例全景索引

规则配置实例总览文档提供了 UDG 业务感知所有配置实例的分类索引，涵盖5大类：

| 实例大类 | 包含的具体实例 |
|----------|---------------|
| **计费与策略控制** | 三四层业务阻塞、七层业务阻塞、七层重定向、三四层QoS保证、七层QoS保证、本地PCC、动态PCC、终端系统码率差异化 |
| **带宽管理** | 基于PCC预定义规则的带宽控制、针对URL应用的流量整形（Shaping） |
| **头增强** | HTTP头增强、RTSP头增强、HTTPS头增强、HTTP头防欺诈 |
| **Web Proxy** | Web Proxy 配置 |
| **IP重定向** | 三四层重定向功能 |
| **智能重定向** | 用户Portal配置 |
| **Remark/FPI** | IM类业务无线资源管控 |

> 注意：本批文档仅覆盖计费与策略控制中的三四层阻塞、IP重定向中的三四层重定向。其余实例（如七层阻塞配置、七层重定向配置、QoS保证、带宽控制、Shaping等）在各自特性指南文档中有完整描述。

### 2.4 特性License开关

**核心规则**：配置业务感知功能前，必须通过 `SET LICENSESWITCH` 命令打开对应特性的License开关。

**License层级关系**：
- **SA-basic（业务感知基础）**：必须开启，是所有业务感知功能的前置条件
- **其他SA特性License**：根据实际需求按需开启（如七层识别、Shaping、QoS保证等）

**命令**：`SET LICENSESWITCH`

**重要性**：License决定SA能力可用性。如果License未加载或开关未打开，即使配置了完整的Filter、FlowFilter、Rule链路，业务感知功能也不会生效。

### 2.5 三四层 vs 七层识别差异

| 对比维度 | 三四层（L3/L4） | 七层（L7） |
|----------|-----------------|------------|
| **识别维度** | IP地址、协议类型（TCP/UDP/ANY）、端口号 | URL、HTTP协议内容、应用层特征 |
| **匹配精度** | IP级别，粒度较粗 | URL/应用级别，粒度较细 |
| **配置复杂度** | 较低：Filter + FlowFilter + Rule | 较高：需额外配置L7Filter、协议绑定、特征库 |
| **依赖项** | 仅需License | 需License + 协议特征库（Signature Database） |
| **阻塞实现** | POLICYTYPE=PCC + PCCACTIONPROP(UPINITDNGATE=DISCARD) | POLICYTYPE=PCC + PCCACTIONPROP(UPINITDNGATE=DISCARD)，但Filter链含L7配置 |
| **重定向实现** | POLICYTYPE=IPREDIR（IP重定向，修改目的MAC） | URL重定向（MOD PCCACTIONPROP的UPINITREDIRNM/DNINITREDIRNM） |
| **Remark实现** | POLICYTYPE=REMARK_FPI（修改DSCP） | POLICYTYPE=REMARK_FPI（修改DSCP） |
| **特征库依赖** | 无 | 需加载协议特征库（DSP SIGNATUREDB / LOD SIGNATUREDB） |
| **适用场景** | 基于已知IP/端口的粗粒度控制 | 基于应用/URL的精细控制（如特定网站阻塞） |

### 2.6 Remark功能与DSCP标记

**定义**：UDG 将匹配到业务规则报文IP头中ToS域的DSCP值修改为指定值，用于调整报文的转发优先级和服务等级。

**配置参数**：
- `REMARKFPISEL=REMARK`：选择Remark动作（区别于FPI）
- `REMARKCFGTYPE=CLASS`：Remark配置类型，按分类方式标记
- `REMARKCLASS=CS1`：具体DSCP分类值（如CS1、CS2、EF等）

**与QoS联动**：Remark修改的DSCP值被下游网络设备读取，用于QoS调度。高优先级DSCP值（如EF）的报文获得更高转发优先级，低优先级DSCP值（如CS1）的报文在拥塞时更可能被丢弃。

**Alias Marking干扰**：调测Remark时必须关闭UserProfile的alias-marking功能（`ALIASMARKFLAG=DISABLE`），否则报文ToS域的值不会被改写，无法验证Remark效果。

### 2.7 七层重定向的两种实现

七层场景下的重定向使用URL重定向机制，与三四层的IP重定向有本质区别：

- **三四层重定向**：修改报文目的MAC地址，将报文转发到重定向设备（IP重定向，不修改目的IP）
- **七层重定向**：UDG模拟服务器向终端发送HTTP重定向报文（携带Location头），终端浏览器自动跳转到指定URL

**七层重定向关键配置**：
```
ADD REDIRECT:REDIRECTNAME="redirect_test",URL="www.example.com";
MOD PCCACTIONPROP:PCCACTPROPNAME="pap_test",UPINITREDIRNM="redirect_test",DNINITREDIRNM="redirect_test";
```

**重定向异常处理**：当用户发起HTTP承载请求但当前报文无法做重定向时，UDG缺省阻塞该报文。若需正常转发，可通过 `ADD IPFARMSERVER / MOD IPFARMSERVER` 设置 `DEFAULTACT=PASS`。

### 2.8 SET REFRESHSRV 刷新机制

**规则**：每次修改Filter配置后，必须执行 `SET REFRESHSRV` 命令使新配置生效。

- `REFRESHTYPE=USERPROFILE`：刷新UserProfile关联的Filter
- `REFRESHTYPE=ALL`：刷新所有Filter

**时序约束**：Filter修改后未执行REFRESHSRV，配置不会生效，会导致调测失败但配置数据看起来正确。

### 2.9 规则切换时的清理操作

在调测流程中，切换不同动作类型（如从阻塞切换到重定向、从重定向切换到Remark）时，必须先删除旧规则：

```
RMV RULE:RULENAME="rule_test",POLICYTYPE=PCC;      // 删除阻塞规则
RMV RULE:RULENAME="rule_test",POLICYTYPE=IPREDIR;   // 删除重定向规则
```

再新增新策略类型的Rule，防止旧策略干扰新动作的调测。

---

## 3. 配置调测要点

### 3.1 调测推荐顺序

六类功能调测存在推荐的先后顺序，基于功能间的复用关系：

```
三四层阻塞 -> 三四层重定向 -> 三四层Remark
                                    |
七层阻塞   -> 七层重定向   -> 七层Remark
```

- 阻塞是基础，后续重定向和Remark在阻塞配置基础上修改策略类型或动作属性
- 三四层和七层各自独立，可并行调测
- 三四层Remark的前置条件包含三四层重定向和三四层阻塞调测完成

### 3.2 三四层阻塞调测

| 步骤 | 动作 | 验证方法 |
|------|------|----------|
| 1 | 终端使用目标APN接入网络 | 终端成功接入 |
| 2 | 终端访问www.huawei.com | 正常访问（验证基础网络连通） |
| 3 | 终端访问10.11.11.11 | **无法访问**（阻塞生效） |
| 4 | 若未阻塞，查DSP SESSIONINFO | 验证APN正确 |
| 5 | 查LST RULEBINDING + LST RULE | 验证UserProfile绑定Rule正确 |
| 6 | 查LST PCCPOLICYGRP + LST PCCACTIONPROP | 验证UPINITDNGATE=DISCARD |
| 7 | 查LST FLTBINDFLOWF + LST FILTER | 验证Filter生效标记为"是" |

**典型问题**：
- Filter生效标记为"否"：未执行SET REFRESHSRV
- UPINITDNGATE不为DISCARD：PCC动作属性配置错误
- SVRIP/协议类型与规划不符：Filter参数配置错误

### 3.3 三四层重定向调测

| 步骤 | 动作 | 验证方法 |
|------|------|----------|
| 1 | MOD FILTER调整过滤条件（协议改为ANY，SVRIPMASK改为255.255.255.255不过滤IP） | - |
| 2 | RMV RULE删除旧PCC规则，ADD RULE新增IPREDIR规则 | - |
| 3 | DSP SESSIONINFO查终端IP | 获取测试终端IP地址 |
| 4 | 重定向设备上开抓包，终端访问www.huawei.com | **重定向设备收到报文且目的MAC为重定向设备MAC** |
| 5 | 若未重定向，查LST RULE | 验证策略类型为IP Redirect、IPREDIRECTIP正确 |
| 6 | 查LST FILTER | 验证三四层协议类型为ANY、生效标记为"是" |

**关键特征**：三四层重定向不修改报文目的IP，仅修改目的MAC地址。验证时必须通过抓包检查目的MAC，而非目的IP。

### 3.4 三四层Remark调测

| 步骤 | 动作 | 验证方法 |
|------|------|----------|
| 1 | MOD FILTER调整协议为UDP、SVRIP为192.168.200.20 | - |
| 2 | RMV RULE删除旧IPREDIR规则，ADD RULE新增REMARK_FPI规则 | REMARKCLASS=CS1 |
| 3 | MOD USERPROFILE关闭ALIASMARKFLAG | ALIASMARKFLAG=DISABLE |
| 4 | DSP SESSIONINFO查终端IP | 获取IP地址 |
| 5 | 终端访问192.168.200.20，镜像接口抓包 | 四个接口对比DSCP值 |
| 6 | 若DSCP未修改，查LST RULE | 验证策略类型为Remark or FPI |
| 7 | 查LST FILTER | 验证协议类型、SVRIP、生效标记 |
| 8 | 查LST USERPROFILE | 验证ALIASMARKFLAG=DISABLE |

**DSCP验证四点法**（上下行各两个接口）：
- S1-U/N3接口侧上行（入口）：DSCP为原始值（如0x00）
- Gi/N6接口侧上行（出口）：DSCP被修改为CS1（0x08）
- Gi/N6接口侧下行（入口）：DSCP为原始值（如0x00）
- S1-U/N3接口侧下行（出口）：DSCP被修改为CS1（0x08）

### 3.5 七层阻塞调测

| 步骤 | 动作 | 验证方法 |
|------|------|----------|
| 1 | 终端使用目标APN接入网络 | 终端成功接入 |
| 2 | 终端访问www.huawei.com | 正常访问 |
| 3 | 终端访问www.example.com | **无法访问**，Gi/N6侧无HTTP GET报文 |
| 4 | 若未阻塞，查DSP SESSIONINFO | 验证APN正确 |
| 5 | 查LST RULEBINDING + LST RULE | 验证策略类型为PCC |
| 6 | 查LST PCCPOLICYGRP + LST PCCACTIONPROP | 验证UPINITDNGATE=DISCARD |
| 7 | 查LST FLOWFILTER + LST PROTBINDFLOWF + LST L7FILTER | 验证七层过滤器URL配置 |
| 8 | 查LST FLTBINDFLOWF + LST FILTER | 验证三四层Filter生效 |
| 9 | 查DSP SIGNATUREDB | 验证协议特征库加载状态为"Load Finish" |

**七层调测特有步骤**：
- 需验证协议特征库（Signature Database）加载状态
- 需检查L7Filter的URL匹配规则
- 需检查PROTBINDFLOWF的协议绑定（如http协议）

### 3.6 七层重定向调测

| 步骤 | 动作 | 验证方法 |
|------|------|----------|
| 1 | ADD REDIRECT配置重定向目标URL，MOD PCCACTIONPROP设置UPINITREDIRNM/DNINITREDIRNM | - |
| 2 | 终端接入网络并访问www.huawei.com | 正常访问 |
| 3 | 终端访问www.example2.com | **终端跳转到www.example.com页面** |
| 4 | 镜像接口抓包验证 | UDG模拟服务器发送重定向报文+拆链报文 |
| 5 | 若未重定向，查LST RULE | 验证PCC策略组绑定 |
| 6 | 查LST PCCACTIONPROP | 验证UPINITREDIRNM已配置 |

**七层重定向报文特征**：
- UDG丢弃终端的HTTP GET请求
- UDG模拟服务器向终端发送HTTP重定向报文（携带重定向URL）
- UDG发送TCP拆链报文（模拟服务器向终端、模拟终端向真实服务器）

### 3.7 七层Remark调测

七层Remark的调测步骤与三四层Remark类似，区别在于：
- 前置条件为七层重定向调测完成（复用L7Filter配置）
- Filter链含L7配置，需验证L7Filter的URL匹配
- 抓包验证同样使用四点法对比DSCP值

**关键验证命令**：
```
LST RULE:RULENAME="rule_test",POLICYTYPE=REMARK_FPI;
LST PROTBINDFLOWF:FLOWFILTERNAME="ff_test";
LST L7FILTER:L7FILTERNAME="l7-test";
```

### 3.8 通用验证命令汇总

| 查询目标 | 命令 | 关键检查项 |
|----------|------|------------|
| 用户上下文 | DSP SESSIONINFO | IMSI、IP地址、APN |
| 规则绑定 | LST RULEBINDING | 规则名称、优先级、策略类型 |
| 规则配置 | LST RULE | 策略类型、流过滤器、PCC策略组/IPREDIR/REMARK参数 |
| PCC策略组 | LST PCCPOLICYGRP | PCC动作属性、URR组 |
| PCC动作属性 | LST PCCACTIONPROP | 门控（GATE）、重定向名称 |
| 流过滤器 | LST FLOWFILTER | 流过滤器名称 |
| 协议绑定 | LST PROTBINDFLOWF | 协议名称、七层过滤器（仅七层） |
| 七层过滤器 | LST L7FILTER | URL匹配规则（仅七层） |
| Filter绑定 | LST FLTBINDFLOWF | 过滤器名称 |
| 三四层Filter | LST FILTER | 协议类型、SVRIP、生效标记 |
| 特征库状态 | DSP SIGNATUREDB | 加载状态、版本（仅七层） |
| 配置导出 | EXP MML | 导出全部配置供分析 |

---

## 4. 与带宽控制的关系

### 4.1 阻塞 -- 带宽控制的极端形态

**阻塞 = 带宽控制的上限（完全阻断）**：
- 三四层阻塞通过PCC门控（GATE=DISCARD）丢弃特定IP/端口的全部报文，等效于带宽控制中的限速值设为0
- 七层阻塞通过URL匹配+PCC门控丢弃特定应用的全部报文，实现应用级完全阻断
- 在FUP（公平使用策略）场景中，当用户超出配额后，可使用阻塞功能完全阻断特定业务

### 4.2 重定向 -- 流量管控的引流手段

**重定向 = 带宽控制中的流量分流**：
- 三四层重定向将特定IP流量引到重定向设备（如防火墙、清洗设备），实现流量分流
- 七层重定向将特定URL流量重定向到指定页面（如Portal页面、提示页面），在带宽控制中常用于：
  - 用户超出配额时重定向到充值/提示页面
  - 特定应用重定向到缓存服务器减少骨干带宽消耗

### 4.3 Remark -- QoS优先级标记

**Remark = 带宽控制中的优先级调度手段**：
- DSCP值直接影响下游设备的QoS调度策略
- 高优先级业务（如VoLTE、视频）标记为高DSCP值（如EF），获得带宽保障
- 低优先级业务（如后台同步）标记为低DSCP值（如CS1），在带宽不足时优先降速
- 与带宽管理（BWM）配合：BWM控制总速率，Remark决定速率内的优先级分配

### 4.4 License -- SA能力的总开关

**License = 带宽控制能力的可用性前置条件**：
- SA-basic是所有业务感知功能的基础License
- 基于业务感知的带宽控制（GWFD-110311）、Shaping（GWFD-020354）等特性各有独立License
- License未加载时，即使配置完整，带宽控制功能也无法生效

### 4.5 在带宽控制场景中的定位

在带宽控制场景知识库中，本批文档提供的能力定位：

| 能力 | 在带宽控制中的角色 | 对应特性 |
|------|-------------------|----------|
| 三四层阻塞 | IP级流量阻断，FUP耗尽后的硬阻断 | SA-Basic, FUP |
| 七层阻塞 | 应用级流量阻断，特定App完全屏蔽 | SA-Basic, FUP |
| 三四层重定向 | IP流量分流到安全/缓存设备 | PCC, BWM |
| 七层重定向 | URL流量引流到Portal/提示页 | PCC, FUP |
| 三四层Remark | IP流量的QoS优先级标记 | QoS保证 |
| 七层Remark | 应用流量的QoS优先级标记 | QoS保证, BWM |

---

## 5. 关键术语

| 术语 | 释义 |
|------|------|
| **Remark** | 重标记，指修改报文IP头ToS域中DSCP值，用于调整报文转发优先级 |
| **DSCP** | Differentiated Services Code Point，差分服务代码点，IP报文头中6bit字段，标识报文的服务等级 |
| **ToS** | Type of Service，服务类型，IP报文头中的1字节字段，DSCP为其高6位 |
| **CS1/EF** | DSCP分类值。CS1（Class Selector 1）为低优先级，EF（Expedited Forwarding）为最高优先级 |
| **三四层（L3/L4）** | 指OSI模型第三层（网络层，IP）和第四层（传输层，TCP/UDP），基于IP地址和端口号识别 |
| **七层（L7）** | 指OSI模型第七层（应用层），基于URL、HTTP协议内容、应用特征识别具体应用 |
| **重定向（Redirect）** | 将匹配特定条件的报文引导到其他设备或地址。三四层为IP重定向（修改目的MAC），七层为URL重定向（HTTP 302跳转） |
| **阻塞（Block）** | 丢弃匹配特定条件的用户报文，使对应业务不可访问 |
| **门控（Gate）** | PCC动作属性中的报文通过/丢弃控制。DISCARD表示丢弃，PASS表示通过 |
| **PCC** | Policy and Charging Control，策略与计费控制。POLICYTYPE=PCC的规则可同时实现阻塞、门控、计费 |
| **IPREDIR** | IP Redirect，IP重定向策略类型。直接在RULE中配置重定向IP，不经过PCC |
| **REMARK_FPI** | Remark或FPI策略类型。REMARKFPISEL=REMARK表示DSCP重标记，REMARKFPISEL=FPI表示转发策略标识 |
| **Filter** | 过滤器，定义三四层匹配条件（IP、协议、端口） |
| **FlowFilter** | 流过滤器，将Filter组织为可被Rule引用的过滤单元 |
| **L7Filter** | 七层过滤器，定义URL、应用等七层匹配条件 |
| **PCCACTIONPROP** | PCC动作属性，定义门控（GATE）、重定向名称等执行参数 |
| **PCCPOLICYGRP** | PCC策略组，将PCC动作属性与URR组组合为策略单元 |
| **UserProfile** | 用户模板，承载规则绑定关系，最终应用到具体用户 |
| **RULEBINDING** | 规则绑定，将Rule绑定到UserProfile，使规则对用户生效 |
| **REFRESHSRV** | 业务刷新命令，Filter修改后必须执行以使配置生效 |
| **Signature Database** | 协议特征库，七层识别的基础数据库，需加载后才能识别应用 |
| **Alias Marking** | 别名标记功能，使能时报文ToS域不被改写，调测Remark时必须关闭 |
| **IPFarm** | IP Farm服务器，当七层重定向无法执行时，DEFAULTACT参数决定报文是阻塞还是正常转发 |
| **SET LICENSESWITCH** | License开关设置命令，开启业务感知特性License |

---

## 6. 知识来源

| 序号 | 文件名 | 内容主题 |
|------|--------|----------|
| 1 | 三四层业务阻塞功能_87804003.md | 三四层阻塞功能配置链与脚本示例 |
| 2 | 三四层重定向功能_92153850.md | 三四层IP重定向功能配置链与脚本示例 |
| 3 | 规则配置实例_92464022.md | 业务感知全部配置实例的全景索引 |
| 4 | 配置特性License开关_93112151.md | SA特性License开关配置规则 |
| 5 | 调测七层Remark功能_87804014.md | 七层DSCP重标记调测步骤与验证方法 |
| 6 | 调测七层重定向功能_87804013.md | 七层URL重定向调测步骤与验证方法 |
| 7 | 调测七层阻塞功能_87804012.md | 七层业务阻塞调测步骤与验证方法 |
| 8 | 调测三四层Remark功能_87804011.md | 三四层DSCP重标记调测步骤与验证方法 |
| 9 | 调测三四层重定向功能_87804010.md | 三四层IP重定向调测步骤与验证方法 |
| 10 | 调测三四层阻塞功能_87804009.md | 三四层业务阻塞调测步骤与验证方法 |

**原始路径前缀**：`output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/`

- 文件1-2：`激活业务感知/规则配置实例/`
- 文件3-4：`激活业务感知/`
- 文件5-10：`调测业务感知/`
