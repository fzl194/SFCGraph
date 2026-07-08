---
id: UNC@20.15.2@MMLCommand@RTR CONSSTATIC
type: MMLCommand
name: RTR CONSSTATIC（清除消费者消息统计计数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: CONSSTATIC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Diameter管理
- 消费者统计
status: active
---

# RTR CONSSTATIC（清除消费者消息统计计数）

## 功能

该命令用于清空Diameter消费者消息统计计数。仅作为可维命令使用，不影响其它类型的消息统计。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CONSSTATIC]] · 消费者统计信息（CONSSTATIC）

## 使用实例

清空Diameter消费者统计计数：

```
RTR CONSSTATIC:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-CONSSTATIC.md`
