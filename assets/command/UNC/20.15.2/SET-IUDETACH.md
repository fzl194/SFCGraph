---
id: UNC@20.15.2@MMLCommand@SET IUDETACH
type: MMLCommand
name: SET IUDETACH（设置Iu分离非活动用户参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IUDETACH
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 分离非活动用户
- Iu模式分离非活动用户参数
status: active
---

# SET IUDETACH（设置Iu分离非活动用户参数）

## 功能

**适用网元：SGSN**

此命令用于设置3G分离非活动用户配置参数。当用户通过附着或路由区更新流程接入到本SGSN后，如果在指定时长(大于 “非活动用户分离定时器(分)” 时长)没有PDP（Packet Data Protocol）激活，则认为该用户为非活动用户对用户进行分离操作；当系统将用户判断为非活动用户进行分离后，如果用户马上重新附着且与上次分离的时间间隔不超过配置的 “永久在线识别定时器长(秒)” 时长， 则该用户被定义为永久在线用户，后续系统不会对该用户进行分离非活动用户操作。SGSN发起分离非活动用户的流程，可以释放这些用户的空闲资源，以支持更多的用户。分离非活动用户的参数设置需要符合运营商的控制策略。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DETACHSW | 非活动用户分离 | 可选必选说明：可选参数<br>参数含义：该参数用于指定当用户处于非活动状态时，是否执行分离操作。该参数为分离非活动用户总开关，只有该开关打开时，后续参数功能才能生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“NO(否)”<br>。<br>说明：- 当参数设置为“YES(是)”时，“主动分离未激活用户”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-106205，License部件编码：LKV2DTUSR02）。 |
| NACTTMR | 非活动用户分离定时器（分） | 可选必选说明：可选参数<br>参数含义：该定时器用于控制当用户处于非活动状态时，等待分离操作所需的时长。用户附着或路由更新完成后其未激活PDP时长超过本定时器时长，则SGSN将在用户进行下一次INTRA SGSN RAU时发起分离用户的流程。<br>前提条件：该参数在<br>“DETACHSW”<br>设置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0分~1440分<br>系统初始设置值：360分。<br>说明：该参数取值为0分时，表示不分离用户。 |
| DETACHONFOR | 是否在Follow-on时启用分离非活动用户功能 | 可选必选说明：可选参数<br>参数含义：该参数用于控制当用户设置了Follon-on request标志时，是否启用分离非活动用户功能。<br>QChat UE发起附着请求时会携带Follon-on request字段。<br>前提条件：该参数在<br>“DETACHSW”<br>设置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“NO(否)”<br>。 |
| DETACHONCONN | 保留参数1 | 可选必选说明：可选参数<br>参数说明：该参数为保留参数，暂未实现。 |
| NACTTMRONCONN | 保留参数2 | 可选必选说明：可选参数<br>参数说明：该参数为保留参数，暂未实现。 |
| REATM | 保留参数3 | 可选必选说明：可选参数<br>参数说明：该参数为保留参数，暂未实现。 |
| ONLINETIMER | 永久在线识别定时器长（秒） | 可选必选说明：可选参数<br>参数说明：该参数用于设置识别用户是否永久在线的时长。非永久在线用户附着请求被接收时，如果其上次分离原因为“非活动分离”，且当前附着与上次分离时间间隔不超过该参数设定的值，则将该用户设置为永久在线。<br>前提条件：该参数在<br>“DETACHSW”<br>设置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1秒~65536秒<br>系统初始设置值：60秒。 |
| ONLINEFOREVER | 永久在线识别 | 可选必选说明：可选参数<br>参数说明：该参数用于指定是否识别永久在线用户。<br>前提条件：该参数在<br>“DETACHSW”<br>设置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“NO(否)”<br>。<br>说明：该参数的取值与性能指标“Iu模式 永久在线用户数”无关。无论此开关是否打开，只要“非活动用户分离”取值为“YES”，系统都会对用户是否为永久在线用户进行判断进而对“Iu模式 永久在线用户数”进行统计。 |
| IMPDTCHNORSP | 是否在分离响应超时后分离用户 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否在非活动用户分离响应超时后，隐式分离用户或不分离用户。<br>前提条件：该参数在<br>“DETACHSW”<br>设置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“YES(是)”<br>。 |
| IMPDTCH | 分离用户方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一般场景下非活动用户的分离方式。<br>前提条件：该参数在<br>“DETACHSW”<br>设置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：<br>- “IMPLICITLY(IMPLICITLY)”：表示隐式分离用户。<br>- “EXPLICITLY(EXPLICITLY)”：表示显式分离用户。<br>系统初始设置值：<br>“IMPLICITLY(IMPLICITLY)”<br>。 |
| IMPIUONNONACT | 保留参数4 | 可选必选说明：可选参数<br>参数说明：该参数为保留参数，暂未实现。 |
| IMPONIUREL | 保留参数5 | 可选必选说明：可选参数<br>参数说明：该参数为保留参数，暂未实现。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IUDETACH]] · Iu分离非活动用户参数（IUDETACH）

## 使用实例

设置在Iu连接保持状态时超过1440分钟后分离非活动用户，对携带Follow-on-request字段的用户不启用分离非活动用户功能：

SET IUDETACH: DETACHSW=YES, NACTTMR=1440, DETACHONFOR=NO, DETACHONCONN=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IUDETACH.md`
