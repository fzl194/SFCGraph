# 查询指定消息类型固定速率流控信息（LST GTPCFIXEDFC）

- [命令功能](#ZH-CN_MMLREF_0000001088377440__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088377440__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088377440__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088377440__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088377440__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088377440)

**适用NF：SGW-C、PGW-C**

该命令用于查询指定消息类型的固定速率流控信息。如果不指定消息类型，则查询所有消息的固定速率流控信息。

## [注意事项](#ZH-CN_MMLREF_0000001088377440)

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001088377440)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088377440)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置GTP-C接口被流控的消息类型。<br>数据来源：全网规划<br>取值范围：<br>- “CREATESESSIONREQUEST（Create Session Request）”：表示Create Session Request消息<br>- “MODIFYBEARERREQUEST（Modify Bearer Request）”：表示Modify Bearer Request消息<br>- “ALLMSGTYPE（All Message Type）”：表示所有消息类型<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001088377440)

查询所有流控消息类型的流控信息，执行如下命令：

```
%%LST GTPCFIXEDFC:;%%
RETCODE = 0  操作成功

结果如下
--------
流控消息类型            固定速率流控开关  流控速率门限(个/秒)  

Create Session Request  开启              1200                 
Modify Bearer Request   开启              15000                
All Message Type        开启              30000                
(结果个数 = 3)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001088377440)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 流控消息类型 | 该参数用于设置GTP-C接口被流控的消息类型。 |
| 固定速率流控开关 | 该参数用于设置指定消息类型流控功能开关。 |
| 流控速率门限(个/秒) | 该参数用于设置单sm-pod指定消息的接收流控速率上限。 |
