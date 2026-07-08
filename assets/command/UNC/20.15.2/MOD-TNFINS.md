---
id: UNC@20.15.2@MMLCommand@MOD TNFINS
type: MMLCommand
name: MOD TNFINS（修改目标NF实例）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TNFINS
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
- 目标NF实例管理
status: active
---

# MOD TNFINS（修改目标NF实例）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改目标NF实例的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：无 |
| SCHEMA | 协议模式 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF通信的协议模式。<br>数据来源：全网规划<br>取值范围：<br>- “UriSchemeINVALID（SchemaInvalid）”：已废弃。<br>- “http（http）”：http<br>- “https（https）”：https<br>- “UriSchemeMAX（SchemaMax）”：已废弃。<br>默认值：无<br>配置原则：<br>建议本端和对端的协议模式一致。否则，无法建立HTTP链接。注意：当设置为“UriSchemeINVALID”和“UriSchemeMAX”时，协议模式默认以“http”方式生效。 |
| FQDN | 域名 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的域名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~127。不区分大小写。<br>默认值：无<br>配置原则：<br>- FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。例如：amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org |
| NFDESCNAME | NF描述名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF实例的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TNFINS]] · 目标NF实例（TNFINS）

## 使用实例

运营商A需要修改索引为1的目标NF实例，将FQDN修改为huawei.com。

```
MOD TNFINS: TNFINSINDEX=1, FQDN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改目标NF实例（MOD-TNFINS）_09651413.md`
