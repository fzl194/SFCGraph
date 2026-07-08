---
id: UNC@20.15.2@MMLCommand@RMV GTPCPATH
type: MMLCommand
name: RMV GTPCPATH（删除GTP-C路径）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCPATH
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径管理
status: active
---

# RMV GTPCPATH（删除GTP-C路径）

## 功能

**适用网元：SGSN、MME**

该命令用于删除GTP-C信令面路径。

通常在当前路径的GTP版本与对端GSN实际支持的最高GTP版本不一致，希望重新创建GTP路径时会执行删除GTP路径的动作，比如对端GSN实际最高支持GTP V1版本，但由于通讯等原因，本端GSN在探测对端支持的GTP版本时，有可能误判为GTP V0版本，则以后所有由本端GSN发起的信令流程，都会使用GTP V0版本与对端进行通讯，尽管本端GSN有路径版本定时核查机制，但如果想立刻重新探测对端GSN支持的最高GTP协议版本，需要删除GTP-C路径。

## 注意事项

- 该命令执行后立即生效。
- 此命令只用于SPP进程/UPP进程。
- 输入参数时，先选择“GTP版本”，指明是删除GTP-C路径的协议版本是“GTPv0(GTPv0)”、“GTPv1(GTPv1)”还是“GTPv2(GTPv2)”。
- 在输入对端IP地址参数时，请确认此IP为对端GSN信令面（GTP-C路径）的IP地址，如果存在与{本端IP地址、对端IP地址}标识对应的路径且路径上没有等待应答的GTP-C信令，则删除此路径；如果不存在该路径，亦会提示删除路径成功。
- 如果删除的是SPP进程上的GTP-C路径，会导致此路径上正在等待响应的请求消息不能正常接收响应消息。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的协议版本。<br>取值范围：<br>- “GTPv0(GTPv0)”<br>- “GTPv1(GTPv1)”<br>- “GTPv2(GTPv2)”<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端GSN信令面（GTP-C路径）的IP地址类型。<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端GSN IPv4地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GSN IPV4地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端GSN IPV6地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV6(IPV6)”<br>时此参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GSN IPV6地址。<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV6(IPV6)”<br>时此参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| SCOPE | 范围 | 可选必选说明：可选参数<br>参数含义：该参数用于删除GTP-C路径的范围。<br>取值范围：<br>- “ALL(所有)”<br>- “SPEC(指定)”<br>默认值：<br>“ALL(所有)”<br>说明：当配置为<br>“ALL(所有)”<br>时会删除所有节点和进程上满足条件的GTP-C路径；当设置为<br>“SPEC(指定)”<br>时只删除指定节点和进程上的GTP-C路径。 |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTP | 进程类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>前提条件：当<br>“范围”<br>设置为<br>“SPEC(指定)”<br>时此参数有效。<br>取值范围：<br>- SPP(SPP)<br>- UPP(UPP)<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定进程的序号。<br>前提条件：当<br>“范围”<br>设置为<br>“SPEC(指定)”<br>时此参数有效。<br>取值范围：0~20<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则:<br>- 当“范围”参数配置为“ALL（所有）”时，VNFC名称需要填写USN的名称。<br>- 当“范围”参数配置为“SPEC（指定）”时:- 如果需要删除SPP进程上的GTPC路径，则SERVICETYPE需要填写USN的名称。<br>- 如果需要删除UPP进程上的GTPC路径，则SERVICETYPE需要填写LINK的名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATH]] · GTP-C路径（GTPCPATH）

## 使用实例

删除本端IP为192.168.14.20，对端IP为192.168.9.20的V1版本的GTP-C路径：

RMV GTPCPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.14.20", PEERIPV4ADDR="192.168.9.20", SERVICETYPE="USN_VNFC";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-C路径(RMV-GTPCPATH)_72345511.md`
