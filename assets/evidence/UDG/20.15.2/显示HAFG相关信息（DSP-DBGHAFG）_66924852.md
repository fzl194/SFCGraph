# 显示HAFG相关信息（DSP DBGHAFG）

- [命令功能](#ZH-CN_MMLREF_0000002066924852__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002066924852__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002066924852__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002066924852__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000002066924852__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000002066924852)

该命令用于查询HAFG服务内部运行信息，方便问题定位。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0000002066924852)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002066924852)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定具体的查询类型，用于获取对应类型的查询结果。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：<br>查询类型举例如下：<br>DSP APPREPORTBASEINFO：该命令用于查询业务上报的基本信息。<br>DSP APPREPORTSTATUSINFO：该命令用于查询业务上报的周边网元状态信息。<br>DSP SELFSTATUS：该命令用于查询本网元状态信息。<br>DSP FUNCTIONSW：该命令用于查询网元级KPI异常检测与容灾和模块级KPI异常检测与恢复功能开关数据。<br>DSP DREXECUTIONINFO：该命令用于查询业务配置的容灾执行规则信息。<br>DSP DIAGNOSIS：该命令用于查询IFCM诊断结果信息。<br>DSP DECISION：该命令用于查询HAFG决策结果信息。<br>DSP EXECUTION：该命令用于查询容灾执行结果信息。<br>DSP VDUPOLICYINFO：该命令用于查询每个VM上policy的信息。 |

## [使用实例](#ZH-CN_MMLREF_0000002066924852)

获取查询类型为“APPID|DSP APPREPORTBASEINFO”时的查询结果，其中APPID为实际网元ID。

```
%%DSP DBGHAFG: QUERYTYPE="0|DSP APPREPORTBASEINFO";%%
RETCODE = 0  操作成功

结果如下
--------
查询结果  =  
AppId                 License Information             Is Refer To NF               NF Number                       
0                     true                            true                         2
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0000002066924852)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 查询结果 | 该参数用于根据不同查询类型，输出查询结果。 |
