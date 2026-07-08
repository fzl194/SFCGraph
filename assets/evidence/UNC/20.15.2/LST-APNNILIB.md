# 查询APNNI库记录（LST APNNILIB）

- [命令功能](#ZH-CN_MMLREF_0000001126305546__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305546__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305546__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305546__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305546__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305546__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305546__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305546)

**适用网元：SGSN**

该命令用于查询APNNI库记录。APNNI库是用户请求的APNNI或签约数据中的APNNI和终端类型的对应关系表。

#### [注意事项](#ZH-CN_MMLREF_0000001126305546)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305546)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305546)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305546)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELMODE | 选择方式 | 可选必选说明：可选参数<br>参数含义：该参数用于选择APNNI库记录的查询方式。<br>取值范围：<br>- “APNNI(APNNI)”<br>- “UE_TYPE(终端类型)”<br>- “ALL(所有)”<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：条件必选参数<br>参数含义：该参数为用于查询APNNI库记录的请求APNNI或签约APNNI。<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- 当“SELMODE（选择方式）”选择为“APNNI(APNNI)”时，此参数才生效。<br>- “APNNI”（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |
| UETYPE | 终端类型 | 可选必选说明：条件必选参数<br>参数含义：该参数为用于查询APNNI库记录的终端类型。<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>默认值：无<br>说明：当<br>“SELMODE（选择方式）”<br>选择为<br>“UE_TYPE(终端类型)”<br>时，此参数才生效。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305546)

查询所有APNNI库记录：

LST APNNILIB:;

```
%%LST APNNILIB:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 APNNI       APN类型  终端类型  终端详细信息

 HUAWEI.COM  请求APN  Android   huawei      
 HUAWEI.CN   签约APN  Windows   cn          
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305546)

参见 [**ADD APNNILIB**](增加APNNI库记录（ADD APNNILIB）_26145736.md) 命令的参数说明。
