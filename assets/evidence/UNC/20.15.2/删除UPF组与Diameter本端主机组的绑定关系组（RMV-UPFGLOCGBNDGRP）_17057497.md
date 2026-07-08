# 删除UPF组与Diameter本端主机组的绑定关系组（RMV UPFGLOCGBNDGRP）

- [命令功能](#ZH-CN_CONCEPT_0000201617057497__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201617057497__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201617057497__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201617057497__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201617057497__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201617057497)

**适用NF：PGW-C、SMF**

此命令用于删除指定的UPF组与Diameter本端主机组的绑定关系组。

#### [注意事项](#ZH-CN_CONCEPT_0000201617057497)

- 该命令执行后立即生效。
- 如果其已经绑定到PCCFUNC，则禁止删除。
- 如果其已经绑定到PCCTEMPLATE，则禁止删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201617057497)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201617057497)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | 可选必选说明：必选参数<br>参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201617057497)

删除UPF组与Diameter本端主机组之间的绑定关系组，“UPFGLOCGBNDGNAME”为“huawei”：

```
RMV UPFGLOCGBNDGRP: UPFGLOCGBNDGNAME="huawei";
```
