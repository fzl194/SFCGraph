# 查询PCC故障场景维持BYPASS状态码配置（LST PCCBYPASSCODE）

- [命令功能](#ZH-CN_MMLREF_0000002183409210__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002183409210__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002183409210__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002183409210__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000002183409210__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002183409210)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询PCRF/PCF Bypass故障状态码配置。

## [注意事项](#ZH-CN_MMLREF_0000002183409210)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000002183409210)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002183409210)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCCTEMPLATE | PCC模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该返回码所绑定的PCC模板。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>- 如果配置为“global”则表示全局配置。<br>- 如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。 |
| INTFTYPE | 接口类型 | 可选必选说明：可选参数<br>参数含义：接口类型。<br>数据来源：对端协商<br>取值范围：<br>- INTFTYPE_N7（N7接口类型）<br>- INTFTYPE_GX（Gx接口类型）<br>默认值：无<br>配置原则：无 |
| N7RESULTCODEVAL | N7返回码 | 可选必选说明：该参数在"INTFTYPE"配置为"INTFTYPE_N7"时为条件可选参数。<br>参数含义：N7返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~3。300-599或者3xx-5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。<br>默认值：无<br>配置原则：<br>配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| GXRESULTCODEVAL | Gx返回码 | 可选必选说明：该参数在"INTFTYPE"配置为"INTFTYPE_GX"时为条件可选参数。<br>参数含义：Gx返回码。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000002183409210)

查询全局PCRF/PCF Bypass故障状态码配置：

```
%%LST PCCBYPASSCODE:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
   PCC Template Name  =  global
      Interface Type  =  Gx Interface
N7 Result Code Value  =  599
   Error Information  =  NULL
Gx Result Code Value  =  5012
(Number of results = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000002183409210)

| 输出项名称 | 输出项解释 |
| --- | --- |
| PCC模板名称 | 该参数用于设置该返回码所绑定的PCC模板。 |
| 接口类型 | 接口类型。 |
| N7返回码 | N7返回码。 |
| 错误信息 | 该参数用于指定N7返回码对应的Protocol or application Error信息。 |
| Gx返回码 | Gx返回码。 |
