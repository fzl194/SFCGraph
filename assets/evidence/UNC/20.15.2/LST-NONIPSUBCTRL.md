# 查询Non-IP APNNI配置(LST NONIPSUBCTRL)

- [命令功能](#ZH-CN_MMLREF_0000001126145774__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145774__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145774__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145774__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145774__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145774__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145774__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145774)

**适用网元：MME**

该命令用于查询Non-IP APNNI配置。

#### [注意事项](#ZH-CN_MMLREF_0000001126145774)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145774)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145774)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145774)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定配置生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145774)

查询所有Non-IP APNNI的配置：

LST NONIPSUBCTRL:;

```
%%LST NONIPSUBCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
         用户范围  =  所有用户
         IMSI前缀  =  NULL
支持Non-IP的APNNI  =  所有APNNI
        APNNI组号  =  NULL
        缺省APNNI  =  NULL
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145774)

参见 [**ADD NONIPSUBCTRL**](增加Non-IP APNNI配置(ADD NONIPSUBCTRL)_72225451.md) 的参数说明。
