---
id: UNC@20.15.2@MMLCommand@RTR IPSTATISTIC
type: MMLCommand
name: RTR IPSTATISTIC（清除IP报文统计）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: IPSTATISTIC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- IP报文统计
status: active
---

# RTR IPSTATISTIC（清除IP报文统计）

## 功能

该命令用于清除IP报文统计信息。

如果需要统计在某一时间内的IP报文统计信息，这时必须在统计开始前清除原有的IP报文统计信息后，使用DSP IPSTATISTIC命令查看IP报文统计信息。

不指定参数时，清除所有接口的统计信息；当指定参数时，可以清除指定接口的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP报文统计的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPSTATISTIC]] · IP报文统计（IPSTATISTIC）

## 使用实例

清除IP报文统计：

```
RTR IPSTATISTIC:IFNAME="GigabitEthernet0/0/1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-IPSTATISTIC.md`
