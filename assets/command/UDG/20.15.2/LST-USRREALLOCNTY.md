---
id: UDG@20.15.2@MMLCommand@LST USRREALLOCNTY
type: MMLCommand
name: LST USRREALLOCNTY（查询主动触发用户位置实时通知功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USRREALLOCNTY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话位置管理
- 位置实时通知
status: active
---

# LST USRREALLOCNTY（查询主动触发用户位置实时通知功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询主动触发用户位置实时通知功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USRREALLOCNTY]] · 主动触发用户位置实时通知功能（USRREALLOCNTY）

## 使用实例

查询主动触发用户位置实时通知功能：

```
%%LST USRREALLOCNTY:;
```

```
%%
RETCODE = 0  操作成功

主动触发用户位置实时通知功能
----------------------------
主动触发用户位置实时通知功能开关  =  不使能
                      用户抽样比  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-USRREALLOCNTY.md`
