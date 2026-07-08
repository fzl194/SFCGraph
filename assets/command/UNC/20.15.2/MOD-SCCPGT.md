---
id: UNC@20.15.2@MMLCommand@MOD SCCPGT
type: MMLCommand
name: MOD SCCPGT（修改SCCP全局翻译码）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SCCPGT
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP全局翻译码
status: active
---

# MOD SCCPGT（修改SCCP全局翻译码）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来修改SCCP全局码翻译表中指定的GT记录的信息。

## 注意事项

- 此命令执行后立即生效。
- 应该增加本局SGSN的ISDN号码的GT码翻译信息。
- 执行此命令之前，需要执行下面的命令：添加SCCP目的信令点的[**ADD SCCPDPC**](../SCCP目的信令点/增加SCCP目的信令点(ADD SCCPDPC)_26306130.md)命令、添加SCCP子系统表的[**ADD SCCPSSN**](../SCCP子系统/增加SCCP子系统(ADD SCCPSSN)_26306144.md)命令（如果翻译结果类型为DPC+SSN）、添加新GT码的[**ADD SCCPNGT**](../SCCP新全局翻译码/增加SCCP新全局翻译码(ADD SCCPNGT)_26146328.md)命令（如果翻译结果类型为DPC+NGT）、添加IMSI-GT翻译表的[**ADD IMSIGT**](../../../MAP应用协议/IMSI GT转换信息/增加IMSI-GT对应关系(ADD IMSIGT)_72345061.md)命令，注意IMSI到GT转换后的MGT最大长度最长为15位，配置对应的SCCPGT时不能超过该长度。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTX | GT码索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GT码索引。<br>数据来源：本端规划<br>取值范围：0~4095<br>默认值：无<br>配置原则：此索引对应的GT记录应该在GT表中存在，可以通过<br>[**LST SCCPGT**](查询SCCP全局翻译码(LST SCCPGT)_72226005.md)<br>命令查看。 |
| NI | 网络指示语 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络指示语。<br>数据来源：整网规划<br>取值范围：<br>- “INT（国际网）”<br>- “INTB（国际备用网）”<br>- “NAT（国内网）”<br>- “NATB（国内备用网）”<br>默认值：无<br>配置原则：配置的信令网络指示语在OFI表中应该配置为有效。 |
| RT | 翻译结果类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GT码的翻译结果类型。<br>数据来源：整网规划<br>取值范围：<br>- “DPCGT（DPC + GT）”<br>- “DPCSSN（DPC + SSN）”<br>- “DPCNEWGT（DPC + 新GT）”<br>- “DPC（DPC）”<br>默认值：无<br>配置原则：<br>- 如果消息发送到DPC以后，需要在DPC对GT码再进行翻译，则使用DPCGT方式。<br>- 如果消息直接发送到最终的目的信令点，则使用DPCSSN或DPC方式，DPCSSN是将消息发送到DPC的指定的一个SCCP用户（配置的SSN），DPC方式则根据SCCP用户填写的SSN决定将消息发送到对方的那个SCCP用户。<br>- 如果消息发送到DPC以后，需要在DPC使用一条新的GT码进行翻译，则使用DPCNEWGT方式。<br>- 在实际的组网环境中，一般本地的信令点使用DPC方式，外地的信令点一般使用DPCGT方式，注意对本局SGSN的ISDN号码的GT码的翻译结果类型应该选择DPC方式。 |
| GTEXP | GT码表示语 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GT码的类型。<br>数据来源：整网规划<br>取值范围：<br>- “FOUR（ITU四类）”<br>- “SIX（ANSI二类）”<br>默认值：无 |
| TT | 翻译类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定翻译类型。<br>前提条件：只有当<br>“GT码表示语”<br>为<br>“SIX（ANSI二类）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “ANSI9（ANSI 9类）”<br>- “ANSI10（ANSI 10类）”<br>默认值：无 |
| NP | 编号计划 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定编号计划。<br>前提条件：只有当<br>“GT码表示语”<br>为<br>“FOUR（ITU四类）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “ISDNP（ISDN/电话编号计划）”<br>- “DATA（数据编号计划）”<br>- “TELEX（Telex编号计划）”<br>- “SMS（海事移动编号计划）”<br>- “PMS（陆地移动编号计划）”<br>- “ISDNMS（ISDN/移动编号计划）”<br>默认值：无 |
| ADDREXP | 地址性质表示语 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定地址性质表示语。<br>前提条件：只有当<br>“GT码表示语”<br>为<br>“FOUR（ITU四类）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：<br>- “ FREE（空闲）”<br>- “SUBDN（用户号码）”<br>- “NSU（国内备用号码）”<br>- “NVU（国内有效号码）”<br>- “INTDN（国际号码）”<br>默认值：无 |
| ADDR | 地址信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址信息。<br>数据来源：整网规划<br>取值范围：1～20位十进制数字<br>默认值：无 |
| DPC | 目的信令点编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定目的信令点编码，分为24位信令点编码和14位信令点编码。<br>数据来源：整网规划<br>取值范围：长度不超过8的字符串<br>默认值：无<br>配置原则：<br>- 配置的信令点编码结构需要和信令属性表中对应的有效信令网络的网络结构保持一致，输入的DPC必须在SCCP的目的信令点或本局信令点表中存在。 |
| SSN | 子系统号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定子系统编码，如果消息可能会发送到一个信令点上的多个SSN（不包括SCMG），则到该信令点的GT码的翻译结果类型应该选择为“DPC”，子系统不需要配置，而是根据SCCP用户在消息中填写的SSN决定将消息发送到对方信令点的哪个SCCP用户。<br>数据来源：整网规划<br>取值范围：<br>- “NODEFINE（未定义）”<br>- “SCMG（1）”<br>- “STANDBY0（2）”<br>- “RANAP（142）”<br>- “OMAP（4）”<br>- “MAP（5）”<br>- “HLR（6）”<br>- “VLR（7）”<br>- “MSC（8）”<br>- “STANDBY1（11）”<br>- “INAP（12）”<br>- “CAP（146）”<br>- “SGSN（149）”<br>- “GGSN（150）”<br>- “BSSAP（254）”<br>- “BSSAP+（BSSAP+）”<br>- “GMLC（145）”<br>- “EIR（9）”<br>默认值：无<br>配置原则：若选择SCCPGT的翻译结果类型为DPCSSN方式，则需要输入SSN，输入的SSN必须在SCCP的子系统表中存在。 |
| NGTX | 新GT码索引 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定新GT码对应的索引值。<br>数据来源：整网规划<br>取值范围：0~4095<br>默认值：无<br>配置原则：<br>- 如果配置了新GT码，则对应的记录在新GT码表里面应该存在。<br>- 如果翻译结果类型配置为DPCNEWGT，此值必须配置。 |
| NAME | SCCP GT名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCCP GT名称。<br>数据来源：本端规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [SCCP全局翻译码（SCCPGT）](configobject/UNC/20.15.2/SCCPGT.md)

## 使用实例

以下命令修改SCCP全局码翻译表中指定记录的信息， “GT码索引” 为 “1” ， “网络标识” 为 “国内网” ， “GT码表示语” 为 “FOUR” ：

MOD SCCPGT: GTX=1, NI=NAT, GTEXP=FOUR;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改SCCP全局翻译码(MOD-SCCPGT)_26146326.md`
