---
id: UDG@20.15.2@MMLCommand@LST NPLINKCHECK
type: MMLCommand
name: LST NPLINKCHECK（查询全局NP交换网口检测配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPLINKCHECK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# LST NPLINKCHECK（查询全局NP交换网口检测配置）

## 功能

该命令用于查询全局NP交换网口检测配置：包括端口检测使能、端口检测周期、端口检测超时检测倍数。

> **说明**
> - 该命令执行后立即生效。
> - 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [全局NP交换网口检测配置（NPLINKCHECK）](configobject/UDG/20.15.2/NPLINKCHECK.md)

## 使用实例

查询全局NP交换网口检测配置

```
LST NPLINKCHECK:;
RETCODE = 0  操作成功

结果如下
--------
        NP交换网口检测功能  =  使能
        NP交换网口检测周期  =  100
NP交换网口检测超时检测倍数  =  15
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局NP交换网口检测配置（LST-NPLINKCHECK）_94730467.md`
