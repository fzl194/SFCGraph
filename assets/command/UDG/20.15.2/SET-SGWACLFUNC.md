---
id: UDG@20.15.2@MMLCommand@SET SGWACLFUNC
type: MMLCommand
name: SET SGWACLFUNC（设置SGW ACL功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SGWACLFUNC
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户ACL管理
- SgwAcl
status: active
---

# SET SGWACLFUNC（设置SGW ACL功能）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于控制SGW\I-UPF\ULCL\BP上ACL功能是否使能。当SGW\I-UPF\ULCL\BP不作为透传设备需要开启其ACL功能，使用该命令配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SGWACL |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWACL | S-GW ACL功能 | 可选必选说明：必选参数<br>参数含义：该参数用于控制SGW上ACL功能是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能SGW ACL功能。<br>- ENABLE：使能SGW ACL功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SGWACLFUNC]] · SGW ACL功能（SGWACLFUNC）

## 使用实例

- 当SGW\I-UPF\ULCL\BP不作为透传设备时，使能其ACL功能：
  ```
  SET SGWACLFUNC:SGWACL=ENABLE;
  ```
- 当SGW\I-UPF\ULCL\BP作为透传设备时，不使能其ACL功能：
  ```
  SET SGWACLFUNC:SGWACL=DISABLE;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SGWACLFUNC.md`
