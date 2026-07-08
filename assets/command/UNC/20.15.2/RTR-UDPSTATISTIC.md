---
id: UNC@20.15.2@MMLCommand@RTR UDPSTATISTIC
type: MMLCommand
name: RTR UDPSTATISTIC（清除UDP报文统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: UDPSTATISTIC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- UDP报文统计
status: active
---

# RTR UDPSTATISTIC（清除UDP报文统计）

## 功能

该命令用于清除UDP报文统计信息。

如果需要统计在某一时间内的UDP报文统计信息，这时必须在统计开始前清除原有的UDP报文统计信息后，使用DSP UDPSTATISTIC命令查看UDP报文统计信息。不。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UDP报文统计的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |

## 操作的配置对象

- [UDP报文统计（UDPSTATISTIC）](configobject/UNC/20.15.2/UDPSTATISTIC.md)

## 使用实例

清除当前系统的UDP报文统计：

```
RTR UDPSTATISTIC:IPVERSION=IPv4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除UDP报文统计（RTR-UDPSTATISTIC）_49961478.md`
