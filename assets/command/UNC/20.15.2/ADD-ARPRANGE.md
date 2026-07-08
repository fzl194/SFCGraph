---
id: UNC@20.15.2@MMLCommand@ADD ARPRANGE
type: MMLCommand
name: ADD ARPRANGE（增加ARP策略范围配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: ARPRANGE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 差异化服务配置
status: active
---

# ADD ARPRANGE（增加ARP策略范围配置）

## 功能

**适用网元：SGSN**

该命令用于配置ARP策略实施的用户范围。

## 注意事项

- 本命令中引用的ARP策略数据需要先在[**ADD ARPPARA**](../../../QoS管理/Pre-R8 QoS/QoS应用/ARP转换/增加ARP策略参数配置(ADD ARPPARA)_72225903.md)命令中配置完毕，才能在本命令中引用。
- 此命令的最大记录数为1024。
- 如果IMSI前缀的组合同时匹配到多条记录，“IMSI前缀”长度不相等时，使用“IMSI前缀”最长匹配的记录。例如用户123030000000001，在表1所示场景下，匹配到记录2。
  *表1 示例*

  | 记录 | IMSI前缀 | ARP策略组 | ARP策略组 |
  | --- | --- | --- | --- |
  | 记录1 | 12303 | G1(自定义组1) | G1(自定义组1) |
  | 记录2 | 123030000000001 | G2(自定义组2) | G2(自定义组2) |

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进行匹配的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>数据来源：整网规划<br>取值范围：1~15位字符串<br>默认值：无 |
| GROUPID | ARP策略组 | 可选必选说明：必选参数<br>参数含义：用于指定用户群使用的ARP策略组。<br>数据来源：整网规划<br>取值范围：<br>- “G1(自定义组1)”<br>- “G2(自定义组2)”<br>- “G3(自定义组3)”<br>- “G4(自定义组4)”<br>- “G5(自定义组5)”<br>- “G6(自定义组6)”<br>- “G7(自定义组7)”<br>- “G8(自定义组8)”<br>- “G9(自定义组9)”<br>配置原则：<br>- 必须先在[**ADD ARPPARA**](../../../QoS管理/Pre-R8 QoS/QoS应用/ARP转换/增加ARP策略参数配置(ADD ARPPARA)_72225903.md)中已经配置了有效的ARP策略组才能被引用，否则配置会添加失败。<br>默认值：无<br>说明：- 一个完整的ARP策略组：由用户级别和业务级别确定，总共有21条记录，详细参见[**ADD ARPPARA**](../../../QoS管理/Pre-R8 QoS/QoS应用/ARP转换/增加ARP策略参数配置(ADD ARPPARA)_72225903.md)。<br>- 针对当前用户范围内的用户，如果“自定义组”的ARP策略记录没有配置完整，那么系统针对未配置完整的ARP策略部分使用“系统缺省组”中的ARP策略。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：用于设置本条记录的配置描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [ARP策略范围配置（ARPRANGE）](configobject/UNC/20.15.2/ARPRANGE.md)

## 使用实例

*表2 系统预先设置值*

| ARP策略组 | 用户级别 | 业务级别 | 承载优先级 | 抢占性 | 被抢占性 | 排队属性 |
| --- | --- | --- | --- | --- | --- | --- |
| G1(自定义组1) | 高端用户 | Conversation | 4 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 高端用户 | StreamingGBRMore25Kbps | 5 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 高端用户 | StreamingGBRLess24Kbps | 5 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 高端用户 | InteractiveTrafficPri1 | 6 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 高端用户 | InteractiveTrafficPri2 | 6 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 高端用户 | InteractiveTrafficPri3 | 6 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 高端用户 | Background | 7 | 可能触发抢占 | 不允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | Conversation | 7 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | StreamingGBRMore25Kbps | 8 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | StreamingGBRLess24Kbps | 8 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | InteractiveTrafficPri1 | 9 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | InteractiveTrafficPri2 | 9 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | InteractiveTrafficPri3 | 9 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 普通用户 | Background | 10 | 可能触发抢占 | 允许抢占 | 允许排队 |
| G1(自定义组1) | 低端用户 | Conversation | 10 | 不触发抢占 | 允许抢占 | 不允许排队 |
| G1(自定义组1) | 低端用户 | StreamingGBRMore25Kbps | 11 | 不触发抢占 | 允许抢占 | 不允许排队 |
| G1(自定义组1) | 低端用户 | StreamingGBRLess24Kbps | 11 | 不触发抢占 | 允许抢占 | 不允许排队 |
| G1(自定义组1) | 低端用户 | InteractiveTrafficPri1 | 12 | 不触发抢占 | 允许抢占 | 不允许排队 |
| G1(自定义组1) | 低端用户 | InteractiveTrafficPri2 | 12 | 不触发抢占 | 允许抢占 | 不允许排队 |
| G1(自定义组1) | 低端用户 | InteractiveTrafficPri3 | 12 | 不触发抢占 | 允许抢占 | 不允许排队 |
| G1(自定义组1) | 低端用户 | Background | 13 | 不触发抢占 | 允许抢占 | 不允许排队 |

1. 如表1，已经通过 [**ADD ARPPARA**](../../../QoS管理/Pre-R8 QoS/QoS应用/ARP转换/增加ARP策略参数配置(ADD ARPPARA)_72225903.md) 命令完成了自定义策略组G1的配置，针对IMSI前缀为123030000000001用户选择G1策略组的ARP策略配置。
  ADD ARPRANGE: IMSIPRE="123030000000001", GROUPID=G1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加ARP策略范围配置(ADD-ARPRANGE)_26145672.md`
