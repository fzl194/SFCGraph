# Canonical Compound 登记表 — UDG@20.15.2
> 派生自 index.json compounds 段(spec §8.3)。Agent 复用查找用;人审通过的新 compound 自动入表(重跑 build_index.py 刷新)。
> compound 总数 24 | backbone(≥5 特性复用) 4 | 专用 20

## backbone(高频复用,≥5 特性)

### 1-00003 规则与用户模板绑定  (复用 25 特性)
- intent: 配置规则ADD RULE→用户模板ADD USERPROFILE→绑定ADD RULEBINDING
- command_set: ADD RULE, ADD RULEBINDING, ADD USERPROFILE
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00005, 2-00006, 2-00009, 2-00010, 2-00011, 2-00012, 2-00013, 2-00014, 2-00015, 2-00016, 2-00017, 2-00018, 2-00030, 2-00031, 2-00034, 2-00036, 2-00037, 2-00050, 2-00083, 2-00089, 2-00091

### 1-00002 过滤链  (复用 22 特性)
- intent: 配置三四层/七层过滤器→聚合为FLOWFILTER→绑定（三四层FLTBINDFLOWF / 七层PROTBINDFLOWF）
- command_set: ADD FILTER, ADD FILTERIPV6, ADD FLOWFILTER, ADD FLTBINDFLOWF, ADD L7FILTER, ADD PROTBINDFLOWF
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00005, 2-00006, 2-00009, 2-00010, 2-00011, 2-00012, 2-00014, 2-00015, 2-00016, 2-00017, 2-00018, 2-00030, 2-00031, 2-00032, 2-00033, 2-00050, 2-00089, 2-00091

### 1-00001 计费三件套  (复用 20 特性)
- intent: 配置 URR→URRGROUP→PCCPOLICYGRP 三级引用链，建立费率到策略组的绑定
- command_set: ADD PCCPOLICYGRP, ADD URR, ADD URRGROUP
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00006, 2-00009, 2-00010, 2-00011, 2-00012, 2-00013, 2-00016, 2-00030, 2-00031, 2-00034, 2-00048, 2-00050, 2-00051, 2-00052, 2-00083, 2-00091

### 1-00004 收尾  (复用 9 特性)
- intent: 配置缺省费率→（可选）防欺诈URR列表→刷新生效
- command_set: ADD SPECURRGRPLIST, SET REFRESHSRV, SET URRGRPBINDING
- features_using: 2-00001, 2-00002, 2-00003, 2-00004, 2-00006, 2-00009, 2-00010, 2-00011, 2-00030

## 专用(单/少特性,<5)

### 1-00005 ICAP互通数据  (复用 1 特性)
- intent: 配置 UDG 与 ICAP Server 的互通数据（VPN实例→逻辑接口→ICAP Server+本端信息→服务器组→绑定关系），URL过滤基本功能的部署前置子流程
- command_set: ADD ICAPLOCALINFO, ADD ICAPSERVER, ADD ICAPSVRBINDISG, ADD ICAPSVRGRP, ADD INTERFACE, ADD VPNINST
- features_using: 2-00083

### 1-00006 内容过滤策略链  (复用 1 特性)
- intent: 配置 URL 内容过滤策略链（策略→模板→APN绑模板→策略绑模板→分类组→策略绑分类组），URL过滤基本功能核心子流程
- command_set: ADD CFPROFBINDCFT, ADD CFPROFILE, ADD CFTEMPLATE, ADD CONTCATEGBIND, ADD CONTCATEGROUP, SET APNCFTEMPLATE
- features_using: 2-00083

### 1-00007 QoS流行为与流动作配置(B侧)  (复用 1 特性)
- intent: 配置 MQC CB 对的 B 侧——先建流行为(MQCBEHAVIOR)再挂流动作(主场景重定向下一跳 QOSACTRDRNHP;deny/重标记/级联/CAR/URPF/重定向VPN组等可选动作 atom 暂缺)。QoS复杂流分类 md 操作步骤2-3
- command_set: ADD MQCBEHAVIOR, ADD QOSACTRDRNHP
- features_using: 2-00065

