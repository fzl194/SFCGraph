# 增加用户位置组（ADD USRLOCATIONGRP）

- [命令功能](#ZH-CN_CONCEPT_0209897148__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897148__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897148__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897148__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897148__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897148)

**适用NF：PGW-C、SMF**

该命令用于增加位置组。位置组是一种初始接入位置的位置组定义。当需要将多个位置信息组合起来对外呈现时，可将其绑定到同一位置组。该位置组可以在ADD UPBINDUPG命令中用于UsrProfGroup下的UserProfile的策略选择。

#### [注意事项](#ZH-CN_CONCEPT_0209897148)

- 该命令执行后立即生效。
- 系统最多支持配置1000条UsrLocationGrp，每个UsrLocationGrp最多支持配置20个UserLocation。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897148)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897148)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGROUPNAME | 位置组名称 | 可选必选说明：必选参数<br>参数含义：指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCATIONNAME | 位置名称 | 可选必选说明：可选参数<br>参数含义：指定位置信息名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD USRLOCATION命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0209897148)

假如运营商需要希望增加一个位置组用于后续绑定位置信息使用：

```
ADD USRLOCATIONGRP:LOCGROUPNAME="test01",LOCATIONNAME="testloc01";
```
