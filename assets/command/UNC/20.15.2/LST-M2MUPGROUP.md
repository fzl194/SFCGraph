---
id: UNC@20.15.2@MMLCommand@LST M2MUPGROUP
type: MMLCommand
name: LST M2MUPGROUP（查询M2M关联的UPF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M2MUPGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M关联的UPF组管理
status: active
---

# LST M2MUPGROUP（查询M2M关联的UPF组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询M2M关联的UPF组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M2MUPGROUP]] · M2M关联的UPF组（M2MUPGROUP）

## 使用实例

查询M2M关联的UPF组：

```
LST M2MUPGROUP:;
RETCODE = 0  操作成功

结果如下
--------
UPF组名称 

upfgrp1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-M2MUPGROUP.md`
