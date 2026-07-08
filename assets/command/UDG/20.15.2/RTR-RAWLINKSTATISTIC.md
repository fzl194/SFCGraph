---
id: UDG@20.15.2@MMLCommand@RTR RAWLINKSTATISTIC
type: MMLCommand
name: RTR RAWLINKSTATISTIC（清除Raw-link报文统计）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: RAWLINKSTATISTIC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- Raw-link报文统计
status: active
---

# RTR RAWLINKSTATISTIC（清除Raw-link报文统计）

## 功能

该命令用于用来清除Raw-link报文统计信息。

如果需要统计在某一时间内的Raw-link报文统计信息，这时必须在统计开始前清除原有的Raw-link报文统计信息后，使用DSP RAWLINKSTATISTIC命令查看Raw-link报文统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RAWLINKSTATISTIC]] · Raw-link报文统计（RAWLINKSTATISTIC）

## 使用实例

清除当前系统的Raw-link报文统计：

```
RTR RAWLINKSTATISTIC:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-RAWLINKSTATISTIC.md`
