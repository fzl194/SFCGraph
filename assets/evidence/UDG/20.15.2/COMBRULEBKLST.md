# 设置组合规则黑名单（SET COMBRULEBKLST）

- [命令功能](#ZH-CN_CONCEPT_0186530161__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186530161__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186530161__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186530161__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186530161__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0186530161)

**适用NF：PGW-U、UPF**

该命令用于配置如果同时存在组合rule和拆分rule，组合rule type中未配置，且组合rule优先级低，则网关当做是的blacklist的策略类型。

#### [注意事项](#ZH-CN_CONCEPT_0186530161)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | BLPOLICYTYPE |
| --- | --- |
| 初始值 | NULL |

#### [操作用户权限](#ZH-CN_CONCEPT_0186530161)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186530161)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BLPOLICYTYPE | 黑名单策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用来设置组合rule中未配置的策略作为黑名单策略处理的策略类型。<br>数据来源：本端规划<br>取值范围：位域类型。<br>- SMARTREDIRECT：指定url重定向策略在组合rule中未配置时作为黑名单策略。<br>- ADC：指定ADC策略在组合rule中未配置时作为黑名单策略。<br>- QOS：指定Qos策略在组合rule中未配置时作为黑名单策略。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0186530161)

设置组合规则黑名单为ADC：

```
SET COMBRULEBKLST: BLPOLICYTYPE=SMARTREDIRECT-0&ADC-1&QOS-0;
```
