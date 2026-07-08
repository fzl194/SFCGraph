---
id: UDG@20.15.2@MMLCommand@ADD NGVNVLANWL
type: MMLCommand
name: ADD NGVNVLANWL（增加基于5G LAN组的VLAN白名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NGVNVLANWL
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN VLAN配置
- VLAN白名单配置
status: active
---

# ADD NGVNVLANWL（增加基于5G LAN组的VLAN白名单）

## 功能

**适用NF：UPF**

该命令用于增加基于5GLAN组的VLAN白名单。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD NGVNINSTANCE命令配置生成。 |
| VLANID | VLAN ID | 可选必选说明：必选参数<br>参数含义：该参数用于设置VLAN ID。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～4094。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [基于5G LAN组的VLAN白名单（NGVNVLANWL）](configobject/UDG/20.15.2/NGVNVLANWL.md)

## 使用实例

增加VLAN白名单：

```
ADD NGVNVLANWL: VNINSTANCE="a0000001-460-003-01", VLANID=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加基于5G-LAN组的VLAN白名单（ADD-NGVNVLANWL）_23157716.md`
