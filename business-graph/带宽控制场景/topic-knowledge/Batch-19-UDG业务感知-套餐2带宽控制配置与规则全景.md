# Batch-19: UDG业务感知专题 - 套餐2带宽控制配置与规则全景

> **批次**: Batch-19 | **主题**: 业务感知规则配置全景 + 套餐2带宽控制配置实例 | **来源**: UDG业务感知专题
> **文件数**: 10 | **核心度**: ★★★★★（带宽控制场景的直接配置指南）

---

## 1. 概述

本批文档来自UDG业务感知专题的"业务感知配置 > 激活业务感知"模块，涵盖两大核心板块：

**板块一：基于业务套餐的配置实例**
- **套餐2：带宽控制**（★绝对重点）：5个带宽控制业务场景的端到端MML配置实例，包含最低速率保障、最高速率限制、流量整形、普通业务限速、超量降速共5种BWM策略类型，以及黑名单例外配置
- **套餐3：访问限制场景**（参照）：阻塞、头增强、IP重定向、URL重定向4种PCC/HEADEN/IPREDIR策略类型的配置实例，用于对比理解Rule的多策略类型支持

**板块二：规则配置体系**
- **规则配置全景**：SA规则的完整配置地图（流过滤条件 + 流动作 + Rule + User Profile四层架构）
- **配置Rule**：Rule的结构、字段、PCC/IPREDIR/BWM三种策略类型、黑名单规则
- **配置User Profile与公共策略**：用户模板、规则绑定、URL白名单、兜底计费（URR）
- **配置PCC策略**：PCC动作属性（门控、重定向）、PCC策略组
- **配置带宽控制策略**：CategoryProp（分类属性），作为BWM策略的入口
- **配置流过滤条件**：三四层过滤器、七层过滤器、协议识别、流过滤器（组）

**板块三：规则配置实例**
- **七层业务阻塞功能**：PCC DISCARD门控实现URL阻塞的完整配置流程
- **七层重定向功能**：PCC重定向实现URL到URL跳转的完整配置流程

这批文档是带宽控制场景的核心配置指南，套餐2直接对应带宽控制的完整业务实现。

---

## 2. 核心知识点

### KP-01: 套餐2带宽控制 - 业务场景定义与策略矩阵

套餐2定义了5个带宽控制业务，覆盖了带宽管理的全部典型场景：

| 业务编号 | 三四层过滤 | 七层过滤 | 策略类型 | 策略 | 优先级 |
|----------|-----------|---------|---------|------|--------|
| 业务1-高速业务 | 任意 | https://www.huawei.com | BWM | 最低10Mbps保障 | 100 |
| 业务2-限速业务 | 任意 | FTP | BWM | 最高8Mbps限制 | 110 |
| 业务3-直播业务 | 任意（例外：10.11.12.13） | https://www.example.com旗下所有网站 | BWM | 整形至10Mbps | 120 |
| 业务4-普通业务 | 任意 | 任意 | BWM | 最高20Mbps限制 | 200 |
| 业务5-限速限额业务 | 任意 | 任意 | BWM | 最高2Mbps限制 | 50 |

关键设计要点：
- 业务1-3过滤条件无交集，优先级相近（100/110/120）
- 业务4是兜底规则，优先级最低（200），匹配剩余流量
- 业务5是强制降速规则，优先级最高（50），优先于业务1-4生效
- 业务3存在例外情况（FTP访问10.11.12.13不受限速），通过黑名单规则实现

### KP-02: 套餐2带宽控制 - 三四层与七层过滤条件配置

**三四层过滤器配置**：所有业务的三四层过滤条件均为"任意"，共用filterA；业务3的例外情况需要额外配置filterC1

```
ADD FILTER:FILTERNAME="filterA",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FILTER:FILTERNAME="filterC1",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRIPMODE=IP,SVRIP="10.11.12.13",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0";
```

**七层过滤器配置**：业务1-3需要七层过滤，业务4-5不需要

```
ADD L7FILTER:L7FILTERNAME="l7filterA",SUBL7FLTNAME="sl7A",URLTYPE=URL,URL="www.huawei.com";
ADD L7FILTER:L7FILTERNAME="l7filterB",SUBL7FLTNAME="sl7B";
ADD L7FILTER:L7FILTERNAME="l7filterC",SUBL7FLTNAME="sl7C",URLTYPE=URL,URL="www.example.com*/*";
```

