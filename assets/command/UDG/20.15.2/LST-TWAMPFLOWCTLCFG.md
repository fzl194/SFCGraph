---
id: UDG@20.15.2@MMLCommand@LST TWAMPFLOWCTLCFG
type: MMLCommand
name: LST TWAMPFLOWCTLCFG（查询跟踪流控配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TWAMPFLOWCTLCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP流控跟踪配置
status: active
---

# LST TWAMPFLOWCTLCFG（查询跟踪流控配置）

## 功能

用于查询TWAMP功能的跟踪流控配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TWAMPFLOWCTLCFG]] · 跟踪流控配置（TWAMPFLOWCTLCFG）

## 使用实例

查询TWAMP功能的跟踪流控配置参数。

```
%%LST TWAMPFLOWCTLCFG:;%%
RETCODE = 0  操作成功

结果如下
--------
    跟踪流控开关  =  打开
    流控恢复阈值  =  60
    流控触发阈值  =  70
允许跟踪创建阈值  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TWAMPFLOWCTLCFG.md`
