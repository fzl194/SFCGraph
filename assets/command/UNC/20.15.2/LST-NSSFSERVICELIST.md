---
id: UNC@20.15.2@MMLCommand@LST NSSFSERVICELIST
type: MMLCommand
name: LST NSSFSERVICELIST（查看NSSF功能实例服务列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFSERVICELIST
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NSSF性能对象管理
status: active
---

# LST NSSFSERVICELIST（查看NSSF功能实例服务列表）

## 功能

**适用NF：NSSF**

本命令用于查看NSSF功能实例服务列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NSSF功能实例服务（NSSFSERVICELIST）](configobject/UNC/20.15.2/NSSFSERVICELIST.md)

## 使用实例

查询NSSF功能实体服务列表：

```
LST NSSFSERVICELIST;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查看NSSF功能实例服务列表（LST-NSSFSERVICELIST）_09651509.md`
