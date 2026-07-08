---
id: UNC@20.15.2@MMLCommand@RMV PNFSMFINFO
type: MMLCommand
name: RMV PNFSMFINFO（删除对端SMF的信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PNFSMFINFO
command_category: 配置类
applicable_nf:
- AMF
- NCG
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端SMF域名信息管理
status: active
---

# RMV PNFSMFINFO（删除对端SMF的信息）

## 功能

**适用NF：AMF、NCG、SMF**

该命令用于删除本地配置的对端SMF支持的PGW域名信息和接入方式等信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。NFINSTANCEID参数建议满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| PGWFQDN | PGW域名 | 可选必选说明：必选参数<br>参数含义：当SMF与PGW-C合一部署时，该参数表示PGW-C的FQDN名称，用于用户从EPC到5G互操作流程中，帮助AMF找到EPC承载所在的融合网关。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PNFSMFINFO]] · 对端SMF的信息（PNFSMFINFO）

## 使用实例

删除对端SMF的信息，NF标识为SMF_Instance_0，PGWFQDN为huawei.com。

```
RMV PNFSMFINFO: NFINSTANCEID="SMF_Instance_0", PGWFQDN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PNFSMFINFO.md`
