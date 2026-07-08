---
id: UNC@20.15.2@MMLCommand@ADD IMSIBINDUPFADDR
type: MMLCommand
name: ADD IMSIBINDUPFADDR（增加用户和UPF地址的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMSIBINDUPFADDR
command_category: 配置类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP路径选择管理
status: active
---

# ADD IMSIBINDUPFADDR（增加用户和UPF地址的绑定关系）

## 功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于增加用户和UPF地址的绑定关系。在拨测场景下如果用户需要使用绑定的UPF地址建立PFCP会话，系统支持添加一个用户和UPF地址的绑定关系，同时也支持添加连续IMSI号段用户和UPF地址的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 该命令不用于UPF选择。
- 该命令可用于单偶联多路径场景。在该场景下，此命令需要打开软参DWORD1052 BIT16才会生效。
- 如果该命令中设置的IP地址在UPFADDRATTR配置中存在且对应的SILENTSW开关为ENABLE，则需要将SILENTSW开关设置为DISABLE，否则用户绑定不生效。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STARTIMSI | 起始IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI号段的起始IMSI，当只有一个IMSI时，起始IMSI和末位IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~15。STARTIMSI参数每一位只能是数字0-9;当STARTIMSI长度不足15位时，会自动低位补0直到15位。<br>默认值：无<br>配置原则：无 |
| ENDIMSI | 终止IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于标识IMSI号段的最后一个IMSI，包含在号段内。当只有一个IMSI时，起始IMSI和末位IMSI相同。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~15。ENDIMSI参数每一位只能是数字0-9;当ENDIMSI长度不足15位时，会自动低位补9直到15位。<br>默认值：无<br>配置原则：无 |
| UPINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致。 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF地址的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPV4类型地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。IPv4只支持A，B，C类地址。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“IPV4地址1”、“IPV4地址2”、“IPV4地址3”或“IPV4地址4”参数取值保持一致。 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPV6类型地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。IPv6必须是全球单播地址；不能为“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“IPV6地址1”、“IPV6地址2”、“IPV6地址3”或“IPV6地址4”参数取值保持一致。 |

## 操作的配置对象

- [用户和UPF地址的绑定关系（IMSIBINDUPFADDR）](configobject/UNC/20.15.2/IMSIBINDUPFADDR.md)

## 使用实例

增加IMSI前缀为“111111”的用户在5G的UPF地址绑定关系：主锚点为UP1，IPV4地址为10.0.0.2：

```
ADD IMSIBINDUPFADDR: STARTIMSI="111111", ENDIMSI="111111", UPINSTANCEID="UP1", IPTYPE=IPV4, IPV4ADDRESS="10.0.0.2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用户和UPF地址的绑定关系（ADD-IMSIBINDUPFADDR）_49962077.md`
