---
id: UDG@20.15.2@MMLCommand@MOD AUTOSCALINGOSPFPROCGRP
type: MMLCommand
name: MOD AUTOSCALINGOSPFPROCGRP（修改OSPF进程组自动化配置模板）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: AUTOSCALINGOSPFPROCGRP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- OSPF入不转板自动化配置
status: active
---

# MOD AUTOSCALINGOSPFPROCGRP（修改OSPF进程组自动化配置模板）

## 功能

该命令用于修改OSPF进程组自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 修改该模板时，要保证该模板添加过。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；生效配置，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | OSPF进程组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定OSPF进程组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～16。<br>默认值：无 |
| VERSION | OSPF版本号 | 可选必选说明：必选参数<br>参数含义：该参数用来表示自动化配置模板中OSPF版本号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OSPFv2：OSPFv2。<br>- OSPFv3：OSPFv3。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| PROCSEGMENTID | OSPF起始进程ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩容业务OSPF进程组自动分配的OSPF进程ID的基础数值（OSPF进程号计算公式：OSPF起始进程ID * 1000 + RUID）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4000。<br>默认值：无 |
| AREAID | OSPF区域ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩容业务OSPF的区域ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| INSTID | OSPF实例ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“VERSION”配置为“OSPFv3”时为可选参数。<br>参数含义：该参数用于指定扩容业务OSPFv3的实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| COST | OSPF开销 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩容业务OSPF的开销值。 根据VERSION来区分是OSPFv2协议还是OSPFv3协议。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：当配置成0时，表示删除该配置。 |
| HELLOTIMER | 邻居发送Hello包时间间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口发送Hello报文的时间间隔。OSPFHELLOTIMER的值写入Hello报文中后随之发送。OSPFHELLOTIMER的值越小，发现网络拓扑改变的速度越快，路由开销也就越大。确定接口和邻接路由器的参数要保持一致。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。单位是秒。<br>默认值：无<br>配置原则：当配置成0时，表示不配置该选项，实际生成配置为10。 |
| DEADTIMER | 邻居失效的时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定OSPF邻居失效的时间。OSPF邻居的失效时间是指：在该时间间隔内，若未收到邻居的Hello报文，就认为该邻居已失效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～235926000。单位是秒。当VERSION为OSPFv3的取值范围为0～65535，OSPFv2的范围为0～235926000。<br>默认值：无<br>配置原则：<br>- DEADTIMER的值至少应为HELLOTIMER的值的4倍，同一网段上的路由器的DEADTIMER值也必须相同。<br>- 当配置成0时，表示不配置该选项，实际生成配置为OSPF Hello Timer的4倍。 |
| BFDGTMPNAME | BFD模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BFD自动化配置模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～59。不支持空格和中文。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 可通过LST AUTOSCALINGBFD命令查询可用的BFD自动化配置模板名称。 |
| AREATYPE | OSPF区域类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OSPF区域类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Normal：普通区域。<br>- NSSA：NSSA区域。<br>默认值：无<br>配置原则：骨干区域不能配置为NSSA区域。 |
| ISIPPOOLCFG | 是否配置环回口地址池 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AREATYPE”配置为“NSSA”时为可选参数。<br>参数含义：该参数指定是否配置环回口地址池。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：不使能。<br>- TRUE：使能。<br>默认值：无 |
| IPBGNADDR | 环回口地址池起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISIPPOOLCFG”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于指定环回口地址池的起始地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～50。不支持空格和中文。<br>默认值：无<br>配置原则：当VERSION配置为OSPFv2时，IPBGNADDR应该配置IPv4格式的地址。当VERSION配置为OSPFv3时，IPBGNADDR应该配置IPv6格式的地址。 |
| IPENDADDR | 环回口地址池结束地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISIPPOOLCFG”配置为“TRUE”时为必选参数。<br>参数含义：该参数用于指定环回口地址池的结束地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～50。不支持空格和中文。<br>默认值：无<br>配置原则：当VERSION配置为OSPFv2时，IPENDADDR应该配置IPv4格式的地址。当VERSION配置为OSPFv3时，IPENDADDR应该配置IPv6格式的地址。 |

## 操作的配置对象

- [OSPF进程组自动化配置模板（AUTOSCALINGOSPFPROCGRP）](configobject/UDG/20.15.2/AUTOSCALINGOSPFPROCGRP.md)

## 使用实例

修改一个OSPF进程组ID为1的自动化配置模板：

```
MOD AUTOSCALINGOSPFPROCGRP:GROUPID=1,VERSION=OSPFv2,PROCSEGMENTID=100,AREAID="0.0.0.0",COST=5, HELLOTIMER=12, DEADTIMER=45, BFDGTMPNAME="bfd4ospf2";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF进程组自动化配置模板（MOD-AUTOSCALINGOSPFPROCGRP）_50280614.md`
