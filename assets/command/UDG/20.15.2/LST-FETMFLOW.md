---
id: UDG@20.15.2@MMLCommand@LST FETMFLOW
type: MMLCommand
name: LST FETMFLOW（查询FETM流控配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FETMFLOW
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- FE表管理
- FETM流控
status: active
---

# LST FETMFLOW（查询FETM流控配置）

## 功能

该命令用来查询FETM流控配置：包括流控开关，流控阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速CSLB卸载模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FETMFLOW]] · FETM流控配置（FETMFLOW）

## 使用实例

查询FETM流控配置：

```
LST FETMFLOW:;
RETCODE = 0  操作成功

结果如下
--------
流控开关  =  启用
流控阈值  =  70
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FETMFLOW.md`
