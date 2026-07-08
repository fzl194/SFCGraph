# 查询代理IMSI/MSISDN号段组（LST PRIMSIMSISDNG）

- [命令功能](#ZH-CN_MMLREF_0000001142693472__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001142693472__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001142693472__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001142693472__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001142693472__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001142693472)

**适用NF：PGW-C、GGSN、SGW-C、SMF**

该命令用于查询代理IMSI/MSISDN号段组。

## [注意事项](#ZH-CN_MMLREF_0000001142693472)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001142693472)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001142693472)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001142693472)

查询“IMSI/MSISDN号段组名称”为“grp1”的代理IMSI/MSISDN号段组配置：

```
%%LST PRIMSIMSISDNG: SEGGROUPNAME="grp1";%%
RETCODE = 0  操作成功

结果如下
------------------------
IMSI/MSISDN号段组名称  IMSI/MSISDN号段名称  

grp1                   imsi1                     
grp1                   imsi2                     
grp1                   imsi3                     
grp1                   imsi4                     
(结果个数 = 4)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001142693472)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IMSI/MSISDN号段组名称 | 该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段组名称。 |
| IMSI/MSISDN号段名称 | 该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段名称。 |
