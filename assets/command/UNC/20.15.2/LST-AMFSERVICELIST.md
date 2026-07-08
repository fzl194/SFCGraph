---
id: UNC@20.15.2@MMLCommand@LST AMFSERVICELIST
type: MMLCommand
name: LST AMFSERVICELIST（查询AMF服务列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFSERVICELIST
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST AMFSERVICELIST（查询AMF服务列表）

## 功能

**适用NF：AMF**

本命令用于查询特定AMF功能实体的服务列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFSERVICELIST]] · AMF服务列表（AMFSERVICELIST）

## 使用实例

查询AMF功能实体服务列表：

```
LST AMFSERVICELIST:;
%%LST AMFSERVICELIST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
AMF服务名称  =  namfComm
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF服务列表（LST-AMFSERVICELIST）_09651496.md`
