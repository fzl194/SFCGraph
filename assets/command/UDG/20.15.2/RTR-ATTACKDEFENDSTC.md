---
id: UDG@20.15.2@MMLCommand@RTR ATTACKDEFENDSTC
type: MMLCommand
name: RTR ATTACKDEFENDSTC（清除攻击防范统计信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: ATTACKDEFENDSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- 攻击防范
status: active
---

# RTR ATTACKDEFENDSTC（清除攻击防范统计信息）

## 功能

该命令用于清除攻击防范统计计数。

不指定参数时，清除所有攻击类型的统计信息；当指定参数时，可以清除指定攻击类型的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTACKTYPE | 攻击类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置攻击类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ABNORMAL：畸形报文。<br>- FRAGMENT：分片报文。<br>- TCP-SYN：TCP-SYN报文。<br>- UDP-FLOOD：UDP泛洪报文。<br>- ICMP-FLOOD：ICMP泛洪报文。<br>默认值：无<br>配置原则：如果不输入该参数，则表示所有攻击类型。 |

## 操作的配置对象

- [攻击防范统计信息（ATTACKDEFENDSTC）](configobject/UDG/20.15.2/ATTACKDEFENDSTC.md)

## 使用实例

清除攻击防范统计计数信息：

```
RTR ATTACKDEFENDSTC:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除攻击防范统计信息（RTR-ATTACKDEFENDSTC）_00441269.md`
