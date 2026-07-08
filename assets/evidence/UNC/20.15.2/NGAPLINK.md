# 显示NGAP链路信息（DSP NGAPLINK）

- [命令功能](#ZH-CN_MMLREF_0209651404__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651404__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651404__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651404__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651404__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651404)

![](显示NGAP链路信息（DSP NGAPLINK）_09651404.assets/notice_3.0-zh-cn_2.png)

如果选择“报告输出”，且当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于查询NGAP链路信息。

## [注意事项](#ZH-CN_MMLREF_0209651404)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209651404)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651404)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定输出类型。<br>数据来源：本端规划<br>取值范围：<br>- “Summary（统计信息）”：统计信息<br>- “Screen（报告输出）”：报告输出<br>默认值：无<br>配置原则：无 |
| NGAPLEIDX | NGAP本端实体标识 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定查询的NGAP实体索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |
| PODID | POD ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识系统中的POD ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NGRANTYPE | NgRanNode类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接入的RAN的类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNB）”：gNB<br>- “NgEnb（ng-eNB）”：ng-eNB<br>- “SFgnb（sfgNodeB）”：sfgNodeB<br>默认值：无<br>配置原则：<br>当OUTPUTTYPE选summary时，该参数不生效，无需配置。 |
| MCC | 移动国家码 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GNODEBTYPE | gNodeB类型 | 可选必选说明：该参数在"NGRANTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB的类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNB）”：gNB<br>默认值：无<br>配置原则：无 |
| GNODEBID | gNodeB标识 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>当OUTPUTTYPE选summary时，该参数不生效，无需配置。 |
| NGENBTYPE | ng-eNB类型 | 可选必选说明：该参数在"NGRANTYPE"配置为"NgEnb"时为条件可选参数。<br>参数含义：该参数用于指定ng-eNB类型。<br>数据来源：对端协商<br>取值范围：<br>- “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB<br>- “ShortMacroNgEnb（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LongMacroNgEnb（Long Macro ng-eNB）”：Long Macro ng-eNB<br>默认值：无<br>配置原则：无 |
| MNGENBID | Macro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~1048575。<br>默认值：无<br>配置原则：无 |
| SMNGENBID | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Short Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~262143。<br>默认值：无<br>配置原则：无 |
| LMNGENBID | LongMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Long Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~2097151。<br>默认值：无<br>配置原则：无 |
| GNBIDBITLEN | gNodeB ID 有效比特长度 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于显示gNodeB ID 有效比特长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |
| SFGNODEBID | sfgNodeB标识 | 可选必选说明：该参数在"NGRANTYPE"配置为"SFgnb"时为条件必选参数。<br>参数含义：该参数用于指定sfgNodeB标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>该参数仅支持用于建链的感知主基站标识。感知主基站的标识可以通过查看SFG接口跟踪获取，或通过将" OUTPUTTYPE"参数设置为"Screen"，同时不输入"NGRANTYPE"参数，过滤查询所有结果中"NGRANTYPE"字段为SFgnb的记录来获取。 |

## [使用实例](#ZH-CN_MMLREF_0209651404)

查询NGAP链路信息，输出类型为统计信息，执行如下命令：

```
%%DSP NGAPLINK: OUTPUTTYPE=Summary;%%
RETCODE = 0  操作成功

结果如下
--------
POD ID    NGAP链路数  正常的NGAP链路数  SFGAP链路数  正常的SFGAP链路数  

uncpod-0  8301        0                 1            1                  
total     8301        0                 1            1                  
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209651404)

| 输出项名称 | 输出项解释 |
| --- | --- |
| POD ID | 该参数用于标识系统中的POD ID。 |
| NGAP链路数 | 该参数用于显示NGAP链路数。 |
| 正常的NGAP链路数 | 该参数用于显示正常的NGAP链路数量。 |
| SCTP偶联ID | 该参数用于显示SCTP偶联ID。 |
| 移动国家码 | 该参数用于指定PLMN的移动国家码。 |
| 移动网号 | 该参数用于指定PLMN的移动网号。 |
| NG-RAN基站类型 | 该参数用于指定基站类型。<br>取值说明：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>- “SFgnb（sfgNodeB）”：sfgNodeB |
| NG-RAN基站标识 | 该参数用于指定NG-RAN基站的标识。 |
| 基站标识长度(比特) | 该参数用于指定NG-RAN基站的标识长度(比特)。 |
| 本端IPv4地址1 | 该参数用于显示本端IPv4地址1。 |
| 本端IPv4地址2 | 该参数用于显示本端IPv4地址2。 |
| 本端IPv6地址1 | 该参数用于显示本端IPv6地址1。 |
| 本端IPv6地址2 | 该参数用于显示本端IPv6地址2。 |
| 本端端口号 | 该参数用于显示本端端口号。 |
| 对端IPv4地址1 | 该参数用于显示对端IPv4地址1。 |
| 对端IPv4地址2 | 该参数用于显示对端IPv4地址2。 |
| 对端IPv6地址1 | 该参数用于显示对端IPv6地址1。 |
| 对端IPv6地址2 | 该参数用于显示对端IPv6地址2。 |
| 对端端口号 | 该参数用于显示对端端口号。 |
| 链路状态 | 该参数用于显示链路状态。<br>取值说明：<br>- “Connected（连接态）”：正常<br>- “Releasing（释放）”：故障 |
| 接入节点名称 | 该参数用于指定接入节点的名字。 |
| POD版本号信息 | 该参数用于指定pod版本号。非灰度升级期间，该参数不显示。 |
| sfgNodeB标识 | 该参数用于指定sfgNodeB标识。 |
| SFGAP链路数 | 该参数用于显示SFGAP链路数。 |
| 正常的SFGAP链路数 | 该参数用于显示正常的SFGAP链路数量。 |
