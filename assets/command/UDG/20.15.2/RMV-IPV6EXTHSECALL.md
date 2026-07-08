---
id: UDG@20.15.2@MMLCommand@RMV IPV6EXTHSECALL
type: MMLCommand
name: RMV IPV6EXTHSECALL（删除IPv6扩展头选项安全配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: IPV6EXTHSECALL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6扩展头选项安全配置
status: active
---

# RMV IPV6EXTHSECALL（删除IPv6扩展头选项安全配置）

## 功能

该命令用于删除IPv6扩展头选项安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCHOP | IPv6过滤规则 | 可选必选说明：必选参数<br>参数含义：该参数表示允许或拒绝对应选项IPv6报文的处理能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |

## 操作的配置对象

- [IPv6扩展头选项安全配置（IPV6EXTHSECALL）](configobject/UDG/20.15.2/IPV6EXTHSECALL.md)

## 使用实例

删除IPv6扩展头选项安全配置：

```
RMV IPV6EXTHSECALL:SWITCHOP=deny;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除IPv6扩展头选项安全配置（RMV-IPV6EXTHSECALL）_49802466.md`
