---
id: UDG@20.15.2@MMLCommand@RMV GLBURRGROUP
type: MMLCommand
name: RMV GLBURRGROUP（删除全局计费属性）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: GLBURRGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 全局使用量上报规则组
status: active
---

# RMV GLBURRGROUP（删除全局计费属性）

## 功能

**适用NF：PGW-U、UPF**

RMV GLBURRGROUP命令用于将全局计费属性恢复成默认记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBURRGROUP]] · 全局计费属性（GLBURRGROUP）

## 使用实例

假如用户要删除全局计费属性：

```
RMV GLBURRGROUP:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除全局计费属性（RMV-GLBURRGROUP）_86528078.md`
