---
id: UNC@20.15.2@MMLCommand@MOD APNCTRLPARA
type: MMLCommand
name: MOD APNCTRLPARA（修改基于APN的信令控制参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: APNCTRLPARA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- 基于APN的信令控制参数
status: active
---

# MOD APNCTRLPARA（修改基于APN的信令控制参数）

## 功能

**适用网元：SGSN**

该命令用于修改基于APN的信令控制相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令用于修改信令控制的门限，对应参数取值需要评估网关PDP激活能力，否则配置不当可能导致业务受损或无法起到保护网关的作用。
- 此配置涉及基于APN的接入速率控制特性（特性编号：WSFD-106302，License部件编码：82207627），执行[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性的License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APNNI组号 | 可选必选说明：必选参数<br>参数含义：本参数用于指定开启APN信令控制功能的APNNI组号。<br>数据来源：全网规划<br>取值范围：0～15<br>默认值：无 |
| ATTACHTHRESH | 附着请求控制门限（次/秒） | 可选必选说明：可选参数<br>参数含义：本参数用于指定开启APN信令控制的附着消息控制门限。<br>数据来源：全网规划<br>取值范围：0次/秒～10000000次/秒<br>默认值：无<br>配置原则：<br>- 用户需要根据网关PDP激活能力折算该门限。<br>- 当用户输入为“0”时，该信令控制功能不生效。 |
| PDPCONTTHRESH | PDP上下文请求控制门限（次/秒） | 可选必选说明：可选参数<br>参数含义：本参数用于指定开启APN信令控制的PDP上下文请求消息控制门限。<br>数据来源：全网规划<br>取值范围：0次/秒～10000000次/秒<br>默认值：无<br>配置原则：<br>- 用户需要根据网关PDP激活能力折算该门限。<br>- 当用户输入为“0”时，该信令控制功能不生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNCTRLPARA]] · 基于APN的信令控制参数（APNCTRLPARA）

## 使用实例

修改 “APNNI组号” 为 “0” ， “附着请求控制门限（次/秒）” 为 “1000” ， “PDP上下文请求控制门限（次/秒）” 为 “1000” ：

MOD APNCTRLPARA: APNGRPID=0, ATTACHTHRESH=1000, PDPCONTTHRESH=1000;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改基于APN的信令控制参数(MOD-APNCTRLPARA)_26145784.md`
