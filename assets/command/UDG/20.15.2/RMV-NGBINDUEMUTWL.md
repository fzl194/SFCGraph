---
id: UDG@20.15.2@MMLCommand@RMV NGBINDUEMUTWL
type: MMLCommand
name: RMV NGBINDUEMUTWL（删除5G LAN组绑定PA口UE互访白名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: NGBINDUEMUTWL
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN用户互访控制
- UE互访白名单绑定5G LAN组
status: active
---

# RMV NGBINDUEMUTWL（删除5G LAN组绑定PA口UE互访白名单）

## 功能

**适用NF：UPF**

该命令用于删除5G LAN组与PA口UE互访白名单的绑定关系。

## 注意事项

该命令执行后，对新激活的用户生效；对于已在线的用户，需要N9承载的对端IP地址发生变更时才会生效，该修改通过承载更新消息下发。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |
| WLISTNAME | 白名单名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE互访白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGBINDUEMUTWL]] · 5G LAN组绑定PA口UE互访白名单（NGBINDUEMUTWL）

## 使用实例

将白名单名称为testwlist1的PA口UE互访白名单与5G LAN组实例a0000001-460-01-01解绑：

```
RMV NGBINDUEMUTWL: VNINSTANCE="a0000001-460-01-01", WLISTNAME="testwlist1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-NGBINDUEMUTWL.md`
