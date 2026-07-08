---
id: UDG@20.15.2@MMLCommand@ADD RELAYTEMPLATE
type: MMLCommand
name: ADD RELAYTEMPLATE（增加媒体中继模板）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: RELAYTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 5
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继模板
status: active
---

# ADD RELAYTEMPLATE（增加媒体中继模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加媒体中继模板。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYTPLNAME | 媒体中继模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定媒体中继模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DNSCNAME | DNS规范名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定DNS的规范名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。不支持空格，不区分大小写。仅支持数字、字母、'.'和'-'进行组合，必须以数字或字母开头和结尾，不能出现连续两个'.'。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| DNSLIVETIME | DNS存活时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定DNS的存活时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是为30～1800，默认值为60，单位是秒。<br>默认值：60<br>配置原则：无 |
| DNSIPNOTMTACT | DNS IP不匹配操作 | 可选必选说明：可选参数<br>参数含义：该参数用来指定DNS请求的IP类型与配置的媒体中继IP类型不匹时，DNS代理的处理动作。只对IPv4IPv6双栈用户生效。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BYPASS：不做DNS代理，消息透传给DNS服务器。<br>- RETNOTFOUND：代理DNS响应，携带“xxx”原因。<br>默认值：BYPASS<br>配置原则：无 |
| TLSCFGNAME | TLS配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该Relay业务TLS配置描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。不区分大小写。<br>默认值：无<br>配置原则：<br>- 该取值必须和ADD RELAYTLSCFG中配置的“TLSCONFIGNAME”参数取值相同。<br>- 输入单空格将删除该参数已有配置项。 |
| UNKNOWNDMACT | UE访问未知域名处理动作 | 可选必选说明：可选参数<br>参数含义：该参数用于设置UE访问未知域名的处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- REDIRECT：重定向。<br>- FORBIDDEN：拒绝。<br>默认值：FORBIDDEN<br>配置原则：无 |
| VENDORID | 厂商ID | 可选必选说明：可选参数<br>参数含义：该参数用于设置媒体厂商ID，用于进行媒体厂商差异化控制。<br>数据来源：本端规划<br>取值范围：取值范围0~5，默认值为0。<br>默认值：0<br>配置原则：无 |
| MEDIAAGETIME | 媒体文件老化时间（小时） | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体文件老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~720，默认值为168，单位为小时。<br>默认值：168<br>配置原则：无 |
| MEDIAAUTHTIME | 媒体文件有效性校验时长（分钟） | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体文件有效性校验时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5~1440，默认值为15，单位为分钟。<br>默认值：15<br>配置原则：无 |
| MEDIAAUTHMETHOD | 媒体文件有效性校验方式 | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体文件有效性校验方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GET：GET请求方式。<br>- HEAD：HEAD请求方式。<br>默认值：HEAD<br>配置原则：无 |
| MEDIAINFOUPDTM | 媒体属性更新时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用来指定媒体属性更新时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~3600，默认值为60，单位为秒。<br>默认值：60<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYTEMPLATE]] · 媒体中继模板（RELAYTEMPLATE）

## 使用实例

假如需要创建一组媒体中继模板，则命令如下：

```
ADD RELAYTEMPLATE: RELAYTPLNAME="test", DNSLIVETIME=120, DNSIPNOTMTACT=RETNOTFOUND, UNKNOWNDMACT=REDIRECT, VENDORID=2, MEDIAAUTHMETHOD=GET, CFGDOMAINNAME="testDomain";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-RELAYTEMPLATE.md`
