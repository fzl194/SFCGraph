---
id: UNC@20.15.2@MMLCommand@ADD MVNO
type: MMLCommand
name: ADD MVNO（增加MVNO配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MVNO
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- MVNO管理
- MVNO配置表
status: active
---

# ADD MVNO（增加MVNO配置信息）

## 功能

**适用网元：SGSN、MME**

此命令用于增加MVNO的配置。MVNO（Mobile Virtual Network Operator，移动虚拟网络运营商）利用MNO（Mobile Network Operator，移动网络运营商）授权的网络资源，提供业务（包括MNO提供的业务以及MVNO自己定制的业务），并能对授权的资源进行维护。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为64。
- 此配置涉及MVNO特性（特性编号：WSFD-207005，license部件编码：LKV2MVNO02），执行命令请使用[**DSP LICENSE**](../../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“ENABLE(打开)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MVNOID | MVNO标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MVNO的标识。<br>数据来源：整网规划<br>取值范围：1～64<br>默认值：无<br>说明：- MVNOID参数必须要与已配置的MVNOID不同。 |
| MVNON | 运营商全称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商全称。<br>数据来源：整网规划<br>取值范围：0～79位字符串，数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符<br>默认值：无<br>说明：- GMM information/EMM information消息中携带的“Full name for network”信元值来源于该参数。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商全称不能输入“NULL”，字母不区分大小写。 |
| SHORTNAME | 运营商简称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商简称。<br>数据来源：整网规划<br>取值范围：0～79位字符串，数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符<br>默认值：无<br>说明：- GMM information/EMM information消息中携带的“Short name for network”信元值来源于该参数。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商简称不能输入“NULL”，字母不区分大小写。 |
| S5S8TYPE | 协议类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定虚拟运营商在S5/S8口使用的协议类型。<br>数据来源：整网规划<br>取值范围：<br>- “GTP(GTP)”<br>- “PMIP(PMIP)”<br>默认值：GTP(GTP) |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MVNO]] · MVNO配置信息（MVNO）

## 使用实例

增加一个MVNO标识为1，运营商全称为aaa，运营商简称为a，协议类型为GTP的MVNO配置信息：

ADD MVNO: MVNOID=1, MVNON="aaa", SHORTNAME="a", S5S8TYPE=GTP;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MVNO.md`
