---
id: UNC@20.15.2@MMLCommand@RMV USERPROFILE
type: MMLCommand
name: RMV USERPROFILE（删除用户模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USERPROFILE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# RMV USERPROFILE（删除用户模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除用户模板。

## 注意事项

- 该命令执行后立即生效。
- 如果用户模板已经绑定在用户模板组中，则不允许删除，需要执行命令RMV UPBINDUPG解除绑定关系后再删除。
- 如果Rule与用户模板绑定，删除用户模板会自动解除与rule的绑定关系。
- 如果用户模板与数据网络访问标识符（DNAI）绑定，删除用户模板会自动解除与数据网络访问标识符的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USERPROFILE]] · 用户模板（USERPROFILE）

## 使用实例

假如运营商需要删除用户模板，用户模板名称为“testuserprofilename”：

```
RMV USERPROFILE:USERPROFILENAME="testuserprofilename";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USERPROFILE.md`
