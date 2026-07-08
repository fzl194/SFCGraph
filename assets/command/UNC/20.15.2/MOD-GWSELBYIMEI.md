---
id: UNC@20.15.2@MMLCommand@MOD GWSELBYIMEI
type: MMLCommand
name: MOD GWSELBYIMEI（修改基于IMEI选择GGSN/P-GW配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GWSELBYIMEI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- 基于IMEI选择GGSN P-GW
status: active
---

# MOD GWSELBYIMEI（修改基于IMEI选择GGSN/P-GW配置）

## 功能

**适用网元：SGSN、MME**

该命令用于修改基于IMEI选择GGSN/P-GW配置记录。

## 注意事项

- 此命令执行后立即生效。
- 此配置涉及“Category 6 网关选择”特性（特性编号：WSFD-205008，License部件编码：LKV2C6GS01），请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指示IMEI群组标识，<br>UNC<br>需要为这些类型终端选择特定GGSN/P-GW。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |
| LABEL | 定制标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指示特定类型终端的定制APN域名标识，以便为终端选择特定GGSN/P-GW。<br>数据来源：本端规划<br>取值范围：0~32位字符串<br>默认值：无<br>说明：- 在使用APN进行DNS解析寻址GGSN/P-GW前，将为特定类型终端的定制标识加入到APN-NI和APN-OI之间，然后将扩展的APN发送到DNS Server或Hostfile进行DNS解析。 例如APN-NI为“HUAWEI.COM”，APN-OI为“MNC123.MCC456.GPRS”，定制标识为“CAT6”，则发送到DNS Server或Hostfile进行DNS解析的扩展APN为“HUAWEI.COM.CAT6.MNC123.MCC456.GPRS”<br>- 如果启用定制标识后，APN长度超过100字节，可能会被DNS服务器拒绝。<br>- LABEL的构成字符只能是字母A～Z或a～z、数字0～9、符号“-”和“.”，并且“-”和“.”不能是LABEL的开头和结尾，字母不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWSELBYIMEI]] · 基于IMEI选择GGSN/P-GW配置（GWSELBYIMEI）

## 使用实例

场景参见 [**ADD GWSELBYIMEI**](增加基于IMEI选择GGSN_P-GW配置(ADD GWSELBYIMEI)_72345541.md) 的命令使用实例。

将IMEI群组标识为1的IMEI群组使用的定制标识修改为“CAT6”：

MOD GWSELBYIMEI: IMEIGPID=1, LABEL="CAT6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GWSELBYIMEI.md`
