---
id: UDG@20.15.2@MMLCommand@RMV SECPOLICYACL
type: MMLCommand
name: RMV SECPOLICYACL（删除安全策略ACL规则）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SECPOLICYACL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略ACL
status: active
---

# RMV SECPOLICYACL（删除安全策略ACL规则）

## 功能

该命令用来删除一个安全策略规则。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：安全策略号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- WhiteList：白名单。<br>- BlackList：黑名单。<br>- UserFlow：用户自定义流。<br>- IPV6WhiteList：IPv6白名单。<br>- IPV6BlackList：IPv6黑名单。<br>- IPV6UserFlow：IPv6用户自定义流。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“UserFlow” 或 “IPV6UserFlow”时为必选参数。<br>参数含义：安全策略类型编号，对应不同策略类型其含义不同，如SECPOLICYTYPE为User Flow，则此值为1－32的数值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [安全策略ACL规则（SECPOLICYACL）](configobject/UDG/20.15.2/SECPOLICYACL.md)

## 使用实例

删除安全策略规则：

```
RMV SECPOLICYACL:SECPOLICYID=1,SECPOLICYTYPE=WhiteList;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除安全策略ACL规则（RMV-SECPOLICYACL）_50280586.md`
