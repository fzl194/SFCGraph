# 流分类下删除ACL规则组（RMV QOSRULEACL）

- [命令功能](#ZH-CN_CONCEPT_0000001600841669__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600841669__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600841669__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600841669__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600841669__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600841669)

该命令用来删除流分类下配置的ACL匹配规则。

#### [注意事项](#ZH-CN_CONCEPT_0000001600841669)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600841669)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600841669)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流分类名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| IPVERSION | IP协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的IP协议版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：无 |
| ACLTYPE | ACL类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ACL规则的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- acl-number：ACL编号。<br>- acl-name：ACL名称。<br>默认值：无 |
| ACLNUM | ACL编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“acl-number”时为必选参数。<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2000～4999。<br>默认值：无 |
| ACLNAME | ACL名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ACLTYPE”配置为“acl-name”时为必选参数。<br>参数含义：该参数用于指定基于IPv4或IPv6的ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600841669)

- 删除在流分类c1上配置基于名称acl1的IPv4 ACL规则：
  ```
  RMV QOSRULEACL: CLASSIFIERNAME="c1",IPVERSION=IPv4,ACLTYPE=acl-name,ACLNAME="acl1";
  ```
- 删除在流分类c1上配置基于编号2001的IPv6 ACL规则：
  ```
  RMV QOSRULEACL: CLASSIFIERNAME="c1",IPVERSION=IPv6,ACLTYPE=acl-number,ACLNUM=2001;
  ```
