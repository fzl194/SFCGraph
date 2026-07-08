---
id: UDG@20.15.2@MMLCommand@LST SFEPKTBATCHRCV
type: MMLCommand
name: LST SFEPKTBATCHRCV（查询SFE批量收取的报文数量）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFEPKTBATCHRCV
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE批量收取报文数量
status: active
---

# LST SFEPKTBATCHRCV（查询SFE批量收取的报文数量）

## 功能

该命令用来查询SFE批量收取的报文数量。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非池化场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SFE批量收取的报文数量（SFEPKTBATCHRCV）](configobject/UDG/20.15.2/SFEPKTBATCHRCV.md)

## 使用实例

查询SFE批量收取的报文数量：

```
LST SFEPKTBATCHRCV:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
批量收取报文数量  =  16
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SFE批量收取的报文数量-（LST-SFEPKTBATCHRCV）_94196890.md`
