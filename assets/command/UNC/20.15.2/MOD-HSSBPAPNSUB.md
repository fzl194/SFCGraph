---
id: UNC@20.15.2@MMLCommand@MOD HSSBPAPNSUB
type: MMLCommand
name: MOD HSSBPAPNSUB（修改HSS BYPASS最小APN签约数据配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: HSSBPAPNSUB
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS BYPASS最小签约数据配置管理
status: active
---

# MOD HSSBPAPNSUB（修改HSS BYPASS最小APN签约数据配置）

## 功能

**适用网元：MME**

此命令用于修改最小APN签约数据群组对应的最小APN签约数据。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN本地签约数据索引。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用来指定APNNI信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~62<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”或者配置为通配符“*”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |
| PDNTYPE | PDN类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定PDN类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>- IPV4_AND_IPV6（IPv4和IPv6）<br>- IPV4_OR_IPv6（IPv4或IPv6）<br>默认值：无<br>配置原则：无 |
| APNAMBRULK | 上行APN AMBR （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户Non-GBR承载的上行APN最大速率。<br>数据来源：全网规划<br>取值范围：1kbps～65000000kbps。<br>默认值：无<br>配置原则：无 |
| APNAMBRDLK | 下行APN AMBR （kbps） | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户Non-GBR承载的下行APN最大速率。<br>数据来源：整网规划<br>取值范围：1kbps～65000000kbps。<br>默认值：无<br>配置原则：无 |
| ISNRIWK | 4-5G互操作 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN对应的承载是否支持4-5G互操作。<br>数据来源：全网规划<br>取值范围：<br>- SUPPORT（支持）<br>- NOT_SUPPORT（不支持）<br>默认值：无<br>配置原则：无 |
| QCI | QCI | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN的QCI。<br>数据来源：全网规划<br>取值范围：0~254<br>默认值：无<br>配置原则：无 |
| PRIORITY | 控制优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN的QCI控制优先级。<br>数据来源：全网规划<br>取值范围：1~15<br>默认值：无<br>配置原则：参数值越小优先级越高 |
| CHARGINGCHAR | 计费属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN的计费属性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0000~FFFF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HSS BYPASS最小APN签约数据配置（HSSBPAPNSUB）](configobject/UNC/20.15.2/HSSBPAPNSUB.md)

## 使用实例

修改HSS BYPASS最小APN签约数据配置，可以用如下命令：

```
MOD HSSBPAPNSUB: APNSUBIDX=1, APNNI="1234", PDNTYPE=IPV4, APNAMBRULK=2, APNAMBRDLK=2, ISNRIWK=SUPPORT, QCI=0, PRIORITY=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改HSS-BYPASS最小APN签约数据配置-(MOD-HSSBPAPNSUB)_63705566.md`
