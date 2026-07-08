---
id: UNC@20.15.2@MMLCommand@ADD SCCPNGT
type: MMLCommand
name: ADD SCCPNGT（增加SCCP新全局翻译码）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCCPNGT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP新全局翻译码
status: active
---

# ADD SCCPNGT（增加SCCP新全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于增加SCCP新全局码表指定记录的信息。此项配置命令关联SCCPGT中的翻译结果类型一项。当“翻译结果类型”为“DPCNEWGT（DPC + 新GT）”，这里的新GT是用于远端GT翻译的，如果本端发出的消息到达远端例如HLR、VLR后，希望将消息中的GT进行替换为更为合理的新GT，则需要先配置此项，然后在SCCPGT的GT翻译表中对新GT的索引进行关联即可。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为4096。
- GT码不能重复。
- 参数的枚举值描述和配置原则可以参考[**ADD SCCPGT**](../SCCP全局翻译码/增加SCCP全局翻译码(ADD SCCPGT)_26306136.md)中的配置。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTX | 新GT码索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GT码对应的索引值。<br>数据来源：本端规划<br>取值范围：0~4095<br>默认值：无 |
| GTEXP | GT码表示语 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GT码表示语。<br>数据来源：整网规划<br>取值范围：<br>- “FOUR(ITU四类)”<br>- “SIX(ANSI二类)”<br>默认值：<br>“FOUR(ITU四类)” |
| ITUTT | ITU翻译类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定ITU模式的GT码翻译类型。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“FOUR(ITU四类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：0~255<br>默认值：0<br>配置原则：当运营商需要使用STP基于GT码的Translation Type再次进行分类路由转发时，配置此参数。 |
| TT | 翻译类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定翻译类型。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“SIX(ANSI二类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ANSI9(ANSI 9类)”<br>- “ANSI10(ANSI 10类)”<br>默认值：<br>“ANSI9(ANSI 9类)” |
| NP | 编号计划 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定编号计划。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“FOUR(ITU四类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ISDNP(ISDN/电话编号计划)”<br>- “DATA(数据编号计划)”<br>- “TELEX(Telex编号计划)”<br>- “SMS(海事移动编号计划)”<br>- “PMS(陆地移动编号计划)”<br>- “ISDNMS(ISDN/移动编号计划)”<br>默认值：<br>“ISDNP(ISDN/电话编号计划)” |
| ADDREXP | 地址性质表示语 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定地址性质表示语。<br>前提条件：该参数在<br>“GT码表示语”<br>参数设置为<br>“FOUR(ITU四类)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “FREE(空闲)”<br>- “SUBDN(用户号码)”<br>- “NSU(国内备用号码)”<br>- “NVU(国内有效号码)”<br>- “INTDN(国际号码)”<br>默认值：<br>“INTDN(国际号码)” |
| ADDR | 地址信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址信息。<br>数据来源：整网规划<br>取值范围：长度不超过20的十进制数字字符串<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCCP新全局码表的记录名称。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：NULL |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPNGT]] · SCCP新全局翻译码（SCCPNGT）

## 使用实例

场景1：

当运营商需要使用信令转接点基于GT码的Translation Type再次进行分类路由转发时，通过SCCP新全局码表配置所有到该目的信令点的全局码的Translation Type，SCCP新全局码的参数 “GT码表示语” ， “编号计划” ， “地址性质表示语” ， “地址信息” 与对应的SCCP全局码保持一致。例如将到HLR101的SCCP全局码的Translation Type配置为9，配置命令如下：

ADD SCCPNGT: NGTX=2, GTEXP=FOUR, ITUTT=9, NP=ISDNP, ADDR="8613915101", DESC="FOR HLR101";

ADD SCCPNGT: NGTX=3, GTEXP=FOUR, ITUTT=9, NP=ISDNMS, ADDR="8613915", DESC="FOR HLR101";

ADD SCCPGT: GTX=151, NI=NAT, RT=DPCNEWGT, GTEXP=FOUR, NP=ISDNP, ADDREXP=INTDN, ADDR="8613915101", DPC="0x15101", NGTX=2, NAME="FOR HLR101";

ADD SCCPGT: GTX=251, NI=NAT, RT=DPCNEWGT, GTEXP=FOUR, NP=ISDNMS, ADDREXP=INTDN, ADDR="8613915", DPC="0x15101", NGTX=3, NAME="FOR HLR101";

场景2：

增加SCCP新全局码表指定记录的信息：

ADD SCCPNGT: NGTX=1, GTEXP=FOUR, ADDR="123", DESC="FOR HLR1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SCCPNGT.md`
