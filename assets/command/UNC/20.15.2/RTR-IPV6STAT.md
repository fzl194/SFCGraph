---
id: UNC@20.15.2@MMLCommand@RTR IPV6STAT
type: MMLCommand
name: RTR IPV6STAT（清除IPv6统计计数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: IPV6STAT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6统计计数
status: active
---

# RTR IPV6STAT（清除IPv6统计计数）

## 功能

该命令用于对IPv6报文统计计数清零。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6STAT]] · IPv6统计计数（IPV6STAT）

## 使用实例

清除IPv6报文统计计数：

```
RTR IPV6STAT:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-IPV6STAT.md`
