---
id: UNC@20.15.2@MMLCommand@DSP NGPAGING
type: MMLCommand
name: DSP NGPAGING（显示5G寻呼表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGPAGING
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼数据
status: active
---

# DSP NGPAGING（显示5G寻呼表）

## 功能

![](显示5G寻呼表（DSP NGPAGING）_09651526.assets/notice_3.0-zh-cn_2.png)

如果选择“全量查询”，且当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于查询UNC系统的NG寻呼表信息。NG寻呼表记录了接入到UNC的接入网设备及其支持的TAI信息。

## 注意事项

该命令下发时，如果QUERYTYPE为QUERYALL，那么查询的是全部的寻呼表信息；如果QUERYTYPE为PRECISEQUERY，则会查询指定的接入设备支持的寻呼表信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定寻呼表查询的范围。<br>数据来源：本端规划<br>取值范围：<br>- “QUERYALL（全量查询）”：查询所有基站的寻呼表信息<br>- “PRECISEQUERY（精确查询）”：查询特定基站的寻呼表信息<br>- “SPECIFIEDTAI（指定TAI）”：查询指定TAI寻呼表信息<br>- “SPECIFIEDTAIPRE（指定TAI前缀）”：查询指定TAI前缀寻呼表信息<br>默认值：无<br>配置原则：无 |
| PLMN | PLMN | 可选必选说明：该参数在"QUERYTYPE"配置为"PRECISEQUERY"时为条件必选参数。<br>参数含义：该参数用于指定NG接入网中基站的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"PRECISEQUERY"时为条件必选参数。<br>参数含义：该参数表示gNodeB类型，包含Global gNB或者Global N3IWF，以及Macro ng-eNB、Short Macro ng-eNB、Long Macro ng-eNB等五种细分类型。<br>数据来源：全网规划<br>取值范围：<br>- “GNB（Global gNB）”：Global gNB<br>- “MACRONGENB（Macro ng-eNB）”：Macro ng-eNB<br>- “SHORTNGENB（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LONGNGENB（Long Macro ng-eNB）”：Long Macro ng-eNB<br>- “N3IWF（Global N3IWF）”：Global N3IWF<br>默认值：无<br>配置原则：无 |
| NGRANNODEID | NG-RAN基站标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"PRECISEQUERY"时为条件必选参数。<br>参数含义：该参数用于指定NG接入网中基站的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。由十进制数字组成。<br>默认值：无<br>配置原则：无 |
| GNBLEN | gNB标识长度(比特) | 可选必选说明：该参数在"NGRANNODETYPE"配置为"GNB"时为条件必选参数。该参数在"QUERYTYPE"配置为"PRECISEQUERY"时为条件必选参数。<br>参数含义：该参数表示gNB标识的长度（比特）。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |
| TAI | 跟踪区标识 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIEDTAI"时为条件必选参数。<br>参数含义：该参数表示NG-RAN基站支持的跟踪区信息。TAI由PLMN ID和TAC组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~255。TAI由MCC、MNC和TAC组成。MCC由3个十进制数字组成，MNC由2到3个十进制数字组成，TAC由十六进制数字组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| TAIPRE | 跟踪区标识前缀 | 可选必选说明：该参数在"QUERYTYPE"配置为"SPECIFIEDTAIPRE"时为条件必选参数。<br>参数含义：该参数表示NG-RAN基站支持的跟踪区标识前缀。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~12。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGPAGING]] · 5G寻呼表（NGPAGING）

## 使用实例

查询系统中的所有寻呼表信息，执行如下命令：

```
%%DSP NGPAGING: QUERYTYPE=QUERYALL;%%
RETCODE = 0  操作成功

结果如下
------------------------
                  PLMN  =  12303
        NG-RAN基站类型  =  Global gNB
        NG-RAN基站标识  =  1114449
     gNB标识长度(比特)  =  24
            跟踪区标识  =  12303110101
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGPAGING.md`
