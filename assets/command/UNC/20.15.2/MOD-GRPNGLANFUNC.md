---
id: UNC@20.15.2@MMLCommand@MOD GRPNGLANFUNC
type: MMLCommand
name: MOD GRPNGLANFUNC（修改指定群组的5G LAN会话扩展参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GRPNGLANFUNC
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 5G LAN组级扩展功能
status: active
---

# MOD GRPNGLANFUNC（修改指定群组的5G LAN会话扩展参数）

## 功能

**适用NF：SMF**

该命令用于修改指定会话组NGLAN扩展功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPID | 5G LAN组ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>GROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |
| N19SUPPORT | 是否支持N19通信 | 可选必选说明：可选参数<br>参数含义：该参数用于控制5G LAN会话的跨园区会话场景下是否支持通过UPF间的N19接口进行通信。<br>数据来源：本端规划<br>取值范围：<br>- INHERIT（继承）<br>- SUPPORT（支持）<br>- NOTSUPPORT（不支持）<br>默认值：无<br>配置原则：<br>当此参数配置为INHERIT时继承SET NGLANFUNC配置的N19SUPPORT取值。 |
| PSAPRIFLAG | 优选5G LAN组内已有的主锚点UPF的开关 | 可选必选说明：可选参数<br>参数含义：该参数控制是否支持优选5G LAN组内已建立组会话的锚点UPF。<br>数据来源：本端规划<br>取值范围：该参数用于控制是否支持优选5G LAN组内已建立组会话的锚点UPF。<br>- INHERIT（继承）<br>- SUPPORT（支持）<br>- NOTSUPPORT（不支持）<br>默认值：无<br>配置原则：<br>当此参数配置为INHERIT时继承SET NGLANFUNC配置的PSAPRIFLAG取值。 |
| MULTICAST | 是否创建组播PDR规则 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否创建组播PDR规则，以支持5G LAN组通过N6接口或N19接口进行组播通信。<br>数据来源：本端规划<br>取值范围：<br>- INHERIT（继承）<br>- SUPPORT（支持）<br>- NOTSUPPORT（不支持）<br>默认值：无<br>配置原则：<br>当此参数配置为INHERIT时继承SET NGLANFUNC配置的MULTICAST取值。 |
| N6BROADCASTSW | 是否支持N6侧上行广播 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否为5G LAN PDU会话创建N6上行广播规则，以支持UE与存量网络通过N6接口进行上行广播。<br>数据来源：全网规划<br>取值范围：<br>- INHERIT（继承）<br>- SUPPORT（支持）<br>- NOTSUPPORT（不支持）<br>默认值：无<br>配置原则：<br>当此参数配置为INHERIT时继承SET NGLANFUNC配置的N6BROADCASTSW取值。 |
| PKTELIMINATESSW | 是否支持报文增殖消除 | 可选必选说明：可选参数<br>参数含义：该参数用于控制标准5G LAN是否支持报文增殖消除方案，避免报文环回。<br>数据来源：全网规划<br>取值范围：<br>- INHERIT（继承）<br>- SUPPORT（支持）<br>- NOTSUPPORT（不支持）<br>默认值：无<br>配置原则：<br>当此参数配置为INHERIT时继承SET NGLANFUNC配置的PKTELIMINATESSW取值。 |
| MACPROCMODE | MAC地址处理模式 | 可选必选说明：可选参数<br>参数含义：该参数用于控制UPF上报单播、组播MAC时，SMF的处理模式。<br>数据来源：本端规划<br>取值范围：<br>- SINGLE（MAC地址单条上报）<br>- FULL（MAC地址全量上报）<br>默认值：无<br>配置原则：<br>同一组内该配置需要与UPF上的MAC地址上报方式保持一致。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GRPNGLANFUNC]] · 指定群组的5G LAN会话扩展参数（GRPNGLANFUNC）

## 使用实例

将当前GROUPID="A0000001-460-003-01"的记录中的N19SUPPORT和PSAPRIFLAG参数修改为NOTSUPPORT和NOTSUPPORT。

```
MOD GRPNGLANFUNC: GROUPID="A0000001-460-003-01", N19SUPPORT=NOTSUPPORT, PSAPRIFLAG=NOTSUPPORT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GRPNGLANFUNC.md`
