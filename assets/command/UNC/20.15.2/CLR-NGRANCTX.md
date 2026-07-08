---
id: UNC@20.15.2@MMLCommand@CLR NGRANCTX
type: MMLCommand
name: CLR NGRANCTX（清除NG-RAN上下文）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NGRANCTX
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- 清除NG-RAN上下文
status: active
---

# CLR NGRANCTX（清除NG-RAN上下文）

## 功能

![](清除NG-RAN上下文（CLR NGRANCTX）_09651514.assets/notice_3.0-zh-cn_2.png)

执行本命令将导致AMF释放与指定NG-RAN之间的SCTP连接，同时会释放通过该NG-RAN接入的用户上下文或基站上下文，从而导致业务中断。

**适用NF：AMF**

该命令用于在AMF上清除指定的NG-RAN上下文。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGRANNODETYPE | NG-RAN基站类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接入的RAN的类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNodeB）”：gNodeB<br>- “NgEnb（ng-eNB）”：ng-eNB<br>- “SFgnb（sfgNodeB）”：sfgNodeB<br>默认值：无<br>配置原则：无 |
| SFGCLRTYPE | 感知基站清除方式 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"SFgnb"时为条件必选参数。<br>参数含义：该参数用于指定感知基站信息的清除方式。<br>数据来源：本端规划<br>取值范围：<br>- “MasterRanID（指定感知链路主基站ID清除上下文）”：指定感知链路主基站ID清除上下文<br>- “SenseRanID（指定感知基站ID删除感知能力）”：指定感知基站ID删除感知能力<br>默认值：无<br>配置原则：<br>若希望仅删除某基站的感知能力，选择“SenseRanID”清除方式。若希望将指定感知主基站链路，以及该链路下挂载的所有感知基站能力都清除，选择“MasterRanID”清除方式。 |
| PLMNID | PLMN标识 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"、"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定NG接入网侧基站的PLMN标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| GNBTYPE | gNodeB类型 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB的类型。<br>数据来源：对端协商<br>取值范围：<br>- “Gnb（gNodeB）”：gNodeB<br>默认值：无<br>配置原则：无 |
| GNBID | gNodeB标识 | 可选必选说明：该参数在"GNBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| NGENBTYPE | ng-eNB类型 | 可选必选说明：该参数在"NGRANNODETYPE"配置为"NgEnb"时为条件必选参数。<br>参数含义：该参数用于指定ng-eNB类型。<br>数据来源：对端协商<br>取值范围：<br>- “MacroNgEnb（Macro ng-eNB）”：Macro ng-eNB<br>- “ShortMacroNgEnb（ShortMacro ng-eNB）”：ShortMacro ng-eNB<br>- “LongMacroNgEnb（LongMacro ng-eNB）”：LongMacro ng-eNB<br>默认值：无<br>配置原则：无 |
| MACRONGENBID | Macro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"MacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~1048575。<br>默认值：无<br>配置原则：无 |
| SHORTNGENBID | ShortMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"ShortMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Short Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~262143。<br>默认值：无<br>配置原则：无 |
| LONGNGENBID | LongMacro ng-eNB标识 | 可选必选说明：该参数在"NGENBTYPE"配置为"LongMacroNgEnb"时为条件必选参数。<br>参数含义：该参数用于指定Long Macro ng-eNB标识。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是0~2097151。<br>默认值：无<br>配置原则：无 |
| GNBIDBITLEN | gNodeB ID有效比特长度 | 可选必选说明：该参数在"GNBTYPE"配置为"Gnb"时为条件必选参数。<br>参数含义：该参数用于指定gNodeB ID有效比特长度。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围是22~32。<br>默认值：无<br>配置原则：无 |
| SFGNBID | sfgNodeB标识 | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"时为条件必选参数。<br>参数含义：该参数用于指定感知基站的标识ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| SFGPLMNID | 通感基站PLMN标识 | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"时为条件必选参数。<br>参数含义：该参数用于指定感知基站的PLMN标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| SFGMASTERGNBID | 感知主基站标识 | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"、"MasterRanID"时为条件必选参数。<br>参数含义：该参数用于指定感知基站所属的主基站的标识ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| SFGMASTERPLMN | 感知主基站PLMN标识 | 可选必选说明：该参数在"SFGCLRTYPE"配置为"SenseRanID"、"MasterRanID"时为条件必选参数。<br>参数含义：该参数用于指定感知基站所属的主基站的PLMN标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NG-RAN上下文（NGRANCTX）](configobject/UNC/20.15.2/NGRANCTX.md)

## 使用实例

- 删除基站类型为Gnb，PLMN ID为12303，Gnb类型为Gnb，Gnb ID为1179985，gNodeB ID有效比特长度为24的基站对应的上下文。执行如下命令：
  ```
  CLR NGRANCTX: NGRANNODETYPE=Gnb, PLMNID=12303, GNBTYPE=Gnb, GNBID=1179985, GNBIDBITLEN=24;
  ```
- 删除基站类型为SFgnb，清除方式为指定感知链路主基站ID清除上下文，感知主基站PLMN标识为12303，感知主基站标识为1179985的感知基站对应的上下文。执行如下命令：
  ```
  CLR NGRANCTX: NGRANNODETYPE=SFgnb, SFGCLRTYPE=MasterRanID, SFGMASTERGNBID=12303, SFGMASTERPLMN=1179985;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除NG-RAN上下文（CLR-NGRANCTX）_09651514.md`
