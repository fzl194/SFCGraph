---
id: UNC@20.15.2@MMLCommand@MOD SGSNDNS
type: MMLCommand
name: MOD SGSNDNS（修改SGSN DNS域名策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGSNDNS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- SGSN DNS解析
status: active
---

# MOD SGSNDNS（修改SGSN DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于修改SGSN DNS域名策略配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS域名类型。<br>数据来源：整网规划<br>取值范围：<br>- “ALL（ALL）”<br>- “RAI（RAI）”<br>- “NRI（NRI）”<br>- “RNC_ID（RNC ID）”<br>- “LAI（LAI）”<br>默认值：无<br>配置原则：<br>- 如果系统中同时存在ALL和其他域名类型的记录，优先匹配其他域名类型。如果匹配其他域名类型失败，则使用ALL的域名类型进行匹配。<br>- “ALL（All）”表示非特定的域名类型，即业务流程中使用何种域名类型，和消息流程相关。具体含义参见其他4种域名类型的介绍。<br>- “RAI（RAI）”表示特定路由区组装域名采用的域名类型。例如当MNC、MCC为4位十进制数时，域名格式如下：- ORG后缀：RACxxxx.LACyyyy.RAC.EPC.MNCmmmm.MCCnnnn.3GPPNETWORK.ORG<br>- GPRS后缀：RACxxxx.LACyyyy.MNCmmmm.MCCnnnn.GPRS<br>- “NRI（NRI）”表示在SGSN Pool组网场景中，特定NRI组装域名采用的域名类型。例如当NRI为4位十六进制数，MNC、MCC为3位十进制数时，域名格式如下：- NRI域名格式采用标准方式，ORG后缀：NRI-SGSNxxxx.RACyyyy.LACzzzz.RAC.EPC.MNCmmm.MCCnnn.3GPPNETWORK.ORG<br>- NRI域名格式采用标准方式，GPRS后缀：NRIxxxx.RACyyyy.LACzzzz.MNCmmm.MCCnnn.GPRS<br>- NRI域名格式采用简化方式，ORG后缀：NRI-SGSNxxxx.EPC.MNCmmm.MCCnnn.3GPPNETWORK.ORG<br>- NRI域名格式采用简化方式，GPRS后缀：NRIxxxx.MNCmmm.MCCnnn.GPRS<br>- “RNC_ID（RNC ID）”表示特定RNC ID组装域名采用的域名类型，仅用于Inter relocation流程中。例如当RNC ID为4位十六进制数，MNC、MCC为3位十进制数时，域名格式如下：- ORG后缀：RNCxxxx.RNC.EPC.MNCmmm.MCCnnn.3GPPNETWORK.ORG<br>- GPRS后缀：RNCxxxx.MNCmmm.MCCnnn.GPRS<br>- “LAI（LAI）”表示特定位置区组装域名采用的域名类型。例如当MNC、MCC为4位十进制数时，域名格式如下：- ORG后缀：LACxxxx.LAC.EPC.MNCmmmm.MCCnnnn.3GPPNETWORK.ORG<br>- GPRS后缀：LACxxxx.MNCmmmm.MCCnnnn.GPRS<br>说明：- xxxx：表示4位十六进制数字。<br>- yyyy：表示4位十六进制数字。<br>- zzzz：表示4位十六进制数字。<br>- mmmm：表示4位十进制数字。<br>- nnnn：表示4位十进制数字。<br>- mmm：表示3位十进制数字。<br>- nnn：表示3位十进制数字。<br>- MNC、MCC格式可参见“DNSFMT（DNS域名组装形式）”的参数描述。<br>- NRI类型中，简化方式不携带RAC、LAC标识，其他字段与标准方式的规则相同。 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“RAI（RAI）”<br>或<br>“LAI（LAI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值 ：无 |
| LACRANGE | 位置区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定位置区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“LAI（LAI）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“位置区域码”的值。<br>- 新添加的位置区域码范围不能与原有的位置区域码范围出现重叠。<br>- 如果该参数不输入，表示配置单个LAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定路由区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“RAI（RAI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |
| RACRANGE | 路由区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码范围。与RAC参数构成一个RAC区段，可以配置连续的路由区域。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“RAI（RAI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>说明：- 如果该参数不输入，表示配置单个RAC。<br>- 相同域名类型的各条配置的RAC区段的覆盖范围是不允许交叉的。<br>- 此参数的取值不小于参数“路由区域码”的值。 |
| NRI | NRI | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定NRI（Net Resource Identify）。NRI用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“NRI（NRI）”<br>后生效。<br>数据来源：整网规划<br>取值范围： 0～1023<br>默认值： 无 |
| NRIRANGE | NRI范围 | 可选必选说明：可选参数<br>参数含义：该参数用来指定NRI范围。与NRI参数构成一个NRI区段，可以配置连续的NRI。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“NRI（NRI）”<br>后生效。<br>数据来源：整网规划<br>取值范围： 0～1023<br>默认值： 无<br>说明：- 如果该参数不输入，表示配置单个NRI。<br>- 相同域名类型的各条配置的NRI区段的覆盖范围是不允许交叉的。<br>- 该参数的取值不小于参数“NRI”的值。 |
| NRINAMEFMT | NRI域名格式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否采用标准的NRI域名格式。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“NRI（NRI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>“STANDARD（标准方式）”<br>、<br>“SIMPLY（简化方式）”<br>默认值： 无 |
| RNCID | RNC ID | 可选必选说明：条件必选参数<br>参数含义：该参数用来指定RNC标识。RNC标识用于在一个PLMN中唯一标识一个RNC。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“RNC_ID（RNC ID）”<br>后生效。<br>数据来源：整网规划<br>取值范围： 0～4096<br>默认值： 无 |
| RNCIDRANGE | RNC ID范围 | 可选必选说明：可选参数<br>参数含义：该参数用来指定RNC标识范围。与RNC标识参数构成一个RNC标识区段，可以配置连续的路由区域。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“RNC_ID（RNC ID）”<br>后生效。<br>数据来源：整网规划<br>取值范围： 0～4096<br>默认值： 无<br>说明：- 如果该参数不输入，表示配置单个RNC。<br>- 相同域名类型的各条配置的RNC标识区段的覆盖范围是不允许交叉的。<br>- 该参数的取值不小于参数“RNC标识”的值。 |
| PLMNID | PLMN ID选择方式 | 可选必选说明：可选参数<br>参数含义：该参数用于在网络共享的场景下可以统一配置PLMNID，以减少重复的DNS配置记录。<br>数据来源：整网规划<br>取值范围：<br>“STANDARD_MODE（标准方式）”<br>、<br>“CUSTOMIZE_MODE（自定义方式）”<br>默认值： 无<br>配置原则:<br>- 选择使用“STANDARD_MODE（标准方式）”，将根据流程消息获取对应的PLMN ID组成域名。<br>- 选择使用“CUSTOMIZE_MODE（自定义方式）”，将根据配置的MNC和MCC组成域名。 |
| MCC | 移动国家代码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定PLMN或HPLMN的移动国家号码。<br>前提条件：该参数在<br>“PLMNID”<br>参数配置为<br>“CUSTOMIZE_MODE（自定义方式）”<br>后生效。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定PLMN或HPLMN的移动网号码。<br>前提条件：该参数在<br>“PLMNID”<br>参数配置为<br>“CUSTOMIZE_MODE（自定义方式）”<br>后生效。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| DNSPOLICY | DNS域名策略 | 可选必选说明：可选参数<br>参数含义：该参数用来指定确定使用的DNS后缀模式。<br>数据来源：整网规划<br>取值范围：<br>“GPRS（.gprs）”<br>、<br>“ORG（.org）”<br>默认值： 无<br>配置原则:<br>- GPRS（.gprs）：该参数用来指定使用的DNS后缀模式为.gprs。格式如：RAC1234.LAC5678.MNC003.MCC123.GPRS<br>- ORG（.org）：该参数用来指定NRI域名格式为.org。格式如：RAC1234.LAC5678.RAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG |
| DNSFMT | DNS域名组装形式 | 可选必选说明：可选参数<br>参数含义：该参数用来指定系统在SGSN间的移动性管理流程中使用的DNS域名格式。<br>前提条件：该参数在<br>“DNSPOLICY”<br>参数配置为<br>“GPRS（.gprs）”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>“ FOUR_DEC_MNC_MCC（4位十进制MNC和MCC）”<br>、<br>“FOUR_HEX_MNC_MCC（4位十六进制MNC和MCC）”<br>、<br>“THREE_DEC_MNC_MCC（3位十进制MNC和MCC）”<br>默认值：无<br>配置原则:<br>- 选择使用“FOUR_DEC_MNC_MCC（4位十进制MNC和MCC）”，配置查询格式：RAC1234.LAC5678.MNC0003.MCC0123.GPRS<br>- 选择使用“FOUR_HEX_MNC_MCC（4位十六进制MNC和MCC）”，配置查询格式：RAC1234.LAC5678.MNC0003.MCC01CC.GPRS<br>- 选择使用“THREE_DEC_MNC_MCC（3位十进制MNC和MCC）”，配置查询格式：RAC1234.LAC5678.MNC003.MCC123.GPRS |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSNDNS]] · SGSN DNS域名策略（SGSNDNS）

## 使用实例

修改一个SGSN DNS域名策略，位置区域码为0x000f，路由区域码为0xf0，路由区域码范围为0xf0，DNS域名策略为ORG（.org）：

**MOD SGSNDNS: DNTYPE=RAI, LAC="0xf", RAC="0xf0", RACRANGE="0xf0", DNSPOLICY=ORG;**

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SGSNDNS.md`
