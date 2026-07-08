---
id: UDG@20.15.2@MMLCommand@LST PFCPSSUSTATERPT
type: MMLCommand
name: LST PFCPSSUSTATERPT（查询智能单元状态上报相关属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PFCPSSUSTATERPT
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
- SGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- PFCP负荷上报管理
- SSU负荷上报
status: active
---

# LST PFCPSSUSTATERPT（查询智能单元状态上报相关属性）

## 功能

**适用NF：UPF、PGW-U、SGW-U**

该命令用来查询智能单元状态上报相关属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PFCPSSUSTATERPT]] · 智能单元状态上报相关属性（PFCPSSUSTATERPT）

## 使用实例

查询查询智能单元状态上报相关属性：

```
LST PFCPSSUSTATERPT:;
```

```

```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PFCPSSUSTATERPT.md`
