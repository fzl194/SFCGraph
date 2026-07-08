# 修改缺省Acl绑定（MOD ACLDEFAULT）

- [命令功能](#ZH-CN_CONCEPT_0182837740__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837740__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837740__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837740__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837740__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837740)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于修改默认的ACL。当APN下没有配置任何ACL时，APN会使用默认ACL，而该命令用于修改APN使用的默认ACL。

#### [注意事项](#ZH-CN_CONCEPT_0182837740)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837740)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837740)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定默认ACL的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：按实际需要控制的方向来置值。 |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置默认ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 当参数Direction配置为UPIN、DOWNIN时，该参数只能配置ACL节点的动作为gate、remark的ACL名称。<br>- 当参数Direction配置为UPOUT、DOWNOUT时，该参数只能配置ACL节点的动作为redirect的ACL名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837740)

假如运营商需要将上行、进系统方向的默认ACL修改为“testacl1”：

```
MOD ACLDEFAULT:DIRECTION=UPIN,ACLNAME="testacl1";
```
