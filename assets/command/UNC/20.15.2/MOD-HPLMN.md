---
id: UNC@20.15.2@MMLCommand@MOD HPLMN
type: MMLCommand
name: MOD HPLMN（修改本地PLMN）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: HPLMN
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
- 网络管理
- 归属网络运营商管理
- MNO管理
- MNO网络配置表
status: active
---

# MOD HPLMN（修改本地PLMN）

## 功能

**适用网元：SGSN、MME**

此命令用于修改归属PLMN的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：待修改HPLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：待修改HPLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| SM | 是否允许SM业务 | 可选必选说明：可选参数<br>参数含义：待修改是否允许这个PLMN用户使用会话业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“YES(允许)”<br>。 |
| MAXSMNUM | 最大承载数 | 可选必选说明：条件可选参数<br>参数含义：待修改根据运营商业务规划对应的用户最多建立的承载个数。用户请求建立的承载个数不能超过该值，超过则会建立失败。<br>前提条件：该参数在<br>“SM”<br>参数设置为<br>“YES(允许)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～11<br>默认值：无<br>配置原则：建议值为11。 |
| SMS | 是否允许SMS业务 | 可选必选说明：可选参数<br>参数含义：待修改是否允许HPLMN用户使用短消息业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“YES(允许)”<br>。 |
| SMSCR | 是否允许纠正短消息中心 | 可选必选说明：条件可选参数<br>参数含义：待修改是否允许HPLMN用户使用纠正短消息中心业务。<br>前提条件：该参数在<br>“SMS”<br>参数设置为<br>“YES(允许)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“NO(不允许)”<br>。 |
| SMSCT | 纠正后的短消息中心 | 可选必选说明：条件必选参数<br>参数含义：待修改纠正后的短消息中心。<br>前提条件：该参数在<br>“SMSCR”<br>参数设置为<br>“YES(允许)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：1～15<br>默认值：无 |
| LCS | 是否允许LCS业务 | 可选必选说明：可选参数<br>参数含义：待修改是否允许这个PLMN用户使用2G/3G的LCS业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：建议值为<br>“YES(允许)”<br>。 |
| S5S8TYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：待修改运营商在S5/S8接口使用的协议类型。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”：表示S5/S8口使用GTP协议。<br>- “PMIP(PMIP)”：表示S5/S8口使用PMIP协议。<br>默认值：无<br>配置原则：建议值为<br>“GTP(GTP)”<br>。 |
| PLMNN | 运营商名称 | 可选必选说明：可选参数<br>参数含义：待修改标识运营商名称。<br>数据来源：整网规划<br>取值范围：1～50位字符串<br>默认值：无 |
| EMCBS | 是否允许紧急呼叫业务 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否允许使用紧急呼叫业务。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不允许)”<br>- “YES(允许)”<br>默认值：无<br>配置原则：如果不支持VOLTE紧急呼叫业务，期望在CS域做紧急呼叫时，建议配置为<br>“NO（不允许）”<br>。 |
| EMGCNUMSW | 紧急号码下发开关 | 可选必选说明：可选参数<br>参数含义：该参数用来控制系统在给本网用户发送Attach Accept、TAU Accept、RAU Accept消息时，是否将紧急号码携带在消息中发送给UE。<br>数据来源：整网规划<br>取值范围：<br>- “ON(开启)”<br>- “OFF(关闭)”<br>默认值：无<br>配置原则：当本参数设置为<br>“ON(开启)”<br>时，系统将在Attach Accept、TAU Accept、RAU Accept消息中给本网用户发送紧急号码列表。其中，紧急号码列表来源于ADD EMGCNUM中的配置，如果ADD EMGCNUM没有配置，则不下发紧急号码。<br>说明：紧急号码下发还受其它配置（SET MMFUNC中EMNUM参数、DWORD_EX6 BIT10、DWORD_EX6 BIT11、DWORD_EX33 BIT13、DWORD_EX33 BIT12）控制，共同决策是否下发紧急号码。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HPLMN]] · 本地PLMN（HPLMN）

## 使用实例

修改一个移动国家号为460，移动网号为00，不允许SM业务，不允许SMS业务，协议类型为GTP的HPLMN：

MOD HPLMN: MCC="460", MNC="00", SM=NO, SMS=NO, S5S8TYPE=GTP, PLMNN="noname";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改本地PLMN(MOD-HPLMN)_26305884.md`
