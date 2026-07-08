# 查询别名APN配置(LST ALIASAPN)

- [命令功能](#ZH-CN_MMLREF_0000001126305496__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305496__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305496__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305496__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305496__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305496__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305496__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305496)

**适用网元：SGSN、MME**

该命令用于查询别名APN（Access Point Name）转换配置。

#### [注意事项](#ZH-CN_MMLREF_0000001126305496)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305496)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305496)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305496)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：待查询的IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据IMSI、“原始APNNI”映射唯一的“转换APNNI”。 |
| OLDAPN | 原始APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约数据进行匹配后的APN NI。<br>取值范围：1～62<br>默认值：无<br>说明：- “原始APNNI”由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。例如“HUAWEI.COM”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305496)

查询所有APN NI转换配置记录：

LST ALIASAPN:;

```
%%LST ALIASAPN:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 用户范围      IMSI 前缀  原始APNNI  转换APNNI  描述
 
 所有用户      NULL       CDMA       ABCD123  NULL
 指定IMSI前缀  12345      WCDMA      ASD123   NULL
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305496)

参见 [**ADD ALIASAPN**](增加别名APN配置(ADD ALIASAPN)_72345281.md) 的参数说明。
