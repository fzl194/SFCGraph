---
id: UDG@20.15.2@MMLCommand@RTR IKEALLSTATISTIC
type: MMLCommand
name: RTR IKEALLSTATISTIC（恢复全部IKE统计信息）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: IKEALLSTATISTIC
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- 操作维护
- 系统调测
- IPsec调测
- IKE统计信息
status: active
---

# RTR IKEALLSTATISTIC（恢复全部IKE统计信息）

## 功能

该命令用于清除所有的IKE统计数据，包括错误计数统计。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：该参数表示Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IKEALLSTATISTIC]] · 全部IKE统计信息（IKEALLSTATISTIC）

## 使用实例

清除所有的IKE统计数据，包括错误计数统计：

```
RTR IKEALLSTATISTIC:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RTR-IKEALLSTATISTIC.md`
