---
id: UNC@20.15.2@MMLCommand@LST ADDRUPGROUP
type: MMLCommand
name: LST ADDRUPGROUP（查询UPF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ADDRUPGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配UPF组管理
status: active
---

# LST ADDRUPGROUP（查询UPF组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询UPF组的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格及特殊字符“#”、“$”和“&”等，由“-”、“_”、数字、字母和“.”组成，不能以“.”开头或结尾，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UPF组（ADDRUPGROUP）](configobject/UNC/20.15.2/ADDRUPGROUP.md)

## 使用实例

查询所有UPF组的信息：

```
LST ADDRUPGROUP:;
RETCODE = 0  操作成功。

结果如下
------------------------
UPF组名称  =  upfgrp1
UPF组类型  =  本地
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF组（LST-ADDRUPGROUP）_49644917.md`
