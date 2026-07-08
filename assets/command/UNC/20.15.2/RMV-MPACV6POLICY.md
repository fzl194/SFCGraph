---
id: UNC@20.15.2@MMLCommand@RMV MPACV6POLICY
type: MMLCommand
name: RMV MPACV6POLICY（删除IPv6 MPAC策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MPACV6POLICY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- MPAC
- 管理平面接入控制IPv6策略
status: active
---

# RMV MPACV6POLICY（删除IPv6 MPAC策略）

## 功能

该命令用于删除IPv6策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定创建策略的策略名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。大小写敏感，英文字母开头，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPACV6POLICY]] · IPv6 MPAC策略（MPACV6POLICY）

## 使用实例

删除IPv6 MPAC策略：

```
RMV MPACV6POLICY:POLICYNAME="policyV6";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPv6-MPAC策略（RMV-MPACV6POLICY）_00601473.md`
