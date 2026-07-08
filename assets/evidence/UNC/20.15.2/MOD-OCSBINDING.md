# 修改Ocs绑定关系（MOD OCSBINDING）

- [命令功能](#ZH-CN_CONCEPT_0209896964__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896964__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896964__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896964__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896964__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896964)

**适用NF：PGW-C、SMF**

该命令用来修改OCS绑定关系。

#### [注意事项](#ZH-CN_CONCEPT_0209896964)

- 该命令执行后立即生效。
- 修改绑定关系，可能导致在线计费用户查找不到OCS，在线计费用户可能激活失败。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896964)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896964)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSGRPNAME | Ocs组名称 | 可选必选说明：必选参数<br>参数含义：指定OCS组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD OCSGROUP命令配置生成。 |
| OCSHOSTNAME | Ocs主机名称 | 可选必选说明：必选参数<br>参数含义：指定OCS主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD OCS命令配置生成。 |
| SEGGROUPNAME | IMSI/MSISDN号码段组名称 | 可选必选说明：可选参数<br>参数含义：使用用户号段组。如果命令中配置了多个用户号段组，则根据优先级来选择ocs-info。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD SUBSCRIBERIDSEGGRP命令配置生成。<br>- 输入单空格将删除该参数已有配置项。 |
| IMSIPRIORITY | IMSI/MSISDN号码段组优先级 | 可选必选说明：可选参数<br>参数含义：指定Imsi/Msisdn号码段组优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。值越小优先级越高，优先级唯一。<br>默认值：无<br>配置原则：无 |
| OCSPERCENTAGE | Ocs在OcsGroup中的负荷分担比 | 可选必选说明：可选参数<br>参数含义：指定OCS在OcsGroup中的负荷分担比。同一个OcsGroup内所有ocs的负荷分担百分比总和不能超过100。如果有若干ocs的负荷分担百分比被指定，则未被指定的ocs将平分剩余的百分比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209896964)

修改OCS绑定关系，OCSGRPNAME为test，OCSHOSTNAME为test01，SEGGROUPNAME为test03，IMSIPRIORITY为2，命令为：

```
MOD OCSBINDING:OCSGRPNAME="test",OCSHOSTNAME="test01",SEGGROUPNAME="test03",IMSIPRIORITY=2;
```
