---
id: UDG@20.15.2@MMLCommand@MOD ACLDEFAULT
type: MMLCommand
name: MOD ACLDEFAULT（修改缺省Acl绑定）
nf: UDG
version: 20.15.2
verb: MOD
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

# MOD ACLDEFAULT（修改缺省Acl绑定）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于修改默认的ACL。当APN下没有配置任何ACL时，APN会使用默认ACL，而该命令用于修改APN使用的默认ACL。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用于指定默认ACL的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPIN：APN绑定ACL的方向为上行进系统。<br>- UPOUT：APN绑定ACL的方向为上行出系统。<br>- DOWNIN：APN绑定ACL的方向为下行进系统。<br>- DOWNOUT：APN绑定ACL的方向为下行出系统。<br>默认值：无<br>配置原则：按实际需要控制的方向来置值。 |
| ACLNAME | ACL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置默认ACL名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 当参数Direction配置为UPIN、DOWNIN时，该参数只能配置ACL节点的动作为gate、remark的ACL名称。<br>- 当参数Direction配置为UPOUT、DOWNOUT时，该参数只能配置ACL节点的动作为redirect的ACL名称。 |

## 操作的配置对象

- [缺省Acl绑定（ACLDEFAULT）](configobject/UDG/20.15.2/ACLDEFAULT.md)

## 使用实例

假如运营商需要将上行、进系统方向的默认ACL修改为“testacl1”：

```
MOD ACLDEFAULT:DIRECTION=UPIN,ACLNAME="testacl1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改缺省Acl绑定（MOD-ACLDEFAULT）_82837740.md`
