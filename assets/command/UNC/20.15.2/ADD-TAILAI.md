---
id: UNC@20.15.2@MMLCommand@ADD TAILAI
type: MMLCommand
name: ADD TAILAI（增加TAI与LAI对应关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TAILAI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- TAI与LAI对应关系
status: active
---

# ADD TAILAI（增加TAI与LAI对应关系）

## 功能

**适用网元：MME**

该命令用于增加TAI与LAI的对应关系。在启用CSFB功能时，MME可以根据TAI获得对应的LAI。

## 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为10000。
- “起始TAI”、“用户范围”和“IMSI前缀”或“起始IMSI”的组合确定唯一一条TAI与LAI的对应关系记录。
- LAI可以重复，一个LAI可对应多个TAI区间。
- 针对用户群的TAI可以重复，同一个TAI或者同一连续TAI区段，“IMSI前缀”或“起始IMSI”不同可以对应不同LAI。
- 同一个TAI或者同一连续TAI区段，只允许配置一条“用户范围”为“ALL_USER（所有用户）”的记录。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE（打开）”，具体相关特性请参考参数的说明。
- 输入的起始IMSI必须小于或者等于终止IMSI。判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时， 将该IMSI补足0到规定长度后进行大小比较，且起始IMSI必须小于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。 对于系统规定IMSI长度为15的情况，如[表1](#ZH-CN_MMLREF_0000001172345017__tab1)所示：
  *表1 IMSI限定范围*

  | 起始IMSI | 终止IMSI | 实际限定IMSI范围 |
  | --- | --- | --- |
  | 123002666 | 123002 | 增加记录失败，起始IMSI大于终止IMSI |
  | 123002 | 123002666 | 123002000000000 ~ 123002666000000，即区间[123002000000000， 123002666000000] |
  | 123002 | 123002 | 增加记录失败，起始IMSI不能等于终止IMSI |
  | 123002000000000 | 123002000000000 | 仅限定IMSI号码123002000000000 |
  | 123003000000000 | 123004000000000 | 123003000000000 ~ 123004000000000，即区间[123003000000000， 123004000000000] |
- 输入的起始IMSI和终止IMSI定义的IMSI号段范围不允许与其它记录定义的IMSI号段范围相互交叉、包含或重合。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BGNTAI | 起始TAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个起始跟踪区。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无<br>配置原则：<br>- 起始TAI由MCC，MNC，TAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足补0。<br>- 新增的TAI区间不能和TAILAI表中已有的TAI区间存在交集。<br>- 需要配置系统缺省LAI记录，则输入的TAI为“FFFFFFFFFF”。 |
| ENDTAI | 终止TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个终止跟踪区。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无<br>配置原则：<br>- 终止TAI由MCC，MNC，TAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足补0。<br>- 输入参数终止TAI要大于或等于起始TAI。<br>- 如果未输入终止TAI或输入值等于起始TAI，则表示某个固定的TAI。<br>- 新增的TAI区间不能和TAILAI表中已有的TAI区间存在交集。 |
| SELMODE | 选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示选择LAI的匹配模式。<br>数据来源：整网规划<br>取值范围：<br>- “SUBRANGE(用户范围)”：匹配IMSI号段的用户。<br>- “HOST(主机名)”：匹配HSS主机名的用户。<br>- “REALM(域名)”：匹配HSS域名的用户。<br>默认值：“SUBRANGE(用户范围)”<br>配置原则：当用户能够匹配多条选择模式时，优先选择HOST(主机名)，次选REALM(域名)，再次选SUBRANGE(用户范围)对应的配置。 |
| HOST | 主机名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户HSS的主机名。<br>前提条件：该参数在“<br>**选择模式**<br>”参数设置为“HOST(主机名)”时，才需要配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置字符串“null”。 |
| REALM | 域名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户HSS的域名。<br>前提条件：该参数在“<br>**选择模式**<br>”参数设置为“REALM(域名)”时，才需要配置。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。<br>默认值：无<br>配置原则:<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”，不区分大小写。例如：epc.mnc123.mcc123.3gppnetwork.org。<br>- 不允许配置以“null”开头的字符串。 |
| SUBRANGE | 用户范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定用户的范围。<br>前提条件：该参数在“<br>**选择模式**<br>”参数设置为“SUBRANGE(用户范围)”时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：无匹配IMSI前缀的所有用户。<br>- “IMSI_PREFIX（指定IMSI前缀）”：IMSI前缀最长长度优先匹配的用户。<br>- “IMSI_RANGE（指定IMSI范围）”:IMSI范围匹配用户<br>默认值：<br>“ALL_USER（所有用户）”<br>配置原则：<br>说明：- 当存在“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”的记录时，不允许再添加“用户范围”为“IMSI_RANGE（指定IMSI范围）”的记录。同理，当存在“用户范围”为“IMSI_RANGE（指定IMSI范围）”的记录时，不允许再添加“用户范围”为“IMSI_PREFIX（指定IMSI前缀）”的记录。<br>- 当开启“WSFD-102505 基于CSFB的Multi PLMN”特性时，系统会按照“IMSI_PREFIX（指定IMSI前缀）”记录或“IMSI_RANGE（指定IMSI范围）”记录优先匹配。<br>- 当关闭“WSFD-102505 基于CSFB的Multi PLMN”特性时，“IMSI_PREFIX（指定IMSI前缀）”记录和“IMSI_RANGE（指定IMSI范围）”记录均不会生效。<br>- 当关闭“WSFD-102505 基于CSFB的Multi PLMN”特性时，并且存在“IMSI_RANGE（指定IMSI范围）”记录和“ALL_USER（所有用户）”记录时，由软参BYTE_EX_B24 BIT6控制配置生效方式。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15位的数字<br>默认值：无<br>说明：- 当“用户范围”设置为“IMSI_PREFIX（指定IMSI前缀）”时，基于CSFB的Multi PLMN特性相关的license授权并开启后，此参数配置才生效（特性编号：WSFD-102505，License部件编码：LKV2CSFB04）。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_RANGE（指定IMSI范围）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字字符串<br>默认值：无<br>配置原则：当起始IMSI与终止IMSI长度全为15位时，起始IMSI要小于等于终止IMSI，否则起始IMSI要小于终止IMSI。<br>说明：- 当“用户范围”设置为“IMSI_RANGE（指定IMSI范围）”时，基于CSFB的Multi PLMN特性相关的license授权并开启后，此参数配置才生效（特性编号：WSFD-102505，License部件编码：LKV2CSFB04）。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_RANGE（指定IMSI范围）”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字字符串<br>默认值：无<br>配置原则：当终止IMSI与起始IMSI长度全为15位时，终止IMSI要大于等于起始IMSI，否则终止IMSI要大于起始IMSI。 |
| LAI | LAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区标识，标识一个位置区。<br>前提条件：<br>在“MML命令行-UNC”窗口上执行命令<br>[**ADD LAIVLR**](../LAI与VLR号对应关系/增加LAI与VLR号对应关系(ADD LAIVLR)_72345015.md)<br>设置此参数。<br>数据来源：整网规划<br>取值范围：9～10位的字符串<br>默认值：无<br>配置原则：<br>- LAI由MCC，MNC，LAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- LAC编码为16进制数，固定为4位，不足补0。<br>- LAI可以重复，一个LAI可对应多个TAI区间。 |

## 操作的配置对象

- [TAI与LAI对应关系（TAILAI）](configobject/UNC/20.15.2/TAILAI.md)

## 使用实例

1. 增加 “起始TAI” 为 “308014101” ， “终止TAI” 为 “308014103” ， “用户范围” 为 “ALL_USER（所有用户）” ， “LAI” 为 “308010001” 的TAI与LAI对应关系：
  ADD TAILAI: BGNTAI="308014101", ENDTAI="308014103", SUBRANGE=ALL_USER, LAI="308010001";
2. 增加 “起始TAI” 为 “308015101” ， “用户范围” 为 “IMSI_PREFIX（指定IMSI前缀）” ， “IMSI前缀” 为 “12345” ， “LAI” 为 “308010002” 的TAI与LAI对应关系：
  ADD TAILAI: BGNTAI="308015101", SUBRANGE=IMSI_PREFIX, IMSIPRE="12345", LAI="308010002";
3. 增加 “起始TAI” 为 “308015101” ， “用户范围” 为 “IMSI_PREFIX（指定IMSI前缀）” ， “IMSI前缀” 为 “67890” ， “LAI” 为 “308020003” 的TAI与LAI对应关系：
  ADD TAILAI: BGNTAI="308015101", SUBRANGE=IMSI_PREFIX, IMSIPRE="67890", LAI="308020003";
4. 增加 “起始TAI” 为 “308015101” ， “用户范围” 为 “IMSI_RANGE（指定IMSI范围）” ， “起始IMSI” 为 “567890” ， “终止IMSI” 为 “567892” ， “LAI” 为 “308020003” 的TAI与LAI对应关系：
  ADD TAILAI: BGNTAI="308015101", SUBRANGE=IMSI_RANGE, BEGIMSI="567890",ENDIMSI="567892", LAI="308020003";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加TAI与LAI对应关系(ADD-TAILAI)_72345017.md`
