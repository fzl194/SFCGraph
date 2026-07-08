---
id: UNC@20.15.2@MMLCommand@ACT SFEPKTDBG
type: MMLCommand
name: ACT SFEPKTDBG（激活报文调测过滤）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: SFEPKTDBG
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 软转发报文调测
status: active
---

# ACT SFEPKTDBG（激活报文调测过滤）

## 功能

该命令用来设置报文调测过滤配置及激活调测功能。执行DSP SFEDBGPKT可查询相匹配的SFE报文统计信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBGTYPE | 诊断类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示调测类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- display：显示模式。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～60。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| PKTINFO | 报文信息 | 可选必选说明：可选参数<br>参数含义：该参数用来表示调测报文特征信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～160。区分大小写。<br>默认值：无<br>配置原则：<br>- 不支持输入空格。<br>- 有效过滤字符为0～9和a～f，范围之外的字符会被忽略过滤。 |
| PKTNUM | 报文数量 | 可选必选说明：可选参数<br>参数含义：该参数用来表示最大显示报文数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2048。<br>默认值：64 |
| PKTCAPLEN | 获取的报文头长度 | 可选必选说明：可选参数<br>参数含义：该参数用来表示获取的报文头最大长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为34～64。<br>默认值：34 |
| PKTTYPE | 报文类型 | 可选必选说明：可选参数<br>参数含义：该参数用来表示报文类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4报文。<br>- IPV6：IPv6报文。<br>- arp：ARP报文。<br>- mpls：MPLS报文。<br>默认值：无<br>配置原则：如果不设置该参数，则报文调测过滤不指定报文类型。 |
| PROTOCOLNUM | 协议号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV4” 或 “IPV6”时为可选参数。<br>参数含义：该参数用来表示协议号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无<br>配置原则：如果不设置该参数，则报文调测过滤不指定报文协议。 |
| PKTDBGTYPE | 报文诊断类型 | 可选必选说明：可选参数<br>参数含义：该参数用来表示报文诊断类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LDM：从LDM收到的报文。<br>- SFE：从SFE收到的报文。<br>- PAE：从PAE收到的报文。<br>- DISCARD：系统丢弃的报文。<br>- TOCP：上送CPU的报文。<br>- TOPAE：发给PAE的报文。<br>- TOLDM：发给LDM的报文。<br>默认值：无<br>配置原则：如果不设置该参数，则报文调测过滤不指定报文诊断类型。 |
| SRCPORT | 源端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV4” 或 “IPV6”时为可选参数。<br>参数含义：该参数用来表示源端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 协议类型为TCP或UDP此配置才生效。<br>- 如果不设置该参数，则报文调测过滤不指定源端口。 |
| DESTPORT | 目的端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV4” 或 “IPV6”时为可选参数。<br>参数含义：该参数用来表示目的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 协议类型为TCP或UDP此配置才生效。<br>- 如果不设置该参数，则报文调测过滤不指定目的端口。 |
| SRCIP | 源IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV4”时为可选参数。<br>参数含义：该参数用来表示源IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：X.X.X.X。 |
| DESTIP | 目的IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV4”时为可选参数。<br>参数含义：该参数用来表示目的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：X.X.X.X。 |
| SRCIP6 | 源IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV6”时为可选参数。<br>参数含义：该参数用来表示源IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：X:X:X:X:X:X:X:X。 |
| DESTIP6 | 目的IPv6地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTTYPE”配置为“IPV6”时为可选参数。<br>参数含义：该参数用来表示目的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：X:X:X:X:X:X:X:X。 |
| CAUSEID | 报文丢弃原因码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTDBGTYPE”配置为“DISCARD”时为可选参数。<br>参数含义：该参数用来表示报文丢弃原因。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65536。<br>默认值：无<br>配置原则：如果不设置该参数，则报文调测过滤不指定丢包原因。 |
| PORTTYPE | 接口类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PKTDBGTYPE”配置为“PAE” 或 “TOPAE”时为可选参数。<br>参数含义：该参数用来表示报文收发接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- pkt-all-type：所有接口类型。<br>- pkt-extern：外联口类型。<br>- pkt-fabric：Fabric接口类型。<br>- pkt-fab-tunnel：Fabric-Tunnel接口类型。<br>默认值：无<br>配置原则：如果不设置该参数，则报文调测过滤不指定端口类型。 |
| FIRSTLABEL | 第一层标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LABELTYPE”配置为“firstlabel”时为必选参数。<br>参数含义：该参数用来表示第一层标签。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：4294967295<br>配置原则：至少选择一个有效的参数(FIRSTLABEL，SECONDLABEL，THIRDLABEL，INNERLABEL)，并且与参数LABELTYPE取值保持一致。 |
| SECONDLABEL | 第二层标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LABELTYPE”配置为“secondlabel”时为必选参数。<br>参数含义：该参数用来表示第二层标签。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：4294967295<br>配置原则：至少选择一个有效的参数(FIRSTLABEL，SECONDLABEL，THIRDLABEL，INNERLABEL)，并且与参数LABELTYPE取值保持一致。 |
| THIRDLABEL | 第三层标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LABELTYPE”配置为“thirdlabel”时为必选参数。<br>参数含义：该参数用来表示第三层标签。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：4294967295<br>配置原则：至少选择一个有效的参数(FIRSTLABEL，SECONDLABEL，THIRDLABEL，INNERLABEL)，并且与参数LABELTYPE取值保持一致。 |
| INNERLABEL | 内层标签 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LABELTYPE”配置为“innerlabel”时为必选参数。<br>参数含义：该参数用来表示内层标签。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：4294967295<br>配置原则：至少选择一个有效的参数(FIRSTLABEL，SECONDLABEL，THIRDLABEL，INNERLABEL)，并且与参数LABELTYPE取值保持一致。 |
| LABELTYPE | 标签类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PKTTYPE”配置为“mpls”时为必选参数。<br>参数含义：该参数用来表示标签类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- firstlabel：第一层标签。<br>- secondlabel：第二层标签。<br>- thirdlabel：第三层标签。<br>- innerlabel：内层标签。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用来表示接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～60。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFEPKTDBG]] · 报文调测过滤（SFEPKTDBG）

## 使用实例

配置模式为屏幕显示模式，报文类型为IPv4，源IP为192.168.1.1，最大显示1000条报文，资源单元名称为“VNODE_VNRS_VNFC_IPU_0064”：

```
ACT SFEPKTDBG: DBGTYPE=display, RUNAME="VNODE_VNRS_VNFC_IPU_0064", PKTNUM=1000, PKTTYPE=IPV4, SRCIP="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-SFEPKTDBG.md`
