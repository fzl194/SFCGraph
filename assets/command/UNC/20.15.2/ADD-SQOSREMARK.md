---
id: UNC@20.15.2@MMLCommand@ADD SQOSREMARK
type: MMLCommand
name: ADD SQOSREMARK（增加重标记配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SQOSREMARK
command_category: 配置类
effect_mode: ''
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重标记
status: active
---

# ADD SQOSREMARK（增加重标记配置）

## 功能

该命令用来增加重标记。

可以对匹配的报文进行DSCP、DF、TOS、IP-precedence等重标记。在一个流行为下只能添加一次Remark动作，再添加或修改Remark动作时需要使用MOD SQOSREMARK命令。

## 注意事项

- 该命令最大记录数为65535。
- 需要使用ADD MQCBEHAVIOR命令先配置流行为。
- V4DSCPVALUE和V4TOSVALUE、V4PRECEDENCE互斥，不能同时配置。
- V6DSCPVALUE和V6TOSVALUE、V6PRECEDENCE互斥，不能同时配置。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| V4DSCPVALUE | IPv4的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv4的DSCP（差分服务码点）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～63，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6DSCPVALUE | IPv6的DSCP值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv6的DSCP（差分服务码点）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～63，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| DFVALUE | DF值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置DF（不分片标记）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～1，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V4TOSVALUE | IPv4的TOS值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv4的TOS（服务类型）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～15，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V4PRECEDENCE | IPv4的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv4的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6TOSVALUE | IPv6的TOS值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv6的TOS（服务类型）值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～15，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6PRECEDENCE | IPv6的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置IPv6的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| VLAN8021P | 802.1p值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VLAN报文的802.1p值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。<br>默认值：255<br>配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |

## 操作的配置对象

- [重标记配置（SQOSREMARK）](configobject/UNC/20.15.2/SQOSREMARK.md)

## 使用实例

增加重标记配置：

```
ADD SQOSREMARK:BEHAVIORNAME="b1",DFVALUE=1,V4TOSVALUE=2,V6TOSVALUE=2,V6PRECEDENCE=2,VLAN8021P=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加重标记配置（ADD-SQOSREMARK）_00441017.md`
