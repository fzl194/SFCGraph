---
id: UNC@20.15.2@MMLCommand@ADD IPAREAAPN
type: MMLCommand
name: ADD IPAREAAPN（增加IP区域APN网络标识）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPAREAAPN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于位置分配IP地址管理
- 基于位置分配IP地址APN信息配置
status: active
---

# ADD IPAREAAPN（增加IP区域APN网络标识）

## 功能

**适用网元：SGSN、MME**

该命令用于为“基于位置的IP地址重分配”功能配置APN网络标识。当本网本地用户和本网异地用户激活PDP或者创建PDN连接时，且使用的APN网络标识与本命令配置的任意一条APN网络标识匹配时，系统就会对该用户启用“基于位置的IP地址重分配”功能。

## 注意事项

- 此命令最大记录数为128。
- 此命令执行后立即生效。
- 此配置涉及License（License部件编码：LKV2IPRL01），执行命令请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定支持“基于位置的IP地址重分配”功能的APN网络标识。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>- “*”表示通配符，如果APN网络标识为“*”，表示所有APN网络标识都支持“基于位置的IP地址重分配”功能。 |

## 操作的配置对象

- [IP区域APN网络标识（IPAREAAPN）](configobject/UNC/20.15.2/IPAREAAPN.md)

## 使用实例

期望对网络中使用 “HUAWEI.COM” 这个APN网络标识的业务启用“基于位置的IP地址重分配”功能，通过本命令增加 “HUAWEI.COM” APN网络标识。配置如下：

ADD IPAREAAPN: APNNI="HUAWEI.COM";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IP区域APN网络标识(ADD-IPAREAAPN)_72345201.md`
