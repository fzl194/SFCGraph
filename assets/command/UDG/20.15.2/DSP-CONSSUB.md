---
id: UDG@20.15.2@MMLCommand@DSP CONSSUB
type: MMLCommand
name: DSP CONSSUB（显示消费者订阅信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CONSSUB
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 消费者订阅状态
status: active
---

# DSP CONSSUB（显示消费者订阅信息）

## 功能

该命令用于显示Diameter消费者订阅状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CONSSUB]] · 消费者订阅信息（CONSSUB）

## 使用实例

显示Diameter消费者订阅状态信息：

```
DSP CONSSUB:;
```

```

RETCODE = 0 操作成功

结果如下
------------------------
用户PID        用户订阅类型     对端地址     服务ID

0x2DF0056      服务ID           0.0.0.0      2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示消费者订阅信息（DSP-CONSSUB）_00600565.md`
