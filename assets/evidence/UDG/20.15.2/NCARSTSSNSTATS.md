# 清除NETCONF会话统计信息（RTR NCARSTSSNSTATS）

- [命令功能](#ZH-CN_CONCEPT_0259103632__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0259103632__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0259103632__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0259103632__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0259103632__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0259103632)

该命令用于清除NETCONF会话统计信息。

#### [注意事项](#ZH-CN_CONCEPT_0259103632)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0259103632)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0259103632)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONID | 会话ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定NETCONF会话ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| STCTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NETCONF清除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NTFFAIL：Notification失败统计信息。<br>- NTFSTC：Notification统计信息。<br>- SESSIONSTC：会话统计信息。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0259103632)

清除NETCONF会话统计信息：

```
RTR NCARSTSSNSTATS:SESSIONID=456,STCTYPE=SESSIONSTC
,SERVICEINSTANCE="vnfc"
;
```
