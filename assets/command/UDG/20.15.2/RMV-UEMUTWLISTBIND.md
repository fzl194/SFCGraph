---
id: UDG@20.15.2@MMLCommand@RMV UEMUTWLISTBIND
type: MMLCommand
name: RMV UEMUTWLISTBIND（删除APN绑定PA口UE互访白名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: UEMUTWLISTBIND
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- UE互访白名单绑定APN
status: active
---

# RMV UEMUTWLISTBIND（删除APN绑定PA口UE互访白名单）

## 功能

**适用NF：UPF、PGW-U**

该命令用于删除APN与PA口UE互访白名单的绑定关系。

## 注意事项

- 该命令执行后，对新激活的用户生效；对于已在线的用户，需要N9承载的对端IP地址发生变更时才会生效，该修改通过承载更新消息下发。
- 该命令执行后，发生ssg进程复位后对所有用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| WLISTTYPE | 白名单类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定白名单类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SGWU<br>- UPF<br>默认值：无<br>配置原则：无 |
| WLISTNAME | 白名单名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE互访白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN绑定PA口UE互访白名单（UEMUTWLISTBIND）](configobject/UDG/20.15.2/UEMUTWLISTBIND.md)

## 使用实例

删除 APN名称为testapn下绑定的类型为UPF的白名单名称为testwlist的白名单：

```
RMV UEMUTWLISTBIND:APNNAME="testapn",WLISTTYPE=UPF,WLISTNAME="testwlist";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除APN绑定PA口UE互访白名单（RMV-UEMUTWLISTBIND）_72322912.md`
