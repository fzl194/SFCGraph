---
id: UNC@20.15.2@MMLCommand@RMV IUACCAREALST
type: MMLCommand
name: RMV IUACCAREALST（删除Iu模式区域漫游限制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IUACCAREALST
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 区域漫游限制管理
- Iu模式区域漫游限制参数
status: active
---

# RMV IUACCAREALST（删除Iu模式区域漫游限制参数）

## 功能

**适用网元：SGSN**

该命令用于删除Iu模式区域漫游限制参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREA | 区域范围 | 可选必选说明：必选参数<br>参数含义：待删除的区域范围。<br>取值范围：<br>- “AG(区域组)”：表示该区域标识类型为区域组。<br>- “LA(指定位置区)”：表示该区域标识类型为指定位置区。<br>- “RA(指定路由区)”：表示该区域标识类型为指定路由区。<br>- “OTHER(其他)”：表示该区域标识类型为其他。<br>默认值：无<br>说明：- 区域范围表示进行接入控制所适用的位置区域。<br>- 区域范围按照粒度从粗到细分为以下几个级别： 区域组，指定位置区，指定路由区，其他。<br>- 相同粒度区域范围的各记录的区域范围不能交迭。<br>- 使用时先按照位置区域查找记录，然后按照用户的IMSI查找是否存在对应记录，查找不到再使用较粗的区域粒度进行查找。<br>- 未配置在该表区域范围中的用户缺省允许接入。 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：待删除的移动国家代码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时，才需要配置。<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：待删除的移动网号。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时，才需要配置。<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：待删除的位置区域码。<br>前提条件：<br>“AREA(区域范围)”<br>参数设置为<br>“LA(位置区)”<br>或<br>“RA(路由区)”<br>时，才需要配置。<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：待删除的路由区域码。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“RA(路由区)”<br>时，才需要配置。<br>取值范围：0x00～0xFF<br>默认值：无 |
| AREAID | 区域群标识 | 可选必选说明：条件必选参数<br>参数含义：待删除用户的区域群标识。<br>前提条件：该参数在<br>“AREA(区域范围)”<br>参数设置为<br>“AG(区域组)”<br>时，才需要配置。<br>取值范围：1～50<br>默认值：无<br>说明：该区域ID必须已经通过<br>[**ADD AREAGP**](../区域群管理/增加区域群(ADD AREAGP)_26145542.md)<br>命令添加成功，且在区域群成员表中的记录对应的IDTYPE只能为LA或RA。可执行<br>[**LST AREAGP**](../区域群管理/查询区域群(LST AREAGP)_72345141.md)<br>进行查看。 |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：待删除的用户范围。<br>取值范围：<br>- “ALL_USER(所有用户)”：表示用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “USER_GROUP(用户群)”：表示用户范围为用户群。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>- “UE_TYPE(终端类型)”：保留，暂未实现。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：待删除用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位的十进制数字<br>默认值：无<br>说明：- 支持IMSI最长匹配的查询方式。<br>- 该参数在用户群成员管理配置中不能存在对应记录，可执行[**LST SUBGPMEM**](../用户群成员管理/查询用户群成员(LST SUBGPMEM)_26145564.md)进行查看。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，对该IMSI所在的号段进行删除。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>参数设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>取值范围：1～15位的十进制数字<br>默认值：无 |
| SUBID | 用户群标识 | 可选必选说明：条件必选参数<br>参数含义：待删除的用户群标识。<br>前提条件：该参数在<br>“SUBRANGE(用户范围)”<br>设置<br>“USER_GROUP(用户群)”<br>时，才需要配置。<br>取值范围：1～100<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IUACCAREALST]] · Iu模式区域漫游限制参数（IUACCAREALST）

## 使用实例

删除一条Iu模式区域漫游限制参数记录，区域范围为区域组，区域群标识为1：

RMV IUACCAREALST: AREA=AG, AREAID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IUACCAREALST.md`
