---
id: UDG@20.15.2@MMLCommand@RTR MPACCOUNTERV6
type: MMLCommand
name: RTR MPACCOUNTERV6（清除IPv6 MPAC策略匹配统计计数）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: MPACCOUNTERV6
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- IPv6规则匹配统计
status: active
---

# RTR MPACCOUNTERV6（清除IPv6 MPAC策略匹配统计计数）

## 功能

该命令用于清除当前策略匹配统计计数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无<br>配置原则：不指定策略名字，默认清除IPv6所有策略匹配统计计数。 |

## 操作的配置对象

- [IPv6 MPAC策略匹配统计计数（MPACCOUNTERV6）](configobject/UDG/20.15.2/MPACCOUNTERV6.md)

## 使用实例

清除IPv6 MPAC策略匹配统计计数：

```
RTR MPACCOUNTERV6:POLICYNAME="policyV6";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除IPv6-MPAC策略匹配统计计数（RTR-MPACCOUNTERV6）_49961078.md`
