---
id: UNC@20.15.2@MMLCommand@ADD NFSUPIRANGE
type: MMLCommand
name: ADD NFSUPIRANGE（增加NF SUPIRANGE信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFSUPIRANGE
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
- NF SUPIRANGE信息管理
status: active
---

# ADD NFSUPIRANGE（增加NF SUPIRANGE信息）

## 功能

**适用NF：SMSF**

该命令用于添加NF实例支持的SUPIRANGE信息。当NF实例向NRF注册时，将实例的SUPIRANGE信息带给NRF，为业务流程中其他NF发现该NF时提供选择信息。

## 注意事项

- 该命令执行后立即生效。

- 对于同一个NF实例，起始号段不能重复。
- 当本地没有配置NF实例支持的SUPIRANGE时，代表此NF允许所有SUPI号段范围的用户访问。

- 最多可输入20000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SUPIRANGE对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，SMSF_Instance_0。<br>默认值：无<br>配置原则：<br>本参数取值与ADD NFUUID命令中的“NF实例名称”参数取值保持一致时，关联关系生效。 |
| RANGESTART | 起始号段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SUPI的起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>SUPI的终止号段需要不小于SUPI的起始号段，且终止号段和起始号段长度需相等。 |
| RANGEEND | 终止号段 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SUPI的终止号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。<br>默认值：无<br>配置原则：<br>SUPI的终止号段需要不小于SUPI的起始号段，且终止号段和起始号段长度需相等。 |

## 操作的配置对象

- [NF SUPIRANGE信息（NFSUPIRANGE）](configobject/UNC/20.15.2/NFSUPIRANGE.md)

## 使用实例

增加NF SUPIRANGE信息，NF实例标识为SMSF_Instance_0，起始号段为123031200100001，终止号段为123031200100001。

```
ADD NFSUPIRANGE: NFINSTANCENAME="SMSF_Instance_0", RANGESTART="123031200100001",RANGEEND="123031200100001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NF-SUPIRANGE信息（ADD-NFSUPIRANGE）_91460553.md`
