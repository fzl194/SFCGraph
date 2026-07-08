---
id: UDG@20.15.2@MMLCommand@ADD NGVNBINDVXLAN
type: MMLCommand
name: ADD NGVNBINDVXLAN（增加5G LAN实例绑定VXLAN组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NGVNBINDVXLAN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- 5GLAN实例绑定VXLAN组
status: active
---

# ADD NGVNBINDVXLAN（增加5G LAN实例绑定VXLAN组）

## 功能

**适用NF：UPF**

该命令用于配置5GLAN会话实例使用的VXLAN链路信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为512。
- 使用相同VNI的5G LAN会话实例不能使用相同的VXLAN组并且不同VXLAN组的VTEP不能相同。
- 一个5G LAN会话实例只能绑定一个VXLAN组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD NGVNINSTANCE命令配置生成。 |
| VXLANGRPNAME | VXLAN隧道组名称 | 可选必选说明：必选参数<br>参数含义：VXLAN隧道组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：该参数使用ADD VXLANGRP命令配置生成。 |
| VNI | VNI | 可选必选说明：必选参数<br>参数含义：配置VXLAN隧道头中的VNI标识的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G LAN实例绑定VXLAN组配置（NGVNBINDVXLAN）](configobject/UDG/20.15.2/NGVNBINDVXLAN.md)

## 使用实例

配置5GLAN会话实例"A0000001-460-003-01"的VXLAN隧道信息，隧道组名字为vxlangrp，VNI为258：

```
ADD NGVNBINDVXLAN: VNINSTANCE="A0000001-460-003-01", VXLANGRPNAME="vxlangrp", VNI=258;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加5G-LAN实例绑定VXLAN组（ADD-NGVNBINDVXLAN）_25397182.md`
