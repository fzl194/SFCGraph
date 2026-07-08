---
id: UNC@20.15.2@MMLCommand@ADD NFROUTEPLCY
type: MMLCommand
name: ADD NFROUTEPLCY（增加NF路由策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NFROUTEPLCY
command_category: 配置类
applicable_nf:
- SMF
- AMF
- SMSF
- NCG
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- NF通信模式管理
- NF间接路由管理
status: active
---

# ADD NFROUTEPLCY（增加NF路由策略）

## 功能

**适用NF：SMF、AMF、SMSF、NCG、NSSF**

该命令用于增加对端NF路由策略。

## 注意事项

- 该命令执行后立即生效。

- 对于Model A、Model B和Model C模式，此命令优先级高于SET SCPFUNCSW。
- 此命令对于Model D模式不生效。对Model C拨测模式下的非拨测号段用户不生效。
- 该命令不支持国际漫游场景跨PLMN的NF之间的路由配置。
- 同时配置对端NF实例标识、FQDN、IP的策略时，策略匹配优先级从高到低分别为对端NF实例标识、FQDN、IP地址。
- 根据对端NF IP判断路由策略时，如果匹配多条记录，则使用掩码最长的记录所配置的路由策略。
- 根据对端NF FQDN判断路由策略时，如果匹配多条记录，则使用FQDNSUFFIX长度最长的记录所配置的路由策略。
- 当通过IP或FQDN配置路由策略时，需将对应对端NF使用的所有FQDN及IP均配置相同的路由策略，否则与此对端NF通信时可能出现路由策略不一致的情况。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| INFOTYPE | 信息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信息类型。<br>数据来源：全网规划<br>取值范围：<br>- “NFID（NFID）”：使用NF实例ID信息<br>- “IP（IP）”：使用IP信息<br>- “FQDN（FQDN）”：使用FQDN信息<br>默认值：NFID<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：该参数在"INFOTYPE"配置为"NFID"时为条件必选参数。<br>参数含义：该参数用于指定对端NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。NFINSTANCEID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9和“-”的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：10.0.0.0、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：FF00::、2001:DB8::。3.不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：该参数在"INFOTYPE"配置为"IP"时为条件必选参数。<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPTypeV4（IPTypeV4）<br>- IPTypeV6（IPTypeV6）<br>默认值：IPTypeV4<br>配置原则：无 |
| IPV4PREFIX | IPv4前缀 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4前缀。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6PREFIX | IPv6前缀 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6前缀。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| IPV4MASKLEN | IPv4掩码长度 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4类型地址的掩码长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~32。<br>默认值：无<br>配置原则：无 |
| IPV6MASKLEN | IPv6掩码长度 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6类型地址的掩码长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~128。<br>默认值：无<br>配置原则：无 |
| FQDNSUFFIX | FQDN后缀 | 可选必选说明：该参数在"INFOTYPE"配置为"FQDN"时为条件必选参数。<br>参数含义：该参数用于指定FQDN后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数大小写不敏感。<br>默认值：无<br>配置原则：无 |
| ROUTEPLCY | 路由策略 | 可选必选说明：必选参数<br>参数含义：该参数用于指定到对端NF的路由策略。<br>数据来源：全网规划<br>取值范围：<br>- “DIRECT（直连通信）”：通过直连通信<br>- “SCP（通过SCP通信）”：通过SCP Model C间接路由通信<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFROUTEPLCY]] · NF路由策略（NFROUTEPLCY）

## 使用实例

- 通过实例标识增加到对端NF的路由策略，对端NF实例标识为udm_instance_0，到对端NF的路由策略为SCP Model C。
  ```
  ADD NFROUTEPLCY: INDEX=1, INFOTYPE=NFID, NFINSTANCEID="udm_instance_0", ROUTEPLCY=SCP;
  ```
- 通过IP掩码增加到对端NF的路由策略，对端NF IP地址类型为IPv4，IPv4前缀为192.168.0.1，掩码为30，到对端NF的路由策略为SCP Model C。
  ```
  ADD NFROUTEPLCY: INDEX=2, INFOTYPE=IP, IPADDRESSTYPE=IPTypeV4, IPV4PREFIX="192.168.0.1", IPV4MASKLEN=30, ROUTEPLCY=SCP;
  ```
- 通过FQDN后缀增加到对端NF的路由策略，对端NF FQDN后缀为"udm1.huawei.com"，到对端NF的路由策略为SCP Model C。
  ```
  ADD NFROUTEPLCY: INDEX=3, INFOTYPE=FQDN, FQDNSUFFIX="udm1.huawei.com", ROUTEPLCY=SCP;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NFROUTEPLCY.md`
