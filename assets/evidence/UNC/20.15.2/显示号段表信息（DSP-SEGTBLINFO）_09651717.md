# 显示号段表信息（DSP SEGTBLINFO）

- [命令功能](#ZH-CN_MMLREF_0209651717__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651717__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651717__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651717__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651717__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651717)

**适用NF：NRF**

该命令用于查询所有A、B表的主备状态及NF的号段支持等信息。

当需要通过号段配置文件方式刷新NF支持的号段信息时，可以通过此命令查看备表的状态信息，进而执行ACT SEGFILE命令进行备表的激活。

若要查询所有的记录，请不要输入参数；若要查询特定号段类型的记录，请输入“号段类型”参数。

## [注意事项](#ZH-CN_MMLREF_0209651717)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209651717)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651717)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGTYPE | 号段类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示号段的号段类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651717)

查询号段表的信息：

```
DSP SEGTBLINFO:;
            %%DSP SEGTBLINFO:;%%
            RETCODE = 0  操作成功

            结果如下
            ------------------------
            号段类型  NF类型  号段表类型  号段总数  版本号       操作状态         是否主表  号段文件名称                     进度   加载时间

            IMSI      AUSF    A表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             100%   2019-10-07 02:29:29
            IMSI      AUSF    B表         4         v1           激活态           是        segdata1569419846013729800.zip   100%   2019-10-07 02:29:29
            IMSI      UDR     A表         0         NULL         初始状态         是        NULL                             0%     NULL
            IMSI      UDR     B表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             0%     2019-10-07 02:29:29
            IMSI      CHF     A表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             100%   2019-10-07 02:29:29
            IMSI      CHF     B表         4         v1           激活态           是        segdata1569419846013729800.zip   100%   2019-10-07 02:29:29
            MSISDN    PCF     A表         0         NULL         初始状态         是        NULL                             0%     NULL
            MSISDN    PCF     B表         1000      NULL         加载完成未激活   否        segdata-all-9000.zip             0%     2019-10-07 02:29:29
            (结果个数 = 8)
```

## [输出结果说明](#ZH-CN_MMLREF_0209651717)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 号段类型 | 该参数用于表示号段的号段类型。<br>取值说明：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>- IMSIRT（IMSIRT）<br>- MSISDNRT（MSISDNRT） |
| NF类型 | 该参数用于表示所选号段类型作用的NF类型。<br>取值说明：<br>- AUSF（AUSF）<br>- PCF（PCF）<br>- UDM（UDM）<br>- UDR（UDR）<br>- CHF（CHF）<br>- CUSTOM_OCS（CUSTOM_OCS）<br>- AUSFUDM（AUSFUDM） |
| 号段表类型 | 该参数用于表示号段的号段表类型，用于区分主、备两个表。<br>取值说明：<br>- ATABLE（A表）<br>- BTABLE（B表） |
| 号段总数 | 该参数用于表示某一NF支持的某号段类型的号段区间个数。 |
| 版本号 | 该参数用于表示使用的支持号段数据的版本号。运营商针对某一NF支持的特定号段类型，可能会规划不同的号段数据，此参数用于区分当前系统使用的具体哪一版本的号段数据。 |
| 操作状态 | 该参数用于表示号段文件的状态。<br>取值说明：<br>- INISTAT（初始状态）<br>- LOADING（加载中）<br>- LOADEDNOACT（加载完成未激活）<br>- LOADEDACT（激活态）<br>- DELETING（删除中）<br>- FAILED（失败）<br>- EXPORTING（导出中）<br>- DOWNLOADFILEFAILED（下载文件失败）<br>- AUTHFAILED（验签失败） |
| 是否主表 | 该参数用于表示号段表是否为主表。<br>取值说明：<br>- MASTERTRUE（是）<br>- MASTERFALSE（否） |
| 号段文件名称 | 该参数用于表示对应信息所在的号段文件名称。 |
| 进度 | 该参数表示加载号段文件、激活号段文件、导出号段文件、删除号段数据的进度。取值范围是0%到100%。 |
| 加载时间 | 该参数用于表示所选号段类型的加载时间点。 |
