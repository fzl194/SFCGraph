# 调试信息（OPR DBGDATA）

- [命令功能](#ZH-CN_MMLREF_0209587904__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209587904__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209587904__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209587904__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209587904)

此命令用于查询服务的调试信息。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0209587904)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209587904)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBGTYPE | 操作对象 | 可选必选说明：可选参数<br>参数含义：该参数用于表示调试消息发送对象类型。<br>数据来源：本端规划<br>取值范围：<br>- CELLTYPE（进程类型）<br>- CELLID（进程标识）<br>默认值：无<br>配置原则：无 |
| CELLTYPE | 进程类型 | 可选必选说明：该参数在"DBGTYPE"配置为"CELLTYPE"时为条件必选参数。<br>参数含义：该参数用于表示发给同一类型的进程。通过DSP MSPROCTYPE来查询。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CELLID | 进程标识 | 可选必选说明：该参数在"DBGTYPE"配置为"CELLID"时为条件必选参数。<br>参数含义：该参数用于表示发给某一个进程。通过DSP MSPROCESS查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~100。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| DEBUGNAME | 调试信息 | 可选必选说明：可选参数<br>参数含义：该参数用于表示调试信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~250。<br>默认值：无<br>配置原则：<br>调试信息举例如下：<br>DSP MSACTIVE：该命令用于查询选举域内的主信息。<br>DSP PREFIX：该命令用于查询环境内所有的选举域。<br>DSP SCF INSTANTSTATUS：查询实例化流程总体进度。<br>DSP DCF TOKENPLY：该命令用于查询Token的策略信息。 |

## [使用实例](#ZH-CN_MMLREF_0209587904)

查询操作对象为进程类型，进程类型为100，DEBUGNAME为DSP CELLID时的调试信息：

```
%%OPR DBGDATA: DBGTYPE=CELLTYPE, CELLTYPE=100, DEBUGNAME="DSP CELLID";%%
RETCODE = 0  操作成功

结果如下
--------
调测输出  =  
all topo cell count is 198

(结果个数 = 1)

---    END
```
