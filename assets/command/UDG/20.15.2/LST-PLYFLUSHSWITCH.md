---
id: UDG@20.15.2@MMLCommand@LST PLYFLUSHSWITCH
type: MMLCommand
name: LST PLYFLUSHSWITCH（查询集合类型策略刷新开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PLYFLUSHSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# LST PLYFLUSHSWITCH（查询集合类型策略刷新开关状态）

## 功能

该命令用于查询集合类型策略刷新开关状态和刷新周期。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/PLYFLUSHSWITCH]] · 集合类型策略刷新开关状态（PLYFLUSHSWITCH）

## 使用实例

查询集合类型策略刷新开关和周期。

```
%%LST PLYFLUSHSWITCH:;%%
RETCODE = 0  操作成功

结果如下
------------------------
       集合类型策略刷新开关  =  打开集合类型策略刷新开关
集合类型策略刷新周期 (分钟)  =  1440
(结果个数 = 1)

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PLYFLUSHSWITCH.md`
