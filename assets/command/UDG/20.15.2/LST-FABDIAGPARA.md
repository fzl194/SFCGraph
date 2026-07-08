---
id: UDG@20.15.2@MMLCommand@LST FABDIAGPARA
type: MMLCommand
name: LST FABDIAGPARA（查询Pod Fabric平面亚健康诊断参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FABDIAGPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST FABDIAGPARA（查询Pod Fabric平面亚健康诊断参数）

## 功能

该命令用来显示Pod Fabric平面亚健康诊断参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABDIAGPARA]] · Pod Fabric平面亚健康诊断参数（FABDIAGPARA）

## 使用实例

显示Pod Fabric平面亚健康诊断参数

```
%%LST FABDIAGPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
POD亚健康阈值 = 50
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Pod-Fabric平面亚健康诊断参数（LST-FABDIAGPARA）_48150373.md`
