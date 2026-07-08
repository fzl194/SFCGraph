# 修改网络切片或DNN纠正配置（MOD LOCALNSDNN）

- [命令功能](#ZH-CN_MMLREF_0212701648__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0212701648__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0212701648__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0212701648__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0212701648)

**适用NF：AMF**

该命令用于修改为指定用户群配置的网络切片或DNN纠正信息。

## [注意事项](#ZH-CN_MMLREF_0212701648)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0212701648)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0212701648)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于表示用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>- “IMSI（指定IMSI）”：IMSI<br>默认值：无<br>配置原则：<br>对于指定的用户（群），策略匹配的优先级从高到低依次为：“IMSI(指定IMSI)”，“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| CORRECTTYPE | 纠正类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定纠正类型。<br>数据来源：全网规划<br>取值范围：<br>- “NS_CORRECTION（纠正网络切片）”：纠正网络切片<br>- “DNN_CORRECTION（纠正DNN）”：纠正DNN<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：该参数在"CORRECTTYPE"配置为"NS_CORRECTION"、"DNN_CORRECTION"时为条件必选参数。<br>参数含义：该参数用于表示组成纠正的网络切片的业务类型信息。网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识是可选的。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"CORRECTTYPE"配置为"NS_CORRECTION"、"DNN_CORRECTION"时为条件可选参数。<br>参数含义：该参数用于表示组成纠正的网络切片的细分标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CORRECTTYPE"配置为"DNN_CORRECTION"时为条件必选参数。<br>参数含义：该参数用于表示纠正的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| DNNPLCY | DNN纠正策略 | 可选必选说明：该参数在"CORRECTTYPE"配置为"DNN_CORRECTION"时为条件必选参数。<br>参数含义：该参数用于表示当UE请求携带的DNN与签约不匹配时，AMF对DNN的纠正策略：仅使用或优先使用AMF本地配置的DNN，还是优先使用签约中的default DNN。<br>数据来源：本端规划<br>取值范围：<br>- “Default_DNN_preferred（签约default DNN优先）”：优先使用签约中的default DNN<br>- “Only_The_Configured_DNN（仅本地配置DNN）”：仅尝试使用AMF本地配置的DNN<br>- “Configured_DNN_Preferred（本地配置DNN优先）”：优先使用AMF本地配置的DNN<br>默认值：无<br>配置原则：<br>当UE请求携带的DNN不在选择的切片签约范围之内，。<br>- 如果期望优先使用签约中的default DNN，则选择“Default_DNN_preferred”。该选择场景下，如果不存在签约的default DNN，那么AMF再尝试使用本地配置的DNN；<br>- 如果期望仅使用AMF本地配置的DNN，则选择“Only_The_Configured_DNN”。该选择场景下，如果配置的DNN也不在签约范围，那么AMF会拒绝UE的请求流程；<br>- 如果期望优先使用AMF本地配置的DNN，则选择“Configured_DNN_Preferred”。该选择场景下，如果配置的DNN也不在签约范围，那么AMF使用签约的default DNN。如果签约的default DNN也不存在，则从签约DNN中随机选择一个。 |
| DISFAILPLCY | SMF发现失败处理策略 | 可选必选说明：该参数在"CORRECTTYPE"配置为"DNN_CORRECTION"时为条件可选参数。<br>参数含义：该参数用于表示UE请求中携带DNN，并且匹配野卡签约数据，AMF未发现目标SMF时的处理策略。<br>数据来源：全网规划<br>取值范围：<br>- “STANDARD_MODEL（标准方式）”：不进行重试。<br>- “RETRY（重试）”：使用本地配置的DNN进行重试。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于描述纠正的网络切片或DNN，在运维中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## [使用实例](#ZH-CN_MMLREF_0212701648)

将本网用户的DNN纠正类型改成优先使用签约的default DNN，执行命令如下：

```
MOD LOCALNSDNN: SUBRANGE=HOME_USER, CORRECTTYPE=DNN_CORRECTION, SST=1, DNN="Huawei", DNNPLCY=Default_DNN_preferred;
```
