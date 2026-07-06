# Task 索引 — UDG@20.15.2（assert/ 权威资产）

> 机器索引以 `index.json` 为准（build_index.py 生成，Agent/UI 共用）；本文件为人工概览。

> 资产目录已从 task-assets/ 迁至 assert/（task-assets/ 弃用）。

## 总量
| 层 | 数量 |
|---|---|
| feature | 10 |
| compound | 4 |
| atom | 187 |
| **合计** | **201** |

## feature（10）

| 编号 | logical_name | status | ref |
|---|---|---|---|
| 2-00001 | 内容计费基本功能 | inferred | GWFD-020301 |
| 2-00002 | 在线计费 | inferred | GWFD-020300 |
| 2-00003 | 离线计费 | inferred | GWFD-010171 |
| 2-00004 | 融合计费 | inferred | GWFD-010173 |
| 2-00005 | PCC基本功能 | inferred | GWFD-020351 |
| 2-00006 | TCP重传识别 | inferred | GWFD-020307 |
| 2-00007 | 7层流量统计 | inferred | GWFD-020308 |
| 2-00008 | 终端异常下行流量检测 | inferred | GWFD-020305 |
| 2-00009 | 基于业务时长的计费 | inferred | GWFD-020302 |
| 2-00010 | 基于业务流量的计费 | inferred | GWFD-020303 |

## compound（4）

| 编号 | logical_name | status | ref |
|---|---|---|---|
| 1-00001 | 计费三件套 | inferred |  |
| 1-00002 | 过滤链 | inferred |  |
| 1-00003 | 规则与用户模板绑定 | inferred |  |
| 1-00004 | 收尾 | inferred |  |

## atom（187）

