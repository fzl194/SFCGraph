---
id: UDG@20.15.2@MMLCommand@MOD ZONE
type: MMLCommand
name: MOD ZONE（修改区域）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ZONE
command_category: 配置类
applicable_nf:
- CloudEPSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- 区域管理
status: active
---

# MOD ZONE（修改区域）

## 功能

**适用NF：CloudEPSN**

本命令实现修改区域的功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VIEWNAME | 视图名称 | 可选必选说明：可选参数<br>参数含义：资源所属的域名解析视图名称。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 输入资源所属的域名解析视图名称。<br>- CloudDNS中视图默认值为"default"。<br>- CloudDNS当前支持视图最大规格为32字符。<br>- 视图最后一位不支持特殊字符。<br>- 执行命令时需要保证视图存在。 |
| ZONE | 区域名称 | 可选必选说明：必选参数<br>参数含义：资源记录的区域名。<br>数据来源：全网规划<br>取值范围：NA。<br>默认值：无<br>配置原则：<br>- 大小写不敏感，由字母（A～Z/a～z），数字（0～9），分隔符（.）构成的以字母和数字开头的字符串。<br>- 分隔符中的字符串长度不能超过63，且需要以字母开始，以字母或数字结束。<br>- CloudDNS当前支持域名最大长度为254，结尾必须以分隔符（.）结尾，且不能以xn--开头。 |
| TTL | TTL | 可选必选说明：必选参数<br>参数含义：NA。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [区域（ZONE）](configobject/UDG/20.15.2/ZONE.md)

## 使用实例

修改区域，“视图名称”填写为“default”，“区域名称”填写为“test.cmnet.mnc000.mcc460.gprs”，“TTL”填写为600：

```
MOD ZONE: VIEWNAME="default", ZONE="test.cmnet.mnc000.mcc460.gprs", TTL=600;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改区域（MOD-ZONE）_81694199.md`
