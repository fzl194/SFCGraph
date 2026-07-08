---
id: UDG@20.15.2@MMLCommand@RMV DNSOVERWRITING
type: MMLCommand
name: RMV DNSOVERWRITING（删除DNS重写动作配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DNSOVERWRITING
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- DNS重写控制
- DNS重写
status: active
---

# RMV DNSOVERWRITING（删除DNS重写动作配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除DNS重写动作配置。

## 注意事项

- 该命令执行后立即生效。
- 如果智能重定向类型的规则引用了该DNS重写，则不允许删除该DNS重写。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 删除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定删除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALL_EXTFILTER：绑定的所有扩展过滤器。<br>- SPECIFIC_EXTFILTER：绑定的特定扩展过滤器。<br>- ERROR_CODE：绑定的错误码。<br>- ALL_SERVER_IP：绑定的所有服务器地址。<br>- SPECIFIC_SERVER_IPv4：绑定的特定IPv4服务器地址。<br>- SPECIFIC_SERVER_IPv6：绑定的特定Ipv6服务器地址。<br>- ALL_DNSOW：所有的dns重写动作。<br>- SPECIFIC_DNSOW：指定的dns重写动作。<br>默认值：无<br>配置原则：<br>- 当运营商需要清空DNS重写动作中所有扩展过滤器时，该参数需配置为ALL_EXTFILTER。<br>- 当运营商需要清空DNS重写动作中指定扩展过滤器时，该参数需配置为SPECIFIC_EXTFILTER。<br>- 当运营商需要清空DNS重写动作中所有错误码范围时，该参数需配置为ALL_ERROR_CODE。<br>- 当运营商需要清空DNS重写动作中指定错误码范围时，该参数需配置为SPECIFIC_ERROR_CODE。<br>- 当运营商需要清空DNS重写动作中所有IP地址时，该参数需配置为ALL_SERVER_IP。<br>- 当运营商需要清空DNS重写动作中指定IPV4地址时，该参数需配置为SPECIFIC_SERVER_IPv4。<br>- 当运营商需要清空DNS重写动作中指定IPV6地址时，该参数需配置为SPECIFIC_SERVER_IPv6。<br>- 当运营商需要删除所有DNS重写动作时，该参数需配置为ALL_DNSOW。<br>- 当运营商需要删除指定DNS重写动作时，该参数需配置为SPECIFIC_DNSOW。 |
| DNSOVERWRTNAME | DNS重写动作名字 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RMVTYPE”配置为“ALL_EXTFILTER”、“SPECIFIC_EXTFILTER”、“ALL_SERVER_IP”、“SPECIFIC_SERVER_IPv4”、“SPECIFIC_SERVER_IPv6”、“SPECIFIC_DNSOW” 或 “ERROR_CODE”时为必选参数。<br>参数含义：该参数用于指定DNS重写动作名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| EXTFLTNAME | 扩展过滤器名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RMVTYPE”配置为“SPECIFIC_EXTFILTER”时为必选参数。<br>参数含义：该参数用于指定扩展过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。ExtFltName为通过ADD EXTENDEDFILTER 命令配置的名称，不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVERIP | 服务器IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RMVTYPE”配置为“SPECIFIC_SERVER_IPv4”时为必选参数。<br>参数含义：该参数用于设置DNS重写动作的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式，有效的单播地址。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD DNSOVERWRITING命令配置生成。<br>- IPv4地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。 |
| SERVERIPV6 | 服务器IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RMVTYPE”配置为“SPECIFIC_SERVER_IPv6”时为必选参数。<br>参数含义：该参数用于设置DNS重写动作的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式，有效的单播地址。<br>默认值：无<br>配置原则：该参数使用ADD DNSOVERWRITING命令配置生成。 |
| BINDERRCODENAME | 绑定错误码名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RMVTYPE”配置为“ERROR_CODE”时为必选参数。<br>参数含义：该参数用于指定绑定的错误码名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD ERRORCODE命令配置生成。<br>- 设置的BindErrCodeName必须是系统已经存在的名称。 |

## 操作的配置对象

- [DNS重写动作配置（DNSOVERWRITING）](configobject/UDG/20.15.2/DNSOVERWRITING.md)

## 使用实例

- 假设运营商需要删除名称为test的DNS重写，配置如下：
  ```
  RMV DNSOVERWRITING: RMVTYPE=ALL_EXTFILTER, DNSOVERWRTNAME="test";
  ```
- 假设运营商需要删除所有的DNS重写，则RmvType为ALL_DNSOW，配置如下：
  ```
  RMV DNSOVERWRITING: RMVTYPE=ALL_DNSOW;
  ```
- 假设运营商需要清除名称为test的DNS重写中所有的扩展过滤器，则RmvType为ALL_EXTFILTER，配置如下：
  ```
  RMV DNSOVERWRITING: RMVTYPE=SPECIFIC_EXTFILTER, DNSOVERWRTNAME="test", EXTFLTNAME="testfilt1";
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除DNS重写动作配置（RMV-DNSOVERWRITING）_82837552.md`
