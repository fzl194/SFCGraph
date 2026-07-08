# 显示外置DB过滤器信息（DSP EXTERDBFILTER）

- [命令功能](#ZH-CN_CONCEPT_0000201106213366__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201106213366__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201106213366__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201106213366__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201106213366__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201106213366)

**适用NF：PGW-U、UPF**

该命令用于查询外置DataBase过滤器。当运营商希望查询外置DataBase过滤器时，则执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0000201106213366)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201106213366)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201106213366)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OTTFILTERNAME | 外部过滤器名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OTTDBQRYTYPE”配置为“OTT_FILTER_INFO”时为必选参数。<br>参数含义：该参数用于设置过滤器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：需配置为当前加载的规则库内FILTER的名字。 |
| FLOWFILTERNAME | 外部流过滤器名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“OTTDBQRYTYPE”配置为“OTT_FLOWFILTER_INFO”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“OTTDBQRYTYPE”配置为“NUMBER”时为可选参数。<br>参数含义：该参数用于设置流过滤器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：需配置为当前加载的规则库内FLOWFILTER的名字。 |
| OTTDBQRYTYPE | OTT库查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OTT库查询类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NUMBER：对外部流过滤器数量查询。<br>- OTT_FILTER_INFO：外部过滤器信息查询。<br>- OTT_FLOWFILTER_INFO：外部流过滤器信息查询。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201106213366)

运营商需要查询名称为ff1的流过滤器：

```
DSP EXTERDBFILTER: OTTDBQRYTYPE=OTT_FLOWFILTER_INFO,FLOWFILTERNAME="ff1";
```

```

RETCODE = 0  Operation Success.

External DB Flow Filter Info
-------------------------
    External Filter Name  =  filter1
External Flowfilter Name  =  ff1
(Number of results = 1)
---    END
```