关键规则：
- l7filterB仅用于绑定FTP协议，不配置URL
- l7filterC配置通配URL `www.example.com*/*`，匹配该域名下所有路径
- filterC1用于例外情况，通过服务器IP 10.11.12.13精确匹配

### KP-03: 套餐2带宽控制 - 流过滤器组装

流过滤器是三四层过滤条件 + 协议识别 + 七层过滤条件的组合：

```
// 业务1（HTTPS + www.huawei.com）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterA";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterA";

// 业务2（FTP）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterB";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterB",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterB",PROTOCOLNAME="FTP",L7FILTERNAME="l7filterB";

// 业务3（HTTPS + www.example.com）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterC";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterC",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterC",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterC";

// 业务4、5（任意，共用flowfilterD）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterD";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterD",FILTERNAME="filterA";

// 黑名单规则（例外情况：FTP访问10.11.12.13）
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterC1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterC1",FILTERNAME="filterC1";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterC",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterC";
```

关键规则：
- PROTBINDFLOWF将协议（HTTPS/FTP）和七层过滤器绑定到流过滤器
- 业务4和5共享flowfilterD，因为它们的过滤条件完全相同（任意），通过优先级区分
- 黑名单流过滤器flowfilterC1绑定filterC1（精确IP匹配），保持相同的协议和七层过滤器

### KP-04: 套餐2带宽控制 - BWM流动作配置（核心）

BWM流动作由四层配置构成，每层都是递进依赖关系：

**层级1：分类属性（CategoryProp）** - BWM策略的入口标识
```
ADD CATEGORYPROP:CATEPROPNAME="catropA";  // 业务1
ADD CATEGORYPROP:CATEPROPNAME="catropB";  // 业务2
ADD CATEGORYPROP:CATEPROPNAME="catropC";  // 业务3
ADD CATEGORYPROP:CATEPROPNAME="catropD";  // 业务4
ADD CATEGORYPROP:CATEPROPNAME="catropE";  // 业务5
```

**层级2：带宽管理服务（BWMService）** - 将分类属性绑定到BWM服务
```
ADD BWMSERVICE:BWMSERVICENAME="bwmservA",BWMSERVICETYPE=NONTOS,
    NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropA";
```

**层级3：带宽管理控制器（BWMController）** - 定义具体的速率控制参数

| 控制器 | 控制类型 | 参数 | 对应业务 | 语义 |
|--------|---------|------|---------|------|
| bwmcontrolA | CAR | CIR=10240 | 业务1 | 最低速率保障10Mbps |
| bwmcontrolB | CAR | PIR=8192 | 业务2 | 最高速率限制8Mbps |
| bwmcontrolC | SHAPING | RATE=10240 | 业务3 | 流量整形至10Mbps |
| bwmcontrolD | CAR | PIR=20480 | 业务4 | 最高速率限制20Mbps |
| bwmcontrolE | CAR | PIR=2048 | 业务5 | 最高速率限制2Mbps |

```
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolA",CTRLTYPE=CAR,CIR=10240;
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolB",CTRLTYPE=CAR,PIR=8192;
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolC",CTRLTYPE=SHAPING,RATE=10240;
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolD",CTRLTYPE=CAR,PIR=20480;
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolE",CTRLTYPE=CAR,PIR=2048;
```

**层级4：用户组 + BWM规则** - 将控制器绑定到用户组，形成BWM规则

```
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",
    USERGROUPPRI=100,USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",
    BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleA",
    BWMSERVICENAME="bwmservA",
    UPBWMCTRLNAME1="bwmcontrolA",DNBWMCTRLNAME1="bwmcontrolA",
    BWMRULEPRI=100;
```

关键参数说明：
- CTRLTYPE=CAR：承诺接入速率，支持CIR（承诺信息速率）和PIR（峰值信息速率）
- CTRLTYPE=SHAPING：流量整形，使用RATE参数设定目标速率
- CIR：保证最低带宽（Committed Information Rate），单位kbps，10240 = 10Mbps
- PIR：限制最高带宽（Peak Information Rate），单位kbps，8192 = 8Mbps
- UPBWMCTRLNAME1/DNBWMCTRLNAME1：上行/下行方向各自绑定控制器，可分别配置不同速率
- BWMRULEPRI：BWM规则内部优先级，与Rule的PRIORITY配合控制匹配顺序

### KP-05: 套餐2带宽控制 - Rule配置与黑名单

