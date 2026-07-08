---
id: UDG@20.15.2@MMLCommand@RTR VOLTEPERFTDELAY
type: MMLCommand
name: RTR VOLTEPERFTDELAY（恢复理想到达报文的最小时延偏差、固定传输时延）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: VOLTEPERFTDELAY
command_category: 动作类
applicable_nf:
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- VoLTE质量监控配置
- VoLTE 理想到达报文
status: active
---

# RTR VOLTEPERFTDELAY（恢复理想到达报文的最小时延偏差、固定传输时延）

## 功能

**适用NF：PGW-U**

该命令用于恢复理想报文的最小时延偏差、固定传输时延为系统初始设置值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/VOLTEPERFTDELAY]] · 理想到达报文的最小时延偏差、固定传输时延（VOLTEPERFTDELAY）

## 使用实例

恢复理想报文的最小时延偏差、固定传输时延为系统初始设置值：

```
RTR VOLTEPERFTDELAY:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复理想到达报文的最小时延偏差、固定传输时延（RTR-VOLTEPERFTDELAY）_69178848.md`
