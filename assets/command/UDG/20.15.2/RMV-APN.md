---
id: UDG@20.15.2@MMLCommand@RMV APN
type: MMLCommand
name: RMV APN（删除APN配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- APN
status: active
---

# RMV APN（删除APN配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来删除指定的APN实例。

## 注意事项

- 该命令执行后立即生效。
- 如果APN已经绑定在用户组中，则不允许删除，需要执行命令RMV APNBINDBWMUSRG解除绑定关系后再删除。
- 如果APN已经包含在UPF性能指标上报范围中，则不允许删除，需要执行命令RMV UPFPERFRANGE从上报范围中移除后再删除。
- 如果APN已经绑定了地址池组映射关系，则不允许删除，需要执行命令RMV POOLGRPMAP解除映射关系后再删除。
- 如果APN已经绑定了用户选择范围，则不允许删除，需要执行命令RMV USERSELRANGE解除绑定关系后再删除。
- 如果APN已经绑定了L2TP接口，则不允许删除，需要执行命令RMV L2tpRdsClient解除绑定关系后再删除。
- APN实例下有用户存在时不允许删除该APN实例。执行该命令将失败。仅在该APN下无用户时，删除操作才能成功。
- 将APN上激活用户数降至0的方法，可以通过LCK APN修改Lock APN参数为ENABLE，使新用户无法接入该APN，随着已激活用户逐渐去激活，该APN上的激活用户数也将逐渐减至0。
- 其他APN关联对象，如果存在该APN相关配置，则会删除对应配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN配置（APN）](configobject/UDG/20.15.2/APN.md)

## 使用实例

假设运营商需要删除指定的APN实例，“APN”为“huawei.com”：

```
RMV APN:APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除APN配置（RMV-APN）_86526622.md`
