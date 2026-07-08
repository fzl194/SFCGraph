# 查询P-CSCF故障恢复策略(LST PCSCFRESTOPLCY)

- [命令功能](#ZH-CN_MMLREF_0000002105322582__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000002105322582__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000002105322582__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000002105322582__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000002105322582__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000002105322582__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000002105322582__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000002105322582)

**适用网元：MME**

该命令用于查询P-CSCF故障恢复策略配置。

#### [注意事项](#ZH-CN_MMLREF_0000002105322582)

- 该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000002105322582)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000002105322582)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000002105322582)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置P-CSCF故障恢复策略的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- ALL_USER（所有用户）：表示用户范围为系统内所有用户。<br>- HOME_USER（本网用户）：表示用户范围为本网用户。<br>- FOREIGN_USER（外网用户）：表示用户范围为外网用户。<br>- IMSI_PREFIX（指定IMSI前缀）：表示用户范围通过IMSI前缀指定。<br>- SPECIFIC_IMSI（特定IMSI）：表示用户范围通过IMSI指定。<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“指定IMSI前缀”<br>后生效。<br>数据来源：整网规划<br>取值范围：5~14位十进制数字字符串<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIFIC_IMSI（特定IMSI）”<br>后生效。<br>数据来源：整网规划<br>取值范围：14~15位十进制数字字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000002105322582)

查询 “用户范围” 为 “所有用户” 的所有记录；

LST PCSCFRESTOPLCY: SUBRANGE=ALL_USER;

```
%%LST PCSCFRESTOPLCY: SUBRANGE=ALL_USER;%%
RETCODE = 0  操作成功 

查询结果如下
------------
                        用户范围  =  所有用户         
                      运营商标识  =  NULL           
                        IMSI前缀  =  NULL        
PCO-based optional extension功能  =  开启
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000002105322582)

请参考 [**ADD PCSCFRESTOPLCY**](增加P-CSCF故障恢复策略(ADD PCSCFRESTOPLCY)_40921453.md) 命令的参数说明。