**Rule配置**：将流过滤器与BWM策略绑定，并设置全局优先级

```
ADD RULE:RULENAME="ruleA",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,
    FLOWFILTERNAME="flowfilterA",POLICYNAME="catropA",PRIORITY=100;
ADD RULE:RULENAME="ruleB",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,
    FLOWFILTERNAME="flowfilterB",POLICYNAME="catropB",PRIORITY=110;
ADD RULE:RULENAME="ruleC",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,
    FLOWFILTERNAME="flowfilterC",POLICYNAME="catropC",PRIORITY=120;
ADD RULE:RULENAME="ruleD",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,
    FLOWFILTERNAME="flowfilterD",POLICYNAME="catropD",PRIORITY=200;
ADD RULE:RULENAME="ruleE",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,
    FLOWFILTERNAME="flowfilterD",POLICYNAME="catropE",PRIORITY=50;
```

**黑名单规则**：业务3的例外情况
```
ADD BLACKLISTRULE:RULENAME="ruleC1",POLICYTYPE=BWM,
    FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC1";
```

黑名单规则的核心机制：
- 当报文命中某规则的同时也命中同策略类型的黑名单规则，则该规则不生效
- PCC类型不支持黑名单规则
- IPREDIR/SRV_TRIGGER策略类型的黑名单规则不支持绑定七层协议和协议组的流过滤器
- 黑名单规则实现"例外"场景：FTP访问10.11.12.13不受带宽整形限制

**Rule优先级规则**：
- 优先级范围1-65535，数值越小优先级越高
- 优先级仅在同种策略类型的规则内生效
- 不同策略类型之间的优先级独立
- ruleE（PRIORITY=50）优先于所有其他BWM规则生效，实现超量降速

### KP-06: 套餐2带宽控制 - User Profile绑定与生效

将所有Rule绑定到同一个User Profile，形成最终业务套餐：

```
ADD USERPROFILE:USERPROFILENAME="up_bwmcontrol";
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleA",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleB",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleC",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleD",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleE",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleC1",POLICYTYPE=BWM;
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

关键点：
- 黑名单规则也需要通过RULEBINDING绑定到User Profile
- SET REFRESHSRV是最后一步，必须执行才能使配置生效
- 一个User Profile可以绑定多种策略类型的Rule（PCC/BWM/HEADEN/IPREDIR等）

### KP-07: 规则配置全景架构（四层模型）

SA规则配置采用四层架构模型：

```
第1层：流过滤条件
  ├── 三四层过滤器（Filter/FilterIPv6/过滤器组）
  ├── 协议识别（特征库识别 / 知名端口识别）
  └── 七层过滤器（L7Filter - URL匹配）
      └── 组合为 → 流过滤器（FlowFilter）/ 流过滤器组（FlowFilterGRP）

第2层：流动作
  ├── PCC策略（门控、重定向、计费）
  ├── BWM策略（CAR限速、SHAPING整形）
  ├── 头增强（HEADEN）
  └── IP重定向（IPREDIR）

第3层：Rule
  ├── ADD RULE（将流过滤器与流动作绑定，设置优先级）
  └── ADD BLACKLISTRULE（黑名单规则，命中则对应策略不生效）

第4层：User Profile
  ├── ADD USERPROFILE（用户模板，公共策略容器）
  ├── ADD RULEBINDING（绑定多条Rule）
  ├── URL白名单
  └── 兜底计费策略（URR + URRGROUP）
