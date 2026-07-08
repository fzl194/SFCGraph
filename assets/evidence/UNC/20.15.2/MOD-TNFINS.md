# 修改目标NF实例（MOD TNFINS）

- [命令功能](#ZH-CN_MMLREF_0209651413__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651413__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651413__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651413__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651413)

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于修改目标NF实例的配置。

## [注意事项](#ZH-CN_MMLREF_0209651413)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651413)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651413)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNFINSINDEX | 目标NF实例索引 | 可选必选说明：必选参数<br>参数含义：本参数用于指定目标NF实例索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2047。<br>默认值：无<br>配置原则：无 |
| SCHEMA | 协议模式 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF通信的协议模式。<br>数据来源：全网规划<br>取值范围：<br>- “UriSchemeINVALID（SchemaInvalid）”：已废弃。<br>- “http（http）”：http<br>- “https（https）”：https<br>- “UriSchemeMAX（SchemaMax）”：已废弃。<br>默认值：无<br>配置原则：<br>建议本端和对端的协议模式一致。否则，无法建立HTTP链接。注意：当设置为“UriSchemeINVALID”和“UriSchemeMAX”时，协议模式默认以“http”方式生效。 |
| FQDN | 域名 | 可选必选说明：可选参数<br>参数含义：本参数用于指定目标NF的域名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~127。不区分大小写。<br>默认值：无<br>配置原则：<br>- FQDN由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。例如：amf1.cluster1.net2.amf.5gc.mnc012.mcc345.3gppnetwork.org |
| NFDESCNAME | NF描述名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF实例的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651413)

运营商A需要修改索引为1的目标NF实例，将FQDN修改为huawei.com。

```
MOD TNFINS: TNFINSINDEX=1, FQDN="huawei.com";
```
