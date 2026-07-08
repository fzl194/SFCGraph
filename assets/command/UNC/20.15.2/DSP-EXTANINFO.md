---
id: UNC@20.15.2@MMLCommand@DSP EXTANINFO
type: MMLCommand
name: DSP EXTANINFO（显示扩展的AN信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: EXTANINFO
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

# DSP EXTANINFO（显示扩展的AN信息）

## 功能

![](显示扩展的AN信息（DSP EXTANINFO）_70382305.assets/notice_3.0-zh-cn_2.png)

如果当前接入到AMF的gNB数量较多时，执行该命令会占用维护终端较长时间，进而导致用户无法继续使用该维护终端。

若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

**适用NF：AMF**

该命令用于显示在指定的NGAP本端实体接入的NG-RAN基站的扩展信息，例如基站支持的RAT类型等。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPLEIDX | NGAP实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的NGAP实体索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1023。<br>默认值：无<br>配置原则：无 |
| PODID | POD ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识系统中的POD ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接入的NG-RAN基站类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNodeB）”：gNodeB<br>- “NgEnb（ng-eNB）”：ng-eNB<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定PLMN的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定PLMN的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GNODEBTYPE | gNodeB类型 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB的类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNB）”：gNB<br>默认值：无<br>配置原则：无 |
| GNODEBID | gNodeB标识 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| GNBIDBITLEN | gNodeB ID有效比特长度 | 可选必选说明：该参数在"GNODEBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于显示gNodeB ID有效比特长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |
| NGENBTYPE | ng-eNB类型 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"时为条件必选参数。<br>参数含义：该参数用于指定ng-eNB类型。<br>数据来源：对端协商<br>取值范围：<br>- “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB<br>- “ShortMacroNgEnb（Short Macro ng-eNB）”：Short Macro ng-eNB<br>- “LongMacroNgEnb（Long Macro ng-eNB）”：Long Macro ng-eNB<br>默认值：无<br>配置原则：无 |
| MACRONGENBID | Macro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~1048575。<br>默认值：无<br>配置原则：无 |
| SHORTMNGENBID | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Short Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~262143。<br>默认值：无<br>配置原则：无 |
| LONGMNGENBID | LongMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Long Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~2097151。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EXTANINFO]] · 扩展的AN信息（EXTANINFO）

## 使用实例

查询基站类型为Gnb，Gnb类型为Gnb，Gnb ID为1179985，gNodeB ID有效比特长度为24的基站扩展信息，执行如下命令：

```
%%DSP EXTANINFO:NGAPLEIDX=1;%%
RETCODE = 0  操作成功

结果如下
--------
               POD ID  =  NULL
         NGAP实体索引  =  1
       NG-RAN基站类型  =  gNodeB
           移动国家码  =  123
             移动网号  =  45
           gNodeB类型  =  gNodeB
           gNodeB标识  =  1179985
gNodeB ID有效比特长度  =  24
           ng-eNB类型  =  NULL
     Macro ng-eNB标识  =  0
ShortMacro ng-eNB标识  =  0
 LongMacro ng-eNB标识  =  0
          RAN基站名称  =  NGRANNodeName1
          RAT信息列表  =  NULL
(结果个数  =  1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示扩展的AN信息（DSP-EXTANINFO）_70382305.md`
