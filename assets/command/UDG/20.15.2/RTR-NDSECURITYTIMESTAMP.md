---
id: UDG@20.15.2@MMLCommand@RTR NDSECURITYTIMESTAMP
type: MMLCommand
name: RTR NDSECURITYTIMESTAMP（清除ND安全时间戳）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: NDSECURITYTIMESTAMP
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND安全
status: active
---

# RTR NDSECURITYTIMESTAMP（清除ND安全时间戳）

## 功能

该命令用于清除ND安全时间戳。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [ND安全时间戳（NDSECURITYTIMESTAMP）](configobject/UDG/20.15.2/NDSECURITYTIMESTAMP.md)

## 使用实例

清除ND安全时间戳：

```
RTR NDSECURITYTIMESTAMP:IFNAME="Ethernet65/0/8";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除ND安全时间戳（RTR-NDSECURITYTIMESTAMP）_50121578.md`
