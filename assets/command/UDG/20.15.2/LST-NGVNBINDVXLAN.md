---
id: UDG@20.15.2@MMLCommand@LST NGVNBINDVXLAN
type: MMLCommand
name: LST NGVNBINDVXLAN（查询5G LAN实例绑定VXLAN组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NGVNBINDVXLAN
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- 5GLAN实例绑定VXLAN组
status: active
---

# LST NGVNBINDVXLAN（查询5G LAN实例绑定VXLAN组）

## 功能

**适用NF：UPF**

该命令用于查询5G LAN会话实例使用的VXLAN链路信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGVNBINDVXLAN]] · 5G LAN实例绑定VXLAN组配置（NGVNBINDVXLAN）

## 使用实例

查询5G LAN会话实例"A0000001-460-003-01"的VXLAN隧道信息：

```
LST NGVNBINDVXLAN: VNINSTANCE="A0000001-460-003-01":;
```

```

RETCODE = 0 操作成功。

5G LAN实例绑定VXLAN组信息
----------------------
5G LAN实例名称 = a0000001-460-003-01
VXLAN隧道组名称 = vxlangrp
VNI = 258
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询5G-LAN实例绑定VXLAN组（LST-NGVNBINDVXLAN）_12222377.md`
