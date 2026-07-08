---
id: UNC@20.15.2@MMLCommand@ULK USER
type: MMLCommand
name: ULK USER（解锁用户）
nf: UNC
version: 20.15.2
verb: ULK
object_keyword: USER
command_category: 动作类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 用户管理
status: active
---

# ULK USER（解锁用户）

## 功能

![](解锁用户（ULK USER）_51174354.assets/notice_3.0-zh-cn_2.png)

该操作执行后，会影响系统的安全保护，可能存在安全风险，请谨慎操作。

**适用NF：NCG**

该命令用于解锁当前已锁定的用户。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug
G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERNAME | 用户名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要解锁的用户名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USER]] · 用户锁定状态（USER）

## 使用实例

解锁当前已锁定的用户：

```
ULK USER: USERNAME="BS";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ULK-USER.md`
