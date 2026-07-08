---
id: UDG@20.15.2@MMLCommand@DSP OPSASSISTSTATE
type: MMLCommand
name: DSP OPSASSISTSTATE（显示系统助手的当前信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OPSASSISTSTATE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 开放可编程系统
status: active
---

# DSP OPSASSISTSTATE（显示系统助手的当前信息）

## 功能

该命令用于显示系统助手的当前信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/OPSASSISTSTATE]] · 系统助手的当前信息（OPSASSISTSTATE）

## 使用实例

显示系统助手的当前信息：

```
DSP OPSASSISTSTATE:;
```

```

 RETCODE = 0  操作成功。

结果如下
------------------------
      助手ID = 2
    助手名称 = _get_all_env.py
    助手状态 = 准备好状态
触发条件类型 = 多条件组合
    助手类型 = 脚本
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示系统助手的当前信息（DSP-OPSASSISTSTATE）_00601449.md`