```

### KP-08: 三四层过滤器与七层过滤器详细配置

**三四层过滤器（ADD FILTER）核心参数**：
- FILTERNAME：过滤器名称
- L34PROTTYPE：三四层协议输入类型（STRING/其他）
- L34PROTOCOL：三四层协议类型（ANY/TCP/UDP）
- MSIPMODE：手机IP配置模式（IPLIST/IP/ANY）
- MSIPLISTNAME：手机IP列表名称（配合ADD IPLIST使用）
- SVRIPMODE：服务器IP配置模式（IP/ANY）
- SVRIP：服务器IP地址
- SVRIPMASKTYPE：掩码类型（IPTYPE/LENGTHTYPE）
- SVRIPMASK / SVRIPMASKLEN：掩码值/掩码长度

**七层过滤器（ADD L7FILTER）核心参数**：
- L7FILTERNAME：七层过滤器名称
- SUBL7FLTNAME：子七层过滤器名称
- URLTYPE：URL类型（URL）
- URL：匹配的URL模式

**URL匹配规则详解**（7条规则）：
1. URL的Host和Path分别匹配；Host末尾有`*`不包含Path时，有Path的报文匹配失败
2. 定义URL和报文URL末尾的`/`在匹配时被忽略
3. Path中含`*`在某级目录中间/结尾时，报文目录层级需与定义一致
4. Path中含`*`作为独立目录或文件名时，报文目录层级需大于或等于定义
5. Host开头或中间支持`*`通配
6. 端口匹配：一方未带端口则忽略端口；都带端口则需匹配；`*`可表示端口通配
7. `?`有两种含义：通配符（&#3f转义）或正常问号（%3f转义）

### KP-09: 协议识别机制

协议识别有两种方式：

1. **特征库识别（默认）**：通过业务感知协议特征库识别协议/协议组，包括HTTP、WAP、P2P、VoIP等
2. **知名端口识别**：通过协议端口识别，效率更高但可能误判
   - HTTP: 80/8080
   - WAP1.X: 9200-9201
   - IMAP4: 143
   - DNS: 53
   - FTP: 20/21
   - SMTP: 25
   - POP3: 110
   - RTSP: 554
   - TFTP: 69

当知名端口与特征库识别结果矛盾时，通过软参BIT414控制：
- BIT414=0（默认）：以知名端口识别结果为准
- BIT414=1：以特征库识别结果为准
- 建议：当知名端口携带非知名协议时（如80端口被Skype使用），将BIT414置为1

### KP-10: PCC策略配置详解

PCC策略用于实现计费、URL重定向、阻塞等动作，由三步组成：

**步骤1（可选）：配置重定向**
```
ADD REDIRECT:REDIRECTNAME="redirect_1",URL="https://www.huawei.com";
```

**步骤2：配置PCC动作属性**

PCC动作属性的四个门控参数：
| 参数 | 含义 | 取值 |
|------|------|------|
| UPINITUPGATE | 上行发起的上行门控 | PASS/DISCARD |
| UPINITDNGATE | 上行发起的下行门控 | PASS/DISCARD |
| DNINITUPGATE | 下行发起的上行门控 | PASS/DISCARD |
| DNINITDNGATE | 下行发起的下行门控 | PASS/DISCARD |

重定向参数：
| 参数 | 含义 |
|------|------|
| UPINITREDIRNM | 上行发起重定向名称 |
| DNINITREDIRNM | 下行发起重定向名称 |

阻塞示例（上行丢弃，下行放行）：
```
ADD PCCACTIONPROP:PCCACTPROPNAME="pccact_2",
    UPINITUPGATE=DISCARD,UPINITDNGATE=PASS,
    DNINITUPGATE=DISCARD,DNINITDNGATE=PASS;
```

重定向示例（上下行均重定向）：
```
ADD PCCACTIONPROP:PCCACTPROPNAME="pccact_1",
    UPINITREDIRNM="redirect_1",DNINITREDIRNM="redirect_1";
```

**步骤3：配置PCC策略组**
```
ADD PCCPOLICYGRP:PCCPOLICYGRPNM="pccpolicygrp_1",
    PCCACTPROPNAME="pccact_1",URRGROUPNAME="urrgroup1";
```

### KP-11: User Profile与公共策略

User Profile（用户模板）是规则的容器，包含公共策略：

**核心配置**：
- ADD USERPROFILE：创建用户模板，配置功能开关（实时位置上报LOCRPTSWITCH、Tethering最大终端数TETHERINGMAXNUM等）
- ADD RULEBINDING：将Rule绑定到User Profile（黑名单规则也需绑定）
- SET REFRESHSRV:REFRESHTYPE=USERPROFILE：使配置生效

**URL白名单**：当用户计费配额不足时，仍可访问白名单中的URL
```
ADD WHITEURLLIST:WHITELISTNAME="list_1",URL="www.huawei.com";
SET WHITEURLLISTBIND:USERPROFILENAME="up_1",WHITELISTNAME="list_1";
```

**兜底计费**：当报文未命中任何规则时使用默认计费策略
```
ADD URR:URRNAME="URR_default",URRID=1000,USAGERPTMODE=ONLINE;
ADD URRGROUP:URRGROUPNAME="urrgrp_1",
    UPURRNAME2="URR_default",DOWNURRNAME2="URR_default";
