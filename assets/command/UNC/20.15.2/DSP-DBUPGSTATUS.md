---
id: UNC@20.15.2@MMLCommand@DSP DBUPGSTATUS
type: MMLCommand
name: DSP DBUPGSTATUS（查询CSDB灰度升级状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBUPGSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 升级管理
status: active
---

# DSP DBUPGSTATUS（查询CSDB灰度升级状态）

## 功能

该命令用于查询灰度升级阶段状态。

## 注意事项

该命令回显结果中所显示的灰度升级阶段与通过 **[LST DBUPGSTAGE](查询CSDB灰度升级阶段(LST DBUPGSTAGE)_33083965.md)** 命令查询到的阶段一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBUPGSTATUS]] · CSDB灰度升级状态（DBUPGSTATUS）

## 使用实例

查询到当前的 **“灰度升级阶段”** 为 **“CSDB灰度升级结束” ，** **“灰度升级阶段状态”** 为 **“已成功”** ：

```
%%DSP DBUPGSTATUS:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
    灰度升级阶段  =  CSDB灰度升级结束
灰度升级阶段状态  =  已成功
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB灰度升级状态(DSP-DBUPGSTATUS)_87804376.md`
