---
id: UNC@20.15.2@MMLCommand@MOD MNO
type: MMLCommand
name: MOD MNO（修改MNO配置信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MNO
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
- 网络管理
- 归属网络运营商管理
- MNO管理
- MNO配置表
status: active
---

# MOD MNO（修改MNO配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于修改MNO的名称。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNOID | MNO标识 | 可选必选说明：必选参数<br>参数含义：待修改MNO的标识。<br>数据来源：整网规划<br>取值范围：0，128~254<br>默认值：无<br>说明：- 输入的需要修改的MNO的“MNOID”参数必须已经配置。<br>- 0为系统初始值。<br>- 由于系统初始化后，已存在一条“MNOID”为0的记录，当“MNOID”参数为0时，执行[**ADD MNO**](增加MNO配置信息(ADD MNO)_72345671.md)的效果等同于执行[**MOD MNO**](修改MNO配置信息(MOD MNO)_72225751.md)命令。 |
| FULLNAME | 运营商全称 | 可选必选说明：可选参数<br>参数含义：待修改运营商全称。<br>数据来源：整网规划<br>取值范围：0～79位字符串，数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符<br>默认值：无<br>说明：GMM information/EMM information消息中携带的“Full name for network”信元值来源于该参数。<br>因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>运营商全称不能输入“NULL”，字母不区分大小写。 |
| SHORTNAME | 运营商简称 | 可选必选说明：可选参数<br>参数含义：待修改运营商简称。<br>数据来源：整网规划<br>取值范围：0～79位字符串，数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符<br>默认值：无<br>说明：GMM information/EMM information消息中携带的“Short name for network”信元值来源于该参数。<br>因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>运营商简称不能输入“NULL”，字母不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MNO]] · MNO配置信息（MNO）

## 使用实例

将 “MNO标识” 为 “128” 的 “运营商全称” 改为 “bbb” ， “运营商简称” 改为 “b” ：

MOD MNO: MNOID=128, FULLNAME="bbb", SHORTNAME="b";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MNO配置信息(MOD-MNO)_72225751.md`
