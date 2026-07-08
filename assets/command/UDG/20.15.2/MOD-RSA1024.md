---
id: UDG@20.15.2@MMLCommand@MOD RSA1024
type: MMLCommand
name: MOD RSA1024（修改RSA1024公钥配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: RSA1024
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- RSA1024公钥配置
status: active
---

# MOD RSA1024（修改RSA1024公钥配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改一个RSA1024的相关配置。

## 注意事项

- 该命令执行后立即生效。
- 当前命令中 RSAPSWDTYPE 中的 CERTIFICATE_FILE 项功能不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RSA1024NAME | RSA1024公钥名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RSA1024公钥配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| RSAPSWDKEYN | 公钥的N值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RSAPSWDTYPE”配置为“PUBLIC_KEY”时为必选参数。<br>参数含义：该参数用于直接配置公钥中的N值，与RSAPSWDKEYE共同组成公钥内容。配置了该参数，则不需要对公钥名称 RSA1024NAME进行文件查找、校验和解析，直接使用配置值进行加密。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～256。由字符0~9和字母A~F、a~f组成，不区分大小写，长度为偶数。<br>默认值：无<br>配置原则：配置字符长度不应少于128字节，并且配置值字符按照十六进制转换成数字后必须大于E值。 |
| RSAPSWDKEYE | 公钥的E值 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RSAPSWDTYPE”配置为“PUBLIC_KEY”时为必选参数。<br>参数含义：该参数用于直接配置公钥中的E值，与RSAPSWDKEYN共同组成公钥内容。配置了该参数，则不需要对公钥名称 RSA1024NAME进行文件查找、校验和解析，直接使用配置值进行加密。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～256。由字符0~9和字母A~F、a~f组成，不区分大小写，长度为偶数。<br>默认值：无<br>配置原则：配置值字符按照十六进制转换成数字后，不应小于2^16 + 1。 |
| HEADPREFIXSW | 头增强前缀开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置头增强RSA1024加密时是否携带前缀。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| COUNTRYCODE | 国家码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HEADPREFIXSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于设置头增强RSA1024加密携带前缀时，前缀中的国家码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。3位数字，000~999。<br>默认值：无<br>配置原则：输入单空格时将删除该参数已有配置。 |
| NETWORKCODE | 网络码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HEADPREFIXSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于设置头增强RSA1024加密携带前缀时，前缀中的网络码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～3。3位数字，000~999。<br>默认值：无<br>配置原则：输入单空格时将删除该参数已有配置。 |
| RSAPSWDTYPE | 公钥配置方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RSA1024公钥证书的公钥配置方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PUBLIC_KEY：配置公钥。<br>- CERTIFICATE_FILE：证书文件。<br>默认值：无<br>配置原则：无 |
| RSACERTFILEID | RSA证书文件索引 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RSAPSWDTYPE”配置为“CERTIFICATE_FILE”时为必选参数。<br>参数含义：该参数用于指定RSA公钥证书的书文件索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1024。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RSA1024]] · RSA1024公钥配置（RSA1024）

## 使用实例

假如运营商希望把名称为“test”的RSA1024配置修改为公钥N值BCDE，E值101010，关闭头增强前缀：

```
MOD RSA1024: RSA1024NAME="test", HEADPREFIXSW=DISABLE, RSAPSWDTYPE=PUBLIC_KEY, RSAPSWDKEYN="BCDE", RSAPSWDKEYE="101010";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-RSA1024.md`
