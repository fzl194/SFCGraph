---
id: UNC@20.15.2@MMLCommand@MOD S1IMEICFG
type: MMLCommand
name: MOD S1IMEICFG（修改S1模式IMEI配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: S1IMEICFG
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 设备检查管理
- S1模式IMEI配置
status: active
---

# MOD S1IMEICFG（修改S1模式IMEI配置）

## 功能

![](修改S1模式IMEI配置(MOD S1IMEICFG)_26145638.assets/notice_3.0-zh-cn_2.png)

此命令可能会导致用户因IMEI校验失败无法接入。

**适用网元：MME**

该命令用于修改EUTRAN用户获取和检查IMEI的策略。

## 注意事项

- 该命令执行后立即生效。
- 此命令可修改EUTRAN所有用户的默认IMEI配置，也可修改指定号段用户的IMEI配置。
- 该表最多包含128条记录。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约用户的范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：需要修改或者删除已通过<br>[**ADD S1IMEICFG**](增加S1模式IMEI配置(ADD S1IMEICFG)_26305448.md)<br>命令配置的用户范围为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>、IMSI前缀为<br>“ALL_USER”<br>的记录时，需要执行<br>**MOD/RMV S1IMEICFG**<br>命令，用户范围设置为<br>“ALL_USER（所有用户）”<br>。 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>配置原则：起始IMSI要小于终止IMSI。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI<br>前提条件：只有<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>配置原则：终止IMSI要大于起始IMSI。 |
| GETIMEIPLC | IMEI获取策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指示网络侧是否需要获取用户设备标识。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不获取)”<br>- “IMEI（获取IMEI）”<br>- “IMEISV(获取IMEISV)”<br>默认值：无<br>配置原则：建议值为<br>“NO(不获取)”<br>。<br>说明：当此参数配置为IMEISV时，会优先获取IMEISV，如果获取失败，会通过身份识别流程获取IMEI。 |
| CHKIMEIPLC | IMEI检查策略 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示网络侧是否需要检查用户设备标识。<br>前提条件：设置本参数之前需要将<br>“IMEI获取策略”<br>参数设置为<br>“IMEI（获取IMEI）”<br>或<br>“IMEISV(获取IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO(不检查)”<br>- “IMEI(检查IMEI)”<br>- “IMEISV(检查IMEISV)”<br>默认值：无<br>配置原则：建议值为<br>“NO(不检查)”<br>。<br>说明：- 当参数设置为“IMEI(检查IMEI)”或“IMEISV(检查IMEISV)”时，“IMEI检查”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-103004，License部件编码：LKV2EIR02）。 |
| ITTYPE | EIR接口类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示给EIR发的CHECK IMEI消息通过的是Gf还是S13接口。<br>前提条件：设置本参数之前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI(检查IMEI)”<br>或<br>“IMEISV(检查IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “Gf(Gf)”<br>- “S13(S13)”<br>- “N17(N17)”<br>默认值：无<br>配置原则：建议值为<br>“Gf(Gf)”<br>。 |
| IMEIACCESS | IMEI获取失败是否允许接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示当获取IMEI失败时是否允许用户接入。获取IMEI失败包括无响应、返回no identity、返回非法等场景。<br>前提条件：设置本参数之前需要将<br>“IMEI获取策略”<br>参数设置为<br>“IMEI(获取IMEI)”<br>或<br>“IMEISV(获取IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| CTFLAG | IMEI检查超时是否允许接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示CHECK IMEI无响应或CHECK IMEI时不存在有效的IMEI时是否允许用户接入。<br>前提条件：设置本参数之前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI(检查IMEI)”<br>或<br>“IMEISV(检查IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| GRALLOW | 是否允许灰名单用户接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于对手机用户执行CHECK IMEI流程后，对于处于灰名单的手机用户是否允许接入。<br>前提条件：设置本参数之前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI(检查IMEI)”<br>或<br>“IMEISV(检查IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| BLALLOW | 是否允许黑名单用户接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于对手机用户执行CHECK IMEI流程后，对于处于黑名单的手机用户是否允许接入。<br>前提条件：设置本参数之前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI(检查IMEI)”<br>或<br>“IMEISV(检查IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| USERERR | 是否允许EIR返回用户原因失败时接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示EIR返回的Check IMEI响应消息中携带User error信元时是否允许用户接入。<br>前提条件：设置本参数之前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI(检查IMEI)”<br>或<br>“IMEISV(检查IMEISV)”<br>，且需要将<br>“EIR接口类型”<br>参数设置为<br>“Gf(Gf)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| PROVIDERR | 是否允许EIR返回设备原因失败时接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示EIR返回的Check IMEI响应消息中携带Provider error信元时是否允许用户接入。<br>前提条件：设置本参数之前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI(检查IMEI)”<br>或<br>“IMEISV(检查IMEISV)”<br>，且需要将<br>“EIR接口类型”<br>参数设置为<br>“Gf(Gf)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| S13FAIL | 是否允许EIR返回失败时接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示S13口IMEI检查失败时是否允许用户接入。<br>前提条件：设置本参数前需要将<br>“是否检查用户的IMEI”<br>参数设置为<br>“IMEI（检查IMEI）”<br>或<br>“IMEISV(检查IMEISV)”<br>，且需要将<br>“EIR接口类型”<br>参数设置为<br>“S13(S13)”<br>或<br>“N17(N17)”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无<br>配置原则：建议值为<br>“YES（是）”<br>。 |
| EIROUTTIMER | EIR响应超时时长 | 可选必选说明：条件可选参数<br>参数含义：在发送Check IMEI Request消息给EIR的时候，启动定时器，时长按照EIROUTTIMER给定的长度设置，在收到Check IMEI Response的时候停止定时器，如果定时器超时，则根据参数CTFLAG决定是否允许用户接入。<br>前提条件：设置本参数前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI（检查IMEI）”<br>或<br>“IMEISV(检查IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：1s～15s<br>默认值：无<br>配置原则：建议值为5s。 |
| CHKIMEITHRESHOLD | IMEI检查上限 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定当IMEI未改变时，每多少次Attach流程<br>UNC<br>发起一次CHECK IMEI，以减少和EIR之间的信令交互。<br>前提条件：设置本参数前需要将<br>“IMEI检查策略”<br>参数设置为<br>“IMEI（检查IMEI）”<br>或<br>“IMEISV(检查IMEISV)”<br>。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值：无<br>配置原则：建议值为0。<br>说明：- 当“IMEI检查策略”参数为“IMEI（检查IMEI）”或“IMEISV(检查IMEISV)”时，用户通过IMSI Attach或者Inter Attach/TAU流程第一次接入系统，UNC必然发起CHECK IMEI，不受此参数控制。<br>- “0”表示IMEI未改变的Attach流程不需要发起CHECK IMEI流程。 |
| ABORTERR | 是否允许底层原因失败时接入 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示在Check IMEI流程中，EIR回复P-ABORT消息或由于底层错误导致流程终止时，是否允许用户接入。<br>前提条件：设置本参数前需要将<br>“EIR接口类型”<br>参数设置为<br>“Gf”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S1模式IMEI配置策略名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1IMEICFG]] · S1模式IMEI配置（S1IMEICFG）

## 使用实例

修改IMSI前缀为“123456”的EUTRAN用户的IMEI配置，获取IMEISV，检查IMEI，EIR接口类型为Gf，IMEI获取失败允许接入，IMEI检查超时允许接入，允许灰名单用户接入，不允许黑名单用户接入，不允许EIR返回用户原因失败时接入，允许EIR返回设备原因失败时接入，EIR响应超时时长为5，IMEI未改变时Attach流程不需要检查IMEI，对应USRGRP2：

MOD S1IMEICFG:SUBRANGE=IMSI_PREFIX, IMSIPRE="123456",GETIMEIPLC=IMEISV,CHKIMEIPLC=IMEI,ITTYPE=Gf,IMEIACCESS=YES,CTFLAG=YES,GRALLOW=YES,BLALLOW=NO,USERERR=NO,PROVIDERR=YES,EIROUTTIMER=5,CHKIMEITHRESHOLD=0, DESC="FOR USRGRP2";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-S1IMEICFG.md`
