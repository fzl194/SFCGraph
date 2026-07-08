---
id: UDG@20.15.2@MMLCommand@RMV TWAMPRESPONDER
type: MMLCommand
name: RMV TWAMPRESPONDER（删除TWAMP响应端）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TWAMPRESPONDER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP响应端配置
status: active
---

# RMV TWAMPRESPONDER（删除TWAMP响应端）

## 功能

该命令用于删除TWAMP响应端。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESPONDERID | 响应端索引 | 可选必选说明：必选参数<br>参数含义：该参数用于配置响应端索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TWAMP响应端（TWAMPRESPONDER）](configobject/UDG/20.15.2/TWAMPRESPONDER.md)

## 使用实例

删除响应端索引为1的实例：

```
RMV TWAMPRESPONDER: RESPONDERID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除TWAMP响应端（RMV-TWAMPRESPONDER）_27102482.md`
