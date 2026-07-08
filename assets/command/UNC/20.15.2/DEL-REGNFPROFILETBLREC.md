---
id: UNC@20.15.2@MMLCommand@DEL REGNFPROFILETBLREC
type: MMLCommand
name: DEL REGNFPROFILETBLREC（删除注册NF的Profile表记录）
nf: UNC
version: 20.15.2
verb: DEL
object_keyword: REGNFPROFILETBLREC
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF维测管理
status: active
---

# DEL REGNFPROFILETBLREC（删除注册NF的Profile表记录）

## 功能

![](删除注册NF的Profile表记录（DEL REGNFPROFILETBLREC）_09651506.assets/notice_3.0-zh-cn_2.png)

该命令将会删除注册NF的Profile表记录，错误执行后导致网元信息缺失。

**适用NF：NRF**

该命令用于删除注册到NRF上的NF的profile表记录，NF Profile在NRF上会分表存储，当确认NRF中存储的NF的Profile信息异常或者冗余影响周边网元业务异常时，可使用该命令删除NF的Profile表记录。为防止误删，该命令需要专业维护人员确认后才可执行，具体NF的Profile表信息可以通过DSP NGCOMMONDBG命令查询。

## 注意事项

- 该命令执行后立即生效。

- 主备场景下，只需在主NRF上执行；双活场景下，只需在其中一个NRF上执行即可。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| TABLENAME | 表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示存储NF Profile相关信息的表名称。<br>数据来源：本端规划<br>取值范围：<br>- TBL_NFPROFILE（表NFPROFILE）<br>- “TBL_IMSINUMRANGES（表IMSINUMRANGES）”：IMSI号段表，存储NF Profile中的Supi号段。<br>- “TBL_MSISDNNUMRANGES（表MSISDNNUMRANGES）”：MSISDN号段表，存储NF Profile中的Gpsi号段。<br>- “TBL_IPV4ADDRRANGES（表IPV4ADDRRANGES）”：IPv4段表，存储/NF Profile/bsfInfo中的IPv4号段。<br>- “TBL_IPV6PREFIXRANGES（表IPV6PREFIXRANGES）”：IPv6前缀段表，存储/NF Profile/bsfInfo中的IPv6前缀号段。<br>- “TBL_DNNLIST（表DNNLIST）”：DnnList表，存储NFProfile中的DnnList、sNssaiSmfInfoList、sNssaiUpfInfoList信息。<br>- “TBL_TAILIST（表TBL_TAILIST）”：TaiList表，存储NF Profile中taiList信息。<br>- “TBL_TAIRANGELIST（表TAIRANGELIST）”：TaiRangleLis表，存储NF Profile中taiRangleList信息。<br>- “TBL_NFIDNFTYPEMAP（表NFIDNFTYPEMAP）”：NfIdNfTypeMap表，存储nfInstanceId和nfType的映射关系。<br>- “TBL_IPDOMAIN（表IPDOMAIN）”：IpDomainList表，存储/NF Profile/bsfInfo中的ipDomainList信息。<br>- “TBL_ALLMATCHFLAG（表ALLMATCHFLAG）”：AllMatchFlag表，存储NF Profile表中部分可选数组类字段是否需要发现时全匹配的标记。<br>- “TBL_EXTGRPIDRANGES（表EXTGRPIDRANGES）”：ExtGroupIdRanges表，存储NF Profile中externalGroupIdentifiersRanges信息。<br>- “TBL_NFADDITIONALINFO（表NFADDITIONALINFO）”：NFADDITIONALINFO表，存储NF附加信息，包含接入客户端地址、接入NRF标识等。<br>- “TBL_NFINFOIDXMAP（表NFINFOIDXMAP）”：NfInfoIdxMap表，存储NFInfo Map格式的Key，其中Key用做唯一标识NFInfo。<br>- “TBL_SCPIPV4ADDR（表SCPIPV4ADDR）”：存储NF Profile中ScpInfo字段ipv4Addresses信息。<br>- “TBL_SCPIPV4RANGE（表SCPIPV4RANGE）”：存储NF Profile中ScpInfo字段ipv4AddrRanges信息。<br>- “TBL_SCPIPV6PEFIX（表SCPIPV6PEFIX）”：存储NF Profile中ScpInfo字段ipv6Prefixes信息。<br>- “TBL_SCPIPV6RANGE（表SCPIPV6RANGE）”：存储NF Profile中ScpInfo字段ipv6PrefixRanges信息。<br>- “TBL_NFNSSAIS（表NFNSSAIS）”：存储NF Profile中sNssais的信息。<br>- “TBL_NFPERPLMNSNSSAIS（表NfPerPlmnSnssais）”：存储NF Profile中perPlmnSnssaiList信息。<br>- “TBL_SMFINFOLISTFIELD（表SmfInfoListField）”：存储NF Profile中SmfInfoList中各SmfInfo的字段信息，包含PgwFqdn，Accesstype，VsmfSupportInd，IsmfSupportInd字段，其中的TaiList，DnnList，TaiRangleLis信息分别可通过“TBL_TAILIST”，“TBL_DNNLIST”，“TBL_TAIRANGELIST”表名称删除。<br>- “TBL_NWDAFINFOLISTFIELD（表NwdafInfoListField）”：存储NF Profile中NwadfInfoList中各NwdafInfo的字段信息，包含NwdafEvents字段，其中的TaiList，TaiRangleLis信息分别可通过“TBL_TAILIST”，“TBL_TAIRANGELIST”表名称删除。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [注册NF的Profile表记录（REGNFPROFILETBLREC）](configobject/UNC/20.15.2/REGNFPROFILETBLREC.md)

## 使用实例

当NRF中NF Profile信息异常或者冗余时，使用该命令删除，删除NF实例标识为123e4567-e89b-12d3-a456-426655440000，表名称为NFPROFILE的记录：

```
DEL REGNFPROFILETBLREC: NFINSTANCEID="123e4567-e89b-12d3-a456-426655440000", TABLENAME=TBL_NFPROFILE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除注册NF的Profile表记录（DEL-REGNFPROFILETBLREC）_09651506.md`
