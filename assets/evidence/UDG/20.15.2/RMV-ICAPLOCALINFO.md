# 删除ICAP本端信息（RMV ICAPLOCALINFO）

- [命令功能](#ZH-CN_CONCEPT_0000203432059917__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203432059917__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203432059917__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203432059917__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203432059917__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203432059917)

**适用NF：PGW-U、UPF**

该命令用于删除ICAP本端信息。

#### [注意事项](#ZH-CN_CONCEPT_0000203432059917)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203432059917)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203432059917)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERTYPE | ICAP服务器类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ICAP服务器类型。<br>数据来源：本端规划<br>取值范围：<br>- URL_FILTERING：支持URL过滤的ICAP服务器。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000203432059917)

删除一条ICAP本端信息，ICAPSERVERTYPE为URL_FILTERING的记录：

```
RMV ICAPLOCALINFO: ICAPSERVERTYPE=URL_FILTERING;
```
