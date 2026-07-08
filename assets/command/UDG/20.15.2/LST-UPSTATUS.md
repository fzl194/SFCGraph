---
id: UDG@20.15.2@MMLCommand@LST UPSTATUS
type: MMLCommand
name: LST UPSTATUS（显示UP 状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPSTATUS
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- UP状态
status: active
---

# LST UPSTATUS（显示UP 状态）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

查询UPF工作状态配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [UP 状态（UPSTATUS）](configobject/UDG/20.15.2/UPSTATUS.md)

## 使用实例

查询UPF工作状态配置：

```
LST UPSTATUS:;
```

```

RETCODE = 0  操作成功。

UP 状态信息:
----------
               UP状态  =  UP
       强制停工开关  =  DISABLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示UP-状态（LST-UPSTATUS）_82837251.md`
