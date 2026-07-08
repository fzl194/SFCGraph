---
id: UDG@20.15.2@MMLCommand@DSP LBSTATUS
type: MMLCommand
name: DSP LBSTATUS（查询CSLB的状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LBSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP LBSTATUS（查询CSLB的状态）

## 功能

该命令用于查询CSLB的状态，服务申请完成则显示为在线状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [CSLB的状态（LBSTATUS）](configobject/UDG/20.15.2/LBSTATUS.md)

## 使用实例

使用如下命令查询CSLB的状态：

```
%%DSP LBSTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
组 ID  =  4
   状态  =  在线
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CSLB的状态（DSP-LBSTATUS）_94730408.md`
