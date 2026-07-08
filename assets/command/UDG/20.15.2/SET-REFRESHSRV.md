---
id: UDG@20.15.2@MMLCommand@SET REFRESHSRV
type: MMLCommand
name: SET REFRESHSRV（业务刷新）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: REFRESHSRV
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 业务刷新
status: active
---

# SET REFRESHSRV（业务刷新）

## 功能

**适用NF：PGW-U、UPF**

![](业务刷新（SET REFRESHSRV）_82837355.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于刷新Filter、FilterGroup、Acl和AclNode配置，将新配置或修改的Filter、FilterGroup、Acl和AclNode置为生效。

## 注意事项

- 该命令执行后立即生效。
- 当用户新配置或修改Filter、FilterGroup、Acl和AclNode配置后，需要执行SET REFRESHSRV，才能使修改和新增的配置生效。
- 使用此命令前进行了Filter、FilterGroup、Acl、AclNode中的某项配置。
- 新增加或者修改Filter配置后，只有在执行SET REFRESHSRV命令后，Filter才能生效，即Filter作为UserProfile中报文匹配规则在进行三四层匹配时生效。删除Filter配置后，只有在执行SET REFRESHSRV命令后，被删除的Filter才不作为三四层匹配规则。
- 新增加或者修改FilterGroup配置后，只有在执行SET REFRESHSRV命令后，FilterGroup才能生效。
- 新增加或者修改Acl、AclNode配置后，必须执行SET REFRESHSRV命令后，Acl、AclNode才能生效，即Acl、AclNode作为APN中匹配和执行动作的规则。在Acl绑定到APN中或者配置默认Acl时，Acl、AclNode会自动生效，Acl从APN中解除绑定或者修改默认Acl时，Acl、AclNode也会自动生效。
- Acl、AclNode配置修改后，在执行SET REFRESHSRV命令30s后生效。
- 执行该命令后，30秒内不允许执行修改Filter和修改被绑定的IPList命令。
- 修改Filter与Rule之间的间接绑定关系后需要执行SET REFRESHSRV才能使修改的配置生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REFRESHTYPE |
| --- | --- |
| 初始值 | ALL |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REFRESHTYPE | 刷新类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定刷新的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL<br>- USERPROFILE<br>- ACL<br>默认值：无<br>配置原则：<br>- ALL：用于刷新Filter、FilterGroup、Acl和AclNode的配置，将Filter、FilterGroup、Acl和AclNode置为生效。<br>- USERPROFILE：用于刷新Filter和FilterGroup的配置，将Filter置为生效。<br>- ACL: 用于刷新Acl和AclNode的配置，将Acl和AclNode置为生效。 |

## 操作的配置对象

- [业务刷新（REFRESHSRV）](configobject/UDG/20.15.2/REFRESHSRV.md)

## 关联任务

- [0-00015](task/UDG/20.15.2/0-00015.md)

## 使用实例

设置REFRESHSRV，RefreshType是“USERPROFILE”：

```
SET REFRESHSRV:REFRESHTYPE=USERPROFILE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/业务刷新（SET-REFRESHSRV）_82837355.md`