### 1-00008 QoS流分类与ACL规则绑定(C侧)  (复用 1 特性)
- intent: 配置 MQC CB 对的 C 侧——先建流分类(MQCCLASSIFIER)再把 ACL 规则组绑定进流分类(QOSRULEACL)。QoS复杂流分类 md 操作步骤4-5
- command_set: ADD MQCCLASSIFIER, ADD QOSRULEACL
- features_using: 2-00065

### 1-00009 QoS流策略组装与接口应用  (复用 1 特性)
- intent: 组装 MQC 流策略并绑定 CB 对(MQCPOLICY+MQCPOLICYNODE),再将流策略应用到接口出入方向(QOSAPPLICATION)。QoS复杂流分类 md 操作步骤6-7,是复杂流分类生效的末步
- command_set: ADD MQCPOLICY, ADD QOSAPPLICATION
- features_using: 2-00065

### 1-00010 DiffServ域与优先级映射  (复用 1 特性)
- intent: 配置 DiffServ 域实例(QOSDIFFERSERV)并设置其上下行优先级映射(SET QOSBA 入口CoS→ToS / SET QOSPHB 出口ToS→CoS)。QoS简单流分类 md 操作步骤1-2(均为可选前置,默认存在 default/5p3d 两 DS 域)
- command_set: ADD QOSDIFFERSERV, SET QOSBA, SET QOSPHB
- features_using: 2-00065

### 1-00011 ACL4规则组与规则  (复用 1 特性)
- intent: 增加 IPv4 ACL 规则组(ACLGROUP)并按匹配需求增加规则(高级 ACLRULEADV4 五元组/基本 ACLRULEBAS4 源IP/以太 ACLRULEETH 源MAC/接口 ACLRULEIF 接口名)。IPFD-012002 ACL4 md 操作步骤1-5
- command_set: ADD ACLGROUP, ADD ACLRULEADV4, ADD ACLRULEBAS4, ADD ACLRULEETH
- features_using: 2-00066

### 1-00012 地址池族（外部地址分配公共子集）  (复用 4 特性)
- intent: 配置外部地址分配的公共地址池链路（地址池→地址段→地址池组→绑定→APN→APN与地址池组映射），作为 GWFD-010104 与 GWFD-010107 共享的可复用步骤
- command_set: ADD APN, ADD POOL, ADD POOLBINDGROUP, ADD POOLGROUP, ADD POOLGRPMAP, ADD SECTION
- features_using: 2-00020, 2-00025, 2-00043, 2-00044

### 1-00013 LoopBack接口族  (复用 2 特性)
- intent: 配置主备UDG的LoopBack接口并绑定VPN实例与IPv4地址，为GRE备份隧道提供源接口（md 步骤1.c-d）
- command_set: ADD IFIPV4ADDRESS, ADD INTERFACE, ADD IPBINDVPN
- features_using: 2-00025, 2-00064

### 1-00014 Tunnel接口族（GRE备份隧道）  (复用 1 特性)
- intent: 配置主备UDG的GRE备份Tunnel接口（接口→GRE隧道→绑VPN→IPv4地址→IPv6使能→IPv6地址），承接LoopBack源接口（md 步骤1.e-h）
- command_set: ADD GRETUNNEL, ADD IFIPV4ADDRESS, ADD IFIPV6ADDRESS, ADD INTERFACE, ADD IPBINDVPN, SET IFIPV6ENABLE
- features_using: 2-00025

### 1-00015 OSPF路由引入族  (复用 1 特性)
- intent: 配置 IPv4 OSPF 动态路由引入族（创建OSPF进程→增加OSPF区域→增加运行OSPF的接口网段→设置OSPF引入路由类型），作为 PGW-U 到对端网元(ePDG/SGW-U等) IP 互通的动态路由子流程
- command_set: ADD OSPF, ADD OSPFAREA, ADD OSPFIMPORTROUTE, ADD OSPFNETWORK
- features_using: 2-00027

### 1-00016 APN级下行数据缓存  (复用 3 特性)
- intent: 配置指定 APN 的 eDRX 下行数据缓存参数（缓存时长 SET APNDLBUFTIME → 长时间缓存 SET APNDLLTBUFFER），APN 级配置优先于全局级
- command_set: SET APNDLBUFTIME, SET APNDLLTBUFFER
- features_using: 2-00059, 2-00075, 2-00082

