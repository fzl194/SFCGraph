# 增加路由类型匹配路由策略（ADD MATCHROUTETYPE）

- [命令功能](#ZH-CN_CONCEPT_0000001549801558__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549801558__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549801558__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549801558__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549801558__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549801558)

该命令用于增加路由类型匹配路由策略。

#### [注意事项](#ZH-CN_CONCEPT_0000001549801558)

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549801558)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549801558)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：不支持输入空格，必须存在该路由策略。 |
| NODESEQUENCE | 路由策略节点号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：必须存在该路由策略节点。 |
| ROUTETYPE | 路由类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- external1：OSPF Type1的外部路由。<br>- external2：OSPF Type2的外部路由。<br>- external1or2：OSPF Type1、Type2的外部路由。<br>- internal：内部路由。<br>- nssaExternal1：OSPF nssa Type1的外部路由。<br>- nssaExternal2：OSPF nssa Type2的外部路由。<br>- nssaExternal1or2：OSPF nssa Type1、Type2的外部路由。<br>- wlr_bh：无线黑洞路由。<br>- wlr_ud：无线用户下行路由。<br>- wlr_sp：无线信令路由。<br>- wlr_gbh：带Gif接口的无线黑洞路由。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549801558)

添加路由策略a节点10的匹配条件，匹配路由类型external1：

```
ADD MATCHROUTETYPE:NODESEQUENCE=10,ROUTETYPE=external1, POLICYNAME="a";
```
