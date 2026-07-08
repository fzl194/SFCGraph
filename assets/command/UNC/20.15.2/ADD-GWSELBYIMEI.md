---
id: UNC@20.15.2@MMLCommand@ADD GWSELBYIMEI
type: MMLCommand
name: ADD GWSELBYIMEI（增加基于IMEI选择GGSN/P-GW配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GWSELBYIMEI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 50
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- 基于IMEI选择GGSN P-GW
status: active
---

# ADD GWSELBYIMEI（增加基于IMEI选择GGSN/P-GW配置）

## 功能

**适用网元：SGSN、MME**

该命令用于配置基于IMEI选择GGSN/P-GW功能。

当运营商有基于IMEI来选择特定网关需求时需要使用，例如需要对特定类型的终端选择到特定GGSN/P-GW。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为50。
- 此命令执行后，满足条件的终端在[**ADD GWSELPLCY**](../GGSN_P-GW选择/增加GGSN_P-GW选择策略（ADD GWSELPLCY）_26145944.md)中配置的基于“定制标识类型”选择网关，并且非CC_IMEI方式时，功能将不再生效。
- 开启本功能之前请确保：
    - IMEI群组已经在[**ADD IMEIGP**](../../../业务安全管理/用户终端管理/IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md)中配置，且终端的IMEI设备型号核准号码已经通过[**ADD IMEIGPMEM**](../../../业务安全管理/用户终端管理/IMEI群组成员管理/增加IMEI群组成员(ADD IMEIGPMEM)_26305568.md)添加到该群组中。
    - 请执行[**LST GBIMEICFG**](../../../业务安全管理/设备检查管理/Gb模式IMEI配置/查询Gb模式IMEI配置(LST GBIMEICFG)_72345231.md)、[**LST IUIMEICFG**](../../../业务安全管理/设备检查管理/Iu模式IMEI配置/查询Iu模式IMEI配置(LST IUIMEICFG)_26145636.md)、[**LST S1IMEICFG**](../../../业务安全管理/设备检查管理/S1模式IMEI配置/查询S1模式IMEI配置(LST S1IMEICFG)_72225319.md)命令确保需要启用功能终端的“IMEI获取策略”为“获取IMEI”或“获取IMEISV”。
- 此配置涉及“Category 6 网关选择”特性（特性编号：WSFD-205008，License项：LKV2C6GS01），请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指示IMEI群组标识，<br>UNC<br>需要为这些类型终端选择特定GGSN/P-GW。<br>前提条件：该参数已在<br>[**ADD IMEIGP**](../../../业务安全管理/用户终端管理/IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md)<br>命令中配置完成。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |
| LABEL | 定制标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指示特定类型终端的定制APN域名标识，以便为终端选择特定GGSN/P-GW。<br>数据来源：本端规划<br>取值范围：1~32位字符串<br>默认值：无<br>说明：- 在使用APN进行DNS解析寻址GGSN/P-GW前，将为特定类型终端的定制标识加入到APN-NI和APN-OI之间，然后将扩展的APN发送到DNS Server或Hostfile进行DNS解析。 例如APN-NI为“HUAWEI.COM”，APN-OI为“MNC123.MCC456.GPRS”，定制标识为“CAT6”，则发送到DNS Server或Hostfile进行DNS解析的扩展APN为“HUAWEI.COM.CAT6.MNC123.MCC456.GPRS”<br>- 如果启用定制标识后，APN长度超过100字节，可能会被DNS服务器拒绝。<br>- LABEL的构成字符只能是字母A～Z或a～z、数字0～9、符号“-”和“.”，并且“-”和“.”不能是LABEL的开头和结尾，字母不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GWSELBYIMEI]] · 基于IMEI选择GGSN/P-GW配置（GWSELBYIMEI）

## 使用实例

假如IMEI设备型号核准号码为86439902和86574302的终端为CAT6的终端，运营商希望为这类终端选择到特定的P-GW/GGSN，则可以按照如下描述操作：

- 执行[**ADD IMEIGP**](../../../业务安全管理/用户终端管理/IMEI群组管理/增加IMEI群组(ADD IMEIGP)_72225435.md)增加一个IMEI群组。
- 执行[**ADD IMEIGPMEM**](../../../业务安全管理/用户终端管理/IMEI群组成员管理/增加IMEI群组成员(ADD IMEIGPMEM)_26305568.md)将IMEI设备型号核准号码为86439902和86574302的终端加入到该群组中。
- 执行本命令使符合条件的终端发送扩展的APN到DNS Server或Hostfile进行DNS解析。
- 部署DNS Server或Hostfile，使得使用扩展的APN的终端选择到特定的P-GW/GGSN。

ADD IMEIGP: IMEIGPID=1, IMEIGPN="CAT6";

ADD IMEIGPMEM: IMEIGPID=1, IMEITAC="86439902";

ADD IMEIGPMEM: IMEIGPID=1, IMEITAC="86574302";

ADD GWSELBYIMEI: IMEIGPID=1, LABEL="CAT6";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-GWSELBYIMEI.md`
