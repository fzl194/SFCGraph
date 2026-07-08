---
id: UNC@20.15.2@MMLCommand@RTR GLOBALNBNS
type: MMLCommand
name: RTR GLOBALNBNS（恢复系统默认NBNS）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: GLOBALNBNS
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- NBNS选择管理
- 缺省NBNS
status: active
---

# RTR GLOBALNBNS（恢复系统默认NBNS）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于恢复系统NBNS属性。NBNS功能开关不会被恢复。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLOBALNBNS]] · 系统默认NBNS（GLOBALNBNS）

## 使用实例

恢复系统NBNS属性：

```
RTR GLOBALNBNS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复系统默认NBNS（RTR-GLOBALNBNS）_22556861.md`
