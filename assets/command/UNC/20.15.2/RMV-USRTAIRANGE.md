---
id: UNC@20.15.2@MMLCommand@RMV USRTAIRANGE
type: MMLCommand
name: RMV USRTAIRANGE（删除用户TAI区域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRTAIRANGE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- 用户TAI区域
status: active
---

# RMV USRTAIRANGE（删除用户TAI区域）

## 功能

![](删除用户TAI区域（RMV USRTAIRANGE）_88377452.assets/notice_3.0-zh-cn_2.png)

删除用户TAI区域不当可能导致动态PCC用户无法基于用户TAI区域绑定的业务服务区选择PCF，进而影响用户使用业务。

**适用NF：SMF、PGW-C、GGSN**

该命令用于删除指定RANGENAME的用户TAI区域。

## 注意事项

- 该命令执行后立即生效。

- 如果用户TAI区域已经与PCF业务服务区绑定，则不允许删除，需要执行命令RMV PCFSSCOPEBIND解除绑定关系后再删除。如需删除所有记录，请使用RMV USRTAIRANGEALL命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGENAME | 区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRTAIRANGE]] · 用户TAI区域（USRTAIRANGE）

## 使用实例

删除区域名称为tai1的用户TAI区域。

```
RMV USRTAIRANGE: RANGENAME="tai1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户TAI区域（RMV-USRTAIRANGE）_88377452.md`
