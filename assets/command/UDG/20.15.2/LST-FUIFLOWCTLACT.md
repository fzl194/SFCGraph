---
id: UDG@20.15.2@MMLCommand@LST FUIFLOWCTLACT
type: MMLCommand
name: LST FUIFLOWCTLACT（查询欠费重定向流控动作）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FUIFLOWCTLACT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- FUI重定向控制
- FUI流控动作
status: active
---

# LST FUIFLOWCTLACT（查询欠费重定向流控动作）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示欠费重定向流控动作。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FUIFLOWCTLACT]] · 欠费重定向流控动作（FUIFLOWCTLACT）

## 使用实例

显示欠费重定向流控动作，命令如下：

```
LST FUIFLOWCTLACT:;
```

```

RETCODE = 0  操作成功。

欠费重定向流控动作信息
----------------------
欠费重定向流控动作  =  流控
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FUIFLOWCTLACT.md`
