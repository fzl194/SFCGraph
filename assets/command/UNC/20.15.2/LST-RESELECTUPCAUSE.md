---
id: UNC@20.15.2@MMLCommand@LST RESELECTUPCAUSE
type: MMLCommand
name: LST RESELECTUPCAUSE（查询重选UPF故障原因值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESELECTUPCAUSE
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 故障原因值重选UPF
status: active
---

# LST RESELECTUPCAUSE（查询重选UPF故障原因值）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询重选UPF故障原因值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESELECTUPCAUSE]] · 重选UPF故障原因值（RESELECTUPCAUSE）

## 使用实例

查询重选UPF故障原因值。

```
LST RESELECTUPCAUSE:
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESELECTUPCAUSE.md`
