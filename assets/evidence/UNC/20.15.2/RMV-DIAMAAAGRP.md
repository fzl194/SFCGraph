# 删除Diameter AAA服务器组（RMV DIAMAAAGRP）

- [命令功能](#ZH-CN_MMLREF_0264343903__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343903__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343903__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343903__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0264343903)

**适用NF：PGW-C**

此命令用于删除一个Diameter AAA组。当某个Diameter AAA组没有绑定到任何APN下，且该组不再被使用时，操作员可以执行此命令删除该组。

## [注意事项](#ZH-CN_MMLREF_0264343903)

- 该命令执行后立即生效。

- 如果Diameter AAA组已经绑定到APN，则不允许删除。
- 如果Diameter AAA组下已经绑定了Diameter AAA，则相应的Diameter AAA绑定关系（DiamAAABndGrp）会删除。

#### [操作用户权限](#ZH-CN_MMLREF_0264343903)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343903)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0264343903)

根据网络规划，删除名称为“diametergroup”的Diameter AAA组：

```
RMV DIAMAAAGRP:GROUPNAME="diametergroup";
```
