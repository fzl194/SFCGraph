---
id: UDG@20.15.2@MMLCommand@LST POLICYFCSWITCH
type: MMLCommand
name: LST POLICYFCSWITCH（查询策略流控开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: POLICYFCSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略流控管理
status: active
---

# LST POLICYFCSWITCH（查询策略流控开关状态）

## 功能

该命令用于查询策略流控开关状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/POLICYFCSWITCH]] · 策略流控开关状态（POLICYFCSWITCH）

## 使用实例

查询策略流控开关状态。

```
%%LST POLICYFCSWITCH:;%%
RETCODE = 0  操作成功

结果如下
------------------------
策略流控开关  =  策略流控开关打开
(结果个数 = 1)

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-POLICYFCSWITCH.md`