### 1-00017 全局下行数据缓存  (复用 3 特性)
- intent: 配置 UDG 全局 eDRX 下行数据缓存参数（缓存时长 SET GLBDLBUFTIME → 长时间缓存 SET GLBDLLTBUFFER），整机级缓存，作为 APN 级未配置时的兜底
- command_set: SET GLBDLBUFTIME, SET GLBDLLTBUFFER
- features_using: 2-00059, 2-00075, 2-00082

### 1-00018 路由策略族  (复用 1 特性)
- intent: 配置一条带匹配类型的路由策略（策略→节点→匹配路由类型），作为路由引入/过滤时引用策略名的可复用步骤
- command_set: ADD MATCHROUTETYPE, ADD ROUTEPOLICY, ADD ROUTEPOLICYNODE
- features_using: 2-00041

### 1-00019 OSPFv3路由引入族  (复用 1 特性)
- intent: 启动OSPFv3进程并建立区域后引入外部路由到骨干网（进程→区域→引入路由），为IPv6承载上下文等场景提供动态路由引入的可复用步骤
- command_set: ADD OSPFV3, ADD OSPFV3AREA, ADD OSPFV3IMPORTROUTE
- features_using: 2-00041

### 1-00020 IPv6接口组网族（外联口Ethernet子接口）  (复用 1 特性)
- intent: 配置VNRS_VNFC外联口的IPv6物理组网（主接口up→子接口→绑VPN→VLAN→IPv6使能→IPv6地址→路径MTU），使UDG用IPv6地址与PDN/DN互通
- command_set: ADD ETHSUBIF, ADD IFIPV6ADDRESS, ADD INTERFACE, ADD IPBINDVPN, ADD IPV6PATHMTU, MOD INTERFACE, SET IFIPV6ENABLE
- features_using: 2-00042

### 1-00021 L2TP激活前置（共享相位基线）  (复用 1 特性)
- intent: L2TP VPN 两种激活方式（AAA 下发属性 / 本地配置）共享的相位前置基线——打开 License 开关、创建 VPN 实例、设置 L2TP 缺省参数；两种方式在 SET GLOBALL2TP 之后按 DP 0-00023 分叉（本地方式额外 ADD L2TPGROUP，AAA 方式规划 INITTUNNELNUM/MAXSESSIONNUM），分叉与互斥参数由 feature 2-00045 级 conditional 表达，不进 compound
- command_set: ADD VPNINST, SET GLOBALL2TP, SET LICENSESWITCH
- features_using: 2-00045

### 1-00022 跨VPN外联口自动部署族  (复用 1 特性)
- intent: 配置外联口自动部署模板(AUTOSCALINGSERVICE)→BFD检测二选一(单臂echo AUTOSCALINGBFD / 双向 AUTOSCALINGSRBFD, DP门控)→跨VPN上行静态路由(AUTOSCALINGSRROUTE)，建立跨VPN外联口自动部署+BFD+上行路由的完整子流程
- command_set: ADD AUTOSCALINGBFD, ADD AUTOSCALINGSERVICE, ADD AUTOSCALINGSRBFD, ADD AUTOSCALINGSRROUTE
- features_using: 2-00047

### 1-00023 IPSEC协商族  (复用 1 特性)
- intent: 配置IPsec微服务侧IKE/IPsec协商参数族（VPN实例→ACL保护流→IPsec安全提议→IKE安全提议→IKE对等体→IPsec安全策略[策略+绑提议+绑Peer]），IPsec隧道协商加解密核心子流程。协商结果由 0-00216 IPSECINTFCFG 应用到隧道接口生效
- command_set: ADD ACLGROUPIPSEC, ADD IKEPEER, ADD IKEPROPOSAL, ADD IPSECPOLICY, ADD IPSECPROPOSALIPSEC, ADD L3VPNINSTIPSEC
- features_using: 2-00067

### 1-00024 IPFarm族  (复用 3 特性)
- intent: 配置单个 IP Farm 实例并加入 server 地址池族（ADD IPFARM→ADD IPFARMSERVER），IP Farm 心跳检测核心子流程；按 P-CSCF/Web Proxy 等 server 用途迭代执行（每个 IP Farm 实例一遍）
- command_set: ADD IPFARM, ADD IPFARMSERVER
- features_using: 2-00030, 2-00031, 2-00057

