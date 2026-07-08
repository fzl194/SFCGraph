---
id: UNC@20.15.2@MMLCommand@ADD GWRESTORAPN
type: MMLCommand
name: ADD GWRESTORAPN（增加网关容灾APN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GWRESTORAPN
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 网关故障管理
status: active
---

# ADD GWRESTORAPN（增加网关容灾APN）

## 功能

**适用网元：MME**

本命令用于增加在S-GW或P-GW故障场景下需要恢复的业务的APN网络标识，即APNNI。启用“S-GW/P-GW故障下的业务恢复”特性后，若受影响的业务所对应的APN网络标识与本命令增加的APN网络标识相同，则恢复此类业务的PDN连接。

## 注意事项

- 此命令受控于“S-GW/P-GW故障下的业务恢复”特性（特性编号：WSFD-201203，License部件编码：LKV2SRGF01），请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。
- IMS和紧急呼叫业务对应的APN无需通过本命令配置，S-GW/P-GW故障场景下，系统默认支持对这两种APN恢复。
- 该命令最大记录数为128条。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：本参数用于增加在S-GW/P-GW故障场景下，待恢复业务的APNNI。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- 每条记录中的“APNNI”字段不能重复。<br>- “APNNI”（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GWRESTORAPN]] · 网关容灾APN（GWRESTORAPN）

## 使用实例

当现网启用“S-GW/P-GW故障下的业务恢复”特性，需要增加网关容灾APN时，执行如下命令：

ADD GWRESTORAPN: APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GWRESTORAPN.md`
