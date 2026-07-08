# 查询PLMN的计费属性参数(LST CHGPLMNCHAR)

- [命令功能](#ZH-CN_MMLREF_0000001172344991__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172344991__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172344991__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172344991__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172344991__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172344991__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172344991__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172344991)

**适用网元：SGSN**

该命令用于查询PLMN类型的用户计费属性参数的配置。

#### [注意事项](#ZH-CN_MMLREF_0000001172344991)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172344991)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172344991)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172344991)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMN | PLMN 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于运营商对不同PLMN用户的话单生成采取不同的策略。<br>取值范围：<br>- “HPLMN（本地 PLMN）”：表示本网用户。<br>- “VPLMN（拜访 PLMN）”：表示拜访用户，非本网用户即拜访用户 。<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172344991)

查询普通计费属性的配置信息：

LST CHGPLMNCHAR: PLMN=HPLMN;

```
%%LST CHGPLMNCHAR: PLMN=HPLMN;%%
RETCODE = 0  操作成功。

输出结果如下
------------
     PLMN 类型  =  本地 PLMN
     生成M-CDR  =  生成
     生成S-CDR  =  生成
 生成S-SMO-CDR  =  生成
 生成S-SMT-CDR  =  生成
生成LCS-MO-CDR  =  生成
生成LCS-MT-CDR  =  生成
生成LCS-NI-CDR  =  生成
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172344991)

参见命令 [**SET CHGPLMNCHAR**](设置PLMN的计费属性参数(SET CHGPLMNCHAR)_26305204.md) 参数说明。
