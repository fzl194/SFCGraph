---
id: UDG@20.15.2@MMLCommand@LST NPWATCHDOG
type: MMLCommand
name: LST NPWATCHDOG（查询喂狗功能相关配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPWATCHDOG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# LST NPWATCHDOG（查询喂狗功能相关配置）

## 功能

该命令用于查询喂狗功能相关配置：喂狗检测周期，喂狗超时时长。

> **说明**
> 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPWATCHDOG]] · 喂狗功能相关配置（NPWATCHDOG）

## 使用实例

查询喂狗功能相关配置：

```
LST NPWATCHDOG:;
RETCODE = 0  操作成功

结果如下
--------
喂狗检测周期  =  500
喂狗超时时长  =  24
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询喂狗功能相关配置（LST-NPWATCHDOG）_18818230.md`
