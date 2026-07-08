# 设置轻量DNS参数（SET DNSLITEPARA）

- [命令功能](#ZH-CN_CONCEPT_0235373561__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0235373561__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0235373561__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0235373561__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0235373561__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0235373561)

**适用NF：PGW-U、UPF**

该命令用于设置轻量DNS参数。

#### [注意事项](#ZH-CN_CONCEPT_0235373561)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DNSLMATCHSW | DNSLPOLICYSW | DNSRULESTATSW |
| --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE |

#### [操作用户权限](#ZH-CN_CONCEPT_0235373561)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0235373561)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSLMATCHSW | 轻量DNS规则匹配开关 | 可选必选说明：可选参数<br>参数含义：当SMF下发PDR规则时，用于控制是否开启将PDR中的Application ID匹配DNS规则。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：静态DNS规则和动态DNS规则都受本开关控制。 |
| DNSLPOLICYSW | 轻量DNS策略执行开关 | 可选必选说明：可选参数<br>参数含义：用于控制命中DNS规则后，是否响应UE的DNS查询请求。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：该参数使用SET DNSLITEPARA命令配置生成。 |
| DNSRULESTATSW | DNS规则状态控制开关 | 可选必选说明：可选参数<br>参数含义：用于控制是否可以修改通过ADD DNSRULE命令配置的静态DNS规则的状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：当DNS规则状态控制开关配置为“DISABLE”时，每条静态DNS规则默认为激活状态。 |

#### [使用实例](#ZH-CN_CONCEPT_0235373561)

在需要配置轻量级DNS规则匹配使能、执行轻量DNS策略并且允许修改静态DNS规则的状态，执行如下命令：

```
SET DNSLITEPARA: DNSLMATCHSW=ENABLE, DNSLPOLICYSW=ENABLE, DNSRULESTATSW=ENABLE;
```
