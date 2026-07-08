---
id: UDG@20.15.2@MMLCommand@RTR IPSECSTATISTIC
type: MMLCommand
name: RTR IPSECSTATISTIC（清除IPsec统计信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: IPSECSTATISTIC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IPsec调测
- IPsec诊断信息
- IPsec处理报文统计信息
status: active
---

# RTR IPSECSTATISTIC（清除IPsec统计信息）

## 功能

该命令用于清除IPsec处理报文统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SANAME | 安全联盟名称 | 可选必选说明：可选参数<br>参数含义：安全联盟名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。不区分大小写。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用DSP RU命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSECSTATISTIC]] · IPsec统计信息（IPSECSTATISTIC）

## 使用实例

清除IPsec处理报文统计信息：

```
RTR IPSECSTATISTIC:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除IPsec统计信息（RTR-IPSECSTATISTIC）_00841613.md`
