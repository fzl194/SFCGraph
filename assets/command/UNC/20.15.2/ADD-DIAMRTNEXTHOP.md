---
id: UNC@20.15.2@MMLCommand@ADD DIAMRTNEXTHOP
type: MMLCommand
name: ADD DIAMRTNEXTHOP（增加Diameter路由下一跳）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DIAMRTNEXTHOP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1280
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 路由管理
- Diameter路由配置
status: active
---

# ADD DIAMRTNEXTHOP（增加Diameter路由下一跳）

## 功能

**适用NF：PGW-C、SMF**

此命令用于添加指定Diameter应用和realm的Diameter路由的下一跳。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1280。
- 一个指定域名和应用下最大允许配置80个下一跳主机。
- 下一跳列表中主机顺序依赖于序号值，下一跳顺序确定了主备路由（主备路由选择模式）以及路由被选择的顺序。主备路由选择模式下，如果主用下一跳被删除，则第一个备用下一跳升主。如需对主备关系进行调整，需要先删除该路由，再按照期望的路由主备顺序配置下一跳主机列表。
- 配置的下一跳主机要与此Diameter路由的应用类型一致，并且需要通过ADD DIAMCONNECTION配置UNC与该下一跳主机的Diameter链路。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DIAMRTREALM命令配置生成。<br>- 如果配置为default则表示缺省路由。 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GY：Gy接口应用。<br>- GX：Gx接口应用。<br>- S6B：S6b接口应用。<br>默认值：无<br>配置原则：无 |
| NEXTHOP | 下一跳 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的下一跳。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DRA命令配置生成。<br>- UNC与DRA之间存在Diameter链路。 |
| SEQUENCE | 序号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由下一跳的序号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：同一个域名和应用的下一跳配置中，在主备模式下，序号值最小的最优先被选中。在轮询模式下，轮选按照序号从小到大的顺序选择路由。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMRTNEXTHOP]] · Diameter路由下一跳（DIAMRTNEXTHOP）

## 使用实例

- 添加一个Gy接口的缺省Diameter路由的下一跳host1：
  ```
  ADD DIAMRTNEXTHOP: REALMNAME="default", APPLICATION=GY, NEXTHOP="host1", SEQUENCE=1;
  ```
- 添加指定realm名为example.com的Gx应用的两个Diameter路由下一跳，host1和host2：
  ```
  ADD DIAMRTNEXTHOP: REALMNAME="example.com", APPLICATION=GX, NEXTHOP="host1", SEQUENCE=1;
  ADD DIAMRTNEXTHOP: REALMNAME="example.com", APPLICATION=GX, NEXTHOP="host2", SEQUENCE=2;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DIAMRTNEXTHOP.md`
