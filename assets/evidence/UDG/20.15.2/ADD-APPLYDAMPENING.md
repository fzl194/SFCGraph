# 增加Dampening设置（ADD APPLYDAMPENING）

- [命令功能](#ZH-CN_CONCEPT_0000001549802078__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549802078__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549802078__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549802078__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549802078__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549802078)

该命令用于添加应用Dampening。

#### [注意事项](#ZH-CN_CONCEPT_0000001549802078)

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 配置该命令前，必须已经通过ADD ROUTEPOLICY配置了指定路由策略的名字以及通过ADD ROUTEPOLICYNODE配置了该策略下的节点。
- 该命令中的各配置参数没有缺省值，必须显式配置。所指定的reuse、suppress、ceiling三个阈值是依次增大的，即必须满足：reuse<suppress<ceiling。根据公式MaxSuppressTime=half-life-reach×60×(ln(ceiling/reuse)/ln(2))，如果MaxSuppressTime小于1就不能抑制。所以要保证MaxSuppressTime大于等于1，即必须满足：ceiling/reuse足够大。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549802078)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549802078)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 路由策略名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～200。<br>默认值：无<br>配置原则：区分大小写。 |
| NODESEQUENCE | 路由策略节点ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由策略节点ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| HALFLIFEVALUE | 路由半生命时期（分钟） | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由半生命时期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～45。<br>默认值：无<br>配置原则：单位为分钟。 |
| REUSEVALUE | 路由再生极限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由再生极限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000。<br>默认值：无 |
| SUPPRESSVALUE | 路由抑制极限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由抑制极限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000。<br>默认值：无<br>配置原则：实际配置的值必须大于REUSEVALUE的值。 |
| CEILINGVALUE | 路由极限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定路由极限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1001～20000。<br>默认值：无<br>配置原则：实际配置的值必须大于SUPPRESSVALUE。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549802078)

增加EBGP路由的衰减参数的设置：

```
ADD APPLYDAMPENING:POLICYNAME="a",NODESEQUENCE=10,HALFLIFEVALUE=1,REUSEVALUE=1000,SUPPRESSVALUE=2000,CEILINGVALUE=5000;
```
