---
id: UDG@20.15.2@MMLCommand@LST DBUPGSTAGE
type: MMLCommand
name: LST DBUPGSTAGE（查询CSDB灰度升级阶段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DBUPGSTAGE
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

# LST DBUPGSTAGE（查询CSDB灰度升级阶段）

## 功能

该命令用于查询当前的灰度升级阶段。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DBUPGSTAGE]] · CSDB灰度升级阶段（DBUPGSTAGE）

## 使用实例

查询到当前的 **“灰度升级阶段”** 为 **“CSDB灰度升级结束”** ：

```
%%LST DBUPGSTAGE:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
灰度升级阶段  =  CSDB灰度升级结束
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DBUPGSTAGE.md`
