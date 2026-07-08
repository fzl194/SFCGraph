---
id: UDG@20.15.2@MMLCommand@LST SCALINGSWITCH
type: MMLCommand
name: LST SCALINGSWITCH（查询扩缩容开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SCALINGSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 弹性开关
status: active
---

# LST SCALINGSWITCH（查询扩缩容开关）

## 功能

此命令用于查询扩缩容开关参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/SCALINGSWITCH]] · 扩缩容开关（SCALINGSWITCH）

## 使用实例

LST SCALINGSWITCH:;

```
%%LST SCALINGSWITCH:;%%
RETCODE = 0  操作成功 
结果如下 
-------- 
扩缩容开关 = MANO触发的扩缩容
  监控周期 = 50
  取样间隔 = 2
  时间单位 = Sec
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询扩缩容开关（LST-SCALINGSWITCH）_09587929.md`
