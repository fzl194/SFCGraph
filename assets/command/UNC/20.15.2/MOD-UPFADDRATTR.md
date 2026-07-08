---
id: UNC@20.15.2@MMLCommand@MOD UPFADDRATTR
type: MMLCommand
name: MOD UPFADDRATTR（修改UPF地址属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: UPFADDRATTR
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- UPF粒度PFCP路径参数管理
status: active
---

# MOD UPFADDRATTR（修改UPF地址属性）

## 功能

![](修改UPF地址属性（MOD UPFADDRATTR）_21742361.assets/notice_3.0-zh-cn_2.png)

ISPROXY参数设置错误会导致UPG热备特性和双UPG故障bypass功能失效。

SMF与UPF之间只允许配置1条直连路径（ISPROXY参数只能设置1条非代理路径），误配置可能会导致双UPG故障bypass功能不可用。

**适用NF：SMF**

该命令用于修改UPF地址属性。

## 注意事项

- 该命令执行后立即生效。

- 配置UPF地址属性前应先通过ADD PNFPROFILE配置NF类型为UPF的实例概述信息。
- 本配置的NFINSTANCEID、IPADDRESSTYPE、IPV4ADDRESS1-4、IPV6ADDRESS1-4应该与PNFPROFILE中的配置相同。
- 静默路径的优先级应低于代理路径的优先级。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“NFINSTANCEID”参数取值相同。 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPADDRESSTYPE”参数取值相同。 |
| IPV4ADDRESS1 | IPV4地址1 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定IPV4类型地址1。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV4ADDRESS1”参数取值相同。 |
| IPV6ADDRESS1 | IPV6地址1 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定IPV6类型地址1。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV6ADDRESS1”参数取值相同。 |
| ADDRPRIORITY1 | 地址1的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址1的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>数值小表示优先级高。 |
| ISPROXY1 | 是否代理路径1 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址1是否为UPG的代理地址。<br>数据来源：全网规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无<br>配置原则：<br>当该路径为和UPF之间的直连路径时，需要配置为FALSE。 |
| SILENTSW1 | 直连路径静默开关1 | 可选必选说明：该参数在"ISPROXY1"配置为"FALSE"时为条件可选参数。<br>参数含义：该参数用于指定直连路径地址的静默开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（关）<br>- ENABLE（开）<br>默认值：无<br>配置原则：<br>当设置为ENABLE时该路径处于静默状态，只作为紧急备路径使用，正常情况下不与对端进行建链。 |
| IPDESCNAME1 | 路径描述信息1 | 可选必选说明：可选参数<br>参数含义：该参数用于表示该路径的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS2 | IPV4地址2 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定IPV4类型地址2。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV4ADDRESS2”参数取值相同。 |
| IPV6ADDRESS2 | IPV6地址2 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定IPV6类型地址2。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV6ADDRESS2”参数取值相同。 |
| ADDRPRIORITY2 | 地址2的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址2的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>数值小表示优先级高。 |
| ISPROXY2 | 是否代理路径2 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址2是否为UPG的代理地址。<br>数据来源：全网规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无<br>配置原则：<br>当该路径为和UPF之间的直连路径时，需要配置为FALSE。 |
| SILENTSW2 | 直连路径静默开关2 | 可选必选说明：该参数在"ISPROXY2"配置为"FALSE"时为条件可选参数。<br>参数含义：该参数用于指定直连路径地址的静默开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（关）<br>- ENABLE（开）<br>默认值：无<br>配置原则：<br>当设置为ENABLE时该路径处于静默状态，只作为紧急备路径使用，正常情况下不与对端进行建链。 |
| IPDESCNAME2 | 路径描述信息2 | 可选必选说明：可选参数<br>参数含义：该参数用于表示该路径的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS3 | IPV4地址3 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定IPV4类型地址3。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV4ADDRESS3”参数取值相同。 |
| IPV6ADDRESS3 | IPV6地址3 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定IPV6类型地址3。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV6ADDRESS3”参数取值相同。 |
| ADDRPRIORITY3 | 地址3的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址3的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>数值小表示优先级高。 |
| ISPROXY3 | 是否代理路径3 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址3是否为UPG的代理地址。<br>数据来源：全网规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无<br>配置原则：<br>当该路径为和UPF之间的直连路径时，需要配置为FALSE。 |
| SILENTSW3 | 直连路径静默开关3 | 可选必选说明：该参数在"ISPROXY3"配置为"FALSE"时为条件可选参数。<br>参数含义：该参数用于指定直连路径地址的静默开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（关）<br>- ENABLE（开）<br>默认值：无<br>配置原则：<br>当设置为ENABLE时该路径处于静默状态，只作为紧急备路径使用，正常情况下不与对端进行建链。 |
| IPDESCNAME3 | 路径描述信息3 | 可选必选说明：可选参数<br>参数含义：该参数用于表示该路径的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS4 | IPV4地址4 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定IPV4类型地址4。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV4ADDRESS4”参数取值相同。 |
| IPV6ADDRESS4 | IPV6地址4 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定IPV6类型地址4。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>该取值必须和ADD PNFPROFILE中配置的“IPV6ADDRESS4”参数取值相同。 |
| ADDRPRIORITY4 | 地址4的优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址4的优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>数值小表示优先级高。 |
| ISPROXY4 | 是否代理路径4 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址4是否为UPG的代理地址。<br>数据来源：全网规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：无<br>配置原则：<br>当该路径为和UPF之间的直连路径时，需要配置为FALSE。 |
| SILENTSW4 | 直连路径静默开关4 | 可选必选说明：该参数在"ISPROXY4"配置为"FALSE"时为条件可选参数。<br>参数含义：该参数用于指定直连路径地址的静默开关。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（关）<br>- ENABLE（开）<br>默认值：无<br>配置原则：<br>当设置为ENABLE时该路径处于静默状态，只作为紧急备路径使用，正常情况下不与对端进行建链。 |
| IPDESCNAME4 | 路径描述信息4 | 可选必选说明：可选参数<br>参数含义：该参数用于表示该路径的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFADDRATTR]] · UPF地址属性（UPFADDRATTR）

## 使用实例

以下命令用于修改实例名称为upf1，IP地址类型为IPv4，IPV4ADDRESS1为192.168.0.1，IPV4ADDRESS2为192.168.0.2的UPF地址属性，ADDRPRIORITY1为0，ADDRPRIORITY2为1。

```
MOD UPFADDRATTR: NFINSTANCEID="upf1", IPADDRESSTYPE=IPV4, IPV4ADDRESS1="192.168.0.1", ADDRPRIORITY1=0, IPV4ADDRESS2="192.168.0.2", ADDRPRIORITY2=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改UPF地址属性（MOD-UPFADDRATTR）_21742361.md`
