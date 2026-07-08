---
id: UNC@20.15.2@MMLCommand@ADD GWSELBYCC
type: MMLCommand
name: ADD GWSELBYCC（增加基于CC选择GGSN/P-GW）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GWSELBYCC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- GGSN_P-GW选择
status: active
---

# ADD GWSELBYCC（增加基于CC选择GGSN/P-GW）

## 功能

**适用网元：SGSN、MME**

该命令用于增加基于特定CC的GGSN/P-GW选择策略，即为不同APN及CC的本网用户配置不同的GGSN/P-GW选择方法，以满足运营商对不同用户选择不同GGSN/P-GW，灵活部署网络的需求。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为256。
- 此命令执行后，当用户的APNNI和签约CC与该配置一致，且[**ADD GWSELPLCY**](增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md)配置中“定制标识类型”配置为“MSISDN”时，UNC组装域名查询网关时不添加MSISDN标识。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定APNNI。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔，每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- 本命令中APNNI不允许配置为“*”。 |
| SUBCC | 签约CC值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定签约CC值。<br>数据来源：全网规划<br>取值范围：0x0000~0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWSELBYCC]] · 基于CC选择GGSN/P-GW（GWSELBYCC）

## 使用实例

假如运营商希望APNNI为HUAWEI.COM，签约CC为0x1234的这类终端选择拜访地的P-GW/GGSN接入，则可以按照如下描述操作：

ADD GWSELBYCC: APNNI="HUAWEI.COM", SUBCC="0x1234";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加基于CC选择GGSN_P-GW(ADD-GWSELBYCC)_26145948.md`
