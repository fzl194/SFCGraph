# 增加Diameter路由下一跳（ADD UPDIAMRTNEXTHOP）

- [命令功能](#ZH-CN_CONCEPT_0000206145432708__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206145432708__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206145432708__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206145432708__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206145432708__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206145432708)

**适用NF：UPF**

此命令用于添加指定Diameter应用和realm的Diameter路由的下一跳。

#### [注意事项](#ZH-CN_CONCEPT_0000206145432708)

- 该命令执行后立即生效。
- 该命令最大记录数为1280。
- 一个指定域名和应用下最大允许配置10个下一跳主机。
- 下一跳列表中主机顺序依赖于序号值，下一跳顺序确定了主备路由（主备路由选择模式）以及路由被选择的顺序。主备路由选择模式下，如果主用下一跳被删除，则第一个备用下一跳升主。如需对主备关系进行调整，需要先删除该路由，再按照期望的路由主备顺序配置下一跳主机列表。
- 配置的下一跳主机要与此Diameter路由的应用类型一致，并且需要通过ADD UPDIAMCONN配置UPF与该下一跳主机的Diameter链路。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206145432708)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206145432708)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMRTREALM命令配置生成。 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| NEXTHOP | 下一跳 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的下一跳。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDRA命令配置生成。 |
| SEQUENCE | 序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由下一跳的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000206145432708)

- 添加一个SWM接口的缺省Diameter路由的下一跳host1：
  ```
  ADD UPDIAMRTNEXTHOP: REALMNAME="default", APPLICATION=SWM, NEXTHOP="host1", SEQUENCE=1;
  ```
- 添加指定realm名为example.com的SWM应用的两个Diameter路由下一跳，host1和host2：
  ```
  ADD UPDIAMRTNEXTHOP: REALMNAME="example.com", APPLICATION=SWM, NEXTHOP="host1", SEQUENCE=1;
  ADD UPDIAMRTNEXTHOP: REALMNAME="example.com", APPLICATION=SWM, NEXTHOP="host2", SEQUENCE=2;
  ```
