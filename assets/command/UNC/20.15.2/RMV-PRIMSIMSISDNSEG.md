---
id: UNC@20.15.2@MMLCommand@RMV PRIMSIMSISDNSEG
type: MMLCommand
name: RMV PRIMSIMSISDNSEG（删除代理IMSI/MSISDN号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PRIMSIMSISDNSEG
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 代理选择的IMSI_MSISDN号段
status: active
---

# RMV PRIMSIMSISDNSEG（删除代理IMSI/MSISDN号段）

## 功能

**适用NF：PGW-C、GGSN、SGW-C、SMF**

该命令用于删除代理IMSI/MSISDN号段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRIMSIMSISDNSEG]] · 代理IMSI/MSISDN号段（PRIMSIMSISDNSEG）

## 使用实例

删除“IMSI/MSISDN号段名称”为“imsi1”的代理IMSI/MSISDN号段配置：

```
RMV PRIMSIMSISDNSEG: SEGMENTNAME="imsi1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PRIMSIMSISDNSEG.md`
