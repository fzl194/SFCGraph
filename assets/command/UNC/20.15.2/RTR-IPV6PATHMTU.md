---
id: UNC@20.15.2@MMLCommand@RTR IPV6PATHMTU
type: MMLCommand
name: RTR IPV6PATHMTU（清除IPv6 Path MTU配置）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: IPV6PATHMTU
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 Path MTU
status: active
---

# RTR IPV6PATHMTU（清除IPv6 Path MTU配置）

## 功能

该命令用于清除IPv6路径MTU。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6PATHMTU]] · IPv6 Path MTU配置（IPV6PATHMTU）

## 使用实例

清除IPv6 Path MTU：

```
RTR IPV6PATHMTU:VRFNAME="vpn1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-IPV6PATHMTU.md`
