# 增加安全策略ACL规则（ADD SECPOLICYACL）

- [命令功能](#ZH-CN_CONCEPT_0000001550281338__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550281338__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550281338__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550281338__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550281338__1.3.5.1)
- [参考信息](#ZH-CN_CONCEPT_0000001550281338__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550281338)

该命令用来增加一个安全策略规则。

#### [注意事项](#ZH-CN_CONCEPT_0000001550281338)

- 该命令执行后立即生效。
- 该命令最大记录数为1024。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550281338)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550281338)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无<br>配置原则：需要先添加安全策略，下发本MML命令前可使用LST SECPOLICY查看已添加的安全策略。 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- WhiteList：白名单。<br>- BlackList：黑名单。<br>- UserFlow：用户自定义流。<br>- IPV6WhiteList：IPv6白名单。<br>- IPV6BlackList：IPv6黑名单。<br>- IPV6UserFlow：IPv6用户自定义流。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“UserFlow” 或 “IPV6UserFlow”时为必选参数。<br>参数含义：安全策略类型编号，对应不同策略类型其含义不同，如SECPOLICYTYPE为User Flow，则此值为1－32的数值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SECACLNUM | 安全ACL规则编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“WhiteList”、“BlackList”、“IPV6BlackList”、“IPV6WhiteList”、“UserFlow” 或 “IPV6UserFlow”时为必选参数。<br>参数含义：安全规则号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～3999。<br>默认值：无<br>配置原则：需要先添加ACL规则组，请使用MML命令LST ACLGROUP。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550281338)

增加安全策略规则：

```
ADD SECPOLICYACL:SECPOLICYID=1,SECPOLICYTYPE=WhiteList,SECACLNUM=2001;
```

#### [参考信息](#ZH-CN_CONCEPT_0000001550281338)

需要先添加安全策略。
