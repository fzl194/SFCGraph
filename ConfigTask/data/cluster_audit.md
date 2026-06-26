# 簇审查清单（二次修复后 134 簇）

## cluster-002 (22人) [其他]
- 核心命令: ['ADD FILTER', 'ADD L7FILTER', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF', 'ADD PROTBINDFLOWF']
  - GWFD-020301#2a63#002: 配置过滤条件与流过滤器 | GWFD-020 | 其他
  - GWFD-020358#bd63#002: 配置三四层过滤条件 | GWFD-020 | 其他
  - GWFD-010173#405a#002: 配置过滤条件 | GWFD-010 | 其他
  - ... (19 more)
## cluster-001 (28人) [计费/其他/访问限制/带宽控制] ⚡跨域
- 核心命令: ['ADD USERPROFILE', 'ADD RULEBINDING']
  - GWFD-020301#2a63#004: 配置User Profile与规则绑定 | GWFD-020 | 其他
  - GWFD-110203#3c81#006: 配置业务策略组合 | GWFD-110 | 其他
  - GWFD-110251#e541#004: 配置内容计费规则绑定用户模板 | GWFD-110 | 计费
  - ... (25 more)
## cluster-003 (19人) [计费]
- 核心命令: ['ADD URR', 'ADD URRGROUP', 'ADD PCCPOLICYGRP']
  - GWFD-020301#2a63#001: 配置计费URR组与PCC策略组 | GWFD-020 | 计费
  - GWFD-110201#9d96#001: 配置License及计费三件套 | GWFD-110 | 计费
  - GWFD-110203#3c81#001: 配置License及计费URR组 | GWFD-110 | 计费
  - ... (16 more)
## cluster-004 (16人) [计费/其他] ⚡跨域
- 核心命令: ['ADD RULE']
  - GWFD-020301#2a63#003: 配置计费规则 | GWFD-020 | 计费
  - GWFD-110251#e541#003: 配置内容计费使用的规则 | GWFD-110 | 计费
  - GWFD-110252#b268#003: 配置内容计费使用的规则 | GWFD-110 | 计费
  - ... (13 more)
## cluster-006 (11人) [带宽控制]
- 核心命令: ['ADD BWMSERVICE', 'ADD BWMCONTROLLER', 'ADD BWMRULE', 'ADD BWMUSERGROUP', 'ADD BWMRULE']
  - GWFD-110311#2ac2#002: 配置BWM业务 | GWFD-110 | 带宽控制
  - GWFD-110311#40a2#002: 配置BWM业务 | GWFD-110 | 带宽控制
  - GWFD-110301#7967#002: 配置BWM业务 | GWFD-110 | 带宽控制
  - ... (8 more)
## cluster-007 (10人) [安全]
- 核心命令: ['ADD ACLGROUPIPSEC', 'ADD ACLRULEADV4IPSEC']
  - IPFD-015004#595f#002: 定义IPsec保护数据流 | IPFD-015 | 安全
  - IPFD-015004#349a#002: 定义IPsec保护数据流 | IPFD-015 | 安全
  - IPFD-015004#7a62#003: 定义数据流并配置IPsec提议 | IPFD-015 | 安全
  - ... (7 more)
## cluster-011 (6人) [其他/安全] ⚡跨域
- 核心命令: ['ADD IKEPROPOSAL', 'ADD IKEPEER']
  - IPFD-015004#595f#003: 配置IPsec提议与IKE对等体 | IPFD-015 | 安全
  - IPFD-015004#349a#003: 配置IPsec提议与IKE对等体 | IPFD-015 | 安全
  - IPFD-015004#7a62#004: 配置IKE提议与对等体 | IPFD-015 | 其他
  - ... (3 more)
## cluster-005 (16人) [安全]
- 核心命令: ['ADD IPSECPOLICY', 'ADD PROPATTACHIPSECPROPOSAL', 'ADD ATTACHIKEPEER', 'ADD IPSECINTFCFGIPSEC', 'SET IKEGLOBALCONFIG']
  - IPFD-015004#595f#004: 配置并应用IPsec安全策略 | IPFD-015 | 安全
  - IPFD-015004#349a#004: 配置并应用IPsec安全策略 | IPFD-015 | 安全
  - IPFD-015004#7a62#005: 配置并应用IPsec策略 | IPFD-015 | 安全
  - ... (13 more)
## cluster-008 (8人) [地址分配]
- 核心命令: ['ADD VPNINST', 'ADD APN', 'SET APNADDRESSATTR']
  - GWFD-020406#0aab#001: 配置License及APN/DNN地址分配属性 | GWFD-020 | 地址分配
  - GWFD-020406#94ae#001: 配置License及APN/DNN地址分配属性 | GWFD-020 | 地址分配
  - GWFD-020406#1e93#001: 配置License及APN/DNN地址分配属性 | GWFD-020 | 地址分配
  - ... (5 more)
## cluster-009 (8人) [安全]
- 核心命令: ['ADD L3VPNINSTIPSEC', 'ADD VPNINSTAFIPSEC', 'ADD INTERFACEIPSEC', 'ADD IPBINDVPNIPSEC', 'ADD IFIPV4ADDRESSIPSEC']
  - IPFD-015004#7a62#002: 创建IPsec微服务VPN | IPFD-015 | 安全
  - IPFD-015004#ba3f#002: 创建IPsec微服务VPN | IPFD-015 | 安全
  - IPFD-015004#2b92#002: 创建IPsec微服务VPN | IPFD-015 | 安全
  - ... (5 more)
## cluster-010 (8人) [其他/安全] ⚡跨域
- 核心命令: ['ADD L3VPNINST', 'ADD VPNINSTAF', 'ADD IPBINDVPN', 'ADD IFIPV4ADDRESS', 'ADD INTERFACE']
  - IPFD-015004#ba3f#001: 创建VNRS VPN及隧道接口 | IPFD-015 | 其他
  - IPFD-015004#2b92#001: 创建VNRS VPN及隧道接口 | IPFD-015 | 其他
  - IPFD-015004#a745#001: 创建VNRS VPN及隧道接口 | IPFD-015 | 其他
  - ... (5 more)
## cluster-012 (6人) [接入控制]
- 核心命令: ['ADD APN']
  - GWFD-110646#eb27#001: 打开本特性的License配置开关 | GWFD-110 | 接入控制
  - GWFD-110647#1630#001: 打开本特性的License控制开关 | GWFD-110 | 接入控制
  - GWFD-110611#f4ef#001: 打开本特性的License配置开关 | GWFD-110 | 接入控制
  - ... (3 more)
## cluster-013 (6人) [其他/访问限制] ⚡跨域
- 核心命令: ['ADD RULE', 'ADD FLOWFILTERGRP']
  - GWFD-110471#55f2#004: 配置业务规则 | GWFD-110 | 其他
  - GWFD-020359#f839#003: 配置IM类业务规则 | GWFD-020 | 其他
  - GWFD-110281#77b6#004: 配置用户Portal业务使用的规则 | GWFD-110 | 访问限制
  - ... (3 more)
## cluster-014 (6人) [地址分配]
- 核心命令: ['ADD POOL', 'ADD SECTION', 'ADD POOLGROUP', 'ADD POOLBINDGROUP', 'ADD CONFLICTIP']
  - GWFD-010105#5e43#002: 配置地址池绑定到地址池组 | GWFD-010 | 地址分配
  - GWFD-010105#434e#002: 配置地址池绑定到地址池组 | GWFD-010 | 地址分配
  - GWFD-010105#8fbf#002: 配置地址池绑定到地址池组 | GWFD-010 | 地址分配
  - ... (3 more)
## cluster-016 (5人) [计费]
- 核心命令: ['SET URRGRPBINDING', 'ADD SPECURRGRPLIST']
  - GWFD-020301#2a63#005: 配置缺省费率、防欺诈与生效 | GWFD-020 | 计费
  - GWFD-010173#405a#006: 配置缺省费率 | GWFD-010 | 计费
  - GWFD-020302#2707#006: 配置缺省URR组 | GWFD-020 | 计费
  - ... (2 more)
## cluster-017 (4人) [其他/访问限制] ⚡跨域
- 核心命令: ['SET IPFARMGLOBAL']
  - GWFD-110281#0d50#001: 配置整机的IPFarm心跳检测功能的相关参数 | GWFD-110 | 其他
  - GWFD-110281#a6a7#001: 配置整机的针对IPFARM配置的重定向Server的负荷分担 | GWFD-110 | 访问限制
  - GWFD-110282#3f85#001: 配置整机的IPFarm心跳检测功能的相关参数 | GWFD-110 | 其他
  - ... (1 more)
## cluster-018 (4人) [其他/安全] ⚡跨域
- 核心命令: ['ADD L3VPNINST', 'ADD VPNINSTAF', 'ADD IPBINDVPN', 'SET IFIPV6ENABLE', 'ADD IFIPV6ADDRESS']
  - IPFD-015004#fbd6#001: 创建VNRS VPN及IPv6隧道接口 | IPFD-015 | 其他
  - IPFD-015004#0b85#001: 创建VNRS VPN及IPv6隧道接口 | IPFD-015 | 其他
  - GWFD-020402#d57a#001: 配置License、VPN实例及外联口IPv6 | GWFD-020 | 其他
  - ... (1 more)
## cluster-019 (4人) [其他]
- 核心命令: ['ADD IKEPEER']
  - IPFD-015004#a85c#005: 配置IKE对等体 | IPFD-015 | 其他
  - IPFD-015004#75c5#005: 配置IKE对等体 | IPFD-015 | 其他
  - IPFD-015004#2f2d#005: 配置IKE对等体 | IPFD-015 | 其他
  - ... (1 more)
## cluster-021 (3人) [接入控制]
- 核心命令: ['ADD APN', 'SET APNDLBUFTIME', 'SET APNDLLTBUFFER', 'SET GLBDLBUFTIME', 'SET GLBDLLTBUFFER']
  - GWFD-110601#376f#001: 配置NB-IoT eDRX模式 | GWFD-110 | 接入控制
  - GWFD-110641#4380#002: 配置eDRX模式所使用的APN | GWFD-110 | 接入控制
  - GWFD-110661#a539#002: 可选eDRX缓存参数 | GWFD-110 | 接入控制
## cluster-022 (3人) [其他]
- 核心命令: ['SET IPALLOCBYSMFGLBSW', 'SET IPALLOCBYSMFSW', 'ADD OSPFV3', 'ADD OSPFV3AREA', 'ADD OSPFV3INTERFACE']
  - GWFD-020406#94ae#003: 配置基于SMF分配开关及OSPFv3路由 | GWFD-020 | 其他
  - GWFD-020406#1e93#003: 配置基于SMF分配开关及OSPFv3路由 | GWFD-020 | 其他
  - GWFD-020406#0aab#003: 配置手机下行OSPFv3路由 | GWFD-020 | 其他
## cluster-023 (3人) [安全]
- 核心命令: ['ADD IPSECPOLICY6', 'ADD PROPATTACHIPSECPROPOSAL', 'ADD ATTACHIKEPEER', 'ADD IPSECINTFCFGIPSEC']
  - IPFD-015004#cc5d#004: 配置并应用IPv6 IPsec安全策略 | IPFD-015 | 安全
  - IPFD-015004#fbd6#005: 配置并应用IPv6 IPsec策略 | IPFD-015 | 安全
  - IPFD-015004#0b85#007: 配置并应用IPv6 IPsec策略 | IPFD-015 | 安全
## cluster-024 (3人) [安全]
- 核心命令: ['ADD ACLGROUP6IPSEC', 'ADD ACLRULEADV6IPSEC']
  - IPFD-015004#cc5d#002: 定义IPv6 IPsec保护数据流 | IPFD-015 | 安全
  - IPFD-015004#fbd6#003: 定义IPv6数据流并配置IPsec提议 | IPFD-015 | 安全
  - IPFD-015004#0b85#003: 定义IPv6数据流并打开国密开关 | IPFD-015 | 安全
## cluster-025 (2人) [访问限制/其他] ⚡跨域
- 核心命令: ['SET SRVCOMMONPARA']
  - GWFD-110281#5baf#001: 基于全局配置HTTP协议的GET请求回应的重定向响应码 | GWFD-110 | 访问限制
  - GWFD-110202#557a#001: 配置License及全局回落开关 | GWFD-110 | 其他
## cluster-026 (2人) [其他]
- 核心命令: ['RMV IPFARMSERVER', 'ADD IPFARMSERVER']
  - GWFD-110281#a8e9#001: 删除原来的类型为IPV4的ServerIP | GWFD-110 | 其他
  - GWFD-110282#bb60#001: 删除原来的类型为IPv4的ServerIP | GWFD-110 | 其他
## cluster-027 (2人) [其他]
- 核心命令: ['MOD IPFARM']
  - GWFD-110281#2bc7#001: 修改IPFARM对应的VIRTUALIP | GWFD-110 | 其他
  - GWFD-110282#fe67#001: 修改IPFARM对应的VIRTUALIP | GWFD-110 | 其他
## cluster-028 (2人) [其他]
- 核心命令: ['ADD LOGICINF', 'MOD IPFARM']
  - GWFD-110281#23a6#001: 配置IPFarm的心跳检测接口 | GWFD-110 | 其他
  - GWFD-110282#6154#001: 配置IPFarm的心跳检测接口 | GWFD-110 | 其他
## cluster-029 (2人) [安全]
- 核心命令: ['SET PKICRLCHECK', 'ADD CERTSCENE', 'DSP PKICERTLIST']
  - IPFD-015004#8f57#001: 上传并验证IPsec证书 | IPFD-015 | 安全
  - IPFD-015004#ccf7#001: 上传并验证国密IPsec证书 | IPFD-015 | 安全
## cluster-030 (2人) [其他]
- 核心命令: ['ADD SRROUTE']
  - IPFD-015004#595f#005: 配置静态路由引流 | IPFD-015 | 其他
  - IPFD-015004#a85c#008: 配置静态路由引流 | IPFD-015 | 其他
## cluster-031 (2人) [安全]
- 核心命令: ['ADD L3VPNINSTIPSEC', 'ADD VPNINSTAFIPSEC', 'ADD INTERFACEIPSEC', 'ADD IPBINDVPNIPSEC', 'SET IFIPV6ENABLEIPSEC']
  - IPFD-015004#fbd6#002: 创建IPsec微服务VPN及IPv6接口 | IPFD-015 | 安全
  - IPFD-015004#0b85#002: 创建IPsec微服务VPN及IPv6接口 | IPFD-015 | 安全
## cluster-032 (2人) [地址分配]
- 核心命令: ['ADD VPNINST', 'ADD APN', 'SET APNADDRESSATTR', 'ADD POOL', 'ADD SECTION']
  - GWFD-020421#4d32#002: 基于APN/DNN实例使能地址分配属性 | GWFD-020 | 地址分配
  - GWFD-020421#0a64#002: 基于APN/DNN实例使能地址分配属性 | GWFD-020 | 地址分配
## cluster-033 (2人) [计费]
- 核心命令: ['ADD URR', 'ADD QOSPROP', 'ADD PCCPOLICYGRP']
  - GWFD-110302#d8ca#003: 配置QoS属性 | GWFD-110 | 计费
  - GWFD-020358#a228#003: 配置QoS属性 | GWFD-020 | 计费
## cluster-034 (2人) [其他]
- 核心命令: ['ADD PCCACTIONPROP', 'ADD PCCPOLICYGRP']
  - GWFD-110331#8942#003: 配置PCC动作属性 | GWFD-110 | 其他
  - GWFD-112001#91ab#002: 配置报文的阻塞动作 | GWFD-112 | 其他
## cluster-035 (2人) [其他]
- 核心命令: ['DSP CELLSTAT']
  - GWFD-110921#025e#001: 检查IPAPM是否已安装，若未安装，请完成IPAPM安装，参 | GWFD-110 | 其他
  - GWFD-110921#c0ef#001: 检查IPAPM是否已安装，若未安装，请完成IPAPM安装，参 | GWFD-110 | 其他
## cluster-036 (2人) [其他]
- 核心命令: ['ADD RULE', 'ADD FLOWFILTERGRP', 'ADD USERPROFILE', 'ADD RULEBINDING']
  - GWFD-020352#ae00#003: 配置阻塞规则与用户策略绑定 | GWFD-020 | 其他
  - GWFD-020358#a228#004: 配置业务规则 | GWFD-020 | 其他
## cluster-037 (2人) [带宽控制/接入控制] ⚡跨域
- 核心命令: ['ADD APN', 'SET APNQOSATTR']
  - GWFD-010151#741a#001: 配置APN接入控制 | GWFD-010 | 接入控制
  - GWFD-020381#dcfa#001: 配置License及带宽控制使能 | GWFD-020 | 带宽控制
## cluster-038 (2人) [其他]
- 核心命令: ['SET UPGTPPATH', 'SET UPN4UPATH']
  - GWFD-010102#f205#001: 设置 UDG 非N4/Sxb接口的GTP请求消息的重发时间间 | GWFD-010 | 其他
  - GWFD-010102#0047#001: 配置非N4接口的GTP路径管理参数 | GWFD-010 | 其他
## cluster-039 (2人) [地址分配]
- 核心命令: ['ADD POOL', 'ADD SECTION', 'ADD POOLGROUP', 'ADD POOLBINDGROUP', 'ADD CONFLICTIPV6']
  - GWFD-020406#0aab#002: 配置地址池组、映射及分配规则 | GWFD-020 | 地址分配
  - GWFD-020406#1e93#002: 配置地址池组、SMF映射及分配规则 | GWFD-020 | 地址分配
## cluster-040 (2人) [安全]
- 核心命令: ['ADD L3VPNINST', 'ADD VPNINSTAF', 'ADD INTERFACE', 'ADD IPBINDVPN', 'ADD IFIPV4ADDRESS']
  - IPFD-015004#595f#001: 创建VNRS与IPsec微服务VPN及隧道接口 | IPFD-015 | 安全
  - IPFD-015004#349a#001: 创建VPN及IPsec隧道接口及引流路由 | IPFD-015 | 安全
## cluster-041 (2人) [其他/安全] ⚡跨域
- 核心命令: ['ADD IPSECPROPOSALIPSEC', 'ADD IKEPROPOSAL', 'ADD IKEPEER6', 'ADD IKEPEER6']
  - IPFD-015004#cc5d#003: 配置IPsec提议与IKE对等体 | IPFD-015 | 安全
  - IPFD-015004#fbd6#004: 配置IKE提议与对等体 | IPFD-015 | 其他
## cluster-042 (2人) [其他]
- 核心命令: ['ADD L3VPNINST', 'ADD VPNINSTAF', 'SET BFD', 'ADD SRROUTE', 'ADD VPNINST']
  - GWFD-010155#a29c#001: 参考初始配置中 **配置静态路由+BFD组网（IPv4）** | GWFD-010 | 其他
  - GWFD-010155#823a#001: 参考初始配置中 **配置静态路由+BFD组网（IPv4）** | GWFD-010 | 其他
## cluster-043 (2人) [其他/访问限制] ⚡跨域
- 核心命令: ['LOD SIGNATUREDB', 'ADD FILTER', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF', 'ADD EXTENDEDFILTER']
  - GWFD-110283#bdc2#002: **可选：**解析七层协议时，需要加载协议特征库文件 | GWFD-110 | 其他
  - GWFD-110284#7287#002: 配置HTTP智能重定向业务使用的三四层过滤条件 | GWFD-110 | 访问限制
## cluster-044 (2人) [接入控制]
- 核心命令: ['ADD VPNINST', 'SET GLOBALL2TP', 'SET APNL2TPATTR', 'SET SOFTPARAOFBIT', 'ADD LOGICINF']
  - GWFD-020412#d714#002: 配置VPN实例 | GWFD-020 | 接入控制
  - GWFD-020412#2a72#002: 配置VPN实例 | GWFD-020 | 接入控制
## cluster-046 (1人) [其他]
- 核心命令: ['SET FPIFUNC', 'ADD FILTER', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF']
  - GWFD-110331#8942#002: 配置FPI使能开关，选择资源优化方法 | GWFD-110 | 其他
## cluster-047 (1人) [其他]
- 核心命令: ['ADD PCCACTIONPROP', 'ADD PCCPOLICYGRP', 'ADD SERVICEPROP', 'ADD SRVPBINDPCCPG']
  - GWFD-020352#ae00#002: 配置PCC动作策略与策略组 | GWFD-020 | 其他
## cluster-048 (1人) [接入控制]
- 核心命令: ['ADD APNIMSSIGFLTR', 'SET APNIMSATTR']
  - GWFD-020251#a69f#001: 配置VoLTE IMS业务 | GWFD-020 | 接入控制
## cluster-049 (1人) [接入控制]
- 核心命令: ['SET APNUEMUTACC', 'ADD UEMUTACCWLIST', 'ADD UEMUTWLISTBIND']
  - UNK#d3f4#001: APN下配置终端互访控制 |  | 接入控制
## cluster-050 (1人) [地址分配]
- 核心命令: ['ADD APN', 'ADD POOLGROUP', 'ADD POOL', 'ADD SECTION', 'ADD POOLBINDGROUP']
  - GWFD-020403#5d74#001: 打开本特性的License配置开关 | GWFD-020 | 地址分配
## cluster-051 (1人) [其他]
- 核心命令: ['ADD SQOSVPNGROUP', 'ADD SQOSVPNGROUPMEM']
  - IPFD-012000#d4fa#001: 增加VPN组 | IPFD-012 | 其他
## cluster-052 (1人) [其他]
- 核心命令: ['RMV SQOSVPNGROUP', 'RMV SQOSVPNGROUPMEM']
  - IPFD-012000#dd87#001: 删除已经创建的VPN组 | IPFD-012 | 其他
## cluster-053 (1人) [其他]
- 核心命令: ['RMV DSCPMAP']
  - IPFD-012000#655c#001: 删除对应的DSCPMAP | IPFD-012 | 其他
## cluster-054 (1人) [其他]
- 核心命令: ['ADD DSCPMAP']
  - IPFD-012000#2c11#001: 配置DSCP到VLAN优先级的映射 | IPFD-012 | 其他
## cluster-055 (1人) [安全]
- 核心命令: ['RMV ACLRULEADV6', 'RMV ACLGROUP6']
  - IPFD-012000#3fc9#001: 删除ACL6规则 | IPFD-012 | 安全
## cluster-056 (1人) [安全]
- 核心命令: ['ADD ACLGROUP6', 'ADD ACLRULEBAS6', 'ADD ACLRULEADV6']
  - IPFD-012000#3199#001: 增加ACL6规则组 | IPFD-012 | 安全
## cluster-057 (1人) [安全]
- 核心命令: ['LST ACLGROUP6', 'DSP ACLRULEADV6']
  - IPFD-012000#5aac#001: 查询ACL6规则组信息 | IPFD-012 | 安全
## cluster-058 (1人) [安全]
- 核心命令: ['RMV GRETUNNEL']
  - IPFD-015000#c732#001: 删除GRE隧道 | IPFD-015 | 安全
## cluster-059 (1人) [访问限制]
- 核心命令: ['SET COMBASEHEALTH']
  - UNK#f7c6#012: 已经登录OM Portal，或者 已登录U2020 ，或者登 |  | 访问限制
## cluster-060 (1人) [其他]
- 核心命令: ['ADD ABNTRAFFICDT']
  - GWFD-020305#6b04#001: 打开本特性的License配置开关 | GWFD-020 | 其他
## cluster-061 (1人) [其他]
- 核心命令: ['SET PFCPLOADRPT']
  - GWFD-020154#2d1c#001: 打开本特性的License配置开关 | GWFD-020 | 其他
## cluster-062 (1人) [其他]
- 核心命令: ['SET CPTEIDUALLOC']
  - GWFD-020161#9ecc#001: 打开本特性的License配置开关 | GWFD-020 | 其他
## cluster-063 (1人) [其他]
- 核心命令: ['SET SESSCHKFUNC']
  - GWFD-020162#a1ff#001: 设置会话核查配置 | GWFD-020 | 其他
## cluster-064 (1人) [其他]
- 核心命令: ['SET UPGTPPATH', 'ADD ECHOIPLIST']
  - GWFD-010102#96a4#001: 开启GTP路径管理的黑白名单开关，配置GTP路径管理名单属性 | GWFD-010 | 其他
## cluster-065 (1人) [其他]
- 核心命令: ['DSP PDNTSTRESULT']
  - GWFD-010108#0fed#001: 启动PDN/DN侧路由探测功能 | GWFD-010 | 其他
## cluster-066 (1人) [安全]
- 核心命令: ['SET DDOS', 'ADD USERPROFILE']
  - GWFD-010253#3c56#001: 设置DDoS攻击防护使用的流控阈值 | GWFD-010 | 安全
## cluster-067 (1人) [其他]
- 核心命令: ['SET SSUAGINGCFG']
  - GWFD-111283#12ca#001: 打开本特性的License配置开关 | GWFD-111 | 其他
## cluster-068 (1人) [接入控制]
- 核心命令: ['SET APNREPORTATTR']
  - GWFD-110332#2728#001: 打开本特性的License配置开关 | GWFD-110 | 接入控制
## cluster-069 (1人) [其他]
- 核心命令: ['SET FLOWLETPARA']
  - GWFD-112002#5a24#001: 打开本特性的License配置开关： | GWFD-112 | 其他
## cluster-070 (1人) [其他]
- 核心命令: ['SET IOTCAPABILITY']
  - GWFD-010296#7150#001: 设置NB-IoT终端标准接入功能 | GWFD-010 | 其他
## cluster-071 (1人) [其他]
- 核心命令: ['ADD NTPSVR']
  - NPFD-010000#660c#001: 配置NTP服务器 | NPFD-010 | 其他
## cluster-072 (1人) [计费]
- 核心命令: ['SET URRGRPBINDING']
  - GWFD-020307#b379#001: 打开本特性的License配置开关 | GWFD-020 | 计费
## cluster-073 (1人) [其他]
- 核心命令: ['SET IPFARMGLOBAL', 'ADD VPNINST', 'ADD LOGICINF', 'ADD IPFARM', 'ADD IPFARMSERVER']
  - GWFD-020253#ccf6#001: 打开本特性的License配置开关 | GWFD-020 | 其他
## cluster-074 (1人) [语音]
- 核心命令: ['SET FASTRECOVERY']
  - GWFD-020254#0050#001: 设置VoLTE业务快速恢复功能 | GWFD-020 | 语音
## cluster-075 (1人) [其他]
- 核心命令: ['ADD VPNINST', 'ADD L3VPNINST', 'ADD VPNINSTAF']
  - GWFD-020401#6d25#001: 配置License及VPN实例 | GWFD-020 | 其他
## cluster-076 (1人) [其他]
- 核心命令: ['ADD ROUTEPOLICY', 'ADD ROUTEPOLICYNODE', 'ADD MATCHROUTETYPE']
  - GWFD-020401#6d25#002: 配置路由策略及节点匹配 | GWFD-020 | 其他
## cluster-077 (1人) [其他]
- 核心命令: ['ADD OSPFV3', 'ADD OSPFV3AREA', 'ADD OSPFV3IMPORTROUTE']
  - GWFD-020401#6d25#003: 启动OSPFv3并发布WLR路由 | GWFD-020 | 其他
## cluster-078 (1人) [其他]
- 核心命令: ['ADD IPV6PATHMTU', 'ADD SRROUTE6', 'ADD SRROUTE']
  - GWFD-020402#d57a#002: 配置IPv6路径MTU及可选静态路由 | GWFD-020 | 其他
## cluster-079 (1人) [地址分配]
- 核心命令: ['ADD POOL', 'ADD SECTION', 'ADD POOLGROUP', 'ADD POOLBINDGROUP', 'ADD TACGROUP']
  - GWFD-020406#c800#002: 配置地址池组及TAC/LAC位置区映射 | GWFD-020 | 地址分配
## cluster-080 (1人) [接入控制]
- 核心命令: ['SET IPALLOCRULE', 'SET APNIPALLOCRULE', 'SET IPALLOCBYLOCGLBSW', 'SET IPALLOCBYLOCSW', 'ADD OSPF']
  - GWFD-020406#c800#003: 配置分配规则、位置开关及OSPF路由 | GWFD-020 | 接入控制
## cluster-081 (1人) [其他]
- 核心命令: ['ADD ADRLOCWHITELST']
  - GWFD-020406#c800#004: 配置位置区分配白名单 | GWFD-020 | 其他
## cluster-082 (1人) [QoS]
- 核心命令: ['RMV QOSAPPLICATION', 'RMV MQCPOLICYNODE', 'RMV MQCPOLICY', 'RMV MQCCLASSIFIER', 'RMV QOSACTRDRNHP']
  - IPFD-012000#2c5e#001: 去激活QoS复杂流分类(删除流策略/分类/行为) | IPFD-012 | QoS
## cluster-083 (1人) [QoS]
- 核心命令: ['ADD MQCBEHAVIOR', 'ADD QOSACTRDRNHP', 'ADD SQOSREMARK', 'SET QOSACTFILTER', 'ADD QOSACTRDRPOLICY']
  - IPFD-012000#63c5#001: 配置ACL规则组、流行为及流分类 | IPFD-012 | QoS
## cluster-084 (1人) [其他]
- 核心命令: ['ADD MQCPOLICY', 'ADD MQCPOLICYNODE', 'ADD QOSAPPLICATION', 'MOD MQCPOLICY']
  - IPFD-012000#63c5#002: 配置流策略并应用到接口 | IPFD-012 | 其他
## cluster-085 (1人) [QoS]
- 核心命令: ['LST ACLGROUP', 'DSP ACLRULEADV4', 'LST QOSRULEACL', 'LST QOSACTRDRNHP', 'LST SQOSREMARK']
  - IPFD-012000#009a#001: 调测QoS复杂流分类(查询验证) | IPFD-012 | QoS
## cluster-086 (1人) [QoS]
- 核心命令: ['RMV QOSIFTRUST', 'RMV QOSDIFFERSERV', 'RMV QOSRDRVPN', 'RMV QOSIFPHB']
  - IPFD-012000#9219#001: 去激活QoS简单流分类 | IPFD-012 | QoS
## cluster-087 (1人) [QoS]
- 核心命令: ['ADD QOSDIFFERSERV', 'SET QOSBA', 'SET QOSPHB', 'ADD QOSIFTRUST', 'ADD QOSRDRVPN']
  - IPFD-012000#2037#001: 激活QoS简单流分类 | IPFD-012 | QoS
## cluster-088 (1人) [安全]
- 核心命令: ['RMV ACLRULEIF', 'RMV ACLRULEETH', 'RMV ACLRULEADV4', 'RMV ACLRULEBAS4', 'RMV ACLGROUP']
  - IPFD-012000#b3bf#001: 去激活ACL(删除规则及组) | IPFD-012 | 安全
## cluster-089 (1人) [安全]
- 核心命令: ['ADD ACLGROUP', 'ADD ACLRULEBAS4', 'ADD ACLRULEADV4', 'ADD ACLRULEETH', 'ADD ACLRULEIF']
  - IPFD-012000#8337#001: 激活ACL(增加规则及组) | IPFD-012 | 安全
## cluster-090 (1人) [安全]
- 核心命令: ['ADD INTERFACE', 'ADD IFIPV4ADDRESS', 'ADD GRETUNNEL', 'ADD IFIPV4ADDRESS', 'MOD INTERFACE']
  - IPFD-015000#f870#001: 配置GRE基础(LoopBack/Tunnel/静态路由) | IPFD-015 | 安全
## cluster-091 (1人) [安全]
- 核心命令: ['ADD GRETUNNEL', 'ADD GRETUNNEL', 'ADD GRETUNNEL']
  - IPFD-015000#f870#002: 配置GRE可选功能(校验/关键字/Keepalive) | IPFD-015 | 安全
## cluster-092 (1人) [地址分配]
- 核心命令: ['ADD VPNINST', 'ADD POOLGROUP', 'ADD POOL', 'ADD SECTION', 'ADD POOLBINDGROUP']
  - GWFD-020406#89d6#001: 配置License、白名单检测及OSPFv3路由 | GWFD-020 | 地址分配
## cluster-093 (1人) [其他]
- 核心命令: ['ADD SRROUTE', 'ADD OSPF', 'ADD OSPFAREA', 'ADD OSPFNETWORK', 'ADD OSPFIMPORTROUTE']
  - IPFD-015004#7a62#007: 配置静态路由及OSPF | IPFD-015 | 其他
## cluster-094 (1人) [安全]
- 核心命令: ['ADD IPSECPROPOSALIPSEC']
  - IPFD-015004#0b85#004: 配置IPsec安全提议 | IPFD-015 | 安全
## cluster-095 (1人) [其他]
- 核心命令: ['ADD IKEPROPOSAL']
  - IPFD-015004#0b85#005: 配置IKE安全提议 | IPFD-015 | 其他
## cluster-096 (1人) [其他]
- 核心命令: ['ADD IKEPEER6']
  - IPFD-015004#0b85#006: 配置IKE对等体 | IPFD-015 | 其他
## cluster-097 (1人) [带宽控制]
- 核心命令: ['SET QOSCAR', 'SET QOSSHAPE']
  - GWFD-020381#dcfa#002: 可选CAR与Shaping开关 | GWFD-020 | 带宽控制
## cluster-098 (1人) [带宽控制]
- 核心命令: ['ADD IPSQMSHAPING']
  - GWFD-110941#7002#001: 配置License及静态整形 | GWFD-110 | 带宽控制
## cluster-099 (1人) [带宽控制]
- 核心命令: ['SET IPSQMQDEPTH', 'SET IPSQMADJUST', 'ADD IPSQMVIPLIST']
  - GWFD-110941#7002#002: 可选整形调优参数 | GWFD-110 | 带宽控制
## cluster-100 (1人) [其他]
- 核心命令: ['SET FABRICSUBHEALTHY', 'SET NODEHEALCTRL']
  - UNK#9845#002: 前置登录及亚健康检测配置 |  | 其他
## cluster-101 (1人) [其他]
- 核心命令: ['LST VNFC', 'SET BASESUBHEALTH', 'SET ELECTSERVICE']
  - UNK#a446#002: 前置登录及亚健康参数配置 |  | 其他
## cluster-102 (1人) [访问限制]
- 核心命令: ['SET APNHTTP2DGRD', 'MOD PCCPOLICYGRP']
  - GWFD-110202#557a#002: 可选APN级与rule级回落开关 | GWFD-110 | 访问限制
## cluster-103 (1人) [访问限制]
- 核心命令: ['ADD HOST', 'ADD FILTER', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF', 'ADD RULE']
  - GWFD-110203#3c81#002: 配置HTTPS解析规则 | GWFD-110 | 访问限制
## cluster-104 (1人) [其他]
- 核心命令: ['ADD WELLKNOWNPORT', 'LOD SIGNATUREDB', 'LOD PARSERDB']
  - GWFD-110203#3c81#004: 配置协议识别库 | GWFD-110 | 其他
## cluster-105 (1人) [其他]
- 核心命令: ['ADD USRRELATEIDEN']
  - GWFD-110203#3c81#005: 可选用户关联识别 | GWFD-110 | 其他
## cluster-106 (1人) [QoS]
- 核心命令: ['SET SRVCOMMONPARA', 'ADD QOSDIFFERSERV', 'SET QOSBA', 'ADD QOSIFTRUST', 'SET SRVCOMMONPARA']
  - GWFD-010201#503d#001: 配置QoS与流量管理(上行+下行+CAR) | GWFD-010 | QoS
## cluster-107 (1人) [其他]
- 核心命令: ['ADD FLOWFILTER', 'ADD PROTBINDFLOWF']
  - GWFD-110251#e541#002: 配置过滤条件 | GWFD-110 | 其他
## cluster-108 (1人) [计费]
- 核心命令: ['LOD EXTERNALDB', 'ADD FLOWFILTER', 'SET EXTOTTMATCHSW', 'ADD URR', 'ADD URRGROUP']
  - GWFD-110321#2433#002: 加载外部OTT业务规则库 | GWFD-110 | 计费
## cluster-109 (1人) [访问限制]
- 核心命令: ['ADD APN', 'SET APNCFFUNC', 'ADD CFPROFILE', 'ADD CFTEMPLATE', 'SET APNCFTEMPLATE']
  - GWFD-110471#55f2#002: 配置URL过滤用户使用的APN | GWFD-110 | 访问限制
## cluster-110 (1人) [其他]
- 核心命令: ['ADD VPNINST', 'ADD LOGICINF', 'ADD ICAPSERVER', 'ADD ICAPLOCALINFO', 'ADD ICAPSVRGRP']
  - GWFD-110471#d1bb#001: 添加VPN实例 | GWFD-110 | 其他
## cluster-111 (1人) [地址分配]
- 核心命令: ['SET ADDRESSATTR', 'ADD UPIPDOMAIN', 'ADD RESELECTUPCAUSE']
  - GWFD-020161#3818#002: 配置地址分配方式 | GWFD-020 | 地址分配
## cluster-112 (1人) [接入控制]
- 核心命令: ['ADD APN', 'SET APNACCESSWAL', 'SET DEACTIVERATE', 'SET SOFTPARA']
  - GWFD-010251#7692#001: 配置APN实例 | GWFD-010 | 接入控制
## cluster-113 (1人) [地址分配]
- 核心命令: ['ADD POOL', 'ADD SECTION', 'ADD POOLGROUP', 'ADD POOLBINDGROUP', 'ADD APN']
  - GWFD-010107#0c8b#001: 配置主用 UDG 静态地址用户路由冗余功能 | GWFD-010 | 地址分配
## cluster-114 (1人) [接入控制]
- 核心命令: ['SET APNADDRESSATTR', 'SET APNFLOWMAXNUM', 'SET SRVCOMMONPARA']
  - GWFD-110910#24e2#002: 使能该APN的Routing Behind MS功能 | GWFD-110 | 接入控制
## cluster-115 (1人) [其他]
- 核心命令: ['ADD L3VPNINST', 'ADD VPNINSTAF', 'SET BFD', 'ADD OSPFV3', 'MOD OSPFV3']
  - GWFD-010155#afa0#001: 参考初始配置中 **配置动态路由OSPFv3+BFD组网（I | GWFD-010 | 其他
## cluster-116 (1人) [其他]
- 核心命令: ['ADD VPNINST', 'ADD LOGICINF']
  - GWFD-010155#afa0#002: 配置VPN实例及逻辑接口 | GWFD-010 | 其他
## cluster-117 (1人) [其他]
- 核心命令: ['ADD L3VPNINST', 'ADD VPNINSTAF', 'ADD VPNINST', 'SET BFD', 'ADD OSPF']
  - GWFD-010155#aebd#001: 参考初始配置中 **配置动态路由OSPF+BFD组网（IPv | GWFD-010 | 其他
## cluster-118 (1人) [地址分配]
- 核心命令: ['ADD AUTOSCALINGBGPLF', 'ADD AUTOSCALINGIPREACH', 'SET DATAPLANEINFMODE', 'SET DATAPLANEGIINFMODE', 'ADD LOGICINF']
  - GWFD-020482#734c#001: 配置BGP over静态路由+BFD探测 | GWFD-020 | 地址分配
## cluster-119 (1人) [其他]
- 核心命令: ['SET SSUBIGFLOWCTRL', 'SET USRREALLOCNTY', 'ADD FLOWFILTER', 'ADD RULE']
  - GWFD-111701#b82d#002: 配置小区拥塞优化业务大流速率 | GWFD-111 | 其他
## cluster-045 (2人) [访问限制/其他] ⚡跨域
- 核心命令: ['SET IPFARMGLOBAL', 'ADD LOGICINF', 'ADD IPFARM', 'ADD IPFARMSERVER', 'LST IPFARMSERVER']
  - GWFD-110281#77b6#002: 配置用户Portal业务的整机参数 | GWFD-110 | 访问限制
  - GWFD-110282#4e17#002: 配置IPFarm全局参数 | GWFD-110 | 其他
## cluster-120 (1人) [带宽控制]
- 核心命令: ['ADD BWMCONTROLLER', 'ADD BWMCONTROLLER', 'ADD BCSRVLEVELPLY']
  - GWFD-110313#5b86#002: 设置支持用户级公平调度功能 | GWFD-110 | 带宽控制
## cluster-121 (1人) [计费]
- 核心命令: ['ADD URR', 'ADD QOSPROP', 'ADD PCCPOLICYGRP', 'ADD WELLKNOWNPORT', 'ADD SADEDICBEARER']
  - GWFD-020358#bd63#003: 配置QoS属性 | GWFD-020 | 计费
## cluster-122 (1人) [带宽控制]
- 核心命令: ['ADD L7FILTER', 'ADD FLOWFILTER', 'ADD PROTBINDFLOWF', 'ADD RULE', 'ADD BWMSERVICE']
  - GWFD-110311#de35#003: 配置业务感知规则 | GWFD-110 | 带宽控制
## cluster-123 (1人) [带宽控制]
- 核心命令: ['ADD BWMSERVICE', 'ADD BWMCONTROLLER', 'ADD BWMUSERGROUP', 'ADD BWMRULE', 'ADD SNSSAI']
  - GWFD-110311#1b24#002: 配置BWM业务 | GWFD-110 | 带宽控制
## cluster-124 (1人) [其他]
- 核心命令: ['ADD TWAMPVPNINST', 'ADD TWAMPLOGICINF', 'ADD TWAMPRESPONDER', 'SET TCPKEEPALIVECFG']
  - GWFD-110921#025e#002: 配置本端探测逻辑接口，UPF与gNodeB之间采用N3/S1 | GWFD-110 | 其他
## cluster-125 (1人) [其他]
- 核心命令: ['ADD TWAMPVPNINST', 'ADD TWAMPLOGICINF', 'ADD TWAMPCLIENT', 'ADD TWAMPSENDER', 'SET LINKALMCFG']
  - GWFD-110921#c0ef#002: 配置本端探测逻辑接口 | GWFD-110 | 其他
## cluster-126 (1人) [接入控制]
- 核心命令: ['ADD APN', 'ADD LOGICINF']
  - GWFD-110606#1284#002: 配置APN | GWFD-110 | 接入控制
## cluster-127 (1人) [接入控制]
- 核心命令: ['ADD APN', 'SET APNNONIPFUNC']
  - GWFD-110607#661b#002: 配置Non-IP数据传输所使用的APN | GWFD-110 | 接入控制
## cluster-128 (1人) [其他]
- 核心命令: ['SET SIPSIGMIRRORPARA', 'SET SOFTPARA']
  - GWFD-112001#48ae#001: 安装镜像SIP信令功能插件，完成插件安装后再进行配置操作 | GWFD-112 | 其他
## cluster-129 (1人) [计费]
- 核心命令: ['SET URRFAILACTION', 'ADD URR']
  - GWFD-010171#479e#005: **可选** ：设置URR上报失败后的动作处理参数 | GWFD-010 | 计费
## cluster-130 (1人) [计费]
- 核心命令: ['ADD USERPROFILE', 'ADD RULEBINDING', 'SET UPDEFAULTQUOTA', 'ADD URR', 'SET UPGLBCHGPARA']
  - GWFD-020300#94b8#004: 配置内容计费规则绑定用户模板 | GWFD-020 | 计费
## cluster-131 (1人) [计费]
- 核心命令: ['ADD EXTENDEDFILTER', 'ADD REDIRAPPENDINFO', 'SET GYONESHOT', 'ADD URR', 'ADD URRGROUP']
  - GWFD-020356#76a2#002: 配置一次重定向的参数 | GWFD-020 | 计费
## cluster-132 (1人) [其他]
- 核心命令: ['LOD SIGNATUREDB', 'ADD FINGERIDENT', 'LST SUPPFINGERIDEN', 'LST FINGERIDENT']
  - GWFD-110404#feb0#002: 加载特定的完整的特征库文件 | GWFD-110 | 其他
## cluster-133 (1人) [计费]
- 核心命令: ['ADD FILTER', 'ADD FILTERIPV6', 'ADD FLOWFILTER', 'ADD FLTBINDFLOWF', 'ADD URR']
  - GWFD-112000#8dc7#001: 配置语音缺省QoS Flow/缺省承载静态PCC策略 | GWFD-112 | 计费
## cluster-134 (1人) [其他]
- 核心命令: ['SET RTSDNNPARA', 'SET RTSDNNPARA', 'SET RTSDNNPARA']
  - GWFD-020531#7baa#002: 在公网UPF上配置通用DNN漫游分流开关 | GWFD-020 | 其他
## cluster-015 (6人) [其他] ⚡跨域
- 核心命令: ['SET LICENSESWITCH']
  - GWFD-020101#3045#001: 打开本特性的License配置开关 | GWFD-020 | 其他
  - GWFD-111201#911f#001: 打开本特性的License配置开关 | GWFD-111 | 其他
  - GWFD-020451#238e#001: 打开本功能的License配置开关 | GWFD-020 | 其他
  - ... (3 more)
## cluster-020 (4人) [安全]
- 核心命令: ['ADD IPSECPROPOSALIPSEC', 'ADD IKEPROPOSAL']
  - IPFD-015004#a85c#004: 配置IPsec与IKE提议 | IPFD-015 | 安全
  - IPFD-015004#75c5#004: 配置IPsec与IKE提议 | IPFD-015 | 安全
  - IPFD-015004#2f2d#004: 配置IPsec与IKE提议 | IPFD-015 | 安全
  - ... (1 more)
