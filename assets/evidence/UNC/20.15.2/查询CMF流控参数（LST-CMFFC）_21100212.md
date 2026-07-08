# 查询CMF流控参数（LST CMFFC）

- [命令功能](#ZH-CN_MMLREF_0000001721100212__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001721100212__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001721100212__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001721100212__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001721100212__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001721100212)

该命令用于查询CMF流控参数。

## [注意事项](#ZH-CN_MMLREF_0000001721100212)

- CMF Pod单节点部署时不支持CMF流控，第三方CaaS场景不支持CMF流控，CSPEdge裸机场景不支持CMF流控。
- 当未执行[**SET CMFFC**](设置CMF流控参数（SET CMFFC）_68820021.md)命令时，本命令回显数据中除流控功能类型外均显示为0。CMF流控默认参数配置为代码默认值，可通过[**DSP DBGHAFD**](显示HAFD调试命令结果（DSP DBGHAFD）_94730404.md)命令查询实际运行的值。查询时，参数DEBUGNAME取值为"cmf fc config"。
- 当执行过[**SET CMFFC**](设置CMF流控参数（SET CMFFC）_68820021.md)命令后，本命令回显数据与[**DSP DBGHAFD**](显示HAFD调试命令结果（DSP DBGHAFD）_94730404.md)回显数据保持一致。

#### [操作用户权限](#ZH-CN_MMLREF_0000001721100212)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001721100212)

无

## [使用实例](#ZH-CN_MMLREF_0000001721100212)

查询CMF流控参数：

```
%%LST CMFFC:;%%
RETCODE = 0  操作成功

结果如下
--------
流控功能类型  一级起控阈值(%)  一级停控阈值(%)  二级起控阈值(%)  二级停控阈值(%)  停控时间窗(s)  

POD           0                0                0                0                0              
RESOURCEBOX   0                0                0                0                0              
(结果个数 = 2)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001721100212)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 流控功能类型 | 该参数用于表示CMF流控功能类型。 |
| 一级起控阈值(%) | 该参数用于表示触发CMF一级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。 |
| 一级停控阈值(%) | 该参数用于表示停止CMF一级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。 |
| 二级起控阈值(%) | 该参数用于表示触发CMF二级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。 |
| 二级停控阈值(%) | 该参数用于表示停止CMF二级流控的CPU阈值。当流控功能类型为POD时，该参数为CMF Pod的CPU值；当流控功能类型为RESOURCEBOX时，在虚机场景中为CMF Pod所在节点的CPU值，在FST裸机场景中为CMF Pod所关联SuperPod的CPU值。 |
| 停控时间窗(s) | 该参数用于表示CMF流控停止所需要的时间窗阈值。 |
