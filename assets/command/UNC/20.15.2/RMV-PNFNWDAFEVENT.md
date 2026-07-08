---
id: UNC@20.15.2@MMLCommand@RMV PNFNWDAFEVENT
type: MMLCommand
name: RMV PNFNWDAFEVENT（删除对端NWDAF信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFNWDAFEVENT
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NWDAF信息管理
status: active
---

# RMV PNFNWDAFEVENT（删除对端NWDAF信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于删除本地配置的对端NWDAF的信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于唯一指定某一个NWDAF实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~38。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，NWDAF_Instance_0。<br>默认值：无<br>配置原则：无 |
| NWDAFINFOID | NwdafInfo标识 | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识NWDAF实例中的某个NwdafInfo。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFNWDAFEVENT]] · 对端NWDAF信息（PNFNWDAFEVENT）

## 使用实例

删除对端NWDAF信息，NF实例标识为NWDAF_Instance_1，NwdafInfo标识为central。

```
RMV PNFNWDAFEVENT: NFINSTANCEID="NWDAF_Instance_1", NWDAFINFOID="central";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NWDAF信息（RMV-PNFNWDAFEVENT）_56264018.md`
