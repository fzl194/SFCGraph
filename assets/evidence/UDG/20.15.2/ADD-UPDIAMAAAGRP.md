# 增加Diameter AAA服务器组（ADD UPDIAMAAAGRP）

- [命令功能](#ZH-CN_CONCEPT_0000206297080177__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206297080177__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206297080177__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206297080177__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206297080177__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206297080177)

**适用NF：UPF**

此命令用于新建一个Diameter AAA组。

#### [注意事项](#ZH-CN_CONCEPT_0000206297080177)

- 该命令执行后对新接入的会话生效。
- 该命令最大记录数为10。
- 此命令为建立会话的核心配置，需绑定到APN后才能生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206297080177)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206297080177)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206297080177)

根据网络规划，需要新增一个名称为“diametergroup”的Diameter AAA组：

```
ADD UPDIAMAAAGRP:GROUPNAME="diametergroup";
```
