# 显示GTP-C IP地址接口属性(DSP GTPCINTFATTR)

- [命令功能](#ZH-CN_MMLREF_0000001172225581__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225581__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225581__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225581__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225581__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225581__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225581__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225581)

**适用网元：SGSN、MME、AMF**

该命令用于查询指定用户范围的某接口使用的GTPC IP地址。

#### [注意事项](#ZH-CN_MMLREF_0000001172225581)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225581)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225581)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225581)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_NOID(指定运营商)"后生效。<br>数据来源：本端规划<br>取值范围：0~64,128~254<br>默认值：无 |
| IMSIPRE_DSP | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照输入IMSI最长匹配进行查询，输出包含最长匹配IMSI前缀的记录。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_IMSIPRE(指定IMSI前缀)"后生效。<br>数据来源：本端规划<br>取值范围：1~15位十进制字符串<br>默认值：无 |
| INTFTP | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “SV(Sv)”<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225581)

查询所有用户使用的Gn-GGSN/Gp接口使用的GTPC IP地址信息：

DSP GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=GN-GGSN/GP;

```
%%DSP GTPCINTFATTR: SUBRANGE=ALL_USER, INTFTP=GN-GGSN/GP;%%
RETCODE = 0  操作成功。

输出结果如下
------------------------
    用户范围  =  所有用户
  运行商标识  =  NULL
    IMSI前缀  =  NULL
    接口类型  =  Gn-GGSN/Gp Interface
        组号  =  1
  IP地址类型  =  IPv4
    IPv4地址  =  192.168.20.1
    IPv6地址  =  2001:db8:10:19:44:55:10:12
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225581)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户范围 | 该参数用于指定GTPC IP地址适用的用户范围。 |
| 运营商标识 | 该参数用于指定运营商标识。 |
| IMSI前缀 | 该参数用于指定IMSI前缀。 |
| 接口类型 | 该参数用于指定GTPC IP地址适用的接口类型。<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “SV(Sv)” |
| 组号 | GTPC IP所属的组号，在<br>[**ADD GTPCLE**](../Gtpc本端实体管理/增加GTP-C本地实体(ADD GTPCLE)_26145966.md)<br>命令中配置。 |
| IP地址类型 | 用于指示该地址属于IPv4网络还是IPv6网络 |
| IPv4地址 | 所查询接口使用的IPv4地址。 |
| IPv6地址 | 所查询接口使用的IPv6地址。 |