SET URRGRPBINDING:USERPROFILENAME="up_1",DFTURRGRPNAME="urrgrp_1";
```

### KP-12: 套餐3访问限制 - 多策略类型对比（参照）

套餐3展示了PCC、HEADEN、IPREDIR三种策略类型的组合使用：

| 业务 | 过滤条件 | 策略类型 | 动作 | 优先级 |
|------|---------|---------|------|--------|
| 阻塞 | www.example.com | PCC | 上下行全DISCARD | 500 |
| 头增强 | www.vmall.com | HEADEN | 插入MSISDN+防欺诈 | 550 |
| IP重定向 | 端口1000-20000 | IPREDIR | 重定向至10.100.111.222 | 700 |
| URL重定向 | 任意 | PCC | 重定向到充值页面 | 400 |

关键差异：
- PCC阻塞通过四个门控全设DISCARD实现：`UPINITUPGATE=DISCARD,UPINITDNGATE=DISCARD,DNINITUPGATE=DISCARD,DNINITDNGATE=DISCARD`
- HEADEN策略通过ADD HEADEN配置头增强，参数包括DATATYPE=MSISDN1,ANTIFRAUD=ENABLE
- IPREDIR策略在Rule级别配置重定向IP：`REDIRIPVERFLAG=IPV4,IPREDIRECTIP=10.100.111.222`
- 三四层过滤条件支持端口范围：`MSSTARTPORT=1000,MSENDPORT=20000`

---

## 3. 配置调测要点

### 3.1 套餐2带宽控制 - 端到端MML命令序列

以下是套餐2带宽控制的完整配置流程（按执行顺序）：

**第1步：配置三四层过滤条件**
```mml
ADD FILTER:FILTERNAME="filterA",L34PROTTYPE=STRING,L34PROTOCOL=ANY;
ADD FILTER:FILTERNAME="filterC1",L34PROTTYPE=STRING,L34PROTOCOL=ANY,SVRIPMODE=IP,SVRIP="10.11.12.13",SVRIPMASKTYPE=IPTYPE,SVRIPMASK="0.0.0.0";
```

**第2步：配置七层过滤条件**
```mml
ADD L7FILTER:L7FILTERNAME="l7filterA",SUBL7FLTNAME="sl7A",URLTYPE=URL,URL="www.huawei.com";
ADD L7FILTER:L7FILTERNAME="l7filterB",SUBL7FLTNAME="sl7B";
ADD L7FILTER:L7FILTERNAME="l7filterC",SUBL7FLTNAME="sl7C",URLTYPE=URL,URL="www.example.com*/*";
```

**第3步：配置流过滤器并绑定过滤条件**
```mml
ADD FLOWFILTER:FLOWFILTERNAME="flowfilterA";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterA",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterA",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterA";

ADD FLOWFILTER:FLOWFILTERNAME="flowfilterB";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterB",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterB",PROTOCOLNAME="FTP",L7FILTERNAME="l7filterB";

ADD FLOWFILTER:FLOWFILTERNAME="flowfilterC";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterC",FILTERNAME="filterA";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterC",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterC";

ADD FLOWFILTER:FLOWFILTERNAME="flowfilterD";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterD",FILTERNAME="filterA";

ADD FLOWFILTER:FLOWFILTERNAME="flowfilterC1";
ADD FLTBINDFLOWF:FLOWFILTERNAME="flowfilterC1",FILTERNAME="filterC1";
ADD PROTBINDFLOWF:FLOWFILTERNAME="flowfilterC",PROTOCOLNAME="HTTPS",L7FILTERNAME="l7filterC";
```

**第4步：配置BWM流动作（5个业务，每个4条命令 = 20条命令）**
```mml
// 业务1：最低速率保障10Mbps (CIR=10240kbps)
ADD CATEGORYPROP:CATEPROPNAME="catropA";
ADD BWMSERVICE:BWMSERVICENAME="bwmservA",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropA";
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolA",CTRLTYPE=CAR,CIR=10240;
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",USERGROUPPRI=100,USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpA",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleA",BWMSERVICENAME="bwmservA",UPBWMCTRLNAME1="bwmcontrolA",DNBWMCTRLNAME1="bwmcontrolA",BWMRULEPRI=100;

