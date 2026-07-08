---
id: UNC@20.15.2@MMLCommand@ADD APNCTRLPARA
type: MMLCommand
name: ADD APNCTRLPARA（增加基于APN的信令控制参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNCTRLPARA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 16
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- 基于APN的信令控制参数
status: active
---

# ADD APNCTRLPARA（增加基于APN的信令控制参数）

## 功能

**适用网元：SGSN**

该命令用于增加基于APN的信令控制相关参数。

现网中存在多类M2M用户，比如电力用户为一类用户，水表用户为另一类用户，这些M2M用户在服务器升级或者故障排除等操作时可能会触发信令风暴，导致网关过载。为了保护网关，可通过本命令配置开启基于APN的信令控制功能。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为16。
- 该命令用于控制信令接入，对应参数取值需要评估网关PDP激活能力，否则配置不当可能导致业务受损或无法起到保护网关的作用。
- 注意区分M2M用户的APN和普通用户的APN，如果配置错误会导致普通用户业务受损。
- 此配置涉及基于APN的接入速率控制特性（特性编号：WSFD-106302，License部件编码：82207627），执行[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性的License是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。
- 该功能仅对2G用户生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APNNI组号 | 可选必选说明：必选参数<br>参数含义：本参数用于指定开启APN信令控制功能的APNNI组号。<br>数据来源：全网规划<br>取值范围：0～15<br>默认值：无<br>配置原则：该参数的取值需要引用<br>[**ADD APNNIGROUP**](../../会话管理/APNNI信息管理/APNNI组管理/增加APNNI组(ADD APNNIGROUP)_26305508.md)<br>命令中的组号，因此在配置该参数前需要首先通过命令<br>[**ADD APNNIGROUP**](../../会话管理/APNNI信息管理/APNNI组管理/增加APNNI组(ADD APNNIGROUP)_26305508.md)<br>配置组号。 |
| ATTACHTHRESH | 附着请求控制门限（次/秒） | 可选必选说明：必选参数<br>参数含义：本参数用于指定开启APN信令控制的附着消息控制门限。<br>数据来源：全网规划<br>取值范围：0次/秒～10000000次/秒<br>默认值：无<br>配置原则：<br>- 用户需要根据网关PDP激活能力折算该门限。<br>- 当用户输入为“0”时，该信令控制功能不生效。 |
| PDPCONTTHRESH | PDP上下文请求控制门限（次/秒） | 可选必选说明：必选参数<br>参数含义：本参数用于指定开启APN信令控制的PDP上下文请求消息控制门限。<br>数据来源：全网规划<br>取值范围：0次/秒～10000000次/秒<br>默认值：无<br>配置原则：<br>- 用户需要根据网关PDP激活能力折算该门限。<br>- 当用户输入为“0”时，该信令控制功能不生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCTRLPARA]] · 基于APN的信令控制参数（APNCTRLPARA）

## 使用实例

指定 “APNNI组号” 为 “0” ， “附着请求控制门限（次/秒）” 为 “1000” ， “PDP上下文请求控制门限（次/秒）” 为 “1000” ：

ADD APNCTRLPARA: APNGRPID=0, ATTACHTHRESH=1000, PDPCONTTHRESH=1000;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-APNCTRLPARA.md`
