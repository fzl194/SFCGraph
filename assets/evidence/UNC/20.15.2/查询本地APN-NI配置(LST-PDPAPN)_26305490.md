# 查询本地APN NI配置(LST PDPAPN)

- [命令功能](#ZH-CN_MMLREF_0000001126305490__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305490__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305490__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305490__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305490__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305490__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305490__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305490)

**适用网元：SGSN、MME**

该命令用于查询指定用户PDP类型与APN NI地址的映射关系。

UNC 中一次激活场景和MME中PDN连接建立场景，用户匹配到野卡或者匹配到多组签约数据时，需要根据IMSI和PDP/PDN类型查询本地的APN NI。

#### [注意事项](#ZH-CN_MMLREF_0000001126305490)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305490)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305490)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305490)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据<br>“IMSI前缀 ”<br>、<br>“PDP/PDN类型”<br>映射唯一的<br>“APN NI”<br>。 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定所要查询的IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据<br>“IMSI ”<br>、<br>“PDP/PDN类型”<br>映射唯一的<br>“APN NI”<br>。 |
| PDPTYPE | PDP/PDN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDP类型。<br>取值范围：<br>- “PT_IPV4(IPV4协议)”：表示用户激活的PDP类型为IPV4协议。<br>- “PT_IPV6(IPV6协议)”：表示用户激活的PDP类型为IPV6协议。<br>- “PT_PPP(点对点通信协议)”：表示用户激活的PDP类型为点对点通信协议。<br>- “PT_IPV4_IPV6(IPV4和IPV6协议)”：表示用户激活的PDP类型为IPV4和IPV6协议。<br>- “PT_ALL(所有类型)”：表示用户激活的PDP类型为所有类型，不包含Non-IP类型。<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305490)

查询所有记录

LST PDPAPN:;

```
%%LST PDPAPN:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
   用户范围  =  指定IMSI前缀
   IMSI前缀  =  11111111
PDP/PDN类型  =  IPV4协议
     APN NI  =  2222
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305490)

请参考 [**ADD PDPAPN**](增加本地APN NI配置(ADD PDPAPN)_72345275.md) 命令的参数标识。
