# 查询获取PLMN优先级（LST PLMNPRIORITY）

- [命令功能](#ZH-CN_MMLREF_0209652282__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652282__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652282__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652282__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652282__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652282)

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来查看当前获取GGSN/SGW-C/PGW-C的PLMN标识方式的优先级。

## [注意事项](#ZH-CN_MMLREF_0209652282)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652282)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652282)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指示UNC的网元形态。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>- SGWC（SGW-C）<br>- PGWC（PGW-C）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652282)

显示网元类型为GGSN的PLMNPRIORITY的记录：

```
%%LST PLMNPRIORITY: NODETYPE=GGSN;%%
RETCODE = 0  操作成功

结果如下
--------
      网元类型  =  GGSN
  获取PLMN方法  =  LOCAL
GGSN第一优先级  =  SGSN_IP
GGSN第二优先级  =  RAI
GGSN第三优先级  =  ULI
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209652282)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元类型 | 该参数用于指示UNC的网元形态。 |
| 获取PLMN方法 | 该参数用于两种获取PLMN方法。 |
| PGW第一优先级 | 该参数用于指定PGW-C第一优先级。 |
| PGW第二优先级 | 该参数用于指定PGW-C第二优先级。 |
| PGW第三优先级 | 该参数用于指定PGW-C第三优先级。 |
| GGSN第一优先级 | 该参数用于指定GGSN第一优先级。 |
| GGSN第二优先级 | 该参数用于指定GGSN第二优先级。 |
| GGSN第三优先级 | 该参数用于指定GGSN第三优先级。 |
| SGW第一优先级 | 该参数用于指定SGW-C第一优先级。 |
| SGW第二优先级 | 该参数用于指定SGW-C第二优先级。 |
