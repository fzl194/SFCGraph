---
id: UNC@20.15.2@MMLCommand@DSP ANINFO
type: MMLCommand
name: DSP ANINFO（显示AN信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ANINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- 查询本端实体下的AN信息
status: active
---

# DSP ANINFO（显示AN信息）

## 功能

![](显示AN信息（DSP ANINFO）_09653795.assets/notice_3.0-zh-cn_2.png)

如果选择“报告输出”，且当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于显示在指定的NGAP/SFGAP本端实体接入的NG-RAN基站的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定输出类型。<br>数据来源：本端规划<br>取值范围：<br>- “Summary（统计信息）”：统计信息<br>- “Screen（报告输出）”：报告输出<br>默认值：无<br>配置原则：无 |
| NGAPLEIDX | NGAP实体索引 | 可选必选说明：该参数在"OUTPUTTYPE"配置为"Screen"时为条件必选参数。<br>参数含义：该参数用于指定查询的NGAP实体索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：<br>当查询感知基站相关信息时，该参数无效。 |
| PODID | POD ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识系统中的POD ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接入的NG-RAN基站类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNodeB）”：gNodeB<br>- “NgEnb（ng-eNB）”：ng-eNB<br>- “SFgnb（sfgNodeB）”：sfgNodeB<br>默认值：无<br>配置原则：<br>当OUTPUTTYPE选summary时，该参数不生效，无需配置。 |
| MCC | 移动国家码 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GNODEBTYPE | gNodeB类型 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB的类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNB）”：gNB<br>默认值：无<br>配置原则：无 |
| GNODEBID | gNodeB标识 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| SHORTMNGENBID | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Short Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~262143。<br>默认值：无<br>配置原则：无 |
| LONGMNGENBID | LongMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Long Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~2097151。<br>默认值：无<br>配置原则：无 |
| NGENBTYPE | ng-eNB类型 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"时为条件必选参数。<br>参数含义：该参数用于指定ng-eNB类型。<br>数据来源：对端协商<br>取值范围：<br>- “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB<br>- “ShortMacroNgEnb（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LongMacroNgEnb（Long Macro ng-eNB）”：Long Macro ng-eNB<br>默认值：无<br>配置原则：无 |
| MACRONGENBID | Macro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~1048575。<br>默认值：无<br>配置原则：无 |
| GNBIDBITLEN | gNodeB ID有效比特长度 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于显示gNodeB ID有效比特长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |
| SFGNODEBID | sfgNodeB标识 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"SFgnb"时为条件必选参数。<br>参数含义：该参数用于指定sfgNodeB标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>该参数仅支持用于建链的感知主基站标识。感知主基站的标识可以通过查看SFG接口跟踪获取，或通过将"OUTPUTTYPE"参数设置为"Screen"，同时不输入"NGRANNODETYPE"参数，过滤查询所有结果中"NGRANNODETYPE"字段为SFgnb的记录来获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ANINFO]] · AN信息（ANINFO）

## 使用实例

查询本端实体下的AN信息：查询类型为统计信息。执行如下命令：

```
%%DSP ANINFO: OUTPUTTYPE=Summary;%%
RETCODE = 0  操作成功

结果如下
--------
POD ID    AN总数  正常的AN数量  gNodeB数量  正常的gNodeB数量  ng-eNB数量  正常的ng-eNB数量  sfgNodeB数量  正常的sfgNodeB数量  

uncpod-0  0       0             0           0                 0           0                 1             1                   
total     0       0             0           0                 0           0                 1             1                   
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ANINFO.md`
