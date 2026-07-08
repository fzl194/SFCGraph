# 查询激活过程控制参数（LST SMACTCTRL）

- [命令功能](#ZH-CN_MMLREF_0000001172225343__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225343__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225343__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225343__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225343__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225343__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225343__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225343)

**适用网元：SGSN、MME**

该命令用于查询在PDN连接建立流程中使用签约数据匹配的纠正功能涉及到的相关参数。PDN连接建立包括UE发起的ATTACH流程和UE请求的PDN连接建立流程。

#### [注意事项](#ZH-CN_MMLREF_0000001172225343)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225343)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225343)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225343)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定启用功能的用户范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_USER(指定用户)”<br>- “SPECIAL_UETYPE(指定终端类型)”<br>默认值：无<br>说明：- “用户范围”+“IMSI前缀”+“请求APNNI”不能重复。<br>- “用户范围”+“终端类型”+“请求APNNI”不能重复。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定的IMSI前缀<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“SPECIAL_USER(指定用户)”<br>时，才需要配置。<br>取值范围：5~15位十进制数字<br>默认值：无<br>说明：使用时按照IMSI最长匹配进行查询，相同IMSI前缀的原始原因值配置不能相同。 |
| UETYPE | 终端类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定终端类型。<br>UNC<br>需要为这些类型终端设置特定请求信息纠正策略。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“SPECIAL_UETYPE(指定终端类型)”<br>时，才需要配置。<br>数据来源：整网规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无<br>说明：“终端类型”<br>需要在<br>[**ADD SMACTIMEILIB**](增加IMEI库记录（ADD SMACTIMEILIB）_26305474.md)<br>中配置。 |
| APNTYPE | UE请求的APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定请求APNNI类型。<br>取值范围：<br>- “ALL_APN(所有APN)”<br>- “NULL_APN(空APN)”<br>- “NOT_NULL_APN(非空APN)”<br>- “SPECIAL_APN(指定APN)”<br>默认值：无<br>说明：- 请求APNNI为空时，选择“NULL_APN”。<br>- 请求APNNI为非空时，选择“NOT_NULL_APN”。<br>- 请求APNNI为指定APN时，选择“SPECIAL_APN”。<br>- 请求APNNI包括空APN和非空APN时，选择“ALL_APN”。 |
| APNNI | APNNI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定APN网络标识。<br>前提条件：该参数在<br>“APNTYPE”<br>参数设置为<br>“SPECIAL_APN(指定APN)”<br>时，才需要配置。<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225343)

查询所有激活过程控制参数记录：

LST SMACTCTRL:;

```
%%LST SMACTCTRL:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
                          用户范围  =  指定用户
                          IMSI前缀  =  123456
                          终端类型  =  NULL
                     UE请求的APNNI  =  空APN
                             APNNI  =  NULL
                          处理策略  =  签约数据匹配失败后进行纠正
                      PDP Type纠正  =  否
                   PDP Address纠正  =  否
                      单组签约数据  =  不纠正
                      多组签约数据  =  不纠正
                  野卡签约数据策略  =  标准
               请求APNNI的处理策略  =  标准方式
                优选非野卡签约数据  =  否
使用Context ID最小的非野卡签约数据  =  否
               只允许使用公共APNNI  =  否
                  限制野卡激活数目  =  否
                  PDP/PDN Type策略  =  IPv4
                    APN纠错CHR上报  =  否
                     要求签约APNNI  =  NULL
                         回落APNNI  =  NULL
                         是否启用扩展拒绝策略  =  是
                         Gb模式扩展拒绝流程  =  PDP Context Activation&Inter RAU
                         Iu模式扩展拒绝流程  =  PDP Context Activation&Inter RAU&Inter SRNS Relocation
                         S1模式扩展拒绝流程  =  Attach&Inter HO&Inter TAU&UE Requested PDN Connectivity         
                     是否启用定制APN纠正策略 = NO
                               本地APNNI组号 = 0
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225343)

请参考命令 [**ADD SMACTCTRL**](增加激活过程控制参数（ADD SMACTCTRL）_26305472.md) 的参数标识。
