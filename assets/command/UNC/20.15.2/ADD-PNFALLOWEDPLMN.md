---
id: UNC@20.15.2@MMLCommand@ADD PNFALLOWEDPLMN
type: MMLCommand
name: ADD PNFALLOWEDPLMN（增加对端NF允许的PLMN信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PNFALLOWEDPLMN
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
- 对端NF的PLMN信息管理
status: active
---

# ADD PNFALLOWEDPLMN（增加对端NF允许的PLMN信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于增加对端NF服务支持的允许访问的PLMN。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 注意事项

- 该命令执行后立即生效。

- 当前该功能尚未实现。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值需要与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |
| SRVINSTANCEID | 服务实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端服务实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数由2~3个十进制数字组成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFALLOWEDPLMN]] · 对端NF允许的PLMN信息（PNFALLOWEDPLMN）

## 使用实例

增加NF实例标识为SMF_Instance_0的对端NF的Service_Instance_0服务实例支持的PLMN信息，MCC为460，MNC为01。

```
ADD PNFALLOWEDPLMN: NFINSTANCEID="SMF_Instance_0", SRVINSTANCEID="Service_Instance_0", MCC="460", MNC="01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加对端NF允许的PLMN信息（ADD-PNFALLOWEDPLMN）_09652467.md`
