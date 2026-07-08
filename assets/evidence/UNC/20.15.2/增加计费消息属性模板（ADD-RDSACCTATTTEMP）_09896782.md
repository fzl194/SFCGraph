# 增加计费消息属性模板（ADD RDSACCTATTTEMP）

- [命令功能](#ZH-CN_CONCEPT_0209896782__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896782__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896782__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896782__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896782__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896782)

**适用NF：PGW-C、SMF**

该命令用来新增计费消息属性模板。

#### [注意事项](#ZH-CN_CONCEPT_0209896782)

- 该命令执行后立即生效。
- 该命令最大记录数为3。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896782)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896782)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRTEMPNAME | 计费消息属性模板名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定计费消息属性模板名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| RULEBASENAME | 支持携带属性Charge-Rule-Base-Name | 可选必选说明：可选参数<br>参数含义：指定是否支持携带信元Charge-Rule-Base-Name。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CRBN：携带该信元且取值为CRBN。<br>- CFCATE：URL过滤分类组名。<br>- DISABLE：不支持携带该信元。<br>- MULTI_CRBN：携带多个CRBN信元。<br>默认值：CRBN<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896782)

新增名为“RDSACCTATTTEMP”的计费消息属性模板，支持携带属性Charge-Rule-Base-Name为DISABLE：

```
ADD RDSACCTATTTEMP: ATTRTEMPNAME="RDSACCTATTTEMP", RULEBASENAME=DISABLE;
```
