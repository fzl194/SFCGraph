# 删除缺省Acl绑定（RMV ACLDEFAULT）

- [命令功能](#ZH-CN_CONCEPT_0182837741__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837741__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837741__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837741__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837741__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837741)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除默认的ACL。默认ACL是在APN下没有配置任何ACL时，如果APN需要使用ACL，则会使用默认ACL。

#### [注意事项](#ZH-CN_CONCEPT_0182837741)

- 该命令执行后立即生效。
- 当需要删除某一默认ACL时需指明方向。
- 当需要删除所有默认ACL时，Driection字段应置为空。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837741)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837741)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIRECTION | 方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定默认ACL的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837741)

- 假如运营商需要删除上行、进系统方向的默认ACL：
  ```
  RMV ACLDEFAULT:DIRECTION=UPIN;
  ```
- 假如运营商需要删除系统当前所有的默认ACL：
  ```
  RMV ACLDEFAULT:;
  ```