// 业务2：最高速率限制8Mbps (PIR=8192kbps)
ADD CATEGORYPROP:CATEPROPNAME="catropB";
ADD BWMSERVICE:BWMSERVICENAME="bwmservB",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropB";
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolB",CTRLTYPE=CAR,PIR=8192;
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpB",USERGROUPPRI=110,USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpB",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleB",BWMSERVICENAME="bwmservB",UPBWMCTRLNAME1="bwmcontrolB",DNBWMCTRLNAME1="bwmcontrolB",BWMRULEPRI=110;

// 业务3：流量整形至10Mbps (RATE=10240kbps)
ADD CATEGORYPROP:CATEPROPNAME="catropC";
ADD BWMSERVICE:BWMSERVICENAME="bwmservC",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropC";
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolC",CTRLTYPE=SHAPING,RATE=10240;
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpC",USERGROUPPRI=120,USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpC",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleC",BWMSERVICENAME="bwmservC",UPBWMCTRLNAME1="bwmcontrolC",DNBWMCTRLNAME1="bwmcontrolC",BWMRULEPRI=120;

// 业务4：普通业务最高20Mbps (PIR=20480kbps)
ADD CATEGORYPROP:CATEPROPNAME="catropD";
ADD BWMSERVICE:BWMSERVICENAME="bwmservD",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropD";
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolD",CTRLTYPE=CAR,PIR=20480;
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpD",USERGROUPPRI=200,USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpD",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleD",BWMSERVICENAME="bwmservD",UPBWMCTRLNAME1="bwmcontrolD",DNBWMCTRLNAME1="bwmcontrolD",BWMRULEPRI=200;

// 业务5：超量降速最高2Mbps (PIR=2048kbps)
ADD CATEGORYPROP:CATEPROPNAME="catropE";
ADD BWMSERVICE:BWMSERVICENAME="bwmservE",BWMSERVICETYPE=NONTOS,NONTOSSRVTYPE=CATEGORY_PROP,CATEPROPNAME="catropE";
ADD BWMCONTROLLER:BWMCNAME="bwmcontrolE",CTRLTYPE=CAR,PIR=2048;
ADD BWMUSERGROUP:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpE",USERGROUPPRI=50,USERLEVSRVTYPE=NONTOS;
ADD BWMRULE:USERGROUPTYPE=SPECIFIC_GROUP,USERGROUPNAME="bwmgrpE",BWMRULETYPE=SUBSCRIBER_SPECIFIC,BWMRULENAME="bwmruleE",BWMSERVICENAME="bwmservE",UPBWMCTRLNAME1="bwmcontrolE",DNBWMCTRLNAME1="bwmcontrolE",BWMRULEPRI=50;
```

**第5步：配置Rule和黑名单规则**
```mml
ADD RULE:RULENAME="ruleA",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterA",POLICYNAME="catropA",PRIORITY=100;
ADD RULE:RULENAME="ruleB",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterB",POLICYNAME="catropB",PRIORITY=110;
ADD RULE:RULENAME="ruleC",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC",POLICYNAME="catropC",PRIORITY=120;
ADD RULE:RULENAME="ruleD",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterD",POLICYNAME="catropD",PRIORITY=200;
ADD RULE:RULENAME="ruleE",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterD",POLICYNAME="catropE",PRIORITY=50;
ADD BLACKLISTRULE:RULENAME="ruleC1",POLICYTYPE=BWM,FILTERINGMODE=FLOWFILTER,FLOWFILTERNAME="flowfilterC1";
```

**第6步：配置User Profile并生效**
```mml
ADD USERPROFILE:USERPROFILENAME="up_bwmcontrol";
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleA",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleB",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleC",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleD",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleE",POLICYTYPE=BWM;
ADD RULEBINDING:USERPROFILENAME="up_bwmcontrol",RULENAME="ruleC1",POLICYTYPE=BWM;
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

### 3.2 BWM控制器关键参数速查表

| 控制类型 | 参数 | 语义 | 带宽控制策略 | 适用场景 |
|---------|------|------|------------|---------|
| CAR | CIR | 承诺信息速率 | 最低带宽保障 | 高速业务、VIP保障 |
| CAR | PIR | 峰值信息速率 | 最高带宽限制 | 限速业务、普通业务、超量降速 |
| CAR | CIR+PIR | 承诺+峰值 | 保障+限制双重控制 | 既有保障又有上限 |
| SHAPING | RATE | 整形目标速率 | 流量整形至固定速率 | 直播业务、需要平滑流量 |