| 编号 | logical_name | status | ref |
|---|---|---|---|
| 0-00001 | 配置URR | inferred | ADD URR |
| 0-00002 | 配置URR组 | inferred | ADD URRGROUP |
| 0-00003 | 配置PCC策略组 | inferred | ADD PCCPOLICYGRP |
| 0-00004 | 配置三四层过滤器-IPv4 | inferred | ADD FILTER |
| 0-00005 | 配置三四层过滤器-IPv6 | inferred | ADD FILTERIPV6 |
| 0-00006 | 配置七层过滤器 | inferred | ADD L7FILTER |
| 0-00007 | 配置流过滤器 | inferred | ADD FLOWFILTER |
| 0-00008 | 绑定三四层过滤条件到流过滤器 | inferred | ADD FLTBINDFLOWF |
| 0-00009 | 绑定七层过滤条件到流过滤器 | inferred | ADD PROTBINDFLOWF |
| 0-00010 | 配置规则 | inferred | ADD RULE |
| 0-00011 | 配置用户模板 | inferred | ADD USERPROFILE |
| 0-00012 | 绑定规则到用户模板 | inferred | ADD RULEBINDING |
| 0-00013 | 配置用户模板URR组绑定 | inferred | SET URRGRPBINDING |
| 0-00014 | 配置防欺诈URR列表 | inferred | ADD SPECURRGRPLIST |
| 0-00015 | 刷新生效 | inferred | SET REFRESHSRV |
| 0-00016 | 设置全局默认配额开关 | inferred | SET UPDEFAULTQUOTA |
| 0-00017 | 设置全局计费参数 | inferred | SET UPGLBCHGPARA |
| 0-00018 | 设置URR上报失败动作 | inferred | SET URRFAILACTION |
| 0-00019 | 设置License开关 | inferred | SET LICENSESWITCH |
| 0-00020 | 配置APN | inferred | ADD APN |
| 0-00021 | 配置APN下异常下行流量检测开关 | inferred | ADD ABNTRAFFICDT |
| 0-00022 | 配置扩展过滤器 | inferred | ADD EXTENDEDFILTER |
| 0-00023 | 配置重定向携带信息 | inferred | ADD REDIRAPPENDINFO |
| 0-00024 | 设置Gy接口一次重定向参数 | inferred | SET GYONESHOT |
| 0-00027 | 加载协议特征库 | inferred | LOD SIGNATUREDB |
| 0-00028 | 配置PCC动作属性 | inferred | ADD PCCACTIONPROP |
| 0-00029 | 配置业务属性 | inferred | ADD SERVICEPROP |
| 0-00030 | 绑定PCC策略组业务属性 | inferred | ADD SRVPBINDPCCPG |
| 0-00031 | 配置ADC参数 | inferred | ADD ADCPARA |
| 0-00032 | 配置分类属性 | inferred | ADD CATEGORYPROP |
| 0-00033 | 配置带宽管理用户组 | inferred | ADD BWMUSERGROUP |
| 0-00034 | 配置带宽管理业务 | inferred | ADD BWMSERVICE |
| 0-00035 | 绑定用户组到APN | inferred | ADD APNBINDBWMUSRG |
| 0-00036 | 配置带宽管理控制器 | inferred | ADD BWMCONTROLLER |
| 0-00037 | 配置带宽管理规则 | inferred | ADD BWMRULE |
| 0-00038 | 配置QoS属性 | inferred | ADD QOSPROP |
| 0-00039 | 配置知名端口 | inferred | ADD WELLKNOWNPORT |
| 0-00040 | 配置SA触发专有承载 | inferred | ADD SADEDICBEARER |
| 0-00041 | 配置VPN实例 | inferred | ADD VPNINST |
| 0-00042 | 配置地址池组 | inferred | ADD POOLGROUP |
| 0-00043 | 配置地址池 | inferred | ADD POOL |
| 0-00044 | 配置地址池IP地址段 | inferred | ADD SECTION |
| 0-00045 | 绑定地址池到地址池组 | inferred | ADD POOLBINDGROUP |
| 0-00046 | 配置APN地址分配属性 | draft | SET APNADDRESSATTR |
| 0-00047 | 配置地址池组与APN映射关系 | inferred | ADD POOLGRPMAP |
| 0-00048 | 启动PDN侧路由探测 | inferred | STR PDNROUTETST |
| 0-00049 | 配置APN的QoS带宽控制属性 | draft | SET APNQOSATTR |
| 0-00050 | 配置APN下用户接入速率 | draft | SET APNACCESSWAL |
| 0-00051 | 配置GTP路径相关属性 | inferred | SET UPGTPPATH |
| 0-00052 | 配置N4接口GTP路径相关属性 | inferred | SET UPN4UPATH |
| 0-00053 | 配置PFCP路径相关属性 | inferred | SET UPPFCPPATH |
| 0-00054 | 配置GTP路径管理IP地址 | inferred | ADD ECHOIPLIST |
| 0-00055 | 配置冗余备份重定向IP | inferred | ADD REDUNDRDTIP |
| 0-00056 | 配置逻辑接口 | inferred | ADD INTERFACE |
| 0-00057 | 配置接口绑定VPN | inferred | ADD IPBINDVPN |
| 0-00058 | 配置接口IPv4地址 | inferred | ADD IFIPV4ADDRESS |
| 0-00059 | 配置GRE隧道 | inferred | ADD GRETUNNEL |
| 0-00060 | 使能接口IPv6并配置MTU | inferred | SET IFIPV6ENABLE |
| 0-00061 | 配置接口IPv6地址 | inferred | ADD IFIPV6ADDRESS |
| 0-00062 | 配置IPv4静态路由 | inferred | ADD SRROUTE |
| 0-00063 | 配置IPv6静态路由 | inferred | ADD SRROUTE6 |
| 0-00064 | 配置静态地址用户路由冗余全局开关 | inferred | SET REDUNDUSER |
| 0-00065 | 配置业务公共参数 | inferred | SET SRVCOMMONPARA |
| 0-00066 | 配置DS域 | inferred | ADD QOSDIFFERSERV |
| 0-00067 | 配置上行BA映射 | inferred | SET QOSBA |
| 0-00068 | 配置QoS接口信任 | inferred | ADD QOSIFTRUST |
| 0-00069 | 配置下行PHB映射 | inferred | SET QOSPHB |
| 0-00070 | 配置QoS CAR功能 | inferred | SET QOSCAR |
| 0-00071 | 配置L3VPN实例 | inferred | ADD L3VPNINST |
| 0-00072 | 配置L3VPN实例地址族 | inferred | ADD VPNINSTAF |
| 0-00073 | 全局激活BFD | inferred | SET BFD |
| 0-00074 | 创建OSPF进程(IPv4) | inferred | ADD OSPF |
| 0-00075 | 创建OSPF区域(IPv4) | inferred | ADD OSPFAREA |
| 0-00076 | 增加OSPF运行接口网段(IPv4) | inferred | ADD OSPFNETWORK |
| 0-00077 | 配置OSPF引入外部路由(IPv4) | inferred | ADD OSPFIMPORTROUTE |
| 0-00078 | 创建OSPFv3进程(IPv6) | inferred | ADD OSPFV3 |
| 0-00079 | 创建OSPFv3区域(IPv6) | inferred | ADD OSPFV3AREA |
| 0-00080 | 配置OSPFv3引入外部路由(IPv6) | inferred | ADD OSPFV3IMPORTROUTE |
| 0-00082 | 创建静态BFD会话(IPv4) | inferred | ADD BFDSESSION |
| 0-00083 | 创建逻辑接口 | inferred | ADD LOGICINF |
| 0-00084 | 设置DDoS防攻击流控阈值 | inferred | SET DDOS |
| 0-00085 | 设置物联网能力上报 | inferred | SET IOTCAPABILITY |
| 0-00086 | 配置IPFarm全局参数 | inferred | SET IPFARMGLOBAL |
| 0-00087 | 配置IPFarm | inferred | ADD IPFARM |
| 0-00088 | 配置IPFarm服务器 | inferred | ADD IPFARMSERVER |
| 0-00089 | 配置错误码 | inferred | ADD ERRORCODE |
| 0-00090 | 配置DNS重写动作 | inferred | ADD DNSOVERWRITING |
| 0-00091 | 配置HTTP智能重定向动作 | inferred | ADD SMARTHTTPREDIR |
| 0-00092 | 加载外置OTT业务规则库 | inferred | LOD EXTERNALDB |
| 0-00093 | 设置OTT业务规则匹配开关 | inferred | SET EXTOTTMATCHSW |
| 0-00106 | 设置带宽管理生效范围 | inferred | SET BANDWIDTHMNG |
| 0-00107 | 设置APN操作系统级带宽管理开关 | inferred | SET APNOSLELBWMSW |
| 0-00108 | 配置带宽管理控制器业务等级策略 | inferred | ADD BCSRVLEVELPLY |
| 0-00109 | 设置FPI差异化控制功能 | inferred | SET FPIFUNC |
| 0-00110 | 设置APN上报属性 | inferred | SET APNREPORTATTR |
| 0-00111 | 配置路由策略 | inferred | ADD ROUTEPOLICY |
| 0-00112 | 配置路由策略节点 | inferred | ADD ROUTEPOLICYNODE |
| 0-00113 | 配置匹配路由类型 | inferred | ADD MATCHROUTETYPE |
| 0-00114 | 修改接口管理状态 | inferred | MOD INTERFACE |
| 0-00115 | 配置以太网子接口VLAN | inferred | ADD ETHSUBIF |
| 0-00116 | 配置IPv6路径MTU | inferred | ADD IPV6PATHMTU |
| 0-00117 | 配置OSPFv3接口(IPv6) | inferred | ADD OSPFV3INTERFACE |
| 0-00131 | 设置L2TP缺省配置 | inferred | SET GLOBALL2TP |
| 0-00132 | 设置APN的L2TP属性 | inferred | SET APNL2TPATTR |
| 0-00133 | 创建L2TP组(本地配置方式专属) | inferred | ADD L2TPGROUP |
| 0-00134 | 绑定APN到L2TP源端接口(AAA下发方式专属) | inferred | ADD L2TPRDSCLIENT |
| 0-00135 | 绑定L2TP组到源端接口(本地配置方式专属) | inferred | ADD L2TPCLIENTIP |
| 0-00137 | 关闭快速流表软参(L2TP前置) | inferred | SET SOFTPARAOFBIT |
| 0-00138 | 设置PPP协商参数(L2TP) | inferred | SET PPPCFG |
| 0-00139 | 设置APN的PPP鉴权(L2TP) | inferred | SET APNPPPACCESS |
| 0-00140 | 设置L2TP N4加密密钥 | inferred | SET L2TPN4KEY |
| 0-00141 | 配置外联口自动部署服务模板 | inferred | ADD AUTOSCALINGSERVICE |
| 0-00142 | 配置跨VPN上行静态路由(路由交叉) | inferred | ADD AUTOSCALINGSRROUTE |
| 0-00143 | 配置BFD单臂echo会话模板(路由交叉) | draft | ADD AUTOSCALINGBFD |
| 0-00144 | 配置静态路由双向BFD自动化模板(路由交叉) | inferred | ADD AUTOSCALINGSRBFD |
| 0-00145 | 修改L3VPN实例地址族(路由交叉) | inferred | MOD VPNINSTAF |
| 0-00146 | 增加VPN Target(路由交叉RT发布/引入) | inferred | ADD VPNTARGET |
| 0-00147 | 使能全局BGP并配置VRF实例与路由引入(路由交叉) | inferred | SET BGP |
| 0-00149 | 设置APN级HTTP2.0协议回落开关 | inferred | SET APNHTTP2DGRD |
| 0-00150 | 设置rule级HTTP2.0协议回落开关 | inferred | MOD PCCPOLICYGRP |
| 0-00151 | 配置Host | inferred | ADD HOST |
| 0-00152 | 加载协议解析库 | inferred | LOD PARSERDB |
| 0-00153 | 配置用户关联识别 | inferred | ADD USRRELATEIDEN |
| 0-00154 | 设置SA业务公共参数 | inferred | SET SACOMMONPARA |
| 0-00155 | 添加APN的IMS信令分类器 | inferred | ADD APNIMSSIGFLTR |
| 0-00156 | 设置APN的IMS属性 | inferred | SET APNIMSATTR |
| 0-00171 | 设置全局业务快速恢复配置 | inferred | SET FASTRECOVERY |
| 0-00172 | 设置全局下行数据缓存时长 | inferred | SET GLBDLBUFTIME |
| 0-00173 | 设置全局下行数据长时间缓存个数 | inferred | SET GLBDLLTBUFFER |
| 0-00174 | 设置基于APN的下行数据缓存时长 | inferred | SET APNDLBUFTIME |
| 0-00175 | 设置基于APN的下行数据长时间缓存配置 | inferred | SET APNDLLTBUFFER |
| 0-00177 | 设置APN Non-IP配置 | inferred | SET APNNONIPFUNC |
| 0-00178 | 修改GRE隧道增强配置 | inferred | MOD GRETUNNEL |
| 0-00197 | 增加ACL规则组(VNRS) | inferred | ADD ACLGROUP |
| 0-00198 | 增加高级ACL规则(VNRS IPv4) | inferred | ADD ACLRULEADV4 |
| 0-00199 | 增加流行为(MQC) | inferred | ADD MQCBEHAVIOR |
| 0-00200 | 配置QoS重定向下一跳动作 | inferred | ADD QOSACTRDRNHP |
| 0-00201 | 增加流分类(MQC) | inferred | ADD MQCCLASSIFIER |
| 0-00202 | 流分类绑定ACL规则 | inferred | ADD QOSRULEACL |
| 0-00203 | 增加流策略并绑定CB对(MQCPOLICY+NODE) | inferred | ADD MQCPOLICY |
| 0-00204 | 接口应用流策略 | inferred | ADD QOSAPPLICATION |
| 0-00207 | 增加基本ACL规则(VNRS IPv4) | inferred | ADD ACLRULEBAS4 |
| 0-00208 | 增加以太/接口ACL规则(VNRS) | inferred | ADD ACLRULEETH |
| 0-00209 | 增加IPv6 ACL规则组与规则(ACL6) | inferred | ADD ACLGROUP6 |
| 0-00210 | 创建IPsec微服务VPN与隧道接口(VNRS+IPSEC双配) | inferred | ADD L3VPNINSTIPSEC |
| 0-00211 | 定义IPsec保护数据流(IPsec ACL) | inferred | ADD ACLGROUPIPSEC |
| 0-00212 | 配置IPsec安全提议 | inferred | ADD IPSECPROPOSALIPSEC |
| 0-00213 | 配置IKE安全提议 | inferred | ADD IKEPROPOSAL |
| 0-00214 | 配置IKE对等体 | inferred | ADD IKEPEER |
| 0-00215 | 配置并组装IPsec安全策略(策略+绑提议+绑IKE Peer) | inferred | ADD IPSECPOLICY |
| 0-00216 | 创建VNRS侧IPsec隧道接口并应用安全策略(VNRS+IPSEC双配) | inferred | ADD IPSECINTFCFG |
| 0-00217 | 设置IKE全局配置(DPD/NAT保活) | inferred | SET IKEGLOBALCONFIG |
| 0-00218 | 配置PFCP负荷上报 | inferred | SET PFCPLOADRPT |
| 0-00219 | 配置F-TEID分配能力(CU Full Mesh) | inferred | SET CPTEIDUALLOC |
| 0-00220 | 配置会话核查功能 | inferred | SET SESSCHKFUNC |
| 0-00222 | 配置APN单用户五元组上限 | inferred | SET APNFLOWMAXNUM |
| 0-00224 | 创建TWAMP VPN实例 | inferred | ADD TWAMPVPNINST |
| 0-00225 | 创建TWAMP逻辑接口 | inferred | ADD TWAMPLOGICINF |
| 0-00226 | 配置TWAMP响应端(Full模式) | inferred | ADD TWAMPRESPONDER |
| 0-00227 | 配置TWAMP客户端(Light模式) | inferred | ADD TWAMPCLIENT |
| 0-00228 | 配置TWAMP发送端(Light模式) | inferred | ADD TWAMPSENDER |
| 0-00229 | 配置TCP保活参数(Full模式) | inferred | SET TCPKEEPALIVECFG |
| 0-00230 | 配置链路丢包告警阈值(Light模式) | inferred | SET LINKALMCFG |
| 0-00231 | 配置IPSQM静态整形带宽 | inferred | ADD IPSQMSHAPING |
| 0-00232 | 配置IPSQM整形队列深度 | inferred | SET IPSQMQDEPTH |
| 0-00233 | 配置IPSQM调整参数 | inferred | SET IPSQMADJUST |
| 0-00234 | 增加IPSQM VIP用户列表 | inferred | ADD IPSQMVIPLIST |
| 0-00248 | 配置NTP服务器 | inferred | ADD NTPSVR |
| 0-00249 | 设置用户面接口模式(入不转板总开关) | inferred | SET DATAPLANEINFMODE |
| 0-00250 | 设置地址分配规则(入不转板) | inferred | SET IPALLOCRULE |
| 0-00251 | 设置APN内容过滤开关 | inferred | SET APNCFFUNC |
| 0-00252 | 增加内容过滤策略 | inferred | ADD CFPROFILE |
| 0-00253 | 增加内容过滤模板 | inferred | ADD CFTEMPLATE |
| 0-00254 | 设置APN内容过滤模板 | inferred | SET APNCFTEMPLATE |
| 0-00255 | 增加内容过滤策略绑定关系 | inferred | ADD CFPROFBINDCFT |
| 0-00256 | 增加内容分类组 | inferred | ADD CONTCATEGROUP |
| 0-00257 | 增加内容分类组绑定关系 | inferred | ADD CONTCATEGBIND |
| 0-00258 | 设置内容过滤缓存参数 | inferred | SET CFCACHEPARA |
| 0-00259 | 增加ICAP服务器 | inferred | ADD ICAPSERVER |
| 0-00260 | 增加ICAP服务器组 | inferred | ADD ICAPSVRGRP |
| 0-00261 | 增加ICAP服务器绑定关系 | inferred | ADD ICAPSVRBINDISG |
| 0-00262 | 增加ICAP本端信息 | inferred | ADD ICAPLOCALINFO |
| 0-00279 | 设置大流优化参数 | inferred | SET FLOWLETPARA |
| 0-00280 | 设置网元形态 | inferred | SET NETYPE |
| 0-00281 | 配置SA指纹识别 | inferred | ADD FINGERIDENT |
| 0-00282 | 设置IMS Bypass功能参数 | inferred | SET IMSBYPASS |
| 0-00283 | 设置RTSDNN参数 | inferred | SET RTSDNNPARA |
