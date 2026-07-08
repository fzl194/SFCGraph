# 查询会话管理的PDP上下文数（DSP SMPDPNUM）

- [命令功能](#ZH-CN_MMLREF_0209653799__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653799__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653799__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653799__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653799__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653799)

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查看SMF/PGW-C/SGW-C/GGSN-C的PDP上下文数、承载上下文、QFI上下文。

## [注意事项](#ZH-CN_MMLREF_0209653799)

- “查询分类”参数不输入时，表示查询汇总的信息。
- 在本命令中，指定查询条件指的是指定查询范围（ALL_POD_INFO、SPECIFIED_POD_INFO）。例如：指定查询条件的PGW-C上激活的5G承载上下文数，指的是查询范围（ALL_POD_INFO、SPECIFIED_POD_INFO）的PGW-C上激活的5G承载上下文数。

#### [操作用户权限](#ZH-CN_MMLREF_0209653799)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653799)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRY_SCOPE | 查询范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询PDP上下文的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以pod粒度呈现<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。<br>默认值：SUMMARY<br>配置原则：无 |
| QRY_CLASS | 查询分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询PDP上下文的分类条件。<br>数据来源：本端规划<br>取值范围：<br>- “APN（APN）”：查询使用该APN激活的当前在线PDP上下文数。<br>- “IMS（IMS）”：查询当前在线的IMS会话的PDP上下文数。<br>- “RAT（无线接入类型）”：查询不同无线接入类型的PDP上下文数目。<br>- “UPF（UPF）”：查询使用该UPF激活的当前在线PDP上下文数。<br>- “SNSSAI（SNSSAI）”：查询使用该切片的QFI上下文数。<br>- “SSC1_MODE（SSC1模式）”：查询SSC1模式用户的QFI上下文数。<br>- “SSC2_MODE（SSC2模式）”：查询SSC2模式用户的QFI上下文数。<br>- “SSC3_MODE（SSC3模式）”：查询SSC3模式用户的QFI上下文数。<br>- “ULCL（上行分类）”：查询ULCL会话用户的QFI上下文数。<br>- “IPV6_MULTIHOMING（IPv6多出口）”：查询IPv6多出口会话用户的QFI上下文数。<br>- “NSA（NSA）”：非独立组网，指以现有的LTE无线接入和核心网作为移动性管理和覆盖的锚点，新增5G接入的组网方式。<br>- “UEIPALLOCBYUPF（UPF分配UE地址）”：查询UPF分配UE地址的PDP上下文数。<br>- “UEIPALLOCBYSUBS（签约数据指定UE地址）”：查询签约数据指定UE地址的PDP上下文数。<br>- “UEIPALLOCBYLOCAL（本地分配UE地址）”：查询本地分配UE地址的PDP上下文数。<br>- “CHG_OFFLINE（离线计费）”：查询离线计费的PDP上下文数。<br>- “CHG_ONLINE（在线计费）”：查询在线计费的PDP上下文数。<br>- “CHG_FBC（内容计费）”：查询内容计费的会话上下文数。<br>- “DYNC_PCC（动态PCC）”：查询动态PCC的PDP上下文数。<br>- “LOCAL_PCC（本地PCC）”：查询本地PCC的PDP上下文数。<br>- “CHG_CONVERGED（融合计费）”：查询融合计费的会话上下文数。<br>- “SUMMARY（汇总信息）”：查询所有类型的汇总会话数信息。<br>- “SUSPEND（挂起状态）”：查询suspend状态上下文数。<br>- “NON_IP（Non-IP）”：查询激活的Non-IP用户上下文数。<br>- “L2TP（L2TP）”：查询当前在线的L2TP用户的PDP上下文数。<br>- “NW5GNSA（5G NSA 网络）”：查询具备5G能力的上下文数及使用了5G网络的上下文数。<br>- “ALIASAPN（别名APN）”：查询使用该别名APN激活的当前在线PDP上下文数。<br>- “CHARGING（计费方式）”：指定APN下按照计费方式查看当前在线上下文数。<br>- “IP_ALLOCATION（IP分配方式）”：指定APN下按照IP地址分配方式查看当前在线上下文数。<br>- “FWA（FWA）”：查询当前在线的FWA用户的PDP上下文数。<br>- “CHG_ONLINETOOFFLINE（在线计费转离线计费）”：查询在线计费转离线计费的PDP上下文数。<br>默认值：SUMMARY<br>配置原则：<br>本参数不输入时，表示查询汇总的信息。 |
| APN | APN | 可选必选说明：该参数在"QRY_CLASS"配置为"APN"、"CHARGING"、"IP_ALLOCATION"时为条件必选参数。<br>参数含义：该参数用于指定APN。使用用户请求的APN对应的上报属性中“上报给话统的APN名”参数的取值，即在SET APNREPORTATTR命令中设置的该APN的PERFORMANCE的取值，指定使用用户请求的APN还是真实的APN进行统计。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。 |
| RAT | 无线接入类型 | 可选必选说明：该参数在"QRY_CLASS"配置为"RAT"时为条件必选参数。<br>参数含义：该参数用于指定RAT。<br>数据来源：全网规划<br>取值范围：<br>- “UTRAN（UTRAN）”：通用陆地无线接入网。<br>- “GERAN（GERAN）”：GSM/EDGE无线接入网。<br>- “EUTRAN（EUTRAN）”：演进型通用陆地无线接入网。<br>- “NGRAN（NGRAN）”：5G无线接入网。<br>- “EUTRAN_NB_IOT（EUTRAN-NB-IOT）”：演进型通用陆地无线接入网-窄带物联网。<br>- “WLAN（WLAN）”：无线局域网<br>- “LTE_M（LTE_M）”：演进的高速包数据网络<br>- “REDCAP（REDCAP）”：轻量化5G<br>默认值：无<br>配置原则：无 |
| UPF_NAME | UPF名称 | 可选必选说明：该参数在"QRY_CLASS"配置为"UPF"时为条件必选参数。<br>参数含义：该参数用于指定UPF名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| SST | 切片/服务类型 | 可选必选说明：该参数在"QRY_CLASS"配置为"SNSSAI"时为条件必选参数。<br>参数含义：该参数用于指定切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| POD_ID | POD名称 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_POD_INFO"时为条件必选参数。<br>参数含义：该参数用于指定POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：该参数在"QRY_CLASS"配置为"SNSSAI"时为条件可选参数。<br>参数含义：本参数用于指定切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~8。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| ALIASAPN | 别名APN | 可选必选说明：该参数在"QRY_CLASS"配置为"ALIASAPN"时为条件必选参数。<br>参数含义：该参数用于指定APN别名。表示查询使用该别名APN激活的PDP上下文数，该别名APN所对应的真实APN必须在系统上已经配置。如果输入真实APN，则显示与真实APN相关联的所有别名APN上的PDP上下文数。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。 |

## [使用实例](#ZH-CN_MMLREF_0209653799)

查询整系统的PDP上下文、承载上下文、QFI上下文数量。

```
%%DSP SMPDPNUM: QRY_SCOPE=SUMMARY, QRY_CLASS=SUMMARY;%%
RETCODE = 0  操作成功

结果如下
--------
                               查询分类  =  汇总信息
                      GTPv1 PDP上下文数  =  0
         PGW-C上激活的GTPv2承载上下文数  =  0
         SGW-C上激活的GTPv2承载上下文数  =  0
       S/PGW-C上激活的GTPv2承载上下文数  =  1
     N16/N16a接口SMF上激活的QFI上下文数  =  0
         I-SMF/V-SMF上激活的QFI上下文数  =  0
          N11接口SMF上激活的QFI上下文数  =  0
 N11接口MultiDNN SMF上激活的QFI上下文数  =  0
      MultiDNN I-SMF上激活的QFI上下文数  =  0
                    GTPv2承载上下文总数  =  1
                          QFI上下文总数  =  0
GGSN-C上激活的信令代理用户PDP上下文总数  =  0
PGW-C上激活的信令代理用户承载上下文总数  =  0
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653799)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询范围 | 该参数用于指定查询PDP上下文的范围。<br>取值说明：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以pod粒度呈现<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。 |
| 查询分类 | 该参数用于指定查询PDP上下文的分类条件。<br>取值说明：<br>- “APN（APN）”：查询使用该APN激活的当前在线PDP上下文数。<br>- “IMS（IMS）”：查询当前在线的IMS会话的PDP上下文数。<br>- “RAT（无线接入类型）”：查询不同无线接入类型的PDP上下文数目。<br>- “UPF（UPF）”：查询使用该UPF激活的当前在线PDP上下文数。<br>- “SNSSAI（SNSSAI）”：查询使用该切片的QFI上下文数。<br>- “SSC1_MODE（SSC1模式）”：查询SSC1模式用户的QFI上下文数。<br>- “SSC2_MODE（SSC2模式）”：查询SSC2模式用户的QFI上下文数。<br>- “SSC3_MODE（SSC3模式）”：查询SSC3模式用户的QFI上下文数。<br>- “ULCL（上行分类）”：查询ULCL会话用户的QFI上下文数。<br>- “IPV6_MULTIHOMING（IPv6多出口）”：查询IPv6多出口会话用户的QFI上下文数。<br>- “NSA（NSA）”：非独立组网，指以现有的LTE无线接入和核心网作为移动性管理和覆盖的锚点，新增5G接入的组网方式。<br>- “UEIPALLOCBYUPF（UPF分配UE地址）”：查询UPF分配UE地址的PDP上下文数。<br>- “UEIPALLOCBYSUBS（签约数据指定UE地址）”：查询签约数据指定UE地址的PDP上下文数。<br>- “UEIPALLOCBYLOCAL（本地分配UE地址）”：查询本地分配UE地址的PDP上下文数。<br>- “CHG_OFFLINE（离线计费）”：查询离线计费的PDP上下文数。<br>- “CHG_ONLINE（在线计费）”：查询在线计费的PDP上下文数。<br>- “CHG_FBC（内容计费）”：查询内容计费的会话上下文数。<br>- “DYNC_PCC（动态PCC）”：查询动态PCC的PDP上下文数。<br>- “LOCAL_PCC（本地PCC）”：查询本地PCC的PDP上下文数。<br>- “CHG_CONVERGED（融合计费）”：查询融合计费的会话上下文数。<br>- “SUMMARY（汇总信息）”：查询所有类型的汇总会话数信息。<br>- “SUSPEND（挂起状态）”：查询suspend状态上下文数。<br>- “NON_IP（Non-IP）”：查询激活的Non-IP用户上下文数。<br>- “L2TP（L2TP）”：查询当前在线的L2TP用户的PDP上下文数。<br>- “NW5GNSA（5G NSA 网络）”：查询具备5G能力的上下文数及使用了5G网络的上下文数。<br>- “ALIASAPN（别名APN）”：查询使用该别名APN激活的当前在线PDP上下文数。<br>- “CHARGING（计费方式）”：指定APN下按照计费方式查看当前在线上下文数。<br>- “IP_ALLOCATION（IP分配方式）”：指定APN下按照IP地址分配方式查看当前在线上下文数。<br>- “FWA（FWA）”：查询当前在线的FWA用户的PDP上下文数。<br>- “CHG_ONLINETOOFFLINE（在线计费转离线计费）”：查询在线计费转离线计费的PDP上下文数。 |
| 无线接入类型 | 该参数用于指定RAT。<br>取值说明：<br>- “UTRAN（UTRAN）”：通用陆地无线接入网。<br>- “GERAN（GERAN）”：GSM/EDGE无线接入网。<br>- “EUTRAN（EUTRAN）”：演进型通用陆地无线接入网。<br>- “NGRAN（NGRAN）”：5G无线接入网。<br>- “EUTRAN_NB_IOT（EUTRAN-NB-IOT）”：演进型通用陆地无线接入网-窄带物联网。<br>- “WLAN（WLAN）”：无线局域网<br>- “LTE_M（LTE_M）”：演进的高速包数据网络<br>- “REDCAP（REDCAP）”：轻量化5G |
| UPF名称 | 该参数用于指定UPF名称。 |
| 切片/服务类型 | 该参数用于指定切片/服务类型。 |
| POD名称 | 该参数用于指定POD名称。 |
| 切片区分码 | 本参数用于指定切片区分码。 |
| GTPv1 PDP上下文数 | 该参数表示整系统GGSN-C形态激活的GTPv1 PDP上下文数。 |
| PGW-C上激活的GTPv2承载上下文数 | 该参数表示整系统用户激活使用独立PGW-C的GTPv2承载上下文数。 |
| SGW-C上激活的GTPv2承载上下文数 | 该参数表示整系统用户激活使用独立SGW-C的GTPv2承载上下文数。 |
| S/PGW-C上激活的GTPv2承载上下文数 | 该参数表示整系统用户激活使用SGW-C/PGW-C合一的GTPv2承载上下文数。 |
| N16/N16a接口SMF上激活的QFI上下文数 | 该参数表示整系统用户激活使用独立N16/N16a接口SMF的QFI上下文数。当查询分类为NSA时，该参数表示从SGW-C、PGW-C或SGW-C/PGW-C切换到N16/N16a SMF的NSA上下文数。 |
| I-SMF/V-SMF上激活的QFI上下文数 | 该参数表示整系统用户激活使用独立I-SMF/V-SMF的QFI上下文数。当查询分类为NSA时，该参数表示从SGW-C、PGW-C或SGW-C/PGW-C切换到I-SMF/V-SMF的NSA上下文数。 |
| N11接口SMF上激活的QFI上下文数 | 该参数表示整系统用户激活使用N11接口SMF的QFI上下文数。当查询分类为NSA时，该参数表示从SGW-C、PGW-C或SGW-C/PGW-C切换到N11 SMF的NSA上下文数。 |
| GTPv2承载上下文总数 | 该参数表示整系统GTPv2承载上下文总数，等于“PGW上激活的GTPv2承载上下文数”、“SGW上激活的GTPv2承载上下文数”、“S/PGW上激活的GTPv2承载上下文数”之和。 |
| QFI上下文总数 | 该参数表示整系统QFI上下文总数，等于“N16/N16a接口SMF上激活的QFI上下文数”、“I-SMF/V-SMF上激活的QFI上下文数”、“N11接口SMF上激活的QFI上下文数”、“N11接口MultiDNN SMF上激活的QFI上下文数”、“MultiDNN I-SMF上激活的QFI上下文数”之和。 |
| 指定查询条件的GTPv1 PDP上下文数 | 该参数表示满足查询条件的GGSN-C形态激活的GTPv1 PDP上下文数。 |
| 指定查询条件的PGW-C上激活的GTPv2承载上下文数 | 该参数表示满足查询条件的用户激活使用独立PGW-C的GTPv2承载上下文数。 |
| 指定查询条件的SGW-C上激活的GTPv2承载上下文数 | 该参数表示满足查询条件的用户激活使用独立SGW-C的GTPv2承载上下文数。 |
| 指定查询条件的S/PGW-C上激活的GTPv2承载上下文数 | 该参数表示满足查询条件的用户激活使用SGW-C/PGW-C合一的GTPv2承载上下文数。 |
| 指定查询条件的N16/N16a接口SMF上激活的QFI上下文数 | 该参数表示满足查询条件的用户激活使用N16/N16a接口SMF的QFI上下文数。当查询分类为NSA时，该参数表示指定条件下从SGW-C、PGW-C或SGW-C/PGW-C切换到N16/N16a SMF的NSA上下文数。 |
| 指定查询条件的I-SMF/V-SMF上激活的QFI上下文数 | 该参数表示满足查询条件的用户激活使用独立I-SMF/V-SMF的QFI上下文数。当查询分类为NSA时，该参数表示指定条件下从SGW-C、PGW-C或SGW-C/PGW-C切换到I-SMF/V-SMF的NSA上下文数。 |
| 指定查询条件的N11接口SMF上激活的QFI上下文数 | 该参数表示满足查询条件的用户激活使用N11接口SMF的QFI上下文数。当查询分类为NSA时，该参数表示指定条件下从SGW-C、PGW-C或SGW-C/PGW-C切换到N11 SMF的NSA上下文数。 |
| 指定查询条件的GTPv2承载上下文总数 | 该参数表示满足查询条件的GTPv2承载上下文总数，等于“指定查询条件的PGW-C上激活的GTPv2承载上下文数”、“指定查询条件的SGW-C上激活的GTPv2承载上下文数”、“指定查询条件的S/PGW-C上激活的GTPv2承载上下文数”之和。 |
| 指定查询条件的QFI上下文总数 | 该参数表示满足查询条件的QFI上下文总数，等于“指定查询条件的N16/N16a接口SMF上激活的QFI上下文数”、“指定查询条件的I-SMF/V-SMF上激活的QFI上下文数”、“指定查询条件的N11接口SMF上激活的QFI上下文数”、“指定查询条件的N11接口MultiDNN SMF上激活的QFI上下文数”、“指定查询条件的MultiDNN I-SMF上激活的QFI上下文数”之和。 |
| SGW上报过5G流量的承载上下文数 | 该参数表示SGW上报过5G流量的承载上下文数。 |
| PGW上报过5G流量的承载上下文数 | 该参数表示PGW上报过5G流量的承载上下文数。 |
| SPGW上报过5G流量的承载上下文数 | 该参数表示S/PGW上报过5G流量的承载上下文数。 |
| GGSN-C上激活的信令代理用户PDP上下文总数 | 该参数表示在GGSN-C上激活的信令代理用户PDP上下文总数。 |
| PGW-C上激活的信令代理用户承载上下文总数 | 该参数表示在PGW-C上激活的信令代理用户承载上下文总数。 |
| 指定查询条件的GGSN-C上激活的信令代理用户PDP上下文总数 | 该参数表示指定查询条件的GGSN-C上激活的信令代理用户PDP上下文总数。 |
| 指定查询条件的PGW-C上激活的信令代理用户承载上下文总数 | 该参数表示指定查询条件的PGW-C上激活的信令代理用户承载上下文总数。 |
| SGW-C上激活的5G承载上下文数 | 该参数表示SGW-C上激活的5G承载上下文数。 |
| PGW-C上激活的5G承载上下文数 | 该参数表示PGW-C上激活的5G承载上下文数。 |
| S/PGW-C上激活的5G承载上下文数 | 该参数表示S/PGW-C上激活的5G承载上下文数。 |
| 指定查询条件的SGW-C上激活的5G承载上下文数 | 该参数表示指定查询条件的SGW-C上激活的5G承载上下文数。 |
| 指定查询条件的PGW-C上激活的5G承载上下文数 | 该参数表示指定查询条件的PGW-C上激活的5G承载上下文数。 |
| 指定查询条件的S/PGW-C上激活的5G承载上下文数 | 该参数表示指定查询条件的S/PGW-C上激活的5G承载上下文数。 |
| 指定查询条件的SGW-C上报过5G流量的承载上下文数 | 该参数表示指定查询条件的SGW-C上报过5G流量的承载上下文数。 |
| 指定查询条件的PGW-C上报过5G流量的承载上下文数 | 该参数表示指定查询条件的PGW-C上报过5G流量的承载上下文数。 |
| 指定查询条件的S/PGW-C上报过5G流量的承载上下文数 | 该参数表示指定查询条件的S/PGW-C上报过5G流量的承载上下文数。 |
| POD版本号信息 | 该参数用于指定POD版本号。非灰度升级期间，该参数不显示。 |
| N11接口MultiDNN SMF上激活的QFI上下文数 | 该参数表示整系统用户激活使用MultiDNN N11接口SMF的QFI上下文数。 |
| MultiDNN I-SMF上激活的QFI上下文数 | 该参数表示整系统用户激活使用MultiDNN I-SMF的QFI上下文数。 |
| 指定查询条件的N11接口MultiDNN SMF上激活的QFI上下文数 | 该参数表示满足查询条件的用户激活使用MultiDNN 11接口SMF的QFI上下文数。 |
| 指定查询条件的MultiDNN I-SMF上激活的QFI上下文数 | 该参数表示满足查询条件的用户激活使用MultiDNN I-SMF的QFI上下文数。 |
| 指定APN当前在线的本地地址分配方式上下文数 | 该参数用于查询指定APN当前在线的本地地址分配方式上下文数。 |
| 指定APN当前在线的静态地址分配方式上下文数 | 该参数用于查询指定APN当前在线的静态地址分配方式上下文数。 |
| 指定APN当前在线的Radius地址分配方式上下文数 | 该参数用于查询指定APN当前在线的Radius地址分配方式上下文数。 |
| 指定APN当前在线的DHCP地址分配方式上下文数 | 该参数用于查询指定APN当前在线的Dhcp地址分配方式上下文数。 |
| 指定APN当前在线的LNS地址分配方式上下文数 | 该参数用于查询指定APN当前在线的Lns地址分配方式上下文数。 |
| 指定APN当前在线的在线计费方式上下文数 | 该参数用于查询指定APN当前在线的在线计费方式上下文数。 |
| 指定APN当前在线的离线计费方式上下文数 | 该参数用于查询指定APN当前在线的离线计费方式上下文数。 |