速率单位换算：参数值单位为kbps
- 1Mbps = 1024kbps
- 10Mbps = 10240kbps
- 8Mbps = 8192kbps
- 20Mbps = 20480kbps
- 2Mbps = 2048kbps

### 3.3 流过滤器配置检查点

| 检查项 | 检查内容 | 预期结果 |
|--------|---------|---------|
| 三四层过滤 | filterA是否配置为ANY | L34PROTOCOL=ANY |
| 七层URL匹配 | URL通配是否正确 | www.example.com*/* 匹配所有路径 |
| 协议绑定 | PROTBINDFLOWF是否正确绑定协议和L7Filter | 协议名与L7Filter名称匹配 |
| 黑名单流过滤器 | flowfilterC1是否绑定正确的filter和协议 | filterC1 + HTTPS + l7filterC |
| REFRESHSRV | 过滤器配置后是否执行刷新 | SET REFRESHSRV:REFRESHTYPE=ALL |

### 3.4 Rule优先级设计检查点

| 检查项 | 检查内容 | 预期结果 |
|--------|---------|---------|
| 强制降速规则 | ruleE优先级是否最高 | PRIORITY=50（数值最小） |
| 兜底规则 | ruleD优先级是否最低（排除黑名单） | PRIORITY=200 |
| 业务1-3 | 优先级是否无交集且预留间隔 | 100/110/120 |
| 黑名单 | 是否配置了BLACKLISTRULE | ruleC1存在 |
| 生效检查 | SET REFRESHSRV是否执行 | USERPROFILE已刷新 |

### 3.5 SET REFRESHSRV使用规则

- 过滤器配置完成后需执行 `SET REFRESHSRV:REFRESHTYPE=ALL` 使过滤条件生效
- User Profile绑定完成后需执行 `SET REFRESHSRV:REFRESHTYPE=USERPROFILE` 使规则生效
- 可配置多个过滤器后再执行一次SET REFRESHSRV，批量生效
- SET REFRESHSRV必须是配置流程的最后一步

---

## 4. 与带宽控制的关系

本批文档是带宽控制场景的**核心配置指南**，关系如下：

### 4.1 直接对应关系

| 文档 | 与带宽控制的关系 | 核心度 |
|------|----------------|--------|
| 套餐2：带宽控制 | 带宽控制场景的完整端到端配置实例，包含5种BWM策略类型 | ★★★★★ |
| 配置带宽控制策略 | CategoryProp的配置方法，是BWM策略的入口 | ★★★★★ |
| 配置Rule | Rule配置方法，BWM策略通过POLICYTYPE=BWM绑定 | ★★★★☆ |
| 规则配置全景 | SA规则四层架构，BWM是其中的流动作类型之一 | ★★★★☆ |
| 配置流过滤条件 | 三四层和七层过滤器配置，是BWM规则匹配的前提 | ★★★★☆ |
| 配置User Profile与公共策略 | 用户模板配置，是BWM规则绑定的终点 | ★★★☆☆ |
| 套餐3：访问限制 | 参照实例，展示PCC/HEADEN/IPREDIR策略类型 | ★★☆☆☆ |
| 配置PCC策略 | PCC策略配置，带宽控制场景中一般不直接使用 | ★★☆☆☆ |
| 七层业务阻塞 | PCC DISCARD实现阻塞，与带宽控制是不同策略类型 | ★★☆☆☆ |
| 七层重定向 | PCC重定向实现URL跳转，与带宽控制是不同策略类型 | ★★☆☆☆ |

### 4.2 BWM策略类型的带宽控制语义

套餐2展示了带宽控制的5种典型业务模式，直接对应带宽控制场景的核心需求：

1. **最低速率保障（CIR）**：业务1模式，保证关键业务最低带宽
2. **最高速率限制（PIR）**：业务2/4/5模式，限制非关键业务带宽消耗
3. **流量整形（SHAPING）**：业务3模式，将流量平滑至目标速率
4. **兜底限速**：业务4模式，对未匹配特定业务的所有流量施加默认限制
5. **超量降速**：业务5模式，当用户累计流量超过阈值后强制降速

### 4.3 与Feature Knowledge的对应

这批文档中出现的配置对象直接对应以下带宽控制场景的特性知识：
- BWMCONTROLLER + BWMRULE + BWMUSERGROUP → 对应 GWFD-110311 基于业务感知的带宽控制
- CATEGORYPROP + BWMSERVICE → BWM分类属性和服务的配置入口
- RULE(POLICYTYPE=BWM) + BLACKLISTRULE → 规则匹配与例外配置
- SHAPING控制类型 → 对应 GWFD-020354/110313 基于业务感知的流量整形

---

## 5. 关键术语

| 术语 | 全称/含义 | 说明 |
|------|----------|------|
| SA | Service Awareness，业务感知 | UDG对用户报文进行深度解析，识别业务类型并执行策略 |
| BWM | Bandwidth Management，带宽管理 | 对业务流进行带宽控制，包括限速、保障、整形 |
| CAR | Committed Access Rate，承诺接入速率 | 带宽控制类型，支持CIR和PIR双速率控制 |
| CIR | Committed Information Rate，承诺信息速率 | 保证的最低带宽，单位kbps |
| PIR | Peak Information Rate，峰值信息速率 | 允许的最高带宽，单位kbps |
| SHAPING | 流量整形 | 将流量平滑至目标速率，使用RATE参数 |
| CategoryProp | 分类属性 | BWM策略的入口标识，通过ADD CATEGORYPROP配置 |
| BWMService | 带宽管理服务 | 将分类属性与带宽控制关联，BWMSERVICETYPE=NONTOS表示非TOS场景 |
| BWMController | 带宽管理控制器 | 定义具体的速率控制参数（CIR/PIR/RATE） |
| BWMUserGroup | BWM用户组 | 承载BWM规则的逻辑分组，USERGROUPTYPE=SPECIFIC_GROUP |
| BWMRule | BWM规则 | 将控制器绑定到用户组，区分上下行控制 |
| FlowFilter | 流过滤器 | 三四层过滤条件+协议识别+七层过滤条件的组合 |
| Rule | 规则 | 将流过滤器与流动作绑定，配置匹配优先级 |
| BlacklistRule | 黑名单规则 | 命中后使对应策略不生效，实现"例外"场景 |
| User Profile | 用户模板 | 规则的容器，包含公共策略 |
| PCC | Policy and Charging Control，策略与计费控制 | 另一种策略类型，支持门控、重定向、计费 |
| UP/DN | Uplink/Downlink，上行/下行 | BWMController可分别配置上行和下行控制器 |
| REFRESHSRV | 业务刷新 | 使配置生效的命令，必须最后执行 |
| NONTOS | 非TOS（Type of Service） | BWM服务类型，表示不基于IP TOS字段分类 |

---

## 6. 知识来源

| 序号 | 文件名 | 核心内容 | 文档ID |
|------|--------|---------|--------|
| 1 | 套餐2：带宽控制_94838085.md | 5个带宽控制业务的端到端配置实例（CIR保障/PIR限速/SHAPING整形/兜底限速/超量降速+黑名单例外） | ZH-CN_TOPIC_0294838085 |
| 2 | 套餐3：访问限制场景_94838086.md | 阻塞/头增强/IP重定向/URL重定向4种策略类型的配置实例（参照） | ZH-CN_TOPIC_0294838086 |
| 3 | 规则配置全景_92882615.md | SA规则四层架构总览，URL匹配7条规则，协议识别两种方式 | ZH-CN_TOPIC_0292882615 |
| 4 | 配置Rule_87803997.md | Rule的配置方法（PCC/IPREDIR/BWM三种场景），黑名单规则 | ZH-CN_OPI_0287803997 |
| 5 | 配置User Profile与公共策略_90601230.md | 用户模板、规则绑定、URL白名单、兜底计费 | ZH-CN_OPI_0290601230 |
| 6 | 配置PCC策略_87803995.md | PCC动作属性（门控/重定向）、PCC策略组 | ZH-CN_OPI_0287803995 |
| 7 | 配置带宽控制策略_92145040.md | CategoryProp分类属性配置（BWM策略入口） | ZH-CN_OPI_0292145040 |
| 8 | 配置流过滤条件_87803991.md | 三四层过滤器、七层过滤器、协议识别、流过滤器（组）完整配置 | ZH-CN_OPI_0287803991 |
| 9 | 七层业务阻塞功能_87804004.md | PCC DISCARD门控实现URL阻塞的完整实例 | ZH-CN_OPI_0287804004 |
| 10 | 七层重定向功能_92393307.md | PCC重定向实现URL到URL跳转的完整实例 | ZH-CN_OPI_0292393307 |
