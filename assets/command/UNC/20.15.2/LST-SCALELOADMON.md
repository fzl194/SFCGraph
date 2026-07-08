---
id: UNC@20.15.2@MMLCommand@LST SCALELOADMON
type: MMLCommand
name: LST SCALELOADMON（查询自动扩缩容监测的虚机资源）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCALELOADMON
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- VNFC公共功能管理
- 操作维护
- 扩缩容管理
status: active
---

# LST SCALELOADMON（查询自动扩缩容监测的虚机资源）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN、AMF**

该命令用于自动扩缩容场景下，查询监测的虚机资源。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCALELOADMON]] · 自动扩缩容监测的虚机资源（SCALELOADMON）

## 使用实例

查看自动扩缩容的资源检测项，执行如下命令：

```
%%LST SCALELOADMON:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
scale in/out load resource category  =  SM session memory resource
(Number of results = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询自动扩缩容监测的虚机资源（LST-SCALELOADMON）_23736552.md`
