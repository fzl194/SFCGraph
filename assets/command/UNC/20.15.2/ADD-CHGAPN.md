---
id: UNC@20.15.2@MMLCommand@ADD CHGAPN
type: MMLCommand
name: ADD CHGAPN（增加APN计费属性）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGAPN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- APN计费属性
status: active
---

# ADD CHGAPN（增加APN计费属性）

## 功能

**适用网元：SGSN**

该命令用于当要求忽略HLR签约的APN计费属性时（通过命令 [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 设置参数 “IGNOREFLG” 的取值），配置基于APN的计费属性信息。

## 注意事项

- 该命令执行后立即生效，但该配置只对之后激活的用户有效。
- 本表最大记录数为1000。
- 各记录的APNNI字段不能重复。
- S-CDR中填写的计费属性按照如下的优先等级进行选择：
    1. 通过 [**LST CHGGNCCCFG**](../Gn接口计费属性选择策略配置/查询Gn接口计费属性选择策略(LST CHGGNCCCFG)_26305186.md) 查看按照用户的IMSI匹配上的 “SPECIAL_USER(指定用户)” 的记录，如果没有匹配的 “SPECIAL_USER(指定用户)” 的记录则查看 “ALL_USER(所有用户)” 的记录，其中的 “S-CDR中的计费属性” 参数取值如果为是，则表示S-CDR中填写的计费属性必须与发送给GGSN的计费属性保持一致，否则按本优先级列表选择下一项。
    2. APN级签约数据中的计费属性，可通过 [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 命令的 “IGNOREFLG” 参数配置忽略APN级签约计费属性。如果根据 “IGNOREFLG” 参数的取值，该用户忽略APN级签约计费属性，则按本优先级列表选择下一项。如果HLR中该用户未签约APN级计费属性，或该用户签约的APN级计费属性为无效值，也按本优先级列表选择下一项。
    3. 忽略APN级签约计费属性情况下， [**ADD CHGAPN**](增加APN计费属性(ADD CHGAPN)_72344965.md) 命令配置的计费属性，通过 [**LST CHGAPN**](查询APN计费属性(LST CHGAPN)_26305180.md) 命令查看。如果该PDP的APNNI没有对应的配置，则按本优先级列表选择下一项。
    4. 用户级签约数据中的计费属性，可通过 [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 命令的 “IGNOREFLG” 参数配置忽略用户级签约计费属性。如果根据 “IGNOREFLG” 参数的取值，该用户忽略用户级签约计费属性，则按本优先级列表选择下一项。如果HLR中该用户未签约用户级计费属性，或该用户签约的用户级计费属性为无效值，也按本优先级列表选择下一项。
    5. 不忽略APN级签约计费属性情况下， [**ADD CHGAPN**](增加APN计费属性(ADD CHGAPN)_72344965.md) 命令配置的计费属性，通过 [**LST CHGAPN**](查询APN计费属性(LST CHGAPN)_26305180.md) 命令查看，如果该PDP的APNNI没有对应的配置，则按本优先级列表选择下一项。
    6. [**ADD CHGDCHAR**](../缺省计费属性参数配置/增加缺省计费属性参数(ADD CHGDCHAR)_26145380.md) 命令配置的计费属性，此命令只对外网用户生效，包括漫游用户和拜访用户。通过 [**LST CHGDCHAR**](../缺省计费属性参数配置/查询缺省计费属性参数(LST CHGDCHAR)_26305196.md) 命令查看，如果按照用户类型、移动国家码、移动网号，该外网用户没有对应的配置，则按本优先级列表选择下一项。
    7. [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 命令配置的计费属性。
-
  M-CDR中填写的计费属性按照如下的优先等级进行选择：

  1. 用户级签约数据中的计费属性，可通过 [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 命令的 “IGNOREFLG” 参数配置忽略用户级签约计费属性。如果根据 “IGNOREFLG” 参数的取值，该用户忽略用户级签约计费属性，则按本优先级列表选择下一项。如果HLR中该用户未签约用户级计费属性，或该用户签约的用户级计费属性为无效值，也按本优先级列表选择下一项。
    2. [**ADD CHGDCHAR**](../缺省计费属性参数配置/增加缺省计费属性参数(ADD CHGDCHAR)_26145380.md) 命令配置的计费属性，此命令只对外网用户生效，包括漫游用户和拜访用户。通过 [**LST CHGDCHAR**](../缺省计费属性参数配置/查询缺省计费属性参数(LST CHGDCHAR)_26305196.md) 命令查看，如果按照用户类型、移动国家码、移动网号，该外网用户没有对应的配置，则按本优先级列表选择下一项。
    3. [**SET CHGCDR**](../计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md) 命令配置的计费属性。
- SGSN发送给GGSN的计费属性由CHGGNCCCFG配置进行控制，请参考 [**ADD CHGGNCCCFG**](../Gn接口计费属性选择策略配置/增加Gn接口计费属性选择策略(ADD CHGGNCCCFG)_72344971.md) 。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>说明：按照3GPP协议，APN网络标识不区分大小写。为统一格式起见，APN网络标识的字母部分全部以大写格式保存。 |
| CC | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当忽略HLR签约的APN计费属性时，应该对该APN的用户按何种计费方式收费。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL(普通计费)”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付费用。<br>- “PREPAID(预付费)”：表示预付费计费属性，按照此种方式计费的用户在获取某种服务之前需要预支付一定的费用。<br>- “FLATRATE(包月制)”：表示包月制计费属性，按照此种方式计费的用户在一个月内的收费是固定的。<br>- “HOTBILLING(实时计费)”：表示实时计费属性，按照此种方式计费的用户将在短时间或流量达到某个值时及时生成话单，保证运营商对此类用户及时收费。<br>默认值：<br>“NORMAL(普通计费)” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGAPN]] · APN计费属性（CHGAPN）

## 关联任务

- [[UNC@20.15.2@Task@0-00016]]

## 使用实例

配置APNNI为"huawei1.com"的用户的计费属性为预付费：

ADD CHGAPN: APNNI="huawei1.com", CC=PREPAID;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN计费属性(ADD-CHGAPN)_72344965.md`
