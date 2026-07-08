---
id: UDG@20.15.2@MMLCommand@RMV UPDIAMRTNEXTHOP
type: MMLCommand
name: RMV UPDIAMRTNEXTHOP（删除Diameter路由下一跳）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UPDIAMRTNEXTHOP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- 路由管理
- Diameter路由配置
status: active
---

# RMV UPDIAMRTNEXTHOP（删除Diameter路由下一跳）

## 功能

**适用NF：UPF**

![](删除Diameter路由下一跳（RMV UPDIAMRTNEXTHOP）_97314575.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会删除Diameter路由下一跳，可能导致无法选到DRA，用户激活失败。

该命令用于删除指定的Diameter路由下一跳的配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令如果不输入“NEXTHOP”，则表示删除指定Diameter路由的所有下一跳。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REALMNAME | Diameter域名名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的realm名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMRTREALM命令配置生成。 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter路由的Diameter应用。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：无 |
| NEXTHOP | 下一跳 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter路由的下一跳。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 2670控制是否区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD UPDRA命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMRTNEXTHOP]] · Diameter路由下一跳（UPDIAMRTNEXTHOP）

## 使用实例

- 删除SWM应用在realm名为“example.com”的所有Diameter路由下一跳：
  ```
  RMV UPDIAMRTNEXTHOP:REALMNAME="example.com",APPLICATION=SWM;
  ```
- 删除SWM应用在realm名为“example1.com”的Diameter路由下一跳host1：
  ```
  RMV UPDIAMRTNEXTHOP:REALMNAME="example1.com",APPLICATION=SWM,NEXTHOP="host1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-UPDIAMRTNEXTHOP.md`
