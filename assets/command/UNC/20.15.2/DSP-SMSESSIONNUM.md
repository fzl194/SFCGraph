---
id: UNC@20.15.2@MMLCommand@DSP SMSESSIONNUM
type: MMLCommand
name: DSP SMSESSIONNUM（显示会话管理的会话上下文数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SMSESSIONNUM
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 查询会话上下文数
status: active
---

# DSP SMSESSIONNUM（显示会话管理的会话上下文数）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查看SMF/PGW-C/SGW-C/GGSN-C的会话上下文数。

## 注意事项

“查询分类”参数不输入时，表示查询汇总的信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRY_SCOPE | 查询范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询会话上下文的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SUMMARY（汇总信息）”：查询汇总信息。以汇总方式呈现。<br>- “ALL_POD_INFO（所有POD信息）”：查询所有POD信息。以POD粒度呈现。<br>- “SPECIFIED_POD_INFO（指定POD信息）”：查询指定POD信息。<br>默认值：SUMMARY<br>配置原则：无 |
| QRY_CLASS | 查询分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询会话上下文的类型。<br>数据来源：本端规划<br>取值范围：<br>- “APN（APN）”：查询使用该APN激活的当前在线会话上下文数。<br>- “IMS（IMS）”：查询当前在线的IMS会话的会话上下文数。<br>- “RAT（无线接入类型）”：查询不同无线接入类型的会话上下文数目。<br>- “UPF（UPF）”：查询使用该UPF激活的当前在线会话上下文数。<br>- “SNSSAI（SNSSAI）”：查询使用该切片的5G会话上下文数。<br>- “SSC1_MODE（SSC1模式）”：查询SSC1模式用户的5G会话上下文数。<br>- “SSC2_MODE（SSC2模式）”：查询SSC2模式用户的5G会话上下文数。<br>- “SSC3_MODE（SSC3模式）”：查询SSC3模式用户的5G会话上下文数。<br>- “ULCL（上行分类）”：查询ULCL会话用户的5G会话上下文数。<br>- “IPV6_MULTIHOMING（IPv6多出口）”：查询IPv6多出口会话用户的5G会话上下文数。<br>- “NSA（NSA）”：非独立组网，指以现有的LTE无线接入和核心网作为移动性管理和覆盖的锚点，新增5G接入的组网方式。<br>- “UEIPALLOCBYUPF（UPF分配UE地址）”：查询UPF分配UE地址的会话上下文数。<br>- “UEIPALLOCBYSUBS（签约数据指定UE地址）”：查询签约数据指定UE地址的会话上下文数。<br>- “UEIPALLOCBYLOCAL（本地分配UE地址）”：查询本地分配UE地址的会话上下文数。<br>- “CHG_OFFLINE（离线计费）”：查询离线计费的会话上下文数。<br>- “CHG_ONLINE（在线计费）”：查询在线计费的会话上下文数。<br>- “CHG_FBC（内容计费）”：查询内容计费的会话上下文数。<br>- “DYNC_PCC（动态PCC）”：查询动态PCC的会话上下文数。<br>- “LOCAL_PCC（本地PCC）”：查询本地PCC的会话上下文数。<br>- “CHG_CONVERGED（融合计费）”：查询融合计费的会话上下文数。<br>- “L2TP（L2TP）”：查询当前在线的L2TP用户的会话上下文数。<br>- “SUMMARY（汇总信息）”：查询所有类型的汇总会话上下文数。<br>- “LOCREPORT（位置订阅）”：查询开启实时位置订阅功能的会话上下文数。<br>- “PRA（PRA）”：查询开启PRA功能的会话上下文数。<br>- “NGLAN（NGLAN）”：查询开启5G LAN功能的上下文会话数。<br>- “TRAFFIC_DIST_APN（专网分流APN）”：查询使用该专网分流APN的5G会话上下文数。<br>- “NW5GNSA（5G NSA 网络）”：查询具备5G能力的上下文数及使用了5G网络的上下文数。<br>- “UDMBYPASS（UDM全故障）”：查询当前处于UDM全故障状态的5G会话上下文数。<br>- “ALIASAPN（别名APN）”：查询使用该别名APN激活的当前在线会话上下文数。<br>- “DNAI（DNAI）”：查询使用该DNAI激活的当前在线会话上下文数。<br>- “MULTIDNN_DEDDNN（智能分流专用DNN）”：查询关联该专用DNN的通用DNN激活的当前在线会话上下文数。<br>- “QOSANA（QOS_ANA事件订阅）”：查询订阅了QOS_ANA事件的会话上下文数。<br>- “QOSEXP（QOS_EXP事件订阅）”：查询订阅了QOS_EXP事件的会话上下文数。<br>- “FWA（FWA）”：查询当前在线的FWA用户的会话上下文数。<br>默认值：SUMMARY<br>配置原则：<br>本参数不输入时，表示查询汇总的信息。 |
| APN | APN | 可选必选说明：该参数在"QRY_CLASS"配置为"APN"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文的APN。使用用户请求的APN对应的上报属性中“上报给话统的APN名”参数的取值，即在SET APNREPORTATTR命令中设置的该APN的PERFORMANCE的取值，指定使用用户请求的APN还是真实的APN进行统计。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| RAT | 无线接入类型 | 可选必选说明：该参数在"QRY_CLASS"配置为"RAT"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的无线接入类型。<br>数据来源：全网规划<br>取值范围：<br>- “UTRAN（UTRAN）”：通用陆地无线接入网。<br>- “GERAN（GERAN）”：GSM/EDGE无线接入网。<br>- “EUTRAN（EUTRAN）”：演进型通用陆地无线接入网。<br>- “NGRAN（NGRAN）”：5G无线接入网。<br>- “EUTRAN_NB_IOT（EUTRAN-NB-IOT）”：演进型通用陆地无线接入网-窄带物联网。<br>- “WLAN（WLAN）”：无线局域网<br>- “LTE_M（LTE_M）”：演进的高速包数据网络<br>- “REDCAP（REDCAP）”：轻量化5G<br>默认值：无<br>配置原则：无 |
| UPF_NAME | UPF名称 | 可选必选说明：该参数在"QRY_CLASS"配置为"UPF"时为条件必选参数。该参数在"QRY_CLASS"配置为"DNAI"时为条件可选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的UPF名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| SST | 切片/服务类型 | 可选必选说明：该参数在"QRY_CLASS"配置为"SNSSAI"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的切片/服务类型。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| POD_ID | POD名称 | 可选必选说明：该参数在"QRY_SCOPE"配置为"SPECIFIED_POD_INFO"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片区分码 | 可选必选说明：该参数在"QRY_CLASS"配置为"SNSSAI"时为条件可选参数。<br>参数含义：本参数用于指定需要查询会话上下文数的切片区分码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~8。只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：无 |
| SELECTEDDNN | 选择的APN | 可选必选说明：该参数在"QRY_CLASS"配置为"TRAFFIC_DIST_APN"时为条件可选参数。<br>参数含义：该参数用于指定需要查询会话上下文的选择APN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| ALIASAPN | 别名APN | 可选必选说明：该参数在"QRY_CLASS"配置为"ALIASAPN"时为条件必选参数。<br>参数含义：该参数用于指定APN别名。表示查询使用该别名APN激活的当前在线会话数，该别名APN所对应的真实APN必须在系统上已经配置。如果输入真实APN，则显示与真实APN相关联的所有别名APN上的当前在线会话数。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| DNAI | 数据网络访问标识符 | 可选必选说明：该参数在"QRY_CLASS"配置为"DNAI"时为条件必选参数。<br>参数含义：该参数用于指定需要查询会话上下文数的数据网络访问标识符。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| MULTIDNNTYPE | 智能分流DNN类型 | 可选必选说明：该参数在"QRY_CLASS"配置为"MULTIDNN_DEDDNN"时为条件必选参数。<br>参数含义：该参数用于指定智能分流DNN类型。该参数仅在拜访地智能分流SMF上生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_DNN（所有专用DNN）”：查询所有专用DNN关联的通用DNN激活的当前在线会话上下文数。<br>- “SPECIAL_DNN（指定专用DNN）”：查询指定专用DNN关联的通用DNN激活的当前在线会话上下文数。<br>默认值：无<br>配置原则：无 |
| DEDDNN | 专用DNN | 可选必选说明：该参数在"MULTIDNNTYPE"配置为"SPECIAL_DNN"时为条件必选参数。<br>参数含义：该参数用于指定查询会话上下文数的专用DNN的APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSESSIONNUM]] · 会话管理的会话上下文数（SMSESSIONNUM）

