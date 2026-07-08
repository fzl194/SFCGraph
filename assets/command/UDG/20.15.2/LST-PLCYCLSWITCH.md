---
id: UDG@20.15.2@MMLCommand@LST PLCYCLSWITCH
type: MMLCommand
name: LST PLCYCLSWITCH（查询冗余策略老化开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PLCYCLSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# LST PLCYCLSWITCH（查询冗余策略老化开关）

## 功能

该命令用于查询冗余策略老化开关。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [冗余策略老化开关（PLCYCLSWITCH）](configobject/UDG/20.15.2/PLCYCLSWITCH.md)

## 使用实例

查询冗余策略老化开关，ON表示开启，OFF表示关闭。

```
%%LST PLCYCLSWITCH:;%%
RETCODE = 0  操作成功

结果如下
------------------------             
冗余策略老化开关 = 打开
    老化阈值 = 10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询冗余策略老化开关（LST-PLCYCLSWITCH）_45881145.md`
