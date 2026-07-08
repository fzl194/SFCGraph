# 增加网络名称(ADD USRMMINFO)

- [命令功能](#ZH-CN_MMLREF_0000001126146058__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146058__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146058__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146058__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146058__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146058__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146058)

**适用网元：SGSN、MME**

该命令用于添加运营商网络名称。在UE接入 UNC 时，如果需要给UE下发网络名称， UNC 判断UE在本命令配置的用户范围，则优选下发本命令配置的网络名称。

#### [注意事项](#ZH-CN_MMLREF_0000001126146058)

- 该命令执行后立即生效。
- 本表最大记录数为1024条。
- 对于4G网络，该命令配置的网络名称在EMM information信元中是否携带由命令[**SET MMFUNC**](../../../移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)中的参数“EMMINFOIEPLY”决定。
- 输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001126146058__tab1)所示：
  *表1 IMSI限定范围*

  | 起始IMSI | 终止IMSI | 实际限定IMSI范围 |
  | --- | --- | --- |
  | 123002666 | 123002 | 增加记录失败，起始IMSI大于终止IMSI |
  | 123002 | 123002666 | 123002000000000 ～ 123002666000000，即区间[123002000000000，123002666000000] |
  | 123002 | 123002 | 增加记录失败，起始IMSI不能等于终止IMSI |
  | 123002000000000 | 123002000000000 | 仅限定IMSI号码123002000000000 |
  | 123003000000000 | 123004000000000 | 123003000000000 ～ 123004000000000，即区间[123003000000000，123004000000000] |
- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与本命令其它记录定义的IMSI号段范围相互交叉、包含或重合。
- 配置生效的优先级：
- 最长 “IMSI_PREFIX(指定IMSI前缀)” 或 “IMSI_RANGE(指定IMSI范围)” 匹配优先级高于 “ALL_USER(所有用户)” ；
-
  如果存在匹配中的记录：

  - 对WB-E-UTRAN和NB-IoT用户：无线侧PLMN匹配中的优先级高于未配置无线侧PLMN；
    - 对GERAN和UTRAN用户：只匹配未配置无线侧PLMN记录。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146058)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146058)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146058)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无<br>说明：“IMSI_PREFIX（指定IMSI前缀）”<br>和<br>“IMSI_RANGE（指定IMSI范围）”<br>取值对应的记录不能同时存在。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：参见<br>“ENDIMSI（终止IMSI）”<br>说明。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：- 输入的起始IMSI必须小于或者等于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。<br>- 判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较。 |
| PLMNPLCY | PLMN匹配策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在给UE下发网络名称时，是否匹配无线侧PLMN，无线侧是多个运营商等场景下，一般需要根据无线侧PLMN给UE下发不同的网络名称，此时配置该参数为YES。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)”<br>说明：- 对GERAN和UTRAN用户匹配时，只根据PLMNPLCY=NO的记录下发。<br>- 对WB-E-UTRAN和NB-IoT用户匹配时，其他条件同等时，PLMNPLCY=YES且PLMN一致的优先级高于PLMNPLCY=NO的记录。<br>- [**ADD TALST**](../../../移动性管理/TA List管理/增加跟踪区列表(ADD TALST)_26305388.md)配置中，同一个跟踪区列表不能同时包含不同PLMN的TAI，否则可能导致网络名称不能及时下发。<br>- 如果系统中存在PLMNPLCY=YES的配置，当WB-E-UTRAN和NB-IoT用户在下列TAU流程中会下发网络名称；如果系统中不存在PLMNPLCY=YES的配置，WB-E-UTRAN和NB-IoT用户在下列TAU流程中不下发网络名称。流程包括：INTER_MME_TAU(MME间TAU)、INTER_RAT_INTER_USN_TAU(USN间异系统类型TAU)、INTER_RAT_INTRA_USN_TAU(USN内异系统类型TAU)、TAU_AFTER_INTER_MME_HANDOVER(MME间切换后的TAU)、TAU_AFTER_INTER_RAT_INTER_USN_HANDOVER(USN间异系统类型TAU)、TAU_AFTER_INTER_RAT_INTRA_USN_HANDOVER(USN内异系统类型切换后的TAU)，无线侧PLMN有变更的INTRA_MME_TAU(MME内TAU)、无线侧PLMN有变更的PERIOD_TAU(周期性TAU) 。 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定无线侧PLMN的移动国家号码。<br>前提条件：该参数在<br>“PLMN匹配策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无<br>说明：该参数仅对WB-E-UTRAN、NB-IoT用户生效。 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定无线侧PLMN的移动网号码。<br>前提条件：该参数在<br>“PLMN匹配策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>说明：该参数仅对WB-E-UTRAN、NB-IoT用户生效。 |
| FULLNAME | 运营商全称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商全称。<br>数据来源：整网规划<br>取值范围：0～79位字符串。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>说明：- GMM information/EMM information消息中携带的“Full name for network”信元值来源于该参数。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商全称不能输入“NULL”，字母不区分大小写。 |
| SHORTNAME | 运营商简称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商简称。<br>数据来源：整网规划<br>取值范围：0～79位字符串。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>说明：- GMM information/EMM information消息中携带的“Short name for network”信元值来源于该参数。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商简称不能输入“NULL”，字母不区分大小写。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126146058)

- 增加IMSI范围为“123456”~“123457”，无线侧PLMN为40101的用户终端的运营商网络名称配置：“运营商全称”为“aaa”，“运营商简称”为“a”：
  ```
  ADD USRMMINFO: SUBRANGE=IMSI_RANGE, BEGIMSI="123456", ENDIMSI="123457", PLMNPLCY=YES, MCC="401", MNC="01", FULLNAME="aaa", SHORTNAME="a";
  ```
- 增加IMSI范围为“123456”~“123457”的用户终端的运营商网络名称配置：“运营商全称”为“bbb”，“运营商简称”为“b”：
  ```
  ADD USRMMINFO: SUBRANGE=IMSI_RANGE, BEGIMSI="123456", ENDIMSI="123457", PLMNPLCY=NO, FULLNAME="bbb", SHORTNAME="b";
  ```
