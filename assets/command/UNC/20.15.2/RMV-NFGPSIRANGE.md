---
id: UNC@20.15.2@MMLCommand@RMV NFGPSIRANGE
type: MMLCommand
name: RMV NFGPSIRANGE（删除NF GPSIRANGE信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFGPSIRANGE
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF GPSIRANGE信息管理
status: active
---

# RMV NFGPSIRANGE（删除NF GPSIRANGE信息）

## 功能

**适用NF：SMSF**

该命令用于删除NF实例支持的GPSIRANGE信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GPSIRANGE对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，SMSF_Instance_0。<br>默认值：无<br>配置原则：<br>本参数取值与ADD NFUUID命令中的“NF实例名称”参数取值保持一致时，关联关系生效。 |
| RANGESTART | 起始号段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GPSI的起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>GPSI的终止号段需要不小于GPSI的起始号段，且终止号段和起始号段长度需相等。 |

## 操作的配置对象

- [NF GPSIRANGE信息（NFGPSIRANGE）](configobject/UNC/20.15.2/NFGPSIRANGE.md)

## 使用实例

删除NF GPSIRANGE信息，NF实例名称为SMSF_Instance_0，起始号段为138100000000000。

```
RMV NFGPSIRANGE: NFINSTANCENAME="SMSF_Instance_0", RANGESTART="138100000000000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF-GPSIRANGE信息（RMV-NFGPSIRANGE）_44339640.md`
