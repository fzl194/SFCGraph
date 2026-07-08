---
id: UDG@20.15.2@MMLCommand@LST SFEPASSGREFRAG
type: MMLCommand
name: LST SFEPASSGREFRAG（查询SFE透传GRE分片报文使能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFEPASSGREFRAG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE透传GRE分片
status: active
---

# LST SFEPASSGREFRAG（查询SFE透传GRE分片报文使能配置）

## 功能

该命令用来查询SFE透传GRE分片报文使能配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 该命令适用于非池化和池化场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFEPASSGREFRAG]] · SFE透传GRE分片报文使能配置（SFEPASSGREFRAG）

## 使用实例

查询SFE透传GRE分片报文使能配置：

```
LST SFEPASSGREFRAG:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
使能标记  =  是
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SFE透传GRE分片报文使能配置（LST-SFEPASSGREFRAG）_60619580.md`
