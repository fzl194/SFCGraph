---
id: UNC@20.15.2@MMLCommand@RMV PNFGROUPID
type: MMLCommand
name: RMV PNFGROUPID（删除对端NF的群组信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFGROUPID
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
- 对端NF组管理
status: active
---

# RMV PNFGROUPID（删除对端NF的群组信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于删除本地配置的对端NF实例支持的群组信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| GROUPID | 群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF服务的群组标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>对端NF如果为LMF，则只可通过此命令配置一个GroupId。 |

## 操作的配置对象

- [对端NF的群组信息（PNFGROUPID）](configobject/UNC/20.15.2/PNFGROUPID.md)

## 使用实例

由于规划变更，对端NF实例标识为UPF_Instance_0的NF不再支持群组GROUP01，需要删除。

```
RMV PNFGROUPID:NFINSTANCEID="SMF_Instance_0", GROUPID="GROUP01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对端NF的群组信息（RMV-PNFGROUPID）_09653640.md`
