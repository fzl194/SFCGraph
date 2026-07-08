# 增加APNNI库记录（ADD APNNILIB）

- [命令功能](#ZH-CN_MMLREF_0000001126145736__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145736__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145736__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145736__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145736__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145736__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145736)

**适用网元：SGSN**

此命令用于增加APNNI库记录。APNNI库是用户请求的APNNI或签约数据中的APNNI和终端类型的对应关系表，用于通过用户请求的APNNI或签约数据中的APNNI识别智能终端类型。

当需要增加一条APNNI和终端类型的对应记录时，需要执行此命令。

#### [注意事项](#ZH-CN_MMLREF_0000001126145736)

- 此命令执行后立即生效。
- 本表最大记录数为256条。
- 添加APNNI对应的终端类型记录后，要使用基于终端类型的性能统计功能，还需要加载License项“Smartphone话务模型统计”。
- 用户请求的APNNI和终端类型的对应关系记录最多能添加128条。签约数据中的APNNI和终端类型的对应关系记录最多也只能添加128条。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145736)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145736)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145736)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于设置PDP激活请求中携带的APNNI或者签约数据中的APNNI。<br>数据来源：本端规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- 每条记录中的“APNNI”字段不能重复。<br>- “APNNI”（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| APNTYPE | APN类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定根据PDP激活请求中携带的APNNI或是签约数据中的APNNI来识别UE。<br>数据来源：本端规划<br>取值范围：<br>- “REQUEST_APN(请求APN)”<br>- “SUBSCRIBED_APN(签约APN)”<br>默认值：无<br>配置原则：<br>- 选择类型为“REQUEST_APN(请求APN)”时，即此请求APNNI识别的用户终端启用Smartphone相关功能。<br>- 选择类型为“SUBSCRIBED_APN(签约APN)”时，即此签约APNNI识别的用户终端启用Smartphone相关功能。 |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置请求APNNI或签约APNNI对应的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无 |
| UEDESC | 终端详细信息 | 可选必选说明：可选参数<br>参数含义：该参数是对终端类型的详细描述。<br>数据来源：本端规划<br>取值范围：长度为255位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145736)

增加一条APNNI为huawei1，APN类型为请求APN，终端类型为Android的APNNI库记录：

ADD APNNILIB: APNNI="huawei1", APNTYPE=REQUEST_APN, UETYPE=ANDROID;
