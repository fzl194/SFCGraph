# 查询KPI门限(LST KPITHD)

- [命令功能](#ZH-CN_MMLREF_0000001126306012__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126306012__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126306012__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126306012__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126306012__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126306012__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126306012__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126306012)

**适用网元：SGSN、MME**

该命令用于查询KPI监控功能的KPI门限值。

#### [注意事项](#ZH-CN_MMLREF_0000001126306012)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126306012)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126306012)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126306012)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MONGRANULARITY | 监控粒度 | 可选必选说明：可选参数<br>参数含义：该参数用来设置监控粒度。<br>取值范围：<br>- “SYSTEM(整系统)”：整系统<br>- “PROCESS(单进程)”：单进程<br>默认值：无。<br>配置原则：系统目前仅支持<br>“PROCESS(单进程)”<br>。 |
| KPINAME | KPI名称 | 可选必选说明：可选参数<br>参数含义：该参数用来设置KPI名称。<br>取值范围：<br>仅支持以下选项。<br>- “2G_ACTIVE_BY_PROC(基于进程的Gb模式MS激活会话成功率(网络原因))”：基于进程的Gb模式MS激活会话成功率(网络原因)<br>- “3G_ATTACH_BY_PROC(基于进程的Iu模式附着成功率(网络原因))”：基于进程的Iu模式附着成功率(网络原因)<br>- “3G_SGSN_RAU_BY_PROC(基于进程的Iu模式SGSN内路由区更新成功率(网络原因))”：基于进程的Iu模式SGSN内路由区更新成功率(网络原因)<br>- “3G_ACTIVE_BY_PROC(基于进程的Iu模式MS激活会话成功率(网络原因))”：基于进程的Iu模式MS激活会话成功率(网络原因)<br>- “3G_SERVICE_REQUEST_BY_PROC(基于进程的Iu模式Service request成功率(网络原因))”：基于进程的Iu模式Service request成功率(网络原因)<br>- “4G_ATTACH_BY_PROC(基于进程的S1模式附着成功率(网络原因))”：基于进程的S1模式附着成功率(网络原因)<br>- “4G_COMBINE_ATTACH_BY_PROC(基于进程的S1模式联合附着成功率(网络原因))”：基于进程的S1模式联合附着成功率(网络原因)<br>- “4G_MME_TAU_BY_PROC(基于进程的S1模式MME内TAU成功率(网络原因))”：基于进程的S1模式MME内TAU成功率(网络原因)<br>- “4G_MME_X2_HANDOVER_BY_PROC(基于进程的S1模式MME内X2 Handover成功率(网络原因))”：基于进程的S1模式MME内X2 Handover成功率(网络原因)<br>- “4G_MME_S1_HANDOVER_BY_PROC(基于进程的S1模式MME内S1 Handover成功率(网络原因))”：基于进程的S1模式MME内S1 Handover成功率(网络原因)<br>- “4G_SERVICE_REQUEST_BY_PROC(基于进程的S1模式 Service request成功率(网络原因))”：基于进程的S1模式 Service request成功率(网络原因)<br>- “4G_DEDICATED_BEARER_BY_PROC(基于进程的S1模式专有承载激活成功率(网络原因))”：基于进程的S1模式专有承载激活成功率(网络原因)<br>- “4G_EXTENDED_SRV_REQUEST_PROC(基于进程的S1模式Extended Service request成功率)”：基于进程的S1模式Extended Service request成功率<br>默认值：无。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126306012)

查询监控粒度是单进程的KPI监控功能的KPI门限值：

LST KPITHD:MONGRANULARITY=PROCESS;

```
%%LST KPITHD:MONGRANULARITY=PROCESS;%%
RETCODE = 0  操作成功。

操作结果如下
------------
监控粒度    KPI名称                                             监控类型    最小业务量    绝对门限值    相对门限值(%)

单进程      基于进程的Gb模式附着成功率(网络原因)                相对值      100           NULL          40           
单进程      基于进程的Gb模式SGSN内路由区更新成功率(网络原因)    相对值      100           NULL          40           
单进程      基于进程的Gb模式MS激活会话成功率(网络原因)          相对值      100           NULL          40           
单进程      基于进程的Iu模式附着成功率(网络原因)                相对值      100           NULL          40           
单进程      基于进程的Iu模式SGSN内路由区更新成功率(网络原因)    相对值      100           NULL          40           
单进程      基于进程的Iu模式MS激活会话成功率(网络原因)          相对值      100           NULL          40           
单进程      基于进程的Iu模式Service request成功率(网络原因)     相对值      100           NULL          40           
单进程      基于进程的S1模式附着成功率(网络原因)                相对值      100           NULL          40           
单进程      基于进程的S1模式联合附着成功率(网络原因)            相对值      100           NULL          40           
单进程      基于进程的S1模式MME内TAU成功率(网络原因)            相对值      100           NULL          40           
单进程      基于进程的S1模式MME内X2 Handover成功率(网络原因)    相对值      100           NULL          40           
单进程      基于进程的S1模式MME内S1 Handover成功率(网络原因)    相对值      100           NULL          40           
单进程      基于进程的S1模式 Service request成功率(网络原因)    相对值      100           NULL          40           
单进程      基于进程的S1模式专有承载激活成功率(网络原因)        相对值      100           NULL          40           
单进程      基于进程的S1模式Extended Service request成功率      相对值      100           NULL          40
(结果个数 = 15)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126306012)

其中，参数值显示为“NULL”，表示没有实现该功能。其他参数，请参考命令 [**SET KPITHD**](设置KPI门限(SET KPITHD)_72225879.md) 的参数标识。
