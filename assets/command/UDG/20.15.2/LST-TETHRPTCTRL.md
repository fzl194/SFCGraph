---
id: UDG@20.15.2@MMLCommand@LST TETHRPTCTRL
type: MMLCommand
name: LST TETHRPTCTRL（查询tethering事件上报的相关参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TETHRPTCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering事件上报控制
status: active
---

# LST TETHRPTCTRL（查询tethering事件上报的相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询tethering事件上报的相关参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [tethering事件上报的相关参数（TETHRPTCTRL）](configobject/UDG/20.15.2/TETHRPTCTRL.md)

## 使用实例

查询tethering事件上报的相关参数：

```
LST TETHRPTCTRL:;
```

```

RETCODE = 0 操作成功

设置tethering事件上报的相关参数
----------------------------------------------------
          Tethering Stop消息上报开关 = 不使能
Tethering Stop消息上报迟滞时间（秒） = 0
               Tethering上报事件模式 = TETHERING行为模式
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询tethering事件上报的相关参数（LST-TETHRPTCTRL）_15208993.md`
