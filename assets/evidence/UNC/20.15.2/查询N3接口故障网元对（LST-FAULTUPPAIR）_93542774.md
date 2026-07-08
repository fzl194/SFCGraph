# 查询N3接口故障网元对（LST FAULTUPPAIR）

- [命令功能](#ZH-CN_MMLREF_0000001193542774__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001193542774__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001193542774__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001193542774__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001193542774__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001193542774)

**适用NF：SGW-C、SMF**

该命令用于查询N3接口故障网元对。

## [注意事项](#ZH-CN_MMLREF_0000001193542774)

该记录最多显示1024条，多余部分将被截断。

#### [操作用户权限](#ZH-CN_MMLREF_0000001193542774)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001193542774)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询类型。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYALL（Query All）”：查询所有<br>- “QUERYBYRAN（Query By RAN）”：根据RAN查询<br>- “QUERYBYUPF（Query By UPF）”：根据UPF查询<br>默认值：无<br>配置原则：无 |
| PLMN | PLMN | 可选必选说明：该参数在"QRYTYPE"配置为"QUERYBYRAN"时为条件必选参数。<br>参数含义：该参数用于标识接入网设备的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。<br>默认值：无<br>配置原则：无 |
| RANNODETYPE | RAN基站类型 | 可选必选说明：该参数在"QRYTYPE"配置为"QUERYBYRAN"时为条件必选参数。<br>参数含义：该参数用于指定RAN基站类型。<br>数据来源：全网规划<br>取值范围：<br>- “MACROENB（Macro eNodeB）”：Macro eNodeB<br>- “SHORTENB（Short Macro eNodeB）”：Short Macro eNodeB<br>- “LONGENB（Long Macro eNodeB）”：Long Macro eNodeB<br>- “GNB（Global gNodeB）”：Global gNodeB<br>默认值：无<br>配置原则：无 |
| RANNODEID | RAN基站标识 | 可选必选说明：该参数在"QRYTYPE"配置为"QUERYBYRAN"时为条件必选参数。<br>参数含义：该参数用于指定RAN基站标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。如果将RANNODETYPE设置为MACROENB，则该参数的值范围为0到1048575；如果将RANNODETYPE设置为SHORTENB，则该参数的取值范围为0到262143；如果将RANNODETYPE设置为LONGENB，则该参数的取值范围为0到2097151；如果将RANNODETYPE设置为GNB，则该参数的值范围为0到4294967295。<br>默认值：无<br>配置原则：无 |
| NODEIDLEN | RAN基站标识长度(比特) | 可选必选说明：该参数在"QRYTYPE"配置为"QUERYBYRAN"时为条件必选参数。<br>参数含义：该参数用于指定RAN基站的标识长度(比特)。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是18~32。当RANNODETYPE选择MACROENB时，本参数应当输入值为20；当RANNODETYPE选择SHORTENB时，本参数应当输入值为18；当RANNODETYPE选择LONGENB时，本参数应当输入值为21；当RANNODETYPE选择GNB时，本参数的输入范围应当是22到32。<br>默认值：无<br>配置原则：无 |
| UPFID | UPF实例标识 | 可选必选说明：该参数在"QRYTYPE"配置为"QUERYBYUPF"时为条件必选参数。<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。UPFID参数不区分大小写且必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。 |

## [使用实例](#ZH-CN_MMLREF_0000001193542774)

查询与UPFID为"upf_instance_0"绑定的RAN信息：

```
%%LST FAULTUPPAIR: QRYTYPE=QUERYBYUPF, UPFID="upf_instance_0";%%
RETCODE = 0  操作成功

结果如下
--------
                 PLMN  =  12303
          RAN基站类型  =  Global gNodeB
          RAN基站标识  =  327697
RAN基站标识长度(比特)  =  24
              RAN组名  =  group1
          UPF实例标识  =  upf_instance_0
          UPF描述名称  =  NULL
              UPF组名  =  group2
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001193542774)

| 输出项名称 | 输出项解释 |
| --- | --- |
| PLMN | 该参数用于标识接入网设备的PLMN信息。 |
| RAN基站类型 | 该参数用于指定RAN基站类型。 |
| RAN基站标识 | 该参数用于指定RAN基站标识。 |
| RAN基站标识长度(比特) | 该参数用于指定RAN基站的标识长度(比特)。 |
| RAN组名 | 该参数用于指定RAN组名。 |
| UPF实例标识 | 该参数用于指定UPF实例标识。 |
| UPF描述名称 | 该参数用于指定UPF描述名称。 |
| UPF组名 | 该参数用于指定UPF组名。 |
