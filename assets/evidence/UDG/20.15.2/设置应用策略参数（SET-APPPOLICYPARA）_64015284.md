# 设置应用策略参数（SET APPPOLICYPARA）

- [命令功能](#ZH-CN_CONCEPT_0264015284__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0264015284__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0264015284__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0264015284__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0264015284__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0264015284)

**适用NF：PGW-U、UPF**

该命令用于设置APP策略参数。

#### [注意事项](#ZH-CN_CONCEPT_0264015284)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ACLSWITCH | BWALLOCATION | DNSREDSWITCH |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0264015284)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0264015284)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLSWITCH | 黑白名单开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否启用黑白名单策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：配置使能时，仅白名单内的用户允许访问业务，黑名单不允许。 |
| BWALLOCATION | 应用带宽策略开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否支持app带宽策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：配置使能时，对访问APP的上下行数据流做带宽控制。 |
| DNSREDSWITCH | DNS重定向开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置DNS重定向开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0264015284)

使能黑白名单策略控制开关、APP带宽策略控制开关和DNS重定向策略控制开关：

```
SET APPPOLICYPARA: ACLSWITCH=ENABLE, BWALLOCATION=ENABLE, DNSREDSWITCH=ENABLE;
```
