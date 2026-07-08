---
id: UDG@20.15.2@MMLCommand@RMV ACLDEFAULT
type: MMLCommand
name: RMV ACLDEFAULT（删除缺省Acl绑定）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ACLDEFAULT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- 缺省ACL绑定
status: active
---

# RMV ACLDEFAULT（删除缺省Acl绑定）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除默认的ACL。默认ACL是在APN下没有配置任何ACL时，如果APN需要使用ACL，则会使用默认ACL。

## 注意事项

- 该命令执行后立即生效。
- 当需要删除某一默认ACL时需指明方向。
- 当需要删除所有默认ACL时，Driection字段应置为空。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIRECTION | 方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定默认ACL的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLDEFAULT]] · 缺省Acl绑定（ACLDEFAULT）

## 使用实例

- 假如运营商需要删除上行、进系统方向的默认ACL：
  ```
  RMV ACLDEFAULT:DIRECTION=UPIN;
  ```
- 假如运营商需要删除系统当前所有的默认ACL：
  ```
  RMV ACLDEFAULT:;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ACLDEFAULT.md`
