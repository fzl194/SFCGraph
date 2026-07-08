---
id: UDG@20.15.2@MMLCommand@ADD XHEADER
type: MMLCommand
name: ADD XHEADER（增加扩展头域）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: XHEADER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 5
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 七层规则管理
- 扩展头域
status: active
---

# ADD XHEADER（增加扩展头域）

## 功能

**适用NF：PGW-U、UPF**

该命令用于增加扩展头域配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5。
- 扩展头域名称及值的匹配均不支持通配符，仅支持全字符匹配。
- 对于XHeader和XHeaderValue，特殊字符的输入要求：
    - 对于普通字符?必须使用%3f代替；例如：x-m?s输入应该是：x-m%3fs。
    - 对于空格必须使用%20代替；例如：x-m s输入应该是：x-m%20s。
    - 对于逗号必须使用％2c代替；例如：x-m,s输入应该是：x-m%2cs。
    - 对于加号尽量使用％2b代替，可以直接输入连续一到两个的加号，但在查询时都会以%2b显示，在业务处理时会转义成加号，例如：x-m+++s输入应该是：x-m%2b%2b%2bs。
    - 当字符串中出现%3f、%2c、%20、%2b或者%25本身时，对于%必须使用%25代替；例如：x-m%3fs输入应该是：x-m%253fs。
    - 其他情况下，%就认为是%本身，可以保持原有实现即可，也可以使用%25替代%；例如：x-m%s输入应该是：x-m%s或者是：x-m%25s。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| XHEADERNAME | 扩展头域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置扩展头域名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| XHEADER | 扩展头域 | 可选必选说明：必选参数<br>参数含义：该参数用于设置扩展头域。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| XHEADERVALUE | 扩展头域取值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置扩展头域值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@XHEADER]] · 扩展头域（XHEADER）

## 使用实例

假如运营商需要增加名称为“x-mms”，值为“1”的扩展头域：

```
ADD XHEADER: XHEADERNAME="testxheader", XHEADER="x-mms", XHEADERVALUE="1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-XHEADER.md`
