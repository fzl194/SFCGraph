# 显示本地缓存中配置的记录数（DSP CSCFGCACHE）

- [命令功能](#ZH-CN_MMLREF_0000001951335377__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001951335377__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001951335377__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001951335377__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001951335377__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001951335377)

**适用NF：AMF、SMF、PGW-C、GGSN、SGW-C**

该命令用于查看本地缓存中配置的记录数和内容。

## [注意事项](#ZH-CN_MMLREF_0000001951335377)

- 当本地缓存中的配置只有一条记录时，会显示该配置的记录数和该记录的详细信息。
- 当本地缓存中的配置有多条记录时，仅显示该配置的记录数。

#### [操作用户权限](#ZH-CN_MMLREF_0000001951335377)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001951335377)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMLNAME | 配置命令名称 | 可选必选说明：必选参数<br>参数含义：该参数表示配置命令的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>该参数表示配置命令的名称，比如PLMNNS，不要输入ADD/RMV/MOD/LST等操作字符，优先LST命令名称。 |

## [使用实例](#ZH-CN_MMLREF_0000001951335377)

查询PFCPPVTEXT配置在本地缓存的信息：

```
%%DSP CSCFGCACHE: MMLNAME="PFCPPVTEXT";%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
配置命令名称                控制业务读取配置数据的策略                 配置的记录数                                                         配置信息      

PFCPPVTEXT                  OMCM                                       [uncpod-0__1012__0][ContainerCtrl] cache num is [30]                 Check cfgCache records in log  
PFCPPVTEXT                  OMCM                                       [uncpod-0__1005__0][ContainerSm]	cache num is [30]                   Check cfgCache records in log  
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001951335377)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 配置命令名称 | 该参数表示配置命令的名称。 |
| 控制业务读取配置数据的策略 | 该参数用于控制业务读取配置数据的策略，决定业务是从本地缓存还是OM数据中读取。<br>取值说明：<br>- “CSAPI（CSAPI）”：本地配置缓存<br>- “OMCM（OMCM）”：OM配置数据 |
| 配置的记录数 | 该参数表示某一配置在本业务进程缓存中的记录数。 |
| 配置信息 | 该参数用于显示具体某一个配置的详细信息。 |
