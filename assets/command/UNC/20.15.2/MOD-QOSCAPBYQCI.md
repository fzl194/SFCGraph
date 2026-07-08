---
id: UNC@20.15.2@MMLCommand@MOD QOSCAPBYQCI
type: MMLCommand
name: MOD QOSCAPBYQCI（修改基于QCI的Non-GBR承载QoS限制配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: QOSCAPBYQCI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- QoS限制配置
- 基于QCI的承载级QoS限制
status: active
---

# MOD QOSCAPBYQCI（修改基于QCI的Non-GBR承载QoS限制配置）

## 功能

**适用网元：MME**

该命令用于修改根据用户范围和承载QCI配置的QoS限制。

## 注意事项

- 该命令执行后对于新接入的EPS承载立即生效。如果当前用户已经激活了EPS承载，该命令的限制会在用户下一次会话管理业务流程中生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数表示使用QoS限制的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”：指网络中的所有用户。<br>- “IMSI_PREFIX(指定IMSI前缀)：指网络中与指定的IMSI前缀匹配的用户。”<br>- “HOME_USER(本网用户)：指网络中的本网签约用户。”<br>- “FOREIGN_USER(外网用户)：指网络中的漫游用户。”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~15位数字。<br>默认值：无 |
| QCI | QCI | 可选必选说明：必选参数<br>参数含义：对Non-GBR承载（QCI取值为5~9），该参数表示用户签约的承载的QCI；对GBR承载（QCI取值为1~4），该参数表示用户请求或网关下发的承载的QCI。<br>数据来源：整网规划<br>取值范围：1~9<br>默认值：无 |
| LOCALQCI | 本地配置QCI | 可选必选说明：可选参数<br>参数含义：当BYTE_EX_B66 BIT4为“1”时，该参数才会生效，此时<br>**[ADD QOSCAPGBR](../GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md)**<br>或者<br>[**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>中的相关QCI的限制将失效。<br>数据来源：整网规划<br>取值范围：1~9<br>默认值：无<br>配置原则：无<br>说明：- 对Non-GBR承载（QCI取值为5~9），该参数表示用户请求或者签约的承载QCI或者网关下发的承载QCI，如果参数“是否覆盖网关下发的QCI”为“NO”，将下发网关携带QCI；如果参数“是否覆盖网关下发的QCI”为“YES”，将下发“本地配置QCI”给UE。<br>- 对GBR承载（QCI取值为1~4），该参数表示用户请求或网关下发的承载QCI，如果参数“是否覆盖网关下发的QCI”为“NO”，将下发网关携带QCI；如果参数“是否覆盖网关下发的QCI”为“YES”，将下发“本地配置QCI”给UE。<br>- 当参数不输入时默认不生效。 |
| COV | 是否覆盖网关下发的QCI | 可选必选说明：可选参数<br>参数含义：当BYTE_EX_B66 BIT4为“1”且参数“本地配置QCI”为有效值时，该参数才会生效，此时<br>**[ADD QOSCAPGBR](../GBR承载QoS限制/增加GBR承载QoS限制配置(ADD QOSCAPGBR)_26146216.md)**<br>或者<br>[**ADD QOSCAP**](../Non-GBR承载QoS限制/增加Non-GBR承载QoS限制配置(ADD QOSCAP)_72225897.md)<br>中的相关QCI的限制将失效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>配置原则：无<br>说明：如果该参数为<br>“NO”<br>，将下发网关携带QCI；如果该参数为<br>“YES”<br>，将下发<br>“本地配置QCI”<br>给UE。 |
| ARPPRL | ARP的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对Non-GBR承载的ARP优先级别限制。<br>数据来源：整网规划<br>取值范围：1~15<br>默认值：无<br>说明：取值越小，优先级越高。 |
| ARPPCI | ARP的抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对Non-GBR承载的ARP抢占能力限制。<br>数据来源：整网规划<br>取值范围：<br>- “ENABLE（启用）：允许该承载抢占其他ARP的优先级别较低的承载的资源。”<br>- “DISABLE（未启用）：不允许该承载抢占其他ARP的优先级别较低的承载的资源。”<br>默认值：无 |
| ARPPVI | ARP的被抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对Non-GBR承载的ARP被抢占能力限制。<br>数据来源：整网规划<br>取值范围：<br>- “ENABLE（启用）：允许其他优先级别较高的承载抢占该承载的资源。”<br>- “DISABLE（未启用）：不允许其他优先级别较高的承载抢占该承载的资源。”<br>默认值：无 |
| GBRMBRULK | 上行最大速率 (kbps) | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的上行最大速率限制。<br>数据来源：整网规划<br>取值范围：1kbps~65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“上行最大速率 (kbps)”<br>和<br>“上行保证速率 (kbps)”<br>，<br>“上行最大速率 (kbps)”<br>必须大于等于<br>“上行保证速率(kbps)”<br>。<br>说明：“0”为无效值，如果“上行最大速率 (kbps)”修改为“0”上行的最大速率不受限制。 |
| GBRMBRDLK | 下行最大速率 (kbps) | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的下行最大速率限制。<br>数据来源：整网规划<br>取值范围：1kbps~65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“下行最大速率 (kbps)”<br>和<br>“下行保证速率 (kbps)”<br>，<br>“下行最大速率 (kbps)”<br>必须大于等于<br>“下行保证速率(kbps)”<br>。<br>说明：“0”为无效值，如果“下行最大速率 (kbps)”修改为“0”下行的最大速率不受限制。 |
| GBRGBRULK | 上行保证速率 (kbps) | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的上行保证速率限制。<br>数据来源：整网规划<br>取值范围：1kbps~65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“上行最大速率 (kbps)”<br>和<br>“上行保证速率 (kbps)”<br>，<br>“上行最大速率 (kbps)”<br>必须大于等于<br>“上行保证速率(kbps)”<br>。<br>说明：“0”为无效值，如果“上行保证速率 (kbps)”修改为“0”上行的保证速率不受限制。 |
| GBRGBRDLK | 下行保证速率 (kbps) | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统对用户GBR承载的下行保证速率限制。<br>数据来源：整网规划<br>取值范围：1kbps~65000000kbps<br>默认值：无<br>配置原则：如果同时配置了<br>“下行最大速率 (kbps)”<br>和<br>“下行保证速率 (kbps)”<br>，<br>“下行最大速率 (kbps)”<br>必须大于等于<br>“下行保证速率(kbps)”<br>。<br>说明：“0”为无效值，如果“下行保证速率 (kbps)”修改为“0”下行的保证速率不受限制。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于描述配置的QoS限制策略。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [基于QCI的Non-GBR承载QoS限制配置（QOSCAPBYQCI）](configobject/UNC/20.15.2/QOSCAPBYQCI.md)

## 使用实例

运营商修改QoS限制策略，对于IMSI前缀为3080107000，QCI为5的用户，不允许该范围内用户抢占其他ARP的优先级别较低的承载的资源：

MOD QOSCAPBYQCI: SUBRANGE=IMSI_PREFIX, IMSIPRE="3080107000", QCI=5, ARPPCI=DISABLE, ARPPVI=DISABLE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于QCI的Non-GBR承载QoS限制配置(MOD-QOSCAPBYQCI)_72345821.md`
