---
id: UDG@20.15.2@MMLCommand@LST DEACTIVERATE
type: MMLCommand
name: LST DEACTIVERATE（显示去活用户会话的速率）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DEACTIVERATE
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 会话去活速率
status: active
---

# LST DEACTIVERATE（显示去活用户会话的速率）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询已配置的去活用户的会话速率。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEACTIVERATE]] · 去活用户会话的速率（DEACTIVERATE）

## 使用实例

运营商配置了去活用户会话的速率，可以使用该命令来查询已配置的去活用户会话速率：

```
LST DEACTIVERATE:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
去活速率（会话/秒）  =  25
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DEACTIVERATE.md`
