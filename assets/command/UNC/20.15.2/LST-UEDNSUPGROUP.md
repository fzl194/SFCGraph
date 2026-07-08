---
id: UNC@20.15.2@MMLCommand@LST UEDNSUPGROUP
type: MMLCommand
name: LST UEDNSUPGROUP（查询DNS关联的UPF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UEDNSUPGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- DNS关联的UPF组管理
status: active
---

# LST UEDNSUPGROUP（查询DNS关联的UPF组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询DNS关联的UPF组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UEDNSUPGROUP]] · DNS关联的UPF组（UEDNSUPGROUP）

## 使用实例

查询DNS关联的UPF组：

```
LST UEDNSUPGROUP:;
RETCODE = 0  操作成功

结果如下
--------
UPF组名称 

upfgrp1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UEDNSUPGROUP.md`
