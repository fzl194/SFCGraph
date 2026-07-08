# 查询SRVCC流程限制策略(LST SRVCCLMTPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001736323428__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001736323428__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001736323428__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001736323428__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001736323428__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001736323428__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001736323428__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001736323428)

**适用网元：MME**

该命令用于查询SRVCC流程限制策略。

#### [注意事项](#ZH-CN_MMLREF_0000001736323428)

此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001736323428)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001736323428)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001736323428)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>- SPECIFIC_IMSI（指定IMSI）：表示用户范围通过IMSI指定。<br>默认值：无<br>配置原则：SRVCC流程限制策略匹配优先级从高到低为：<br>“SPECIFIC_IMSI（指定IMSI）”<br>，<br>“IMSI_PREFIX（指定IMSI前缀）”<br>，<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>，<br>“ALL_USER(所有用户)”<br>。 系统优先匹配高优先级的配置记录，如果匹配不到，再匹配低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，须先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：整网规划<br>取值范围：5～14位十进制字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定用户的IMSI（完整IMSI）。<br>前提条件：该参数在<br>“用户范围”<br>配置为<br>“SPECIFIC_IMSI（指定IMSI）”<br>后生效。<br>数据来源：全网规划<br>取值范围：15位十进制字符串<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001736323428)

1.查询一条 “用户范围” 为 “ALL_USER” 的流程限制策略配置：

LST SRVCCLMTPLCY: SUBRANGE=ALL_USER;

```
%%
LST SRVCCLMTPLCY: SUBRANGE=ALL_USER
;%%
RETCODE = 0  操作成功。

查询结果如下
------------
                 用户范围  =  所有用户
               运营商标识  =  NULL
                 IMSI前缀  =  NULL
                 指定IMSI  =  NULL
    是否限制携带SRVCC能力  =  是
紧急呼叫是否限制SRVCC能力  =  是
(结果个数 = 1)

---    END
```

2.查询全部的流程限制策略配置：

LST SRVCCLMTPLCY:;

```
%%LST SRVCCLMTPLCY:;%%
RETCODE = 0  操作成功。

查询结果如下
------------
用户范围      运营商标识  IMSI前缀         指定IMSI  是否限制携带SRVCC能力  紧急呼叫是否限制SRVCC能力  

所有用户      NULL        NULL             NULL      是                     是
本网用户      0           NULL             NULL      是                     否
指定IMSI前缀  NULL        12345678901234   NULL      是                     是
(结果个数 = 3)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001736323428)

参见 [**ADD SRVCCLMTPLCY**](增加流程限制策略(ADD PROCLMTPLCY)_72225309.md) 命令的参数说明。
