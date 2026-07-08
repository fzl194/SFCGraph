---
id: UDG@20.15.2@MMLCommand@RTR TCPSTATRTTRANGE
type: MMLCommand
name: RTR TCPSTATRTTRANGE（恢复TCP统计功能的RTT区间为初始值）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: TCPSTATRTTRANGE
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- TcpStatRttRange
status: active
---

# RTR TCPSTATRTTRANGE（恢复TCP统计功能的RTT区间为初始值）

## 功能

**适用NF：PGW-U、UPF**

该命令用于把TCP统计功能中的UE侧、SP侧RTT区间恢复到初始值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [TCP统计功能的RTT区间为初始值（TCPSTATRTTRANGE）](configobject/UDG/20.15.2/TCPSTATRTTRANGE.md)

## 使用实例

如果运营商需要把UE侧、SP侧RTT区间恢复到初始值：

```
RTR TCPSTATRTTRANGE:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复TCP统计功能的RTT区间为初始值（RTR-TCPSTATRTTRANGE）_74589219.md`
