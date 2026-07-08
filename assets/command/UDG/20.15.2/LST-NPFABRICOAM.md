---
id: UDG@20.15.2@MMLCommand@LST NPFABRICOAM
type: MMLCommand
name: LST NPFABRICOAM（查询全局OAM相关配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPFABRICOAM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# LST NPFABRICOAM（查询全局OAM相关配置）

## 功能

该命令用于查询全局OAM相关配置：包括OAM使能，OAM报文检测周期，OAM报文超时检测倍数。

> **说明**
> - 该命令执行后立即生效。
> - 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPFABRICOAM]] · 全局OAM相关配置（NPFABRICOAM）

## 使用实例

查询全局OAM相关配置

```
LST NPFABRICOAM:;
RETCODE = 0  操作成功

结果如下
--------
            OAM使能  =  使能
OAM报文发送周期(ms)  =  100
OAM报文超时检测倍数  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NPFABRICOAM.md`
