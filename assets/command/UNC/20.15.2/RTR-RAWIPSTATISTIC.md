---
id: UNC@20.15.2@MMLCommand@RTR RAWIPSTATISTIC
type: MMLCommand
name: RTR RAWIPSTATISTIC（清除RawIP报文统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: RAWIPSTATISTIC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- RawIP报文统计
status: active
---

# RTR RAWIPSTATISTIC（清除RawIP报文统计）

## 功能

该命令用于清除RawIP报文统计信息。

如果需要统计在某一时间内的RawIP报文统计信息，这时必须在统计开始前清除原有的RawIP报文统计信息后，使用DSP RAWIPSTATISTIC命令查看RawIP报文统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RawIP报文统计的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RAWIPSTATISTIC]] · RawIP报文统计（RAWIPSTATISTIC）

## 使用实例

清除当前系统的RawIP报文统计：

```
RTR RAWIPSTATISTIC:IPVERSION=IPv4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-RAWIPSTATISTIC.md`
