# 查询IMSI Direct Tunnel配置(LST IMSIDT)

- [命令功能](#ZH-CN_MMLREF_0000001126305858__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305858__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305858__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305858__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305858__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305858__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305858__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305858)

**适用网元：SGSN**

此命令用于查询IMSI DT属性信息表中的某个IMSI的DT属性信息。

#### [注意事项](#ZH-CN_MMLREF_0000001126305858)

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC、GGSN和APNNI支持DT功能。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305858)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305858)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305858)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>- “IMSI_RANGE（指定IMSI范围）”<br>默认值：无<br>说明：使用时首先按照用户的IMSI在<br>“IMSI_PREFIX（指定IMSI前缀）”<br>或<br>“IMSI_RANGE（指定IMSI范围）”<br>进行查询，如果查询成功则使用该记录对应的配置；如果查询失败，则查询<br>“所有用户”<br>对应的配置记录，如果查询成功则使用<br>“所有用户”<br>的配置，如果查询还失败，则默认支持DT。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时，该参数才有效。<br>取值范围：1～15位十进制字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定所要查询的IMSI。<br>前提条件：当<br>“用户范围”<br>为<br>“IMSI_RANGE（指定IMSI范围）”<br>时，该参数才有效。<br>取值范围：1～15位十进制字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305858)

查询所有IMSI的属性记录：

LST IMSIDT:;

```
%%LST IMSIDT:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 用户范围      IMSI前缀  启用Direct Tunnel

 所有用户      NULL      是               
 指定IMSI前缀  12345     否               
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305858)

参见 [**ADD IMSIDT**](增加IMSI Direct Tunnel配置(ADD IMSIDT)_72345647.md) 的参数说明。
