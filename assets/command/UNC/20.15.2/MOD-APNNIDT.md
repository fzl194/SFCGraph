---
id: UNC@20.15.2@MMLCommand@MOD APNNIDT
type: MMLCommand
name: MOD APNNIDT（修改APNNI Direct Tunnel配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNNIDT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- Direct Tunnel管理
status: active
---

# MOD APNNIDT（修改APNNI Direct Tunnel配置）

## 功能

**适用网元：SGSN**

此命令用于修改APNNI DT属性信息表中的某个APNNI的DT属性记录。

## 注意事项

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC、GGSN和IMSI（使用[**ADD IMSIDT**](增加IMSI Direct Tunnel配置(ADD IMSIDT)_72345647.md)配置）支持DT功能。
- 该命令部分参数与相关特性license共同完成该特性的开启，请在设置参数前使用[**DSP LICENSE**](../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”，具体相关特性请参考参数的说明。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定启用基于APNNI的DT功能的APNNI。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>“APNNI”<br>（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。“*”表示通配符，如果用户使用的APNNI在配置表中无法匹配到对应的记录，则查询“*”通配符对应的配置记录。如果查询成功则使用“*”对应的配置；如果查询失败，则默认支持DT。 |
| DT | 启用Direct Tunnel | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否启用基于APNNI的DT功能。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：- 当参数设置为“YES(是)”时，“支持Direct Tunnel功能”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-104506，License部件编码：LKV2DIRTUN02）。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNIDT]] · APNNI Direct Tunnel配置（APNNIDT）

## 使用实例

修改一条APNNI DT权限属性记录：

MOD APNNIDT: APNNI="huawei.com", DT=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-APNNIDT.md`
