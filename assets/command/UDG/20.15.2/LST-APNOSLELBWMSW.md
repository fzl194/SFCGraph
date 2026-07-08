---
id: UDG@20.15.2@MMLCommand@LST APNOSLELBWMSW
type: MMLCommand
name: LST APNOSLELBWMSW（查询APN操作系统级带宽管理开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNOSLELBWMSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- APN 操作系统级带宽管理
status: active
---

# LST APNOSLELBWMSW（查询APN操作系统级带宽管理开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询APN操作系统级带宽管理开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNAME | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：配置的APN必须是系统已经存在的APN对象名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNOSLELBWMSW]] · APN操作系统级带宽管理开关（APNOSLELBWMSW）

## 使用实例

查询名称为“huawei.com”的APN操作系统级带宽管理开关信息：

```
LST APNOSLelBWMSW:APNNAME="huawei.com";
```

```

RETCODE = 0 Operation Success.

APN OS Level Bandwidth Managament Switch Information
--------------------------------------------------------------------------------
                                      APN = huawei.com
 APN OS Level Bandwidth Managament Switch = INHERIT
(Number of results = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询APN操作系统级带宽管理开关（LST-APNOSLELBWMSW）_82837499.md`
