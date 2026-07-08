# 配置全局费率切换组（SET GLBTARIFFGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209896840__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896840__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896840__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896840__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896840__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896840)

**适用NF：SGW-C、PGW-C、SMF**

该命令用于绑定全局费率切换组，UNC优先选择user-profile实例、APN实例绑定的费率切换组，当上述两者都没有绑定时，UNC选择全局配置的费率切换组。

#### [注意事项](#ZH-CN_CONCEPT_0209896840)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 配置的费率切换组名GLBTARIFFGROUP时，要执行ADD TARIFFGROUP命令添加费率切换组名。如果没有添加，则执行命令失败。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896840)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896840)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLBTARIFFGRP | 费率切换组名 | 可选必选说明：可选参数<br>参数含义：本参数用于指定费率切换组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 该参数使用ADD TARIFFGROUP命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0209896840)

绑定全局费率切换组，GLBTARIFFGRP为huawei，命令为：

```
ADD TARIFFGROUP: TARIFFGRPNAME="huawei.com", GLOBALFLG=CHARGE_CHARACT, CCVALUE="0x0100", CCMASK="0x0100", CCPRIORITY=2, TARIFFTYPE=WORKDAY, STARTTIME=09&00, ENDTIME=17&00;
SET GLBTARIFFGROUP:GLBTARIFFGRP="huawei.com";
```
