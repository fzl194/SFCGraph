---
id: UDG@20.15.2@MMLCommand@ADD UEMUTACCWLIST
type: MMLCommand
name: ADD UEMUTACCWLIST（增加PA口UE互访白名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UEMUTACCWLIST
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
max_records: 1000
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- 用户互访控制
- UE互访白名单
status: active
---

# ADD UEMUTACCWLIST（增加PA口UE互访白名单）

## 功能

**适用NF：UPF、PGW-U**

企业专用DNN漫游场景，增加PA口UE互访白名单。

该命令用于配置漫游场景下UE互访的I-UPF、SGW白名单，对于APNUEMUTACC命令下的InnerAPNS_S5S8P、InnerAPNS_N9A、InterAPNS_S5S8P、InterAPNS_N9A参数，需要开启后生效。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1000。
- 该命令执行后，发生ssg进程复位后对所有用户生效。
- 整机最多支持配置1000个地址。
- 该命令支持绑定的IP地址范围不超过100。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WLISTNAME | 白名单名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE互访白名单名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP协议版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4START | IPV4起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定对端网元N9C口、S5S8_S口ipv4地址范围的起始。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。有效的IP地址。采用点分十进制"X.X.X.X"格式，不能是全0，不能是组播IP，不能是环回IP。<br>默认值：无<br>配置原则：根据环境的网络规划进行配置，点分十进制格式。除A、B、C类地址合法外，其余都为非法地址。 |
| IPV4END | IPV4截止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定对端网元N9C口、S5S8_S口ipv4地址范围的截止。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。有效的IP地址。采用点分十进制"X.X.X.X"格式，不能是全0，不能是组播IP，不能是环回IP。<br>默认值：无<br>配置原则：根据环境的网络规划进行配置，点分十进制格式。除A、B、C类地址合法外，其余都为非法地址。 |
| IPV6START | IPV6起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定对端网元N9C口、S5S8_S口ipv6地址范围的起始。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| IPV6END | IPV6截止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定对端网元N9C口、S5S8_S口ipv6地址范围的截止。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [PA口UE互访白名单（UEMUTACCWLIST）](configobject/UDG/20.15.2/UEMUTACCWLIST.md)

## 使用实例

增加一条PA口UE互访白名单，WLISTNAME为pawlist，地址段范围为192.168.1.1~192.168.1.100：

```
ADD UEMUTACCWLIST: WLISTNAME = "pawlist", IPVERSION=IPV4, IPV4START =  "192.168.1.1",IPV4END =  "192.168.1.100";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加PA口UE互访白名单（ADD-UEMUTACCWLIST）_31719863.md`
