---
id: UDG@20.15.2@MMLCommand@LST DDNCTRL
type: MMLCommand
name: LST DDNCTRL（查询DDN控制策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DDNCTRL
command_category: 查询类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 报文DDN 触发策略
status: active
---

# LST DDNCTRL（查询DDN控制策略）

## 功能

**适用NF：SGW-U、UPF**

该命令用来查询报文DDN触发控制策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DDNCTRL]] · DDN控制策略（DDNCTRL）

## 使用实例

查询报文DDN触发控制策略：

```
LST DDNCTRL:;
```

```

RETCODE = 0 操作成功。

DDN控制策略
------------------
  报文类型 = Tcp 信令
  使能开关 = 使能
  报文策略 = 丢弃报文 
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DDNCTRL.md`
