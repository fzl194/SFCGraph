---
id: UNC@20.15.2@MMLCommand@RMV GLBURRGROUP
type: MMLCommand
name: RMV GLBURRGROUP（删除全局使用量上报规则组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GLBURRGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 全局使用量上报规则组
status: active
---

# RMV GLBURRGROUP（删除全局使用量上报规则组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于PDP用户将全局使用量上报规则组恢复成默认记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBURRGROUP]] · 全局使用量上报规则组（GLBURRGROUP）

## 使用实例

假如用户要删除全局使用量上报规则组：

```
RMV GLBURRGROUP:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GLBURRGROUP.md`
