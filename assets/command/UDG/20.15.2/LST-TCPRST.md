---
id: UDG@20.15.2@MMLCommand@LST TCPRST
type: MMLCommand
name: LST TCPRST（查询欠费用户下行RST报文处理动作）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TCPRST
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 欠费用户下行RST报文控制
status: active
---

# LST TCPRST（查询欠费用户下行RST报文处理动作）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示欠费用户下行TCP RST报文的处理动作。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [欠费用户下行RST报文处理动作（TCPRST）](configobject/UDG/20.15.2/TCPRST.md)

## 使用实例

显示欠费用户下行RST报文的处理动作：

```
LST TCPRST:;
```

```

RETCODE = 0  操作成功。

下行RST报文处理动作
-------------------
欠费用户下行RST报文处理动作  =  允许通过
  欠费用户纯RST报文处理动作  =  丢弃
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询欠费用户下行RST报文处理动作（LST-TCPRST）_82837627.md`
