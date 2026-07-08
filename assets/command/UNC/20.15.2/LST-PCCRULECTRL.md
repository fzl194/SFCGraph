---
id: UNC@20.15.2@MMLCommand@LST PCCRULECTRL
type: MMLCommand
name: LST PCCRULECTRL（查询PCC规则相关控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCRULECTRL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC Rule控制
status: active
---

# LST PCCRULECTRL（查询PCC规则相关控制）

## 功能

**适用NF：SMF**

该命令用于查询PCC规则相关控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCRULECTRL]] · PCC规则相关控制（PCCRULECTRL）

## 使用实例

查询PCC规则相关控制参数。

```
LST PCCRULECTRL:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCCRULECTRL.md`
