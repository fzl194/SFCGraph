---
id: UDG@20.15.2@MMLCommand@LST MULTICASTGRP
type: MMLCommand
name: LST MULTICASTGRP（查询组播组配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MULTICASTGRP
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN静态组播配置
- 组播组配置
status: active
---

# LST MULTICASTGRP（查询组播组配置）

## 功能

**适用NF：UPF**

该命令用于查看组播配置记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCASTGRPNAME | 组播组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置组播组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [组播组配置（MULTICASTGRP）](configobject/UDG/20.15.2/MULTICASTGRP.md)

## 使用实例

查询静态组播组配置：

```
LST MULTICASTGRP: MCASTGRPNAME="group";
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询组播组配置（LST-MULTICASTGRP）_15471326.md`
