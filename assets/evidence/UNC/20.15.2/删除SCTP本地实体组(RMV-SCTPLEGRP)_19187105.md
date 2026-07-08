# 删除SCTP本地实体组(RMV SCTPLEGRP)

- [命令功能](#ZH-CN_CONCEPT_0219187105__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0219187105__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0219187105__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0219187105__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0219187105__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0219187105__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0219187105)

**适用网元：MME、AMF**

该命令用于删除SCTP本端实体组配置。

#### [注意事项](#ZH-CN_CONCEPT_0219187105)

- 该命令执行后立即生效。
- SCTP本地实体组下存在实体或者被NGAP或SFGAP本地实体引用时，不允许删除。

#### [本地用户权限](#ZH-CN_CONCEPT_0219187105)

manage-ug，system-ug，monitor-ug，visit-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0219187105)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0219187105)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPGROUPID | SCTP本地实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本地实体组的标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0219187105)

删除实体组ID为0的SCTP本地实体组。

```
RMV SCTPLEGRP: SCTPGROUPID=0;
```
