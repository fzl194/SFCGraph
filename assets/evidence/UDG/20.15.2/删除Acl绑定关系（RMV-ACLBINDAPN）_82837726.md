# 删除Acl绑定关系（RMV ACLBINDAPN）

- [命令功能](#ZH-CN_CONCEPT_0182837726__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837726__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837726__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837726__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837726__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837726)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定APN下数据流的所有或者某个方向绑定的ACL规则。

#### [注意事项](#ZH-CN_CONCEPT_0182837726)

- 该命令执行后立即生效。
- ACL绑定到APN中或从APN中解绑时，需要等待30s后生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837726)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837726)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DIRECTION | 方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN绑定ACL的down-link in-bound、down-link out-bound、up-link in-bound、up-link out-bound四个方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837726)

假如运营商需要删除APN“testapn”的上行、进系统方向的ACL绑定关系：

```
RMV ACLBINDAPN:APN="testapn",DIRECTION=UPIN;
```
