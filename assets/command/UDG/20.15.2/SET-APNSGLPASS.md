---
id: UDG@20.15.2@MMLCommand@SET APNSGLPASS
type: MMLCommand
name: SET APNSGLPASS（设置APN单通检测开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: APNSGLPASS
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- 单通检测
status: active
---

# SET APNSGLPASS（设置APN单通检测开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置是否开启指定APN的用户数据流量单通故障检测功能。

## 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条。
- 对于一些特殊业务，例如抄表，只有上行流量，没有下行流量，则需要关闭对应APN的单通故障检测功能。
- 如果检测到用户数据流量发生单通故障，会触发设备内环回探测，开启用户数据跟踪，可以跟踪到探测报文。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH |
| --- | --- |
| 初始值 | ENABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SWITCH | 开关标识 | 可选必选说明：必选参数<br>参数含义：用户数据流量单通故障检测功能的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PF_ACT_DISABLE：执行去使能。<br>- PF_ACT_ENABLE：执行使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN单通检测开关（APNSGLPASS）](configobject/UDG/20.15.2/APNSGLPASS.md)

## 使用实例

设置APN为apn1.com的单通故障检测功能开关为关闭：

```
SET APNSGLPASS: APN="apn1.com", SWITCH=PF_ACT_DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置APN单通检测开关（SET-APNSGLPASS）_82837110.md`
