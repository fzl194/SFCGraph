# 删除Diameter路由下一跳（RMV DIAMRTNEXTHOP）

- [命令功能](#ZH-CN_CONCEPT_0209897311__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897311__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897311__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897311__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897311__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897311)

**适用NF：PGW-C、SMF**

该命令用于删除指定的Diameter路由下一跳的配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897311)

- 该命令执行后立即生效。
- 当未指定下一跳时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 该命令如果不输入“NEXTHOP”，则表示删除指定Diameter路由的所有下一跳。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897311)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897311)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：无 |
| NEXTHOP | 下一跳 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的下一跳。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897311)

- 删除Gx应用在realm名为“example.com”的所有Diameter路由下一跳：
  ```
  RMV DIAMRTNEXTHOP:REALMNAME="example.com",APPLICATION=GX;
  ```
- 删除Gy应用在realm名为“example1.com”的Diameter路由下一跳host1：
  ```
  RMV DIAMRTNEXTHOP:REALMNAME="example1.com",APPLICATION=GY,NEXTHOP="host1";
  ```
