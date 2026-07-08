---
id: UDG@20.15.2@MMLCommand@MOD NGVNINSTANCE
type: MMLCommand
name: MOD NGVNINSTANCE（修改5G VNInstance配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: NGVNINSTANCE
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN基础配置
- 5G LAN实例配置
status: active
---

# MOD NGVNINSTANCE（修改5G VNInstance配置）

## 功能

**适用NF：UPF**

该命令用于更新一个5G LAN会话实例下的配置参数。

## 注意事项

- 该命令执行后立即生效。
- 执行MOD NGVNINSTANCE命令的时候，PDNTYPE从ETHERNET变为IP，ETHERNET相关配置参数恢复为默认值且不生效。
- 当存在5G LAN组会话和UE会话的时候不允许修改PDNTYPE。
- 该命令中精简化开关开启后，报文按照精简流程转发，UPF间Vxlan隧道互通、上行未知单播转N6/N19、上行未知组播转N6/N19、上行广播转N6/N19开关不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |
| PDNTYPE | PDN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN组内UE会话的PDN类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ETHERNET：以太网。<br>- IP：IP。<br>默认值：无<br>配置原则：无 |
| PDNCONNECTTYPE | PDN连接类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于设置PDN连接类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- VXLAN：表示使用Vxlan隧道。<br>- ETHTERNET：表示使用以太连接。<br>默认值：无<br>配置原则：无 |
| VXLANINTERWORK | UPF间Vxlan隧道互通 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNCONNECTTYPE”配置为“VXLAN”时为可选参数。<br>参数含义：该参数用于配置UPF间是否可以通过Vxlan隧道互访。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- YES：UPF间可以通过VXLAN 隧道互访。<br>- NO：UPF间不能通过VXLAN 隧道互访。<br>默认值：无<br>配置原则：无 |
| VLANTYPE | VLAN类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PDNCONNECTTYPE”配置为“ETHTERNET”时为必选参数。<br>参数含义：该参数用于设置VLAN类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- UNIQUE：插入唯一的VLAN。<br>- WHITELIST：基于白名单透传VLAN。<br>- QINQ：在原有VLAN基础上插入新VLAN。<br>- VLANMAP：将原有VLAN映射为新VLAN。<br>默认值：无<br>配置原则：无 |
| VLANID | VLAN ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“VLANTYPE”配置为“UNIQUE” 或 “QINQ”时为必选参数。<br>参数含义：该参数用于设置VLAN ID。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～4094。<br>默认值：无<br>配置原则：无 |
| MACIDLESW | N3学习的MAC地址空闲时长开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于设置N3接口学习的MAC地址空闲检查功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PACKETDIRECTION | 报文检测方向 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MACIDLESW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置是通过上行报文还是上下行双向报文检查MAC地址是否空闲。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UP_DOWN_LINK：通过上行和下行报文检测MAC地址空闲。<br>- UP_LINK：通过上行报文检测MAC地址空闲。<br>默认值：无<br>配置原则：无 |
| MACIDLETIME | N3学习的MAC地址空闲时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MACIDLESW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置N3接口学习的MAC地址空闲超时上限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~12000，单位是分钟。<br>默认值：无<br>配置原则：无 |
| IGMPSNOOPINGSW | IGMP Snooping开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于设置是否开启IGMP Snooping功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| IGMPPARSESW | IGMP消息解析开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IGMPSNOOPINGSW”配置为“DISABLE”时为可选参数。<br>参数含义：该参数用于设置是否解析IGMP消息。该参数在此版本已废弃。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| MULTIFLOODSW | 组播泛洪开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于设置组播消息泛洪处理开关。开关开启时未知组播报文会在5G LAN组内泛洪转发，泛洪转发时组播报文目的MAC保持不变。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| MULTIFLOODRATE | 组播泛洪速率 | 可选必选说明：条件可选参数<br>前提条件：该参数在“MULTIFLOODSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置组播泛洪速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-200。<br>默认值：无<br>配置原则：无 |
| BCASTFLOWCTRLSW | 广播流控开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于配置是否使能广播消息流控功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| BCASTDATARATE | 广播数据处理速率 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BCASTFLOWCTRLSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于控制每秒转发的最大广播包数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1-200。<br>默认值：无<br>配置原则：无 |
| SIMPLEIND | 精简组指示 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于指定5G LAN组是否为精简化5G LAN组。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：非精简化5G LAN组。<br>- TRUE：精简化5G LAN组。<br>默认值：无<br>配置原则：无 |
| BROADCASTSW | 广播功能开关 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SIMPLEIND”配置为“TRUE”时为必选参数。<br>参数含义：该参与用户配置精简化5G LAN组内是否支持广播报文转发。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UNICASTFLOODSW | 单播泛洪开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于设置单播消息泛洪处理开关。开关开启时未知单播消息泛洪转发，泛洪转发时消息目的MAC地址不变。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| UNIFLOODRATE | 单播泛洪速率 | 可选必选说明：条件可选参数<br>前提条件：该参数在“UNICASTFLOODSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置单播泛洪速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1-200。<br>默认值：无<br>配置原则：无 |
| N6MACIDLESW | N6学习的MAC地址空闲时长开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于设置N6侧MAC地址空闲检查功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| N6MACIDLETIME | N6侧MAC地址空闲时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“BROADCASTSW”配置为“ENABLE”时为可选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“N6MACIDLESW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置N6侧MAC地址空闲超时上限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~1440，单位是分钟。<br>默认值：无<br>配置原则：无 |
| ULUKNUCASTFWNX | 上行未知单播转N6/N19 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于在单播转广播开关关闭以及单播转广播开关开启但已达到流控阈值场景下，配置上行未知单播消息是否通过N6/N19接口发送。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：无 |
| ULUKNMCASTFWNX | 上行未知组播转N6/N19 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于在组播转广播开关关闭以及组播转广播开关开启但已达到流控阈值场景下，配置上行未知组播消息是否通过N6/N19接口发送。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：无 |
| ULBCASTFWNX | 上行广播转N6/N19 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：该参数用于配置在广播达到流控阈值场景下上行广播消息是否通过N6/N19接口发送。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ENABLE：使能。<br>- DISABLE：不使能。<br>默认值：无<br>配置原则：无 |
| MACRPTMODE | MAC地址上报模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PDNTYPE”配置为“ETHERNET”时为可选参数。<br>参数含义：MAC地址上报模式。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- SINGLE_MAC_RPT：上报单个MAC地址。<br>- ALL_MAC_RPT：上报所有MAC地址。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G VNInstance配置（NGVNINSTANCE）](configobject/UDG/20.15.2/NGVNINSTANCE.md)

## 使用实例

修改会话实例配置。“VNINSTANCE”为“a0000001-460-003-a123456789b987654321”的MACIdleSw为开启：

```
MOD NGVNINSTANCE: VNINSTANCE="a0000001-460-003-01", PDNTYPE=ETHERNET, MACIDLESW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改5G-VNInstance配置（MOD-NGVNINSTANCE）_20594007.md`
