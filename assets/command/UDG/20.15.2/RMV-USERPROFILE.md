---
id: UDG@20.15.2@MMLCommand@RMV USERPROFILE
type: MMLCommand
name: RMV USERPROFILE（删除用户模板）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: USERPROFILE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务规则管理
- 用户模板
status: active
---

# RMV USERPROFILE（删除用户模板）

## 功能

**适用NF：PGW-U、UPF**

![](删除用户模板（RMV USERPROFILE）_82837285.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，会导致正在使用此UserProfile的用户出现规则匹配错误、计费错误等现象。

该命令用于删除用户模板。

## 注意事项

- 该命令执行后立即生效。
- 如果用户模板已经绑定在用户组中，则不允许删除，需要执行命令RMV UPBINDBWMUSRG解除绑定关系后再删除。
- 当前有用户正在使用的用户模板无法被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及“,”、“;”、“"”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户模板（USERPROFILE）](configobject/UDG/20.15.2/USERPROFILE.md)

## 使用实例

假如运营商需要删除用户模板，用户模板名称为“testuserprofilename”：

```
RMV USERPROFILE:USERPROFILENAME="testuserprofilename";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除用户模板（RMV-USERPROFILE）_82837285.md`
