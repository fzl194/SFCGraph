---
id: UDG@20.15.2@MMLCommand@LST USERROUTINGSW
type: MMLCommand
name: LST USERROUTINGSW（显示用户路由可靠性配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERROUTINGSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 用户路由可靠性配置
status: active
---

# LST USERROUTINGSW（显示用户路由可靠性配置）

## 功能

**适用NF：PGW-U、UPF**

命令用于显示用户路由可靠性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@USERROUTINGSW]] · 用户路由可靠性配置（USERROUTINGSW）

## 使用实例

显示当前用户路由可靠性配置：

```
LST USERROUTINGSW:;
```

```

RETCODE = 0  操作成功

用户路由可靠性配置
------------------
    告警开关  =  使能
告警上报阈值  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-USERROUTINGSW.md`