## 使用实例

当希望查询整系统的会话上下文数量时，使用如下命令：

```
%%DSP SMSESSIONNUM: QRY_SCOPE=SUMMARY, QRY_CLASS=SUMMARY;%%
RETCODE = 0  操作成功

结果如下
--------
                                  查询分类  =  汇总信息
           GGSN-C上激活的GTPv1会话上下文数  =  0
            PGW-C上激活的GTPv2会话上下文数  =  0
            SGW-C上激活的GTPv2会话上下文数  =  0
          S/PGW-C上激活的GTPv2会话上下文数  =  0
     N16/N16a接口SMF上激活的SA会话上下文数  =  0
         I-SMF/V-SMF上激活的SA会话上下文数  =  0
          N11接口SMF上激活的SA会话上下文数  =  0
                       GTPv2会话上下文总数  =  0
                          SA会话上下文总数  =  0
            在GGSN-C上激活的信令代理用户会话上下文总数  =  0
            在PGW-C上激活的信令代理用户会话上下文总数  =  0
            在Proxy SMF S8上激活的信令代理用户会话上下文总数  =  0
            N11接口MultiDNN SMF上激活的SA会话上下文数  =  0
            MultiDNN I-SMF上激活的SA会话上下文数  =  0
          在Proxy SMF上激活的信令代理用户会话上下文总数  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SMSESSIONNUM.md`
