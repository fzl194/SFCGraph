---
id: UNC@20.15.2@MMLCommand@RMV PCSCFIMSISDNSEG
type: MMLCommand
name: RMV PCSCFIMSISDNSEG（删除IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCSCFIMSISDNSEG
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
- IMS管理
- P-CSCF管理
- P-CSCF选择的IMSI和MSISDN号段
status: active
---

# RMV PCSCFIMSISDNSEG（删除IMSI和MSISDN号段）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于删除IMSI/MSISDN号码段。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCSCFIMSISDNSEG]] · IMSI和MSISDN号段（PCSCFIMSISDNSEG）

## 使用实例

删除IMSI和MSISDN号段：IMSI/MSISDN号段名称为huawei，命令为：

```
RMV PCSCFIMSISDNSEG:SEGMENTNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PCSCFIMSISDNSEG.md`
